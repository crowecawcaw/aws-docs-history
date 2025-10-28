# Viewing CEV details for Amazon RDS Custom for SQL Server

You can view details about your CEV by using the AWS Management Console or the AWS CLI.

###### To view CEV details

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Custom engine versions**.

The **Custom engine versions** page shows all CEVs that currently exist. If
you haven't created any CEVs, the page is empty. 3. Choose the name of the CEV that you want to view. 4. Choose **Configuration** to view the details.

![View the configuration details for a CEV.](images/rds_custom_sqlserver_cev_viewdetails.PNG)
To view details about a CEV by using the AWS CLI, run the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

You can also specify the following options:

- `--include-all`, to view all CEVs with any lifecycle state. Without the
  `--include-all` option, only the CEVs in an `available` lifecycle state will be returned.

```
aws rds describe-db-engine-versions --engine custom-sqlserver-ee --engine-version 15.00.4249.2.my_cevtest --include-all
{
    "DBEngineVersions": [
        {
            "Engine": "custom-sqlserver-ee",
            "MajorEngineVersion": "15.00",
            "EngineVersion": "15.00.4249.2.my_cevtest",
            "DBParameterGroupFamily": "custom-sqlserver-ee-15.0",
            "DBEngineDescription": "Microsoft SQL Server Enterprise Edition for custom RDS",
            "DBEngineVersionArn": "arn:aws:rds:us-east-1:`{my-account-id}`:cev:custom-sqlserver-ee/15.00.4249.2.my_cevtest/a1234a1-123c-12rd-bre1-1234567890",
            "DBEngineVersionDescription": "Custom SQL Server EE 15.00.4249.2 cev test",
            "Image": {
                "ImageId": "ami-0r93cx31t5r596482",
                "Status": "pending-validation"
            },
            "DBEngineMediaType": "AWS Provided",
            "CreateTime": "2022-11-20T19:30:01.831000+00:00",
            "ValidUpgradeTarget": [],
            "SupportsLogExportsToCloudwatchLogs": false,
            "SupportsReadReplica": false,
            "SupportedFeatureNames": [],
            "Status": "pending-validation",
            "SupportsParallelQuery": false,
            "SupportsGlobalDatabases": false,
            "TagList": [],
            "SupportsBabelfish": false
        }
    ]
}

```

You can use filters to view CEVs with a certain lifecycle status. For example, to view CEVs that have a
lifecycle status of either `pending-validation`, `available`, or `failed`:

```
aws rds describe-db-engine-versions engine `custom-sqlserver-ee`
                region `us-west-2` include-all query 'DBEngineVersions[?Status == pending-validation ||
                Status == available || Status == failed]'
```
