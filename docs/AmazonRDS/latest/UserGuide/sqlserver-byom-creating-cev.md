

# Creating and managing BYOM engine versions for RDS for SQL Server
<a name="sqlserver-byom-creating-cev"></a>

Creating a BYOM engine version requires a one-time setup (License Mobility verification, obtaining RTM media, and uploading it to Amazon S3).

Create and manage BYOM engine versions by using the AWS Management Console, the [AWS CLI](https://aws.amazon.com/cli/), [AWS Tools for PowerShell](https://aws.amazon.com/powershell/), or the [Amazon RDS API](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html). The AWS CLI and AWS Tools for PowerShell come preinstalled in [AWS CloudShell](https://aws.amazon.com/cloudshell/).

## Before you begin
<a name="sqlserver-byom-creating-cev.before-you-begin"></a>

### Step 1: Complete Microsoft License Mobility verification
<a name="sqlserver-byom-creating-cev.step1"></a>

License Mobility through Software Assurance is required for BYOM. You must have active Software Assurance coverage on your SQL Server licenses before deploying them on AWS.

To complete the verification process:

1. **Review eligibility** Visit the [AWS License Mobility page](https://aws.amazon.com/windows/resources/licensemobility/) to review requirements and eligibility criteria.

1. **Submit the verification form** Download and complete the [Microsoft License Mobility verification form](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility.aspx). Submit the form to Microsoft through your licensing partner or directly.

1. **Wait for approval** Microsoft sends you a confirmation email when your verification is approved.

You must submit the form to Microsoft directly or through your Microsoft reseller within 10 days of bringing the products to AWS.

**Important**  
AWS does not validate or enforce Microsoft licensing compliance. You are responsible for maintaining compliance with your Microsoft licensing agreements.

### Step 2: Obtain SQL Server installation media
<a name="sqlserver-byom-creating-cev.step2"></a>

Download the Release to Manufacturing (RTM) file for the SQL Server major version you want to use. The RTM file is the base installation media for a SQL Server major version and edition (for example, SQL Server 2019 Enterprise Edition).

You can obtain the RTM file from one of the following Microsoft sources:
+ **Visual Studio subscription** If you have an active Visual Studio subscription, download the RTM file from the [subscriber downloads page](https://visualstudio.microsoft.com/subscriptions/).
+ **Microsoft 365 admin center** If you purchased products through volume licensing, download the RTM file from the [Microsoft 365 admin center Downloads page](https://admin.microsoft.com).

**Important**  
Download only the English language Core-based ISO file. Do not use the Server\+CAL-based ISO file.  
Core-based refers to per-core licensing, not the Windows Server Core installation option. For Enterprise Edition, download the file labeled Enterprise Core Edition, not Enterprise Edition. Standard Edition has a single download.

**Important**  
For SQL Server 2019 Release to Manufacturing (RTM) installation media (Standard and Enterprise Core editions), download only from the Microsoft 365 Admin Center. SQL Server 2019 media downloaded from Visual Studio Subscriptions is not supported. For SQL Server 2022 and later, you can download RTM installation media from either the Microsoft 365 Admin Center or Visual Studio Subscriptions.

### Step 3: Upload installation media to Amazon S3
<a name="sqlserver-byom-creating-cev.step3"></a>

Upload the SQL Server RTM file to an Amazon S3 bucket in the same AWS Region and account where you plan to create the BYOM engine version.

#### Console
<a name="sqlserver-byom-creating-cev.step3.console"></a>

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Buckets**, and then choose the bucket for your installation media.

1. Choose **Upload**.

1. Choose **Add files**, and then select your SQL Server RTM ISO file.

1. Choose **Upload**.

The Amazon S3 console supports uploading files up to 160 GB.

#### AWS CLI
<a name="sqlserver-byom-creating-cev.step3.cli"></a>

Use the [aws s3 cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) command to upload the RTM file.

Run this command on the computer that has the ISO file. To sign in with your console credentials, use the [aws login](https://docs.aws.amazon.com/cli/latest/reference/login/index.html) command.

```
aws s3 cp {{enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}} \
    s3://{{amzn-s3-demo-bucket}}/{{ISOs/}} \
    --region {{us-west-2}}
```

#### PowerShell
<a name="sqlserver-byom-creating-cev.step3.powershell"></a>

Use the [Write-S3Object](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-S3Object.html) cmdlet to upload the RTM file.

Run this cmdlet on the computer that has the ISO file. To sign in with your console credentials, use the [Invoke-AWSLogin](https://docs.aws.amazon.com/powershell/latest/reference/items/Invoke-AWSLogin.html) cmdlet.

```
Write-S3Object `
    -BucketName {{amzn-s3-demo-bucket}} `
    -Key {{ISOs/enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}} `
    -File {{enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}} `
    -Region {{us-west-2}}
```

**Note**  
If you do not provide a Cumulative Update (CU) file during BYOM engine creation, Amazon RDS automatically downloads the required CU from Microsoft when you create the engine version.

## Creating a BYOM engine version
<a name="sqlserver-byom-creating-cev.creating"></a>

Before you create a BYOM engine version, verify which engine versions are eligible. For supported versions, review [Bring Your Own Media (BYOM) for RDS for SQL Server](sqlserver-byom.md).

### Console
<a name="sqlserver-byom-creating-cev.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Custom engine versions**.

1. Choose **Create custom engine version**.

1. On the **Create custom engine version** page, do the following:

   1. For **Engine type**, choose **SQL Server**.

   1. For **Database management type**, choose **Amazon RDS**.

   1. For **Edition**, choose **SQL Server Enterprise Edition** or **SQL Server Standard Edition**.

   1. For **Engine version**, choose the major version that matches your installation media, for example **SQL Server 2025**.

   1. For **Minor engine version**, choose the minor version, for example `17.00.4075.5.v1`.

   1. Under **Installation media**, for **S3 object**, enter the S3 URI of your SQL Server RTM ISO file, or choose **Browse S3** and select the file.

1. Choose **Create custom engine version**.

The console displays the new BYOM engine version with an initial status of **Pending validation**. The status progresses automatically. For more information, see [BYOM engine version lifecycle states](#sqlserver-byom-creating-cev.lifecycle).

### AWS CLI
<a name="sqlserver-byom-creating-cev.cli"></a>

Use the [create-custom-db-engine-version](https://docs.aws.amazon.com/cli/latest/reference/rds/create-custom-db-engine-version.html) command to create a BYOM engine version from your installation media. Amazon RDS automatically downloads the required cumulative update from Microsoft.

```
aws rds create-custom-db-engine-version \
    --engine sqlserver-ee \
    --engine-version 17.00.4075.5.v1 \
    --database-installation-files-s3-bucket-name {{amzn-s3-demo-bucket}} \
    --database-installation-files-s3-prefix "{{ISOs/}}" \
    --database-installation-files "{{enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}}" \
    --region {{us-west-2}}
```

The output looks like the following.

```
{
    "Engine": "sqlserver-ee",
    "MajorEngineVersion": "17.00",
    "EngineVersion": "17.00.4075.5.v1",
    "DatabaseInstallationFiles": [
        "enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso"
    ],
    "DBEngineDescription": "Microsoft SQL Server Enterprise Edition",
    "DBEngineVersionArn": "arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.4075.5.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Status": "pending-validation",
    ...
}
```

To create a BYOM engine version for a later minor version of the same major version and edition, specify only the engine and engine version. Amazon RDS reuses the installation media that you provided earlier.

```
aws rds create-custom-db-engine-version \
    --engine sqlserver-ee \
    --engine-version 17.00.5005.3.v1 \
    --region {{us-west-2}}
```

### PowerShell
<a name="sqlserver-byom-creating-cev.powershell"></a>

Use the [New-RDSCustomDBEngineVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RDSCustomDBEngineVersion.html) cmdlet to create a BYOM engine version from your installation media. Amazon RDS automatically downloads the required cumulative update from Microsoft.

```
New-RDSCustomDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.4075.5.v1 `
    -DatabaseInstallationFilesS3BucketName {{amzn-s3-demo-bucket}} `
    -DatabaseInstallationFilesS3Prefix {{ISOs/}} `
    -DatabaseInstallationFile {{enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}} `
    -Region {{us-west-2}}
```

The output looks like the following.

```
...
DatabaseInstallationFiles                 : {enu_sql_server_2025_enterprise_core_edition_x64_dvd_1a2b3c4d.iso}
DBEngineDescription                       : Microsoft SQL Server Enterprise Edition
DBEngineVersionArn                        : arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.4075.5.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Engine                                    : sqlserver-ee
EngineVersion                             : 17.00.4075.5.v1
MajorEngineVersion                        : 17.00
Status                                    : pending-validation
...
```

To create a BYOM engine version for a later minor version of the same major version and edition, specify only the engine and engine version. Amazon RDS reuses the installation media that you provided earlier.

```
New-RDSCustomDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.5005.3.v1 `
    -Region {{us-west-2}}
```

## Describing BYOM engine versions
<a name="sqlserver-byom-creating-cev.describing"></a>

After you create a BYOM engine version, check its status and details. The output returns two records for the same engine version: one for License Included and one for BYOM. The License Included record has no media type: the AWS CLI shows `None`, and AWS Tools for PowerShell shows an empty value. The BYOM record shows `Customer Provided`.

While the BYOM engine version is being created, its record shows a status of `pending-validation`, `validating`, or `creating`, and it appears only when you include all engine versions (`--include-all` with the AWS CLI or `-IncludeAll $true` with AWS Tools for PowerShell). The following examples include all engine versions.

### Console
<a name="sqlserver-byom-creating-cev.describing.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Custom engine versions**.

The list shows each engine version with its **Engine**, **Engine media type**, and **Status**. BYOM engine versions have an **Engine media type** of **Customer Provided**. To narrow the list, enter text in **Filter by custom engine versions**.

### AWS CLI
<a name="sqlserver-byom-creating-cev.describing.cli"></a>

Use the [describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) command.

```
aws rds describe-db-engine-versions \
    --engine sqlserver-ee \
    --engine-version 17.00.5005.3.v1 \
    --include-all \
    --output table \
    --query "DBEngineVersions[].{Engine: Engine, Version: EngineVersion, Status: Status, MediaType: DBEngineMediaType}" \
    --region {{us-west-2}}
```

The output looks like the following.

```
-----------------------------------------------------------------------
|                      DescribeDBEngineVersions                       |
+--------------+---------------------+------------+-------------------+
|    Engine    |      MediaType      |  Status    |      Version      |
+--------------+---------------------+------------+-------------------+
|  sqlserver-ee|  None               |  available |  17.00.5005.3.v1  |
|  sqlserver-ee|  Customer Provided  |  available |  17.00.5005.3.v1  |
+--------------+---------------------+------------+-------------------+
```

### PowerShell
<a name="sqlserver-byom-creating-cev.describing.powershell"></a>

Use the [Get-RDSDBEngineVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBEngineVersion.html) cmdlet.

```
Get-RDSDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.5005.3.v1 `
    -IncludeAll $true `
    -Region {{us-west-2}} |
Format-Table Engine, DBEngineMediaType, Status, EngineVersion
```

The output looks like the following.

```
Engine       DBEngineMediaType Status    EngineVersion
------       ----------------- ------    -------------
sqlserver-ee                   available 17.00.5005.3.v1
sqlserver-ee Customer Provided available 17.00.5005.3.v1
```

## BYOM engine version lifecycle states
<a name="sqlserver-byom-creating-cev.lifecycle"></a>


| State | Description | 
| --- | --- | 
| pending-validation | Amazon RDS accepted the request and queued it for processing. | 
| validating | Amazon RDS is validating RTM media file. | 
| creating | Amazon RDS is installing SQL Server from RTM media file. | 
| available | The BYOM engine version is ready for instance creation. | 
| incompatible-installation-media | The installation files are invalid or corrupted. This is a terminal state. Delete the BYOM engine version and retry with correct files. | 

## Modifying a BYOM engine version
<a name="sqlserver-byom-creating-cev.modifying"></a>

You can modify a BYOM engine version by using the AWS Management Console, the AWS CLI, or AWS Tools for PowerShell. You can modify the BYOM engine version description or its availability status. Your BYOM engine version has one of the following status values:
+ `available` (**Active** in the console) – You can use this BYOM engine version to create a new DB instance or upgrade a DB instance. This is the default status for a newly created BYOM engine version.
+ `inactive-except-restore` (**Inactive except restore** in the console) – You can restore a DB snapshot to create a new DB instance with this BYOM engine version, but you can't create or upgrade a DB instance with it.
+ `inactive` (**Inactive all** in the console) – You can't create or upgrade a DB instance with this BYOM engine version. You can't restore a DB snapshot to create a new DB instance with this BYOM engine version.

You can change the BYOM engine version status from `available` to `inactive` or `inactive-except-restore`, or from either of those back to `available`. You might change the status to `inactive` or `inactive-except-restore` to prevent the accidental use of a BYOM engine version, or change the status back to `available` to make a discontinued BYOM engine version eligible for use again.

**Note**  
Existing instances running on a BYOM engine version that you make inactive continue to operate normally. Only new instance creation and restore operations are affected.

### Console
<a name="sqlserver-byom-creating-cev.modifying.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Custom engine versions**.

1. Select the BYOM engine version that you want to modify, and then choose **Actions**, **Modify**.

1. On the **Modify CEV** page, do the following:

   1. Under **CEV status settings**, choose **Active**, **Inactive except restore**, or **Inactive all**.

   1. (Optional) For **Version description**, enter a description.

1. Choose **Modify CEV**.

### AWS CLI
<a name="sqlserver-byom-creating-cev.modifying.cli"></a>

Use the [modify-custom-db-engine-version](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-custom-db-engine-version.html) command.

```
aws rds modify-custom-db-engine-version \
    --engine sqlserver-ee \
    --engine-version 17.00.5005.3.v1 \
    --status inactive \
    --region {{us-west-2}}
```

The output looks like the following.

```
{
    "Engine": "sqlserver-ee",
    "MajorEngineVersion": "17.00",
    "EngineVersion": "17.00.5005.3.v1",
    "DBEngineDescription": "Microsoft SQL Server Enterprise Edition",
    "DBEngineVersionArn": "arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.5005.3.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Status": "inactive",
    ...
}
```

### PowerShell
<a name="sqlserver-byom-creating-cev.modifying.powershell"></a>

Use the [Edit-RDSCustomDBEngineVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-RDSCustomDBEngineVersion.html) cmdlet.

```
Edit-RDSCustomDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.5005.3.v1 `
    -Status inactive `
    -Region {{us-west-2}}
```

The output looks like the following.

```
...
DBEngineDescription                       : Microsoft SQL Server Enterprise Edition
DBEngineVersionArn                        : arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.5005.3.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Engine                                    : sqlserver-ee
EngineVersion                             : 17.00.5005.3.v1
MajorEngineVersion                        : 17.00
Status                                    : inactive
...
```

## Deleting a BYOM engine version
<a name="sqlserver-byom-creating-cev.deleting"></a>

Permanently remove a BYOM engine version that you no longer need. After you delete it, the engine version returns to a single License Included entry.

**Prerequisites for deletion**

Before you can delete a BYOM engine version, ensure the following:
+ No DB instances are using the BYOM version.
+ No DB snapshots reference the BYOM version.

If any of the Amazon RDS resources exist, the API fails the deletion request.

### Console
<a name="sqlserver-byom-creating-cev.deleting.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Custom engine versions**.

1. Select the BYOM engine version that you want to delete, and then choose **Actions**, **Delete**.

1. To confirm, enter **delete me**, and then choose **Delete**.

The **Status** of the BYOM engine version changes to **Deleting**.

### AWS CLI
<a name="sqlserver-byom-creating-cev.deleting.cli"></a>

Use the [delete-custom-db-engine-version](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-custom-db-engine-version.html) command.

```
aws rds delete-custom-db-engine-version \
    --engine sqlserver-ee \
    --engine-version 17.00.5005.3.v1 \
    --region {{us-west-2}}
```

The output looks like the following.

```
{
    "Engine": "sqlserver-ee",
    "MajorEngineVersion": "17.00",
    "EngineVersion": "17.00.5005.3.v1",
    "DBEngineDescription": "Microsoft SQL Server Enterprise Edition",
    "DBEngineVersionArn": "arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.5005.3.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Status": "deleting",
    ...
}
```

### PowerShell
<a name="sqlserver-byom-creating-cev.deleting.powershell"></a>

Use the [Remove-RDSCustomDBEngineVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-RDSCustomDBEngineVersion.html) cmdlet.

```
Remove-RDSCustomDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.5005.3.v1 `
    -Region {{us-west-2}}
```

The cmdlet asks you to confirm the deletion.

The output looks like the following.

```
...
DBEngineDescription                       : Microsoft SQL Server Enterprise Edition
DBEngineVersionArn                        : arn:aws:rds:us-west-2:111122223333:cev:sqlserver-ee/17.00.5005.3.v1/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Engine                                    : sqlserver-ee
EngineVersion                             : 17.00.5005.3.v1
MajorEngineVersion                        : 17.00
Status                                    : deleting
...
```

## Considerations
<a name="sqlserver-byom-creating-cev.considerations"></a>
+ You provide the RTM ISO file once per major version and edition. All minor versions within the same major version and edition will reuse the same installation media.
+ When providing your SQL Server RTM for Bring Your Own Media, you must only use the Core-based RTM ISO and not the Server \+ CAL based RTM ISO file.

## Next steps
<a name="sqlserver-byom-creating-cev.next-steps"></a>

After your BYOM engine version reaches `available` status, you can launch an RDS for SQL Server instance using it. See [Creating a BYOM DB instance for RDS for SQL Server](sqlserver-byom-creating-instance.md).