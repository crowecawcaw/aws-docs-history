# Cross-account cross-Region access to DynamoDB tables

AWS Glue ETL jobs support both cross-region and cross-account access to DynamoDB tables. AWS Glue ETL jobs support both reading data from another AWS Account's DynamoDB table, and writing data into another AWS Account's DynamoDB table. AWS Glue also supports both reading from a DynamoDB table in another region, and writing into a DynamoDB table in another region. This section gives instructions on setting up the access, and provides an example script.

The procedures in this section reference an IAM tutorial for
creating an IAM role and granting access to the role. The tutorial also discusses assuming a
role, but here you will instead use a job script to assume the role in AWS Glue. This tutorial
also contains information about general cross-account practices. For more information, see
[Tutorial: Delegate
Access Across AWS Accounts Using IAM Roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") in the
_IAM User Guide_.

## Create a role

Follow [step 1 in the tutorial](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md#tutorial_cross-account-with-roles-1 "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md#tutorial_cross-account-with-roles-1") to create an IAM role in account A. When defining the permissions of the role, you can choose to attach existing policies such as `AmazonDynamoDBReadOnlyAccess`, or `AmazonDynamoDBFullAccess` to allow the role to read/write DynamoDB. The following example shows creating a role named `DynamoDBCrossAccessRole`, with the permission policy `AmazonDynamoDBFullAccess`.

## Grant access to the role

Follow [step 2 in the tutorial](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md#tutorial_cross-account-with-roles-2 "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md#tutorial_cross-account-with-roles-2") in the _IAM User Guide_ to
allow account B to switch to the newly-created role. The following example creates a new
policy with the following statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/DynamoDBCrossAccessRole"
 }
}`

```

Then, you can attach this policy to the group/role/user you would like to use to access DynamoDB.

## Assume the role in the AWS Glue job script

Now, you can log in to account B and create an AWS Glue job. To create a job, refer to the
instructions at [Configuring job properties for Spark jobs in AWS Glue](add-job.md "add-job.md").

In the job script you need to use the `dynamodb.sts.roleArn` parameter to
assume the `DynamoDBCrossAccessRole` role. Assuming this role allows you to
get the temporary credentials, which need to be used to access DynamoDB in account B.
Review these example scripts.

For a cross-account read across regions (ETL connector):

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dyf = glue_context.create_dynamic_frame_from_options(
    connection_type="dynamodb",
    connection_options={
    "dynamodb.region": "us-east-1",
    "dynamodb.input.tableName": "test_source",
    "dynamodb.sts.roleArn": "<DynamoDBCrossAccessRole's ARN>"
    }
)
dyf.show()
job.commit()
```

For a cross-account read across regions (ELT connector):

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dyf = glue_context.create_dynamic_frame_from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.export": "ddb",
        "dynamodb.tableArn": "<test_source ARN>",
        "dynamodb.sts.roleArn": "<DynamoDBCrossAccessRole's ARN>"
    }
)
dyf.show()
job.commit()
```

For a read and cross-account write across regions:

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dyf = glue_context.create_dynamic_frame_from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.region": "us-east-1",
        "dynamodb.input.tableName": "test_source"
    }
)
dyf.show()

glue_context.write_dynamic_frame_from_options(
    frame=dyf,
    connection_type="dynamodb",
    connection_options={
        "dynamodb.region": "us-west-2",
        "dynamodb.output.tableName": "test_sink",
        "dynamodb.sts.roleArn": "<DynamoDBCrossAccessRole's ARN>"
    }
)

job.commit()
```
