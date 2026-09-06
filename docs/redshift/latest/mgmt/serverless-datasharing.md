

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Data sharing in Amazon Redshift Serverless
<a name="serverless-datasharing"></a>

With *data sharing*, you have live access to data so that your users can see the most up-to-date and consistent information as it's updated in Amazon Redshift Serverless.

You can share data for read purposes across different Amazon Redshift Serverless instances within or across AWS accounts.

You can get started with data sharing by using either the SQL interface or the Amazon Redshift console. For more information, see [Data sharing in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html) in the *Amazon Redshift Database Developer Guide*.

With data sharing, Amazon Redshift Serverless namespaces and provisioned clusters can share live data with each other, whether they are within an AWS account across AWS accounts, or across AWS Regions. For more information, see [Regions where data sharing is available](https://docs.aws.amazon.com/redshift/latest/dg/data_sharing_regions.html).

To get started sharing data within an AWS account, open the AWS Management Console, and then choose the Amazon Redshift console. Choose **Namespace configuration** and then **Datashares**. 

To start querying data in a datashare, create a database in a namespace that has a workgroup associated with it. From a specified datashare, choose a namespace that has a workgroup associated with it and create a database to query data. 

## Considerations
<a name="getting_started_serverless_datasharing_usage"></a>

Consider the following when working with data sharing in Amazon Redshift Serverless:
+ Amazon Redshift supports data sharing as producers or consumers on provisioned RG and RA3 clusters, and serverless endpoint workgroups.
+ Amazon Redshift Serverless is encrypted by default.

For a list of datasharing limitations, including database objects supported, encryption requirements, and sort-key requirements, see [Considerations for data sharing in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-considerations.html) in the *Amazon Redshift Database Developer Guide*. 