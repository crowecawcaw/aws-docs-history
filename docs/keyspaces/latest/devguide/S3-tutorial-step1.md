# Step 1: Create the Amazon S3 bucket, download the required tools, and configure the environment

In this step, you download the external tools and create and configure the AWS
resources required for the automated data export solution of an Amazon Keyspaces table to an Amazon S3
bucket using an AWS Glue job. To perform all these tasks in an efficient way, we
run a shell script with the name `setup-connector.sh` available on
[Github](https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue/setup-connector.sh "https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue/setup-connector.sh").

The script `setup-connector.sh` automates the following steps.

1. Creates an **Amazon S3 bucket** using AWS CloudFormation. This bucket stores the downloaded jar and configuration files,
   as well as the exported table data.
2. Creates an **IAM role** using AWS CloudFormation. AWS Glue jobs use this role to access Amazon Keyspaces and Amazon S3.
3. Downloads the [Apache Spark Cassandra Connector](https://repo1.maven.org/maven2/com/datastax/spark/ "https://repo1.maven.org/maven2/com/datastax/spark/") and uploads it to the Amazon S3 bucket.
4. Downloads the [SigV4 Authentication plugin](https://repo1.maven.org/maven2/software/aws/mcs/aws-sigv4-auth-cassandra-java-driver-plugin/ "https://repo1.maven.org/maven2/software/aws/mcs/aws-sigv4-auth-cassandra-java-driver-plugin/") and uploads it to the Amazon S3 bucket.
5. Downloads the [Apache Spark Extensions](https://repo1.maven.org/maven2/uk/co/gresearch/spark/ "https://repo1.maven.org/maven2/uk/co/gresearch/spark/") and uploads them to the Amazon S3 bucket.
6. Downloads the [Keyspaces Retry Policy](https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers "https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers") from Github, compiles the code using Maven,
   and uploads the output to the Amazon S3 bucket.
7. Uploads the **`keyspaces-application.conf`** file to the Amazon S3 bucket.

###### Use the `setup-connector.sh` shell script to automate the setup and configuration steps.

1.  Copy the files from the [aws-glue](https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue "https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue") repository on Github to your local machine. This directory contains the shell script as well as other
    required files.
2.  Run the shell script `setup-connector.sh`. You can specify the following three optional parameters.

        1. `SETUP_STACKNAME` – This is the name of the AWS CloudFormation stack used to create the AWS resources.
        2. `S3_BUCKET_NAME` – This is the name of the Amazon S3 bucket.
        3. `GLUE_SERVICE_ROLE_NAME` – This is the name of the IAM service role that AWS Glue uses to run jobs that
         connect to Amazon Keyspaces and Amazon S3.

    You can use the following command to run the shell script, provide the three parameters with the following names.

```
./setup-connector.sh `cfn-setup` `s3-keyspaces` `iam-export-role`
```

To confirm that your bucket was created, you can use the following AWS CLI command.

```
aws s3 ls s3://s3-keyspaces
```

The output of the command should look like this.

```
 `PRE conf/
 PRE jars/`
```

To confirm that the IAM role was created and to review the details, you can use the following AWS CLI statement.

```
aws iam get-role --role-name "iam-export-role"
```

```
`{
 "Role": {
 "Path": "/",
 "RoleName": "iam-export-role",
 "RoleId": "AKIAIOSFODNN7EXAMPLE",
 "Arn": "arn:aws:iam::111122223333:role/iam-export-role",
 "CreateDate": "2025-01-28T16:09:03+00:00",
 "AssumeRolePolicyDocument": {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 },
 "Description": "AWS Glue service role to import and export data from Amazon Keyspaces",
 "MaxSessionDuration": 3600,
 "RoleLastUsed": {
 "LastUsedDate": "2025-01-29T12:03:54+00:00",
 "Region": "us-east-1"
 }
 }
}`
```

If the AWS CloudFormation stack process fails, you can review the detailed error information about the failed stack in the AWS CloudFormation console.

After the Amazon S3 bucket containing all scripts and tools has been created and the IAM
role is configured, proceed to [Step 2: Configure the AWS Glue job that exports the
Amazon Keyspaces table](S3-tutorial-step2.md "S3-tutorial-step2.md").
