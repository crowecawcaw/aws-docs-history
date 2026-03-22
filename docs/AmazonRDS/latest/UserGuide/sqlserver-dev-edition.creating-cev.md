# Creating a custom engine version for RDS for SQL Server

A custom engine version (CEV) for RDS for SQL Server consists of your SQL Server Developer Edition
installation media imported into Amazon RDS. It is necessary to upload the base ISO installer and cumulative update files (.exe) to your Amazon S3 bucket. Once uploaded, you should provide the Amazon S3 location to RDS for it to download, validate, and subsequently create your CEV.

## Naming limitations

When creating a CEV, you must follow specific naming conventions:

- CEV name must follow the pattern `major-version.minor-version.customized-string`.
- `customized-string` can contain 1-50 alphanumeric characters, underscores, dashes, and periods. For example: `16.00.4215.2.my-dev-cev` for SQL Server 2022.

To list all supported engine versions, use the following command:

```
aws rds describe-db-engine-versions --engine sqlserver-dev-ee --output json --query "{DBEngineVersions: DBEngineVersions[?Status=='requires-custom-engine-version'].{Engine: Engine, EngineVersion: EngineVersion, Status: Status, DBEngineVersionDescription: DBEngineVersionDescription}}"

{
    "DBEngineVersions": [
        {
            "Engine": "sqlserver-dev-ee",
            "EngineVersion": "`16.00.4215.2.v1`",
            "Status": "requires-custom-engine-version",
            "DBEngineDescription": "Microsoft SQL Server Enterprise Developer Edition",
            "DBEngineVersionDescription": "SQL Server 2022 16.00.4215.2.v1"
        }
    ]
}
```

###### To create the custom engine version

- Use the [create-custom-db-engine-version](../../../cli/latest/reference/rds/create-custom-db-engine-version.md "../../../cli/latest/reference/rds/create-custom-db-engine-version.md") command.

The following options are required:

    + `--engine`
    + `--engine-version`
    + `--database-installation-files-s3-bucket-name`
    + `--database-installation-files`
    + `--region`

You can also specify the following options:

    + `--database-installation-files-s3-prefix`
    + `--description`
    + `--tags`

```
aws rds create-custom-db-engine-version \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.cev-dev-ss2022-cu21` \
--region us-west-2 \
--database-installation-files-s3-bucket-name my-s3-installation-media-bucket \
--database-installation-files-s3-prefix sqlserver-dev-media \
--database-installation-files "SQLServer2022-x64-ENU-Dev.iso" "SQLServer2022-KB5065865-x64.exe"
```

CEV creation typically takes 15-30 minutes. To monitor the CEV
creation progress, use the following command:

```
# Check CEV status
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--region us-west-2
```

## Lifecycle of an RDS for SQL Server CEV

When working with SQL Server Developer Edition on RDS for SQL Server,
your custom engine versions transition through various lifecycle states.

| Lifecycle State                 | Description                                                                                           | When It Occurs                                                                                                                                                                   | Available Actions                                                                                                                                                                                      |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pending-validation              | Initial state when CEV is created                                                                     | This is the initial state after creation with the `create-custom-db-engine-version` command.                                                                                     | Monitor status via `describe-db-engine-version`.                                                                                                                                                       |
| validating                      | CEV Validation state                                                                                  | Amazon RDS is validating your custom engine version (CEV). This asynchronous process may take some time to complete.                                                             | Monitor the status until validation is complete.                                                                                                                                                       |
| available                       | The custom engine version (CEV) validation completed successfully.                                    | Custom Engine Version (CEV) is now available. Amazon RDS successfully validated your SQL Server ISO and cumulative update files. You can now create DB instances using this CEV. | Create DB instances using this CEV                                                                                                                                                                     |
| failed                          | RDS for SQL Server can't create the custom engine version (CEV) because the validation check failed.  | ISO and cumulative media validation failed.                                                                                                                                      | ISO validation failed. Check the failure reason in `describe-db-engine-version`, fix any file issues such as hash mismatches or corrupted content, and then recreate your custom engine version (CEV). |
| deleting                        | The custom engine version (CEV) is deleting                                                           | After customer calls `delete-custom-db-engine-version` until deletion workflow completes.                                                                                        | Monitor status via `describe-db-engine-version`.                                                                                                                                                       |
| incompatible-installation-media | Amazon RDS was unable to validate the installation media provided for the custom engine version (CEV) | The custom engine version (CEV) validation has failed. This is a terminal state.                                                                                                 | See failureReason via `describe-db-engine-versions` for info on why validation failed; delete CEV.                                                                                                     |

### Describe CEV Status

You can see the state of your CEVs using the AWS CLI:

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--region us-west-2 \
--query 'DBEngineVersions[0].{Version:EngineVersion,Status:Status}'
```

Sample output

```
| DescribeDBEngineVersions                     |
+------------+---------------------------------+
| Status | Version                             |
+------------+---------------------------------+
| available | 16.00.4215.2.cev-dev-ss2022-cu21    |
+------------+---------------------------------+
```

When a CEV shows `failed` status, you can determine the reason using the following command:

```
aws rds describe-db-engine-versions \
--engine sqlserver-dev-ee \
--engine-version `16.00.4215.2.my-dev-cev` \
--region us-west-2 \
--query 'DBEngineVersions[0].{Version:EngineVersion,Status:Status,FailureReason:FailureReason}'
```
