# Integrating Amazon Aurora MySQL with other AWS

services

Amazon Aurora MySQL integrates with other AWS services so that you can extend your Aurora MySQL
DB cluster to use additional capabilities in the AWS Cloud. Your Aurora MySQL DB cluster can
use AWS services to do the following:

- Synchronously or asynchronously invoke an AWS Lambda function using the native functions
  `lambda_sync` or `lambda_async`. For more information, see [Invoking a Lambda function from an Amazon Aurora MySQL DB
  cluster](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Load data from text or XML files stored in an Amazon Simple Storage Service (Amazon S3) bucket into your DB
  cluster using the `LOAD DATA FROM S3` or `LOAD XML FROM S3`
  command. For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from
  text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Save data to text files stored in an Amazon S3 bucket from your DB cluster using the
  `SELECT INTO OUTFILE S3` command. For more information, see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3
  bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Automatically add or remove Aurora Replicas with Application Auto Scaling. For more information,
  see [Amazon Aurora Auto Scaling with Aurora Replicas](Aurora.Integrating.md "Aurora.Integrating.md").
- Perform sentiment analysis with Amazon Comprehend, or a wide variety of machine learning algorithms with SageMaker AI.
  For more information, see [Using Amazon Aurora machine learning](aurora-ml.md "aurora-ml.md").
  Aurora secures the ability to access other AWS services by using AWS Identity and Access Management (IAM). You
  grant permission to access other AWS services by creating an IAM role with the necessary
  permissions, and then associating the role with your DB cluster. For details and
  instructions on how to permit your Aurora MySQL DB cluster to access other AWS services on your
  behalf, see [Authorizing Amazon Aurora MySQL to
  access other AWS services on your behalf](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
