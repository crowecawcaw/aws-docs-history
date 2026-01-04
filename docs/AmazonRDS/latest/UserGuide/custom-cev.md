# Preparing to create a CEV

To create a CEV, access the installation files and patches that are stored in your
Amazon S3 bucket for any of the following releases:

- Oracle Database 19c
- Oracle Database 18c
- Oracle Database 12c Release 2 (12.2)
- Oracle Database 12c Release 1 (12.1)
  For example, you can use the April 2021 RU/RUR for Oracle Database 19c, or any valid combination of installation files and
  patches. For more information on the versions and Regions supported by RDS Custom for Oracle, see
  [RDS Custom with RDS for Oracle](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora").

###### Topics

- [Step 1 (Optional): Download the
  manifest templates](#custom-cev.preparing.templates "#custom-cev.preparing.templates")
- [Step 2: Download your database
  installation files and patches from Oracle Software Delivery Cloud](#custom-cev.preparing.download "#custom-cev.preparing.download")
- [Step 3: Upload your installation files to Amazon S3](#custom-cev.preparing.s3 "#custom-cev.preparing.s3")
- [Step 4 (Optional): Share your installation media in S3 across AWS accounts](#custom-cev.preparing.accounts "#custom-cev.preparing.accounts")
- [Step 5: Prepare the CEV
  manifest](#custom-cev.preparing.manifest "#custom-cev.preparing.manifest")
- [Step 6 (Optional): Validate the CEV manifest](#custom-cev.preparing.validating "#custom-cev.preparing.validating")
- [Step 7: Add necessary IAM
  permissions](#custom-cev.preparing.iam "#custom-cev.preparing.iam")

## Step 1 (Optional): Download the

manifest templates

A _CEV manifest_ is a JSON document that includes the list of
database installation .zip files for your CEV. To create a CEV, do the following:

1. Identify the Oracle database installation files that you want to include in your
   CEV.
2. Download the installation files.
3. Create a JSON manifest that lists the installation files.

RDS Custom for Oracle provides JSON manifest templates with our recommended .zip files for each
supported Oracle Database release. For example, the following template is for the
19.17.0.0.0 RU.

```
{
    "mediaImportTemplateVersion": "2020-08-14",
    "databaseInstallationFileNames": [
        "V982063-01.zip"
    ],
    "opatchFileNames": [
        "p6880880_190000_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames": [
        "p34419443_190000_Linux-x86-64.zip",
        "p34411846_190000_Linux-x86-64.zip"
    ],
    "otherPatchFileNames": [
        "p28852325_190000_Linux-x86-64.zip",
        "p29997937_190000_Linux-x86-64.zip",
        "p31335037_190000_Linux-x86-64.zip",
        "p32327201_190000_Linux-x86-64.zip",
        "p33613829_190000_Linux-x86-64.zip",
        "p34006614_190000_Linux-x86-64.zip",
        "p34533061_190000_Linux-x86-64.zip",
        "p34533150_190000_Generic.zip",
        "p28730253_190000_Linux-x86-64.zip",
        "p29213893_1917000DBRU_Generic.zip",
        "p33125873_1917000DBRU_Linux-x86-64.zip",
        "p34446152_1917000DBRU_Linux-x86-64.zip"
    ]
}
```

Each template has an associated readme that includes instructions for downloading the
patches, URLs for the .zip files, and file checksums. You can use these templates as they
are or modify them with your own patches. To review the templates, download [custom-oracle-manifest.zip](samples/custom-oracle-manifest.md "samples/custom-oracle-manifest.md") to your
local disk and then open it with a file archiving application. For more information, see
[Step 5: Prepare the CEV
manifest](#custom-cev.preparing.manifest "#custom-cev.preparing.manifest").

## Step 2: Download your database

installation files and patches from Oracle Software Delivery Cloud

When you have identified the installation files that you want for your CEV,
download them to your local system. The Oracle Database installation files and patches are
hosted on Oracle Software Delivery Cloud. Each CEV requires a base release, such as Oracle
Database 19c or Oracle Database 12c Release 2 (12.2), and an optional list of
patches.

###### To download the database installation files for Oracle Database

1. Go to [https://edelivery.oracle.com/](https://edelivery.oracle.com/ "https://edelivery.oracle.com/") and sign in.
2. In the search box, enter `Oracle Database Enterprise Edition`
   or `Oracle Database Standard Edition 2` and choose
   **Search**.
3. Choose one of the following base releases:

| Database version                         | Enterprise Edition                                                                                   | Standard Edition 2                                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Oracle Database 19c                      | **DLP: Oracle Database 19c Enterprise Edition 19.3.0.0.0 ( Oracle<br>Database Enterprise Edition )** | **DLP: Oracle Database 19c Standard Edition 2 19.3.0.0.0 ( Oracle<br>Database Standard Edition 2 )** |
| Oracle Database 18c                      | **DLP: Oracle Database 18c Enterprise Edition 18.0.0.0.0<br>( Oracle Database Enterprise Edition )** | **DLP: Oracle Database Standard Edition 2 18.0.0.0.0 (<br>Oracle Database Standard Edition 2 )**     |
| Oracle Database 12c Release 2 (12.2.0.1) | **DLP: Oracle Database 12c Enterprise Edition 12.2.0.1.0 ( Oracle<br>Database Enterprise Edition )** | **DLP: Oracle Database Standard Edition 2 12.2.0.1.0 (<br>Oracle Database Standard Edition 2 )**     |
| Oracle Database 12c Release 1 (12.1.0.2) | **DLP: Oracle Database 12c Enterprise Edition 12.1.0.2.0 ( Oracle<br>Database Enterprise Edition )** | **DLP: Oracle Database Standard Edition 2 12.1.0.2.0 (<br>Oracle Database Standard Edition 2 )**     |

4. Choose **Continue**.
5. Clear the **Download Queue** check box.
6. Choose the option that corresponds to your base release:
   - **Oracle Database 19.3.0.0.0 - Long Term
     Release**.
   - **Oracle Database 18.0.0.0.0**
   - **Oracle Database 12.2.0.1.0**.
   - **Oracle Database 12.1.0.2.0**.

7. Choose **Linux x86-64** in **Platform/Languages**.
8. Choose **Continue**, and then sign the Oracle License
   Agreement.
9. Choose the .zip file that corresponds to your database release:

| Database release and edition | Zip files                                        | SHA-256 hash                                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 19c EE and SE2               | **V982063-01.zip**                               | `BA8329C757133DA313ED3B6D7F86C5AC42CD9970A28BF2E6233F3235233AA8D8`                                                                                                                           |
| 18c EE and SE2               | **V978967-01.zip**                               | `C96A4FD768787AF98272008833FE10B172691CF84E42816B138C12D4DE63AB96`                                                                                                                           |
| 12.2.0.1 EE and SE2          | **V839960-01.zip**                               | `96ED97D21F15C1AC0CCE3749DA6C3DAC7059BB60672D76B008103FC754D22DDE`                                                                                                                           |
| 12.1.0.2 EE                  | **V46095-01_1of2.zip**<br>**V46095-01_2of2.zip** | `31FDC2AF41687B4E547A3A18F796424D8C1AF36406D2160F65B0AF6A9CD47355`<br>for V46095-01_1of2.zip<br>`03DA14F5E875304B28F0F3BB02AF0EC33227885B99C9865DF70749D1E220ACCD`<br>for V46095-01_2of2.zip |
| 12.1.0.2 SE2                 | **V77388-01_1of2.zip**<br>**V77388-01_2of2.zip** | `73873369753230F5A0921F95ACEADB591388CB06ED72A7F3AEA7BCBCEA2403BC`<br>for V77388-01_1of2.zip<br>`2492E1BE1E3E3531DA83D0843C09C08E435AC8CEFD9A00C0DF56BE4F15CEEBF3`<br>for V77388-01_2of2.zip |

10. Download your desired Oracle patches from `updates.oracle.com` or
    `support.oracle.com` to your local system. You can find the URLs for
    the patches in the following locations:
    - The readme files in the .zip file that you downloaded in [Step 1 (Optional): Download the
      manifest templates](#custom-cev.preparing.templates "#custom-cev.preparing.templates")
    - The patches listed in each Release Update (RU) in [Release
      notes for Amazon Relational Database Service (Amazon RDS) for Oracle](../OracleReleaseNotes.md "../OracleReleaseNotes.md")

## Step 3: Upload your installation files to Amazon S3

Upload your Oracle installation and patch files to Amazon S3 using the AWS CLI. The S3 bucket
that contains your installation files must be in the same AWS Region as your CEV.

Examples in this section use the following placeholders:

- `install-or-patch-file.zip` –
  Oracle installation media file. For example,
  p32126828_190000_Linux-x86-64.zip is a patch.
- `amzn-s3-demo-destination-bucket`
  – Your Amazon S3 bucket designated for your uploaded installation
  files.
- `123456789012/cev1` – An optional prefix in your Amazon S3 bucket.
- `amzn-s3-demo-source-bucket` – An Amazon S3 bucket where you can optionally stage
  files.

###### Topics

- [Step 3a: Verify that your S3
  bucket is in the correct AWS Region](#custom-cev.preparing.s3.verify-region "#custom-cev.preparing.s3.verify-region")
- [Step 3b: Make sure that your S3
  bucket policy has the correct permissions](#custom-cev.preparing.s3.verify-policy "#custom-cev.preparing.s3.verify-policy")
- [Step 3c: Upload your files using the cp
  or sync commands](#custom-cev.preparing.s3.upload "#custom-cev.preparing.s3.upload")
- [Step 3d: List the files in your S3
  bucket](#custom-cev.preparing.s3.list "#custom-cev.preparing.s3.list")

### Step 3a: Verify that your S3

bucket is in the correct AWS Region

Verify that your S3 bucket is in the AWS Region where you plan to run the
`create-custom-db-engine-version` command.

```
aws s3api get-bucket-location --bucket `amzn-s3-demo-destination-bucket`
```

### Step 3b: Make sure that your S3

bucket policy has the correct permissions

You can create a CEV from scratch or from a source CEV. If you plan to create new CEV
from source CEVs, make sure that your S3 bucket policy has the correct
permissions:

1. Identify the S3 bucket reserved by RDS Custom. The bucket name has the format
   `do-not-delete-rds-custom-`account`-`region`-`string``.
For example, the bucket might be named
`do-not-delete-rds-custom-`123456789012`-`us-east-1`-`abc123EXAMPLE``.
2. Make sure that the following permission is appended to your S3 bucket policy.
   Replace
   `do-not-delete-rds-custom-`123456789012`-`us-east-1`-`abc123EXAMPLE``
   with the name of your bucket.

```
{
    "Sid": "AWSRDSCustomForOracleCustomEngineVersionGetObject",
    "Effect": "Allow",
    "Principal": {
        "Service": "custom.rds.amazonaws.com"
    },
    "Action": [
        "s3:GetObject",
        "s3:GetObjectTagging"
    ],
    "Resource": "arn:aws:s3:::do-not-delete-rds-custom-`123456789012`-`us-east-1`-`abc123EXAMPLE`/CustomEngineVersions/*"
}, ...
```

### Step 3c: Upload your files using the cp

or sync commands

Choose either of the following options:

- Use `aws s3 cp` to upload a single .zip file.

Upload each installation .zip file separately. Don't combine the .zip
files into a single .zip file.

- Use `aws s3 sync` to upload a directory.

The following example uploads
`install-or-patch-file.zip` to the
`123456789012/cev1` folder in the
RDS Custom Amazon S3 bucket. Run a separate `aws s3` command for each .zip that
you want to upload.

For Linux, macOS, or Unix:

```
aws s3 cp `install-or-patch-file.zip` \
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

For Windows:

```
aws s3 cp `install-or-patch-file.zip` ^
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

The following example uploads the files in your local
`cev1` folder to the
`123456789012/cev1` folder in your Amazon S3 bucket.

For Linux, macOS, or Unix:

```
aws s3 sync cev1 \
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

For Windows:

```
aws s3 sync cev1 ^
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

The following example uploads all files in
`amzn-s3-demo-source-bucket` to the
`123456789012/cev1`
folder in your Amazon S3 bucket.

For Linux, macOS, or Unix:

```
aws s3 sync s3://`amzn-s3-demo-source-bucket`/ \
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

For Windows:

```
aws s3 sync s3://`amzn-s3-demo-source-bucket`/ ^
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

### Step 3d: List the files in your S3

bucket

The following example uses the `s3 ls` command to list the files in your
RDS Custom Amazon S3 bucket.

```
aws s3 ls \
    s3://`amzn-s3-demo-destination-bucket`/`123456789012/cev1`/
```

## Step 4 (Optional): Share your installation media in S3 across AWS accounts

For the purposes of this section, the Amazon S3 bucket that contains your uploaded Oracle installation files is your _media
bucket_. Your organization might use multiple AWS accounts in an AWS Region. If so, you might want to use one AWS account
to populate your media bucket and a different AWS account to create CEVs. If you don't intend to share your media bucket, skip to the next
section.

This section assumes the following:

- You can access the account that created your media bucket and a different account in which you intend to create CEVs.
- You intend to create CEVs in only one AWS Region. If you intend to use multiple Regions, create a media bucket in each
  Region.
- You're using the CLI. If you're using the Amazon S3 console, adapt the following steps.

###### To configure your media bucket for sharing across AWS accounts

1. Log in to the AWS account that contains the S3 bucket into which you uploaded your installation media.
2. Start with either a blank JSON policy template or an existing policy that you can adapt.

The following command retrieves an existing policy and saves it as `my-policy.json`. In this example, the
S3 bucket containing your installation files is named `amzn-s3-demo-bucket`.

```
aws s3api get-bucket-policy \
    --bucket `amzn-s3-demo-bucket` \
    --query Policy \
    --output text > `my-policy.json`
```

3. Edit the media bucket permissions as follows:
   - In the `Resource` element of your template, specify the S3 bucket into which you uploaded your Oracle Database
     installation files.
   - In the `Principal` element, specify the ARNs for all AWS accounts that you intend to use to create CEVs. You
     can add the root, a user, or a role to the S3 bucket allow list. For more information, see [IAM identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md") in the _AWS Identity and Access Management User
     Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GrantAccountsAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root",
 "arn:aws:iam::`444455556666`:user/`user-name-with-path`",
 "arn:aws:iam::`123456789012`:role/`role-name-with-path`"
 ]
 },
 "Action": [
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

4. Attach the policy to your media bucket.

In the following example, `amzn-s3-demo-bucket` is the name of the S3 bucket that contains your
installation files, and `my-policy.json` is the name of your JSON file.

```
aws s3api put-bucket-policy \
    --bucket `amzn-s3-demo-bucket` \
    --policy file://`my-policy.json`
```

5. Log in to an AWS account in which you intend to create CEVs.
6. Verify that this account can access the media bucket in the AWS account that created it.

```
aws s3 ls --query "Buckets[].Name"
```

For more information, see [aws s3 ls](../../../cli/latest/reference/s3/ls.md "../../../cli/latest/reference/s3/ls.md") in the _AWS CLI
Command Reference_. 7. Create a CEV by following the steps in [Creating a CEV](custom-cev.md "custom-cev.md").

## Step 5: Prepare the CEV

manifest

A CEV manifest is a JSON document that includes the following:

- (Required) The list of installation .zip files that you uploaded to Amazon S3. RDS Custom
  applies the patches in the order in which they're listed in the
  manifest.
- (Optional) Installation parameters that set nondefault values for the Oracle base, Oracle home, and the ID and name of the UNIX/Linux user and group. Be aware that you can’t modify the
  installation parameters for an existing CEV or an existing DB instance. You also
  can’t upgrade from one CEV to another CEV when the installation parameters have
  different settings.

For sample CEV manifests, see the JSON templates that you downloaded in [Step 1 (Optional): Download the
manifest templates](#custom-cev.preparing.templates "#custom-cev.preparing.templates"). You can also review the samples in [CEV manifest examples](#custom-cev.preparing.manifest.examples "#custom-cev.preparing.manifest.examples").

###### Topics

- [JSON fields in the CEV manifest](#custom-cev.preparing.manifest.fields "#custom-cev.preparing.manifest.fields")
- [Creating the CEV manifest](#custom-cev.preparing.manifest.creating "#custom-cev.preparing.manifest.creating")
- [CEV manifest examples](#custom-cev.preparing.manifest.examples "#custom-cev.preparing.manifest.examples")

### JSON fields in the CEV manifest

The following table describes the JSON fields in the manifest.

| JSON field                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MediaImportTemplateVersion`    | Version of the CEV manifest. The date is in the format `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `databaseInstallationFileNames` | Ordered list of installation files for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `opatchFileNames`               | Ordered list of OPatch installers used for the Oracle DB engine. Only one value is valid. Values for<br>`opatchFileNames` must start with `p6880880_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `psuRuPatchFileNames`           | The PSU and RU patches for this database.<br>ImportantIf you include `psuRuPatchFileNames`, `opatchFileNames` is required. Values for<br>`opatchFileNames` must start with `p6880880_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `OtherPatchFileNames`           | The patches that aren't in the list of PSU and RU patches. RDS Custom applies these patches after applying the<br>PSU and RU patches.<br>ImportantIf you include `OtherPatchFileNames`, `opatchFileNames` is required. Values for<br>`opatchFileNames` must start with `p6880880_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `installationParameters`        | Nondefault settings for the Oracle base, Oracle home, and the ID and name of the UNIX/Linux user and group. You can set the<br>following parameters:<br>**oracleBase**<br>The directory under which your Oracle binaries are<br>installed. It is the mount point of the binary volume<br>that stores your files. The Oracle base directory can<br>include multiple Oracle homes. For example, if<br>`/home/oracle/oracle.19.0.0.0.ru-2020-04.rur-2020-04.r1.EE.1`<br>is one of your Oracle home directories, then<br>`/home/oracle` is the Oracle base<br>directory. A user-specified Oracle base directory is not<br>a symbolic link.<br>If you don't specify the Oracle base, the default<br>directory is `/rdsdbbin`.<br>**oracleHome**<br>The directory in which your Oracle database binaries<br>are installed. For example, if you specify<br>`/home/oracle/` as your Oracle base, then<br>you might specify<br>`/home/oracle/oracle.19.0.0.0.ru-2020-04.rur-2020-04.r1.EE.1/`<br>as your Oracle home. A user-specified Oracle home<br>directory is not a symbolic link. The Oracle home value<br>is referenced by the `$ORACLE_HOME`<br>environment variable.<br>If you don't specify the Oracle home, the default<br>naming format is<br>`/rdsdbbin/oracle.`major-engine-version`.custom.r1.`engine-edition`.1`.<br>**unixUname**<br>The name of the UNIX user that owns the Oracle<br>software. RDS Custom assumes this user when running local<br>database commands. If you specify both<br>`unixUid` and `unixUname`,<br>RDS Custom creates the user if it doesn't exist, and then<br>assigns the UID to the user if it's not the same as the<br>initial UID.<br>The default user name is `rdsdb`.<br>**unixUid**<br>The ID (UID) of the UNIX user that owns the Oracle<br>software. If you specify both `unixUid` and<br>`unixUname`, RDS Custom creates the user if<br>it doesn't exist, and then assigns the UID to the user<br>if it's not the same as the initial UID.<br>The default UID is `61001`. This is the UID<br>of the user `rdsdb`.<br>**unixGroupName**<br>The name of the UNIX group. The UNIX user that owns<br>the Oracle software belongs to this group.<br>The default group name is `rdsdb`.<br>**unixGroupId**<br>The ID of the UNIX group to which the UNIX user<br>belongs.<br>The default group ID is `1000`. This is the<br>ID of the group `rdsdb`. |

Each Oracle Database release has a different list of supported installation
files. When you create your CEV manifest, make sure to specify only files that are
supported by RDS Custom for Oracle. Otherwise, CEV creation fails with an error. All patches listed
in [Release notes
for Amazon Relational Database Service (Amazon RDS) for Oracle](../OracleReleaseNotes.md "../OracleReleaseNotes.md") are supported.

### Creating the CEV manifest

###### To create a CEV manifest

1. List all installation files that you plan to apply, in the order that you want to apply them.
2. Correlate the installation files with the JSON fields described in [JSON fields in the CEV manifest](#custom-cev.preparing.manifest.fields "#custom-cev.preparing.manifest.fields").
3. Do either of the following:
   - Create the CEV manifest as a JSON text file.
   - Edit the CEV manifest template when you create the CEV in the console. For more information, see [Creating a CEV](custom-cev.md "custom-cev.md").

### CEV manifest examples

The following examples show CEV manifest files for different Oracle Database releases. If you include a JSON field in your
manifest, make sure that it isn't empty. For example, the following CEV manifest isn't valid because
`otherPatchFileNames` is empty.

```
{
    "mediaImportTemplateVersion": "2020-08-14",
    "databaseInstallationFileNames": [
        "V982063-01.zip"
    ],
    "opatchFileNames": [
        "p6880880_190000_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames": [
        "p32126828_190000_Linux-x86-64.zip"
    ],
    "otherPatchFileNames": [
    ]
}
```

**Topics**

- [Sample CEV manifest for Oracle Database 12c Release 1 (12.1)](#oracle-cev-manifest-12.1 "#oracle-cev-manifest-12.1")
- [Sample CEV manifest for Oracle Database 12c Release 2 (12.2)](#oracle-cev-manifest-12.2 "#oracle-cev-manifest-12.2")
- [Sample CEV manifest for Oracle Database 18c](#oracle-cev-manifest-18c "#oracle-cev-manifest-18c")
- [Sample CEV manifest for Oracle Database 19c](#oracle-cev-manifest-19c "#oracle-cev-manifest-19c")

###### Example Sample CEV

manifest for Oracle Database 12c Release 1 (12.1)

In the following example for the July 2021 PSU for Oracle Database 12c
Release 1 (12.1), RDS Custom applies the patches in the order specified. Thus, RDS Custom
applies p32768233, then p32876425, then p18759211, and so on. The example sets new
values for the UNIX user and group, and the Oracle home and Oracle base.

```
{
    "mediaImportTemplateVersion":"2020-08-14",
    "databaseInstallationFileNames":[
        "V46095-01_1of2.zip",
        "V46095-01_2of2.zip"
    ],
    "opatchFileNames":[
        "p6880880_121010_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames":[
        "p32768233_121020_Linux-x86-64.zip"
    ],
    "otherPatchFileNames":[
        "p32876425_121020_Linux-x86-64.zip",
        "p18759211_121020_Linux-x86-64.zip",
        "p19396455_121020_Linux-x86-64.zip",
        "p20875898_121020_Linux-x86-64.zip",
        "p22037014_121020_Linux-x86-64.zip",
        "p22873635_121020_Linux-x86-64.zip",
        "p23614158_121020_Linux-x86-64.zip",
        "p24701840_121020_Linux-x86-64.zip",
        "p25881255_121020_Linux-x86-64.zip",
        "p27015449_121020_Linux-x86-64.zip",
        "p28125601_121020_Linux-x86-64.zip",
        "p28852325_121020_Linux-x86-64.zip",
        "p29997937_121020_Linux-x86-64.zip",
        "p31335037_121020_Linux-x86-64.zip",
        "p32327201_121020_Linux-x86-64.zip",
        "p32327208_121020_Generic.zip",
        "p17969866_12102210119_Linux-x86-64.zip",
        "p20394750_12102210119_Linux-x86-64.zip",
        "p24835919_121020_Linux-x86-64.zip",
        "p23262847_12102201020_Linux-x86-64.zip",
        "p21171382_12102201020_Generic.zip",
        "p21091901_12102210720_Linux-x86-64.zip",
        "p33013352_12102210720_Linux-x86-64.zip",
        "p25031502_12102210720_Linux-x86-64.zip",
        "p23711335_12102191015_Generic.zip",
        "p19504946_121020_Linux-x86-64.zip"
    ],
    "installationParameters": {
        "unixGroupName": "dba",
        "unixGroupId": 12345,
        "unixUname": "oracle",
        "unixUid": 12345,
        "oracleHome": "/home/oracle/oracle.12.1.0.2",
        "oracleBase": "/home/oracle"
    }
}
```

###### Example Sample CEV

manifest for Oracle Database 12c Release 2 (12.2)

In following example for the October 2021 PSU for Oracle Database 12c
Release 2 (12.2), RDS Custom applies p33261817, then p33192662, then p29213893, and so
on. The example sets new values for the UNIX user and group, and the Oracle home and
Oracle base.

```
{
    "mediaImportTemplateVersion":"2020-08-14",
    "databaseInstallationFileNames":[
        "V839960-01.zip"
    ],
    "opatchFileNames":[
        "p6880880_122010_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames":[
        "p33261817_122010_Linux-x86-64.zip"
    ],
    "otherPatchFileNames":[
        "p33192662_122010_Linux-x86-64.zip",
        "p29213893_122010_Generic.zip",
        "p28730253_122010_Linux-x86-64.zip",
        "p26352615_12201211019DBOCT2021RU_Linux-x86-64.zip",
        "p23614158_122010_Linux-x86-64.zip",
        "p24701840_122010_Linux-x86-64.zip",
        "p25173124_122010_Linux-x86-64.zip",
        "p25881255_122010_Linux-x86-64.zip",
        "p27015449_122010_Linux-x86-64.zip",
        "p28125601_122010_Linux-x86-64.zip",
        "p28852325_122010_Linux-x86-64.zip",
        "p29997937_122010_Linux-x86-64.zip",
        "p31335037_122010_Linux-x86-64.zip",
        "p32327201_122010_Linux-x86-64.zip",
        "p32327208_122010_Generic.zip"
    ],
    "installationParameters": {
        "unixGroupName": "dba",
        "unixGroupId": 12345,
        "unixUname": "oracle",
        "unixUid": 12345,
        "oracleHome": "/home/oracle/oracle.12.2.0.1",
        "oracleBase": "/home/oracle"
    }
}
```

###### Example Sample CEV manifest for

Oracle Database 18c

In following example for the October 2021 PSU for Oracle Database 18c,
RDS Custom applies p32126855, then p28730253, then p27539475, and so on. The example
sets new values for the UNIX user and group, and the Oracle home and Oracle
base.

```
{
    "mediaImportTemplateVersion":"2020-08-14",
    "databaseInstallationFileNames":[
        "V978967-01.zip"
    ],
    "opatchFileNames":[
        "p6880880_180000_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames":[
        "p32126855_180000_Linux-x86-64.zip"
    ],
    "otherPatchFileNames":[
        "p28730253_180000_Linux-x86-64.zip",
        "p27539475_1813000DBRU_Linux-x86-64.zip",
        "p29213893_180000_Generic.zip",
        "p29374604_1813000DBRU_Linux-x86-64.zip",
        "p29782284_180000_Generic.zip",
        "p28125601_180000_Linux-x86-64.zip",
        "p28852325_180000_Linux-x86-64.zip",
        "p29997937_180000_Linux-x86-64.zip",
        "p31335037_180000_Linux-x86-64.zip",
        "p31335142_180000_Generic.zip"
    ]
    "installationParameters": {
        "unixGroupName": "dba",
        "unixGroupId": 12345,
        "unixUname": "oracle",
        "unixUid": 12345,
        "oracleHome": "/home/oracle/18.0.0.0.ru-2020-10.rur-2020-10.r1",
        "oracleBase": "/home/oracle/"
    }
}
```

###### Example Sample CEV manifest for

Oracle Database 19c

In the following example for Oracle Database 19c, RDS Custom applies
p32126828, then p29213893, then p29782284, and so on. The example sets new values
for the UNIX user and group, and the Oracle home and Oracle base.

```
{
    "mediaImportTemplateVersion": "2020-08-14",
    "databaseInstallationFileNames": [
        "V982063-01.zip"
    ],
    "opatchFileNames": [
        "p6880880_190000_Linux-x86-64.zip"
    ],
    "psuRuPatchFileNames": [
        "p32126828_190000_Linux-x86-64.zip"
    ],
    "otherPatchFileNames": [
        "p29213893_1910000DBRU_Generic.zip",
        "p29782284_1910000DBRU_Generic.zip",
        "p28730253_190000_Linux-x86-64.zip",
        "p29374604_1910000DBRU_Linux-x86-64.zip",
        "p28852325_190000_Linux-x86-64.zip",
        "p29997937_190000_Linux-x86-64.zip",
        "p31335037_190000_Linux-x86-64.zip",
        "p31335142_190000_Generic.zip"
    ],
    "installationParameters": {
        "unixGroupName": "dba",
        "unixGroupId": 12345,
        "unixUname": "oracle",
        "unixUid": 12345,
        "oracleHome": "/home/oracle/oracle.19.0.0.0.ru-2020-04.rur-2020-04.r1.EE.1",
        "oracleBase": "/home/oracle"
    }
}
```

## Step 6 (Optional): Validate the CEV manifest

Optionally, verify that manifest is a valid JSON file by running the
`json.tool` Python script. For example, if you change into the directory
containing a CEV manifest named `manifest.json`, run the following
command.

```
python -m json.tool < manifest.json
```

## Step 7: Add necessary IAM

permissions

Make sure that the IAM principal that creates the CEV has the necessary policies described in [Step 5: Grant required permissions to your
IAM user or role](custom-setup-orcl.md#custom-setup-orcl.iam-user "custom-setup-orcl.md#custom-setup-orcl.iam-user").
