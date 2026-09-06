

# Integrating third-party services with Lake Formation
<a name="Integrating-with-LakeFormation"></a>

Integrating with AWS Lake Formation enables third-party services to securely access data in their Amazon S3 based data lakes. You can use Lake Formation as your authorization engine to manage or enforce permissions to your data lake with integrated AWS services such as AWS Glue ETL, Amazon Athena, Amazon EMR, and Redshift Spectrum. Lake Formation provides two options for integrating services:

1. The Lake Formation application integration settings: Lake Formation can vend scoped-down temporary credentials in the form of AWS STS tokens to registered Amazon S3 locations based on the effective permissions, so that authorized applications can access data on behalf of users.

1.  Central enforcement: Lake Formation[ querying API](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StartQueryPlanning.html) operations retrieve data from Amazon S3 and filter the results based on effective permissions. The engine or application integrating with the querying API operation can depend on Lake Formation to evaluate the calling identity’s permissions and securely filter the data based on these permissions. Third-party query engines only see and operate on filtered data. 

 Lake Formation credential vending doesn't integrate with spark sql queries. Credential vending only works with queries that run through the AWS Glue ETL library. 

**Topics**
+ [Using Lake Formation application integration](using-cred-vending.md)