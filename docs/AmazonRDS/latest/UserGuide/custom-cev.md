# Creating a CEV

You can create a CEV using the AWS Management Console or the AWS CLI. Specify either the multitenant or
non-multitenant architecture. For more information, see [Multitenant architecture considerations](custom-creating.md#custom-creating.overview "custom-creating.md#custom-creating.overview").

Typically, creating a CEV takes about two hours. After you have created the CEV, you can
use it to create or upgrade an RDS Custom DB instance. For more information, see [Creating an RDS Custom for Oracle DB instance](custom-creating.md#custom-creating.create "custom-creating.md#custom-creating.create") and [Upgrading an RDS Custom for Oracle DB instance](custom-upgrading-modify.md "custom-upgrading-modify.md").

###### Note

If your DB instance currently uses Oracle Linux 7.9, create a new CEV that uses the
latest AMI, which uses Oracle Linux 8. Then modify your instance to use the new
CEV.

Note the following requirements and limitations for creating a CEV:

- The Amazon S3 bucket containing your installation files must be in the same
  AWS Region as your CEV. Otherwise, the creation process fails.
- The CEV name must be in the format
  ``major-engine-version`.`customized_string``,
  as in `19.cdb_cev1`.
- The CEV name must contain 1–50 alphanumeric characters, underscores,
  dashes, or periods.
- The CEV name can't contain consecutive periods, as in
  `19..cdb_cev1`.

###### To create a CEV

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Custom engine versions**.

The **Custom engine versions** page shows all CEVs that currently exist. If
you haven't created any CEVs, the page is empty. 3. Choose **Create custom engine version**. 4. In **Engine options**, do the following:

    1. For **Engine type**, choose
     **Oracle**.
    2. For **Architecture settings**, optionally choose
     **Multitenant architecture** to create an
     Oracle multitenant CEV, which uses the DB engine
     `custom-oracle-ee-cdb` or
     `custom-oracle-se2-cdb`. You can create an RDS Custom for Oracle
     CDB with a Multitenant CEV only. If you don't choose this option,
     your CEV is a non-CDB, which uses the engine
     `custom-oracle-ee` or
     `custom-oracle-se2`.


    ###### Note

    The architecture that you choose is a permanent characteristic
     of your CEV. You can't modify your CEV to use a different
     architecture later.
    3. Choose either of the following options:




    	* **Create new CEV** – Create a CEV
    	 from scratch. In this case, you must specify a JSON manifest
    	 specifying the database binaries.
    	* **Create CEV from source** – In
    	 **Specify the CEV that you want to
    	 copy**, choose an existing CEV to use as the
    	 source CEV. In this case, you can specify a new Amazon
    	 Machine Image (AMI), but you can't specify different
    	 database binaries.
    4. For **Engine version**, choose the major engine
     version.

5. In **Version details**, do the following:
   1. Enter a valid name in **Custom engine version
      name**. For example, you might enter the name
      `19.cdb_cev1`.
   2. (Optional) Enter a description for your CEV.

6. In **Installation media**, do the following:
   1. (Optional) For **AMI ID**, either leave the field
      blank to use the latest service-provided AMI, or enter an AMI that
      you previously used to create a CEV. To obtain valid AMI IDs, use
      either of the following techniques:
      - In the console, choose **Custom engine
        versions** in the left navigation pane, and
        choose the name of a CEV. The AMI ID used by the CEV appears
        in the **Configuration** tab.
      - In the AWS CLI, use the
        `describe-db-engine-versions` command. Search
        the output for `ImageID`.

   2. For **S3 location of manifest files**, enter the
      location of the Amazon S3 bucket that you specified in [Step 3: Upload your installation files to Amazon S3](custom-cev.md#custom-cev.preparing.s3 "custom-cev.md#custom-cev.preparing.s3"). For example, enter
      `s3://my-custom-installation-files/123456789012/cev1/`.

   ###### Note

   The AWS Region in which you create the CEV must be in the
   same Region as the S3 bucket. 3. (Create new CEV only) For **CEV manifest**, enter
   the JSON manifest that you created in [Creating the CEV manifest](custom-cev.md#custom-cev.preparing.manifest.creating "custom-cev.md#custom-cev.preparing.manifest.creating").

7. In the **KMS key** section, select **Enter a key
   ARN** to list the available AWS KMS keys. Then select your KMS
   key from the list.

An AWS KMS key is required for RDS Custom. For more information, see [Step 1: Create or reuse a symmetric encryption
AWS KMS key](custom-setup-orcl.md#custom-setup-orcl.cmk "custom-setup-orcl.md#custom-setup-orcl.cmk"). 8. (Optional) Choose **Add new tag** to create a key-value
pair for your CEV. 9. Choose **Create custom engine version**.

If the JSON manifest is in an invalid format, the console displays
**Error validating the CEV manifest**. Fix the
problems, and try again.
The **Custom engine versions** page appears. Your CEV is shown
with the status **Creating**. The process to create a CEV takes
approximately two hours.

To create a CEV by using the AWS CLI, run the [create-custom-db-engine-version](../../../cli/latest/reference/rds/create-custom-db-engine-version.md "../../../cli/latest/reference/rds/create-custom-db-engine-version.md") command.

The following options are required:

- `--engine` – Specify the engine type. For a CDB, specify
  either `custom-oracle-ee-cdb` or
  `custom-oracle-se2-cdb`. For a non-CDB, specify either
  `custom-oracle-ee` or `custom-oracle-se2`. You can
  create CDBs only from a CEV created with `custom-oracle-ee-cdb`
  or `custom-oracle-se2-cdb`. You can create non-CDBs only from a
  CEV created with `custom-oracle-ee` or
  `custom-oracle-se2`.
- `--engine-version` – Specify the engine version. The
  format is
  `major-engine-version`.`customized_string`.
  The CEV name must contain 1–50 alphanumeric characters, underscores,
  dashes, or periods. The CEV name can't contain consecutive periods, as in
  `19..cdb_cev1`.
- `--kms-key-id` – Specify an AWS KMS key.
- `--manifest` – Specify either
  `manifest_json_string` or
  `--manifest file:`file_name`.
Newline characters aren't permitted in
`manifest_json_string``. Make
  sure to escape double quotes (") in the JSON code by prefixing them with a
  backslash (\).

The following example shows the
`manifest_json_string` for 19c
from [Step 5: Prepare the CEV
manifest](custom-cev.md#custom-cev.preparing.manifest "custom-cev.md#custom-cev.preparing.manifest"). The example sets new
values for the Oracle base, Oracle home, and the ID and name of the UNIX/Linux user and group. If you
copy this string, remove all newline characters before you paste it into
your command.

`"{\"mediaImportTemplateVersion\":
 \"2020-08-14\",\"databaseInstallationFileNames\":
 [\"V982063-01.zip\"],\"opatchFileNames\":
 [\"p6880880_190000_Linux-x86-64.zip\"],\"psuRuPatchFileNames\":
 [\"p32126828_190000_Linux-x86-64.zip\"],\"otherPatchFileNames\":
 [\"p29213893_1910000DBRU_Generic.zip\",\"p29782284_1910000DBRU_Generic.zip\",\"p28730253_190000_Linux-x86-64.zip\",\"p29374604_1910000DBRU_Linux-x86-64.zip\",\"p28852325_190000_Linux-x86-64.zip\",\"p29997937_190000_Linux-x86-64.zip\",\"p31335037_190000_Linux-x86-64.zip\",\"p31335142_190000_Generic.zip\"]\"installationParameters\":{
 \"unixGroupName\":\"dba\", \ \"unixUname\":\"oracle\", \
 \"oracleHome\":\"/home/oracle/oracle.19.0.0.0.ru-2020-04.rur-2020-04.r1.EE.1\",
 \ \"oracleBase\":\"/home/oracle/\"}}"`

- `--database-installation-files-s3-bucket-name` – Specify
  the same bucket name that you specified in [Step 3: Upload your installation files to Amazon S3](custom-cev.md#custom-cev.preparing.s3 "custom-cev.md#custom-cev.preparing.s3"). The AWS Region in which you run
  `create-custom-db-engine-version` must be the same Region as
  your Amazon S3 bucket.
  You can also specify the following options:

- `--description` – Specify a description of your
  CEV.
- `--database-installation-files-s3-prefix` – Specify the
  folder name that you specified in [Step 3: Upload your installation files to Amazon S3](custom-cev.md#custom-cev.preparing.s3 "custom-cev.md#custom-cev.preparing.s3").
- `--image-id` – Specify an AMI ID that want to reuse. To
  find valid IDs, run the `describe-db-engine-versions` command,
  and then search the output for `ImageID`. By default, RDS Custom for Oracle
  uses the most recent available AMI.
  The following example creates an Oracle multitenant CEV named
  `19.cdb_cev1`. The example reuses an existing AMI rather than use the
  latest available AMI. Make sure that the name of your CEV starts with the major
  engine version number.

For Linux, macOS, or Unix:

```
aws rds create-custom-db-engine-version \
    --engine `custom-oracle-se2-cdb` \
    --engine-version `19.cdb_cev1` \
    --database-installation-files-s3-bucket-name `us-east-1-123456789012-custom-installation-files` \
    --database-installation-files-s3-prefix `123456789012/cev1` \
    --kms-key-id `my-kms-key` \
    --description "`test cev`" \
    --manifest `manifest_string` \
    --image-id `ami-012a345678901bcde`
```

For Windows:

```
aws rds create-custom-db-engine-version ^
    --engine `custom-oracle-se2-cdb` ^
    --engine-version `19.cdb_cev1` ^
    --database-installation-files-s3-bucket-name `us-east-1-123456789012-custom-installation-files` ^
    --database-installation-files-s3-prefix `123456789012/cev1` ^
    --kms-key-id `my-kms-key` ^
    --description "`test cev`" ^
    --manifest `manifest_string` ^
    --image-id `ami-012a345678901bcde`
```

Get details about your CEV by using the `describe-db-engine-versions` command.

```
aws rds describe-db-engine-versions \
    --engine custom-oracle-se2-cdb \
    --include-all
```

The following partial sample output shows the engine, parameter groups,
manifest, and other information.

```
{
    "DBEngineVersions": [
        {
            "Engine": "custom-oracle-se2-cdb",
            "EngineVersion": "19.cdb_cev1",
            "DBParameterGroupFamily": "custom-oracle-se2-cdb-19",
            "DBEngineDescription": "Containerized Database for Oracle Custom SE2",
            "DBEngineVersionDescription": "test cev",
            "Image": {
                "ImageId": "ami-012a345678901bcde",
                "Status": "active"
            },
            "ValidUpgradeTarget": [],
            "SupportsLogExportsToCloudwatchLogs": false,
            "SupportsReadReplica": true,
            "SupportedFeatureNames": [],
            "Status": "available",
            "SupportsParallelQuery": false,
            "SupportsGlobalDatabases": false,
            "MajorEngineVersion": "19",
            "DatabaseInstallationFilesS3BucketName": "us-east-1-123456789012-custom-installation-files",
            "DatabaseInstallationFilesS3Prefix": "123456789012/cev1",
            "DBEngineVersionArn": "arn:aws:rds:us-east-1:123456789012:cev:custom-oracle-se2-cdb/19.cdb_cev1/abcd12e3-4f5g-67h8-i9j0-k1234l56m789",
            "KMSKeyId": "arn:aws:kms:us-east-1:732027699161:key/1ab2345c-6d78-9ef0-1gh2-3456i7j89k01",
            "CreateTime": "2023-03-07T19:47:58.131000+00:00",
            "TagList": [],
            "SupportsBabelfish": false,
...
```

## Failure to create a CEV

If the process to create a CEV fails, RDS Custom issues `RDS-EVENT-0198` with the message `Creation failed for custom
 engine version `major-engine-version.cev_name``, and includes details about the failure. For
example, the event prints missing files.

You can't modify a failed CEV. You can only delete it, then try again to create a CEV after fixing the causes of the
failure. For information about troubleshooting the reasons for CEV creation failure, see [Troubleshooting custom engine version creation for RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting.cev "custom-troubleshooting.md#custom-troubleshooting.cev").
