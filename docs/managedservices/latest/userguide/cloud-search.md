# Use AMS SSP to provision Amazon CloudSearch in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon CloudSearch capabilities directly in your AMS managed account. Amazon CloudSearch is a managed service in the AWS Cloud that you use to
cost-effective to set up, manage, and scale a search solution for your website or application. Amazon CloudSearch supports 34 languages and popular search features such as highlighting,
autocomplete, and geospatial search. To learn more, see [Amazon CloudSearch](https://aws.amazon.com/cloudsearch/ "https://aws.amazon.com/cloudsearch/").

###### Note

AWS has closed new customer access to Amazon CloudSearch, effective July 25, 2024. Amazon CloudSearch existing customers can continue to use the service as normal. AWS continues to invest in
security, availability, and performance improvements for Amazon CloudSearch, but we do not plan to introduce new features.

To understand the differences between Amazon CloudSearch and Amazon OpenSearch Service, and how you can transition to OpenSearch Service, reach out to your cloud architect (CA) for guidance.
For more information on transitioning to OpenSearch Service, see
[Transition from Amazon CloudSearch to Amazon OpenSearch Service service](https://aws.amazon.com/blogs/big-data/transition-from-amazon-cloudsearch-to-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/transition-from-amazon-cloudsearch-to-amazon-opensearch-service/").

## Amazon CloudSearch in AWS Managed Services FAQ

**Q: How do I request access to Amazon CloudSearch in my AMS account?**

Request access to Amazon CloudSearch by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account:
`customer_csearch_admin_role` and
`customer_csearch_dev_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon CloudSearch in my AMS account?**

Full functionality of Amazon CloudSearch is available in your AMS account. All AMS-supported database
solutions are currently supported on Amazon CloudSearch. Note that, currently, DynamoDB is the only managed
AWS database solution that can’t be indexed.

**Q: What are the prerequisites or dependencies to using Amazon CloudSearch in my AMS account?**

Amazon CloudSearch depends on Amazon S3 working with Identity Providers to automatically
analyze input data and determine the table fields. Access to Amazon S3 is not
provided with this RFC, and must be requested separately in a service
request.
