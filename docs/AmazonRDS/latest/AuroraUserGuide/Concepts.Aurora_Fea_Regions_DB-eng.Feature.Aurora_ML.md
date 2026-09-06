

# Supported Regions and DB engines for Aurora machine learning
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML"></a>

By using Amazon Aurora machine learning, you can integrate your Aurora DB cluster with one of the following AWS machine learning services, depending on your needs. They each support specific machine learning use cases.

Amazon Bedrock is a fully managed service that makes leading foundation models from AI companies available through an API, along with developer tooling to help build and scale generative AI applications.

Amazon Comprehend is a *natural language processing* (NLP) service that's used to extract insights from documents. By using Aurora machine learning with Amazon Comprehend, you can determine the sentiment of text in your database tables.

SageMaker AI is a full-featured *machine learning* service. Data scientists use Amazon SageMaker AI to build, train, and test machine learning models for a variety of inference tasks, such as fraud detection. By using Aurora machine learning with SageMaker AI, database developers can invoke the SageMaker AI functionality in SQL code.

Not all AWS Regions support all machine learning services. Only certain AWS Regions support Aurora machine learning and thus provide access to these services from an Aurora DB cluster. The integration process for Aurora machine learning also differs by database engine. For more information, see [Using Amazon Aurora machine learning](aurora-ml.md).

**Topics**
+ [Aurora machine learning with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML.amy)
+ [Aurora machine learning with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML.apg)

## Aurora machine learning with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML.amy"></a>

Amazon Bedrock is supported only on Aurora MySQL version 3.06 and higher. For information on Region availability for Amazon Bedrock, see [Model support by AWS Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) in the *Amazon Bedrock User Guide*.

Aurora machine learning with Amazon Comprehend and Amazon SageMaker AI is supported for Aurora MySQL in the AWS Regions listed in the table. In addition to having your version of Aurora MySQL available, the AWS Region must also support the service that you want to use. For a list of AWS Regions where Amazon SageMaker AI is available, see [Amazon SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *Amazon Web Services General Reference*. For a list of AWS Regions where Amazon Comprehend is available, see [Amazon Comprehend endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/comprehend.html) in the *Amazon Web Services General Reference*.


| Region | Aurora MySQL version 3 | Aurora MySQL version 8.4 | Aurora MySQL version 2 | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| US East (Ohio) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| US West (N. California) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| US West (Oregon) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Africa (Cape Town) | Not available | Not available | Not available | 
| Asia Pacific (Hong Kong) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Hyderabad) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Jakarta) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Malaysia) | Version 3.04.0 and higher | All available versions | Not available | 
| Asia Pacific (Melbourne) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Mumbai) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (New Zealand) | Not available | Not available | Not available | 
| Asia Pacific (Osaka) | Version 3.01.0 and higher | All available versions | Version 2.07.3 and higher | 
| Asia Pacific (Seoul) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Singapore) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Sydney) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Asia Pacific (Taipei) | Not available | Not available | Not available | 
| Asia Pacific (Thailand) | Not available | Not available | Not available | 
| Asia Pacific (Tokyo) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Canada (Central) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Canada West (Calgary) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| China (Beijing) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| China (Ningxia) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Frankfurt) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Ireland) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (London) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Milan) | Not available | Not available | Not available | 
| Europe (Paris) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Spain) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Stockholm) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Europe (Zurich) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Israel (Tel Aviv) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Mexico (Central) | Not available | Not available | Not available | 
| Middle East (Bahrain) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| Middle East (UAE) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| South America (São Paulo) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| AWS GovCloud (US-East) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 
| AWS GovCloud (US-West) | Version 3.01.0 and higher | All available versions | Version 2.07 and higher | 

## Aurora machine learning with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML.apg"></a>

For information on version support for Amazon Bedrock on Aurora PostgreSQL, see [Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock](AuroraPostgreSQL.VectorDB.md).

Aurora machine learning with Amazon Comprehend and Amazon SageMaker AI is supported for Aurora PostgreSQL in the AWS Regions listed in the table. In addition to having your version of Aurora PostgreSQL available, the AWS Region must also support the service that you want to use. For a list of AWS Regions where Amazon SageMaker AI is available, see [Amazon SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *Amazon Web Services General Reference*. For a list of AWS Regions where Amazon Comprehend is available, see [Amazon Comprehend endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/comprehend.html) in the *Amazon Web Services General Reference*.

The following Regions and engine versions are available for Aurora machine learning with Aurora PostgreSQL.


| Region | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | Aurora PostgreSQL 12 | Aurora PostgreSQL 11 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| US East (N. Virginia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| US East (Ohio) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| US West (N. California) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| US West (Oregon) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Africa (Cape Town) | Not available | Not available | Not available | Not available | Not available | Not available | Not available | 
| Asia Pacific (Hong Kong) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Hyderabad) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Jakarta) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Malaysia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Melbourne) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Mumbai) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (New Zealand) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Osaka) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Seoul) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Singapore) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Sydney) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Taipei) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Thailand) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Asia Pacific (Tokyo) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Canada (Central) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Canada West (Calgary) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| China (Beijing) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| China (Ningxia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Frankfurt) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Ireland) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (London) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Milan) | Not available | Not available | Not available | Not available | Not available | Not available | Not available | 
| Europe (Paris) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Spain) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Stockholm) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Europe (Zurich) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Israel (Tel Aviv) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Mexico (Central) | Not available | Not available | Not available | Not available | Not available | Not available | Not available | 
| Middle East (Bahrain) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| Middle East (UAE) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| South America (São Paulo) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| AWS GovCloud (US-East) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 
| AWS GovCloud (US-West) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.3 and higher | Version 12.4 and higher | Version 11.9, 11.12 and higher | 