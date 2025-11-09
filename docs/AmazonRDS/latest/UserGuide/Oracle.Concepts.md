# RDS for Oracle licensing options

Amazon RDS for Oracle has two licensing options: License Included (LI) and Bring Your Own License (BYOL). After you create an Oracle DB instance on
Amazon RDS, you can change the licensing model by modifying the DB instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### Important

Make sure that you have the appropriate Oracle Database license, with Software Update
License and Support, for your DB instance class and Oracle Database edition. Also make sure that you
have licenses for any separately licensed Oracle Database features.

###### Topics

- [License Included model for
  SE2](#Oracle.Concepts.Licensing.LicenseIncluded "#Oracle.Concepts.Licensing.LicenseIncluded")
- [Bring Your Own License (BYOL) for EE
  and SE2](#Oracle.Concepts.Licensing.BYOL "#Oracle.Concepts.Licensing.BYOL")
- [Licensing Oracle Multi-AZ deployments](#Oracle.Concepts.Licensing.MAZ "#Oracle.Concepts.Licensing.MAZ")

## License Included model for

SE2

In the License Included model, you don't need to purchase Oracle Database licenses
separately. AWS holds the license for the Oracle database software. The License
Included model is only supported on Amazon RDS for Oracle Database Standard Edition 2
(SE2).

In this model, if you have an AWS Support account with case support, contact Support for
both Amazon RDS and Oracle Database service requests. Your use of RDS for Oracle the LI option is
subject to Section 10.3.1 of the [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").

## Bring Your Own License (BYOL) for EE

and SE2

In the BYOL model, you can use your existing Oracle Database licenses to deploy
databases on Amazon RDS. Amazon RDS supports the BYOL model only for Oracle Database Enterprise
Edition (EE) and Oracle Database Standard Edition 2 (SE2).

Make sure that you have the appropriate Oracle Database license (with Software Update
License and Support) for the DB instance class and Oracle Database edition you wish to run.
You must also follow Oracle's policies for licensing Oracle Database software in the
cloud computing environment. For more information on Oracle's licensing policy for
Amazon EC2, see [Licensing Oracle software in the cloud computing environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf "http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf").

In this model, you continue to use your active Oracle support account, and you contact Oracle directly
for Oracle Database service requests. If you have an AWS Support account with case support, you can contact
Support for Amazon RDS issues.

### Integrating with AWS License Manager

To make it easier to monitor Oracle license usage in the BYOL model, [AWS License Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/") integrates with Amazon RDS for Oracle. License Manager supports
tracking of RDS for Oracle engine editions and licensing packs based on virtual cores (vCPUs). You
can also use License Manager with AWS Organizations to manage all of your organizational accounts centrally.

The following table shows the product information filters for RDS for Oracle.

| Filter                 | Name                                                               | Description                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Engine Edition         | `oracle-ee`                                                        | Oracle Database Enterprise Edition (EE)                                                                                                     |
| `oracle-se2`           | Oracle Database Standard Edition 2 (SE2)                           |
| License Pack           | `data guard`                                                       | See [Working with read replicas for Amazon RDS for Oracle](oracle-read-replicas.md "oracle-read-replicas.md")<br>(Oracle Active Data Guard) |
| `olap`                 | See [Oracle OLAP](Oracle.Options.md "Oracle.Options.md")           |
| `ols`                  | See [Oracle Label Security](Oracle.Options.md "Oracle.Options.md") |
| `diagnostic pack sqlt` | See [Oracle SQLT](Oracle.Options.md "Oracle.Options.md")           |
| `tuning pack sqlt`     | See [Oracle SQLT](Oracle.Options.md "Oracle.Options.md")           |

To track license usage of your Oracle DB instances, you can create a self-managed
license using AWS License Manager. In this case, RDS for Oracle resources that match the
product information filter are automatically associated with the self-managed
license. Discovery of Oracle DB instances can take up to 24 hours. You can also track a
license across accounts by using AWS Resource Access Manager.

###### To create a self-managed license in AWS License Manager to track the license

usage of your RDS for Oracle DB instances

1. Go to [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Choose **Create self-managed license**.

For instructions, see [Create a
self-managed license](../../../license-manager/latest/userguide/create-license-configuration.md "../../../license-manager/latest/userguide/create-license-configuration.md") in the _AWS License Manager User
Guide_.

Add a rule for an **RDS Product Information Filter** in the
**Product Information** panel.

For more information, see [ProductInformation](../../../license-manager/latest/APIReference/API_ProductInformation.md "../../../license-manager/latest/APIReference/API_ProductInformation.md") in the _AWS License Manager API
Reference_. 3. (Cross-account tracking only) Use AWS Resource Access Manager to share your
self-managed licenses with any AWS account or through AWS Organizations.
For more information, see [Sharing
your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md").
To create a self-managed license by using the AWS CLI, call the [create-license-configuration](../../../cli/latest/reference/license-manager/create-license-configuration.md "../../../cli/latest/reference/license-manager/create-license-configuration.md") command. Use the
`--cli-input-json` or `--cli-input-yaml`
parameters to pass the parameters to the command.

###### Example

The following example creates a self-managed license for Oracle
Enterprise Edition.

```
aws license-manager create-license-configuration --cli-input-json file://rds-oracle-ee.json
```

The following is the sample `rds-oracle-ee.json` file used in the
example.

```
{
    "Name": "rds-oracle-ee",
    "Description": "RDS Oracle Enterprise Edition",
    "LicenseCountingType": "vCPU",
    "LicenseCountHardLimit": false,
    "ProductInformationList": [
        {
            "ResourceType": "RDS",
            "ProductInformationFilterList": [
                {
                    "ProductInformationFilterName": "Engine Edition",
                    "ProductInformationFilterValue": ["oracle-ee"],
                    "ProductInformationFilterComparator": "EQUALS"
                }
            ]
        }
    ]
}
```

For more information about product information, see [Automated discovery of resource
inventory](../../../license-manager/latest/userguide/automated-discovery.md "../../../license-manager/latest/userguide/automated-discovery.md") in the _AWS License Manager User Guide_.

For more information about the `--cli-input` parameter, see [Generating AWS CLI skeleton and input parameters
from a JSON or YAML input file](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md") in the _AWS CLI User
Guide_.

### Migrating between Oracle

Database editions

If you have an unused BYOL Oracle Database license appropriate for the edition and
class of DB instance that you plan to run, you can migrate from Standard Edition 2 (SE2)
to Enterprise Edition (EE). You can't migrate from EE to other editions.

###### To change your Oracle Database edition and retain your data

1. Create a snapshot of the DB instance.

For more information, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md"). 2. Restore the snapshot to a new DB instance, and select the Oracle database edition you want
to use.

For more information, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md"). 3. (Optional) Delete the old DB instance, unless you want to keep it running and have the
appropriate Oracle Database licenses for it.

For more information, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").

## Licensing Oracle Multi-AZ deployments

Amazon RDS supports Multi-AZ deployments for Oracle as a high-availability, failover solution. We recommend
Multi-AZ for production workloads. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

If you use the Bring Your Own License model, you must have a license for both the primary DB instance
and the standby DB instance in a Multi-AZ deployment.
