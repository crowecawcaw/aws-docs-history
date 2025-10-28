# Prerequisites for setting up permissions on Amazon Redshift datashares

###### Update default Data Catalog settings

To enable Lake Formation permissions for the Data Catalog resources, we recommend that you disable the default **Data Catalog settings** in Lake Formation.
For more information, see [Change the default permission model or use
hybrid access mode](initial-lf-config.md#setup-change-cat-settings "initial-lf-config.md#setup-change-cat-settings").

###### Update permissions

In addition to data lake administrator permissions
(`AWSLakeFormationDataAdmin`), the following permissions are also required to
accept an Amazon Redshift datashare in Lake Formation:

- `glue:PassConnection on aws:redshift`
- `redshift:AssociateDataShareConsumer`
- `redshift:DescribeDataSharesForConsumer`
- `redshift:DescribeDataShares`

The data lake administrator IAM user has the following permissions implicitly.

- data_location_access
- create_database
- lakefomation:registerResource
