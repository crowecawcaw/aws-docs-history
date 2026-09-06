

# Integrating BYOM DB Instance with AWS License Manager
<a name="sqlserver-byom-license-manager"></a>

To make it easier to monitor SQL Server license usage in the BYOM model, [AWS License Manager](https://aws.amazon.com/license-manager/) integrates with RDS for SQL Server. License Manager supports tracking of RDS for SQL Server engine editions based on virtual cores (vCPUs). You can also use License Manager with AWS Organizations to manage all of your organizational accounts centrally.

The following table shows the product information filters for RDS for SQL Server.


| Filter | Name | Description | 
| --- | --- | --- | 
| Engine Edition | sqlserver-ee | SQL Server Enterprise Edition (EE) | 
| Engine Edition | sqlserver-se | SQL Server Standard Edition (SE) | 

To track license usage of your SQL Server DB instances, you can create a self-managed license using AWS License Manager. In this case, RDS for SQL Server resources that match the product information filter are automatically associated with the self-managed license. Discovery of SQL Server DB instances can take up to 24 hours. You can also track a license across accounts by using AWS Resource Access Manager.

## To create a self-managed license in AWS License Manager
<a name="sqlserver-byom-license-manager.create-console"></a>

To create a self-managed license in AWS License Manager to track the license usage of your RDS for SQL Server DB instances:

1. Go to [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Choose **Create self-managed license**.

   For instructions, see [Create a self-managed license](https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html) in the *AWS License Manager User Guide*.

   Add a rule for an RDS Product Information Filter in the Product Information panel. When selecting the resource type, choose **SQL Server Database**.

   For more information, see [ProductInformation](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ProductInformation.html) in the *AWS License Manager API Reference*.

1. (Cross-account tracking only) Use AWS Resource Access Manager to share your self-managed licenses with any AWS account or through AWS Organizations. For more information, see [Sharing your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html).

## To create a self-managed license by using the AWS CLI
<a name="sqlserver-byom-license-manager.create-cli"></a>

To create a self-managed license by using the AWS CLI, call the [`create-license-configuration`](https://docs.aws.amazon.com/cli/latest/reference/license-manager/create-license-configuration.html) command. Use the `--cli-input-json` or `--cli-input-yaml` parameters to pass the parameters to the command.

**Example**

The following example creates a self-managed license for SQL Server Enterprise Edition.

```
aws license-manager create-license-configuration --cli-input-json file://rds-sqlserver-ee.json
```

The following is the sample `rds-sqlserver-ee.json` file used in the example.

```
{
    "Name": "rds-sqlserver-ee",
    "Description": "RDS SQL Server Enterprise Edition",
    "LicenseCountingType": "vCPU",
    "LicenseCountHardLimit": false,
    "ProductInformationList": [
        {
            "ResourceType": "RDS",
            "ProductInformationFilterList": [
                {
                    "ProductInformationFilterName": "Engine Edition",
                    "ProductInformationFilterValue": ["sqlserver-ee"],
                    "ProductInformationFilterComparator": "EQUALS"
                }
            ]
        }
    ]
}
```

For more information about product information, see [Automated discovery of resource inventory](https://docs.aws.amazon.com/license-manager/latest/userguide/automated-discovery.html) in the *AWS License Manager User Guide*.

For more information about the `--cli-input` parameter, see [Generating AWS CLI skeleton and input parameters from a JSON or YAML input file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html) in the *AWS CLI User Guide*.