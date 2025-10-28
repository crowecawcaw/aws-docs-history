# Using temporary credentials to connect to Amazon Neptune

Amazon Neptune supports IAM authentication using temporary credentials.

You can use an assumed role to authenticate using an IAM authentication policy, like one
of the example policies in the previous sections.

If you are using temporary credentials, you must specify `AWS_SESSION_TOKEN` in
addition to `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and
`SERVICE_REGION`.

###### Note

The temporary credentials expire after a specified interval, _including the session token_.

You must update your session token when you request new credentials. For more
information, see [Using Temporary Security Credentials to Request Access to AWS Resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md").

The following sections describe how to allow access and retrieve temporary
credentials.

###### To authenticate using temporary credentials

1. Create an IAM role with permission to access a Neptune cluster. For information
   about creating this role, see [Using different kinds of IAM policies for
   controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").
2. Add a trust relationship to the role that allows access to the credentials.

Retrieve the temporary credentials, including the `AWS_ACCESS_KEY_ID`,
`AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. 3. Connect to the Neptune cluster and sign the requests using the temporary
credentials. For more information about connecting and signing requests, see [Connecting to your Amazon Neptune database using AWS Identity and Access Management authentication](iam-auth-connecting.md "iam-auth-connecting.md").
There are various methods for retrieving temporary credentials depending on the
environment.

###### Topics

- [Getting Temporary Credentials Using the
  AWS CLI](#iam-auth-temporary-credentials-cli "#iam-auth-temporary-credentials-cli")
- [Setting Up AWS Lambda for Neptune
  IAM Authentication](#iam-auth-temporary-credentials-lambda "#iam-auth-temporary-credentials-lambda")
- [Setting Up Amazon EC2 for Neptune IAM
  Authentication](#iam-auth-temporary-credentials-ec2 "#iam-auth-temporary-credentials-ec2")

## Getting Temporary Credentials Using the

AWS CLI

To get credentials using the AWS Command Line Interface (AWS CLI), first you need to add a trust
relationship that grants permission to assume the role to the AWS user that will run the
AWS CLI command.

Add the following trust relationship to the Neptune IAM authentication role.
If you don't have a Neptune IAM authentication role, see [Using different kinds of IAM policies for
controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/test"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For information about adding the trust relationship to the role, see [Editing the Trust
Relationship for an Existing Role](../../../directoryservice/latest/admin-guide/edit_trust.md "../../../directoryservice/latest/admin-guide/edit_trust.md") in the _AWS Directory Service Administration
Guide_.

If the Neptune policy is not yet attached to a role, create a new role. Attach the
Neptune IAM authentication policy, and then add the trust policy. For information about
creating a new role, see [Creating a New
Role](../../../directoryservice/latest/admin-guide/create_role.md "../../../directoryservice/latest/admin-guide/create_role.md").

###### Note

The following sections assume that you have the AWS CLI installed.

###### To run the AWS CLI manually

1. Enter the following command to request the credentials using the AWS CLI. Replace the
   role ARN, session name, and profile with your own values.

```
aws sts assume-role  --role-arn  `arn:aws:iam::123456789012:role/NeptuneIAMAuthRole` --role-session-name `test` --profile `testprofile`
```

2. The following is example output from the command. The `Credentials`
   section contains the values that you need.

###### Note

Record the `Expiration` value because you need to get new credentials
after this time.

```
{
    "AssumedRoleUser": {
        "AssumedRoleId": "AROA3XFRBF535PLBIFPI4:s3-access-example",
        "Arn": "arn:aws:sts::123456789012:assumed-role/xaccounts3access/s3-access-example"
    },
    "Credentials": {
        "SecretAccessKey": "`9drTJvcXLB89EXAMPLELB8923FB892xMFI`",
        "SessionToken": "`AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=`",
        "Expiration": "2016-03-15T00:05:07Z",
        "AccessKeyId": "`ASIAJEXAMPLEXEG2JICEA`"
    }
}
```

3. Set the environment variables using the returned credentials.

```
export AWS_ACCESS_KEY_ID=`ASIAJEXAMPLEXEG2JICEA`
export AWS_SECRET_ACCESS_KEY=`9drTJvcXLB89EXAMPLELB8923FB892xMFI`
export AWS_SESSION_TOKEN=`AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=`

export SERVICE_REGION=`us-east-1 or us-east-2 or us-west-1 or us-west-2 or ca-central-1 or
 sa-east-1 or eu-north-1 or eu-west-1 or eu-west-2 or eu-west-3 or eu-central-1 or me-south-1 or
 me-central-1 or il-central-1 or af-south-1 or ap-east-1 or ap-northeast-1 or ap-northeast-2 or ap-southeast-1 or ap-southeast-2 or ap-south-1 or
 cn-north-1 or cn-northwest-1 or
 us-gov-east-1 or us-gov-west-1`
```

4. Connect using one of the following methods.
   - [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
   - [Connecting to Amazon Neptune databases using IAM with
     Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
   - [Connecting to Amazon Neptune databases using IAM authentication with Java and
     SPARQL](iam-auth-connecting-sparql-java.md "iam-auth-connecting-sparql-java.md")
   - [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")

###### To use a script to get the credentials

1. Run the following command to install the **jq** command. The script
   uses this command to parse the output of the AWS CLI command.

```
sudo yum -y install jq
```

2. Create a file named `credentials.sh` in a text editor and add the
   following text. Replace the service Region, role ARN, session name, and profile with
   your own values.

```
#!/bin/bash

creds_json=$(aws sts assume-role  --role-arn  `arn:aws:iam::123456789012:role/NeptuneIAMAuthRole` --role-session-name `test` --profile `testprofile`)

export AWS_ACCESS_KEY_ID=$(echo "$creds_json" | jq .Credentials.AccessKeyId |tr -d '"')
export AWS_SECRET_ACCESS_KEY=$(echo "$creds_json" | jq .Credentials.SecretAccessKey| tr -d '"')
export AWS_SESSION_TOKEN=$(echo "$creds_json" | jq .Credentials.SessionToken|tr -d '"')

export SERVICE_REGION=`us-east-1 or us-east-2 or us-west-1 or us-west-2 or ca-central-1 or
 sa-east-1 or eu-north-1 or eu-west-1 or eu-west-2 or eu-west-3 or eu-central-1 or me-south-1 or
 me-central-1 or il-central-1 or af-south-1 or ap-east-1 or ap-northeast-1 or ap-northeast-2 or ap-southeast-1 or ap-southeast-2 or ap-south-1 or
 cn-north-1 or cn-northwest-1 or
 us-gov-east-1 or us-gov-west-1`
```

3. Connect using one of the following methods.
   - [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
   - [Connecting to Amazon Neptune databases using IAM with
     Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
   - [Connecting to Amazon Neptune databases using IAM authentication with Java and
     SPARQL](iam-auth-connecting-sparql-java.md "iam-auth-connecting-sparql-java.md")
   - [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")

## Setting Up AWS Lambda for Neptune

IAM Authentication

AWS Lambda includes credentials automatically each time the Lambda function is run.

First you add a trust relationship that grants permission to assume the role to the
Lambda service.

Add the following trust relationship to the Neptune IAM authentication role. If you
don't have a Neptune IAM authentication role, see [Using different kinds of IAM policies for
controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For information about adding the trust relationship to the role, see [Editing the Trust Relationship for an
Existing Role](../../../directoryservice/latest/admin-guide/edit_trust.md "../../../directoryservice/latest/admin-guide/edit_trust.md") in the _AWS Directory ServiceAdministration Guide_.

If the Neptune policy is not yet attached to a role, create a new role. Attach the
Neptune IAM authentication policy, and then add the trust policy. For information about
creating a new role, see [Creating a New
Role](../../../directoryservice/latest/admin-guide/create_role.md "../../../directoryservice/latest/admin-guide/create_role.md") in the _AWS Directory Service Administration Guide_.

###### To access Neptune from Lambda

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Create a new Lambda function for Python version 3.6.
3. Assign the `AWSLambdaVPCAccessExecutionRole` role to the Lambda function.
   This is required to access Neptune resources, which are VPC only.
4. Assign the Neptune authentication IAM role to the Lambda function.

For more information, see [AWS
Lambda Permissions](../../../lambda/latest/dg/intro-permission-model.md "../../../lambda/latest/dg/intro-permission-model.md") in the _AWS Lambda Developer Guide_. 5. Copy the IAM authentication Python sample into the Lambda function code.

For more information about the sample and the sample code, see [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md").

## Setting Up Amazon EC2 for Neptune IAM

Authentication

Amazon EC2 allows you to use instance profiles to automatically provide credentials. For
more information, see [Using Instance Profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the _IAM User Guide_.

First you add a trust relationship that grants permission to assume the role to the
Amazon EC2 service.

Add the following trust relationship to the Neptune IAM authentication role. If you
don't have a Neptune IAM authentication role, see [Using different kinds of IAM policies for
controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For information about adding the trust relationship to the role, see [Editing the Trust Relationship for an Existing Role](../../../directoryservice/latest/admin-guide/edit_trust.md "../../../directoryservice/latest/admin-guide/edit_trust.md") in the _AWS Directory Service
Administration Guide_.

If the Neptune policy is not yet attached to a role, create a new role. Attach the
Neptune IAM authentication policy, and then add the trust policy. For information about
creating a new role, see [Creating a New Role](../../../directoryservice/latest/admin-guide/create_role.md "../../../directoryservice/latest/admin-guide/create_role.md") in the _AWS Directory Service Administration
Guide_.

###### To use a script to get the credentials

1. Run the following command to install the **jq** command. The script
   uses this command to parse the output of the **curl** command.

```
sudo yum -y install jq
```

2. Create a file named `credentials.sh` in a text editor and add the
   following text. Replace the service Region with your own value.

```
TOKEN=$( curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" )
role_name=$( curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ )
creds_json=$( curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/${role_name} )

export AWS_ACCESS_KEY_ID=$(echo "$creds_json" | jq .AccessKeyId |tr -d '"')
export AWS_SECRET_ACCESS_KEY=$(echo "$creds_json" | jq .SecretAccessKey| tr -d '"')
export AWS_SESSION_TOKEN=$(echo "$creds_json" | jq .Token|tr -d '"')

export SERVICE_REGION=`us-east-1 or us-east-2 or us-west-1 or us-west-2 or ca-central-1 or
 sa-east-1 or eu-north-1 or eu-west-1 or eu-west-2 or eu-west-3 or eu-central-1 or me-south-1 or
 me-central-1 or il-central-1 or af-south-1 or ap-east-1 or ap-northeast-1 or ap-northeast-2 or ap-southeast-1 or ap-southeast-2 or ap-south-1 or
 cn-north-1 or cn-northwest-1 or
 us-gov-east-1 or us-gov-west-1`
```

3. Run the script in the `bash` shell using the `source` command:

```
source credentials.sh
```

Even better is to add the commands in this script to the `.bashrc` file on
your EC2 instance so that they will be invoked automatically when you log in, making
temporary credentials available to the Gremlin console. 4. Connect using one of the following methods.

    * [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
    * [Connecting to Amazon Neptune databases using IAM with
     Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
    * [Connecting to Amazon Neptune databases using IAM authentication with Java and
     SPARQL](iam-auth-connecting-sparql-java.md "iam-auth-connecting-sparql-java.md")
    * [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")
