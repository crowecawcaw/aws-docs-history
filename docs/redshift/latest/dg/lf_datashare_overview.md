

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# AWS Lake Formation-managed datashares
<a name="lf_datashare_overview"></a>

With Amazon Redshift, you can access and share live data across AWS accounts and Amazon Redshift clusters through AWS Lake Formation-managed datashares. AWS Lake Formation datashares enable data providers to securely share live data from their Amazon S3 data lake with any consumer, including other AWS accounts and Amazon Redshift clusters.

 Using AWS Lake Formation, you can centrally define and enforce database, table, column, and row-level access permissions of Amazon Redshift datashares and restrict user access to objects within a datashare. By sharing data through Lake Formation, you can define permissions in Lake Formation and apply those permissions to any datashare and its objects. For example, if you have a table containing employee information, you can use Lake Formation's column-level filters to prevent employees who don't work in the HR department from seeing personally identifiable information (PII), such as a social security number. For more information about data filters, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) in the *AWS Lake Formation Developer Guide*. 

You can also use tags in Lake Formation to configure permissions on Lake Formation resources. For more information, see [Lake Formation Tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/tag-based-access-control.html).

 Amazon Redshift currently supports data sharing through Lake Formation when sharing within the same account or across accounts. Cross-Region sharing is currently not supported. 

The following is a high-level overview of how to use Lake Formation to control datashare permissions:

1. In Amazon Redshift, the producer cluster or workgroup administrator creates a datashare on the producer cluster or workgroup and grants usage to a Lake Formation account.

1. The producer cluster or workgroup administrator authorizes the Lake Formation account to access the datashare.

1. The Lake Formation administrator discovers and registers the datashares. They must also discover the AWS Glue ARNs they have access to and associate the datashares with an AWS Glue Data Catalog ARN. If you're using the AWS CLI you can discover and accept datashares with the Redshift CLI operations `describe-data-shares` and `associate-data-share-consumer`. To register a datashare, use the Lake Formation CLI operation `register-resource`.

1. The Lake Formation administrator creates a federated database in the AWS Glue Data Catalog, and configures Lake Formation permissions to control user access to objects within the datashare. For more information about federated databases in AWS Glue, see [Managing permissions for data in an Amazon Redshift datashare](https://docs.aws.amazon.com/lake-formation/latest/dg/data-sharing-redshift.html).

1. The Lake Formation administrator discovers the AWS Glue databases they have access to and associates the datashare with an AWS Glue Data Catalog ARN.

1. The Redshift administrator discovers the AWS Glue database ARNs they have access to, creates an external database in the Amazon Redshift consumer cluster using a AWS Glue database ARN, and grants usage to [database users authenticated with IAM credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/options-for-providing-iam-credentials.html) to start querying the Amazon Redshift database.

1. Database users can use the views SVV\_EXTERNAL\_TABLES and SVV\_EXTERNAL\_COLUMNS to find all of the tables or columns within the AWS Glue database that they have access to, and then they can query the AWS Glue database’s tables.

1. When the producer cluster or workgroup administrator decides to no longer share the data with the consumer cluster, the producer administrator can revoke usage, deauthorize, or delete the datashare from Redshift. The associated permissions and objects in Lake Formation are not automatically deleted.

For more information about sharing a datashare with AWS Lake Formation as a producer cluster or workgroup administrator, see [Working with Lake Formation-managed datashares as a producer](lake-formation-getting-started-producer.md). To consume the shared data from the producer cluster or workgroup, see [Working with Lake Formation-managed datashares as a consumer](lake-formation-getting-started-consumer.md).