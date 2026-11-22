

# Configuring Workday Live Data Query connections

Workday Live Data Query uses the OAuth 2.0 JWT bearer grant type (RFC 7523). AWS Glue creates a JSON Web Token (JWT) for your Workday Integration System User (ISU), signs it with your private key, and exchanges it at your Workday OAuth 2.0 token endpoint for a short-lived access token. AWS Glue requests a new access token when the current one expires, without user interaction. This grant type works well for automation because no user needs to sign in to Workday when the connection is created or used.

You store the OAuth 2.0 client ID, ISU user name, token endpoint, and private key in an AWS Secrets Manager secret. AWS Glue reads the secret but doesn't modify it. The ISU's security permissions in Workday determine which data AWS Glue can read.

Before you begin, collect the values listed in [Configuring Workday Live Data Query](workday-ldq-configuring.md). Workday displays the token endpoint, Integration System User, and client ID after your Workday administrator completes the Register API Client task. For more information, see [Set Up Live Data Query ISU Authentication in Workday](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/set-up-live-data-query-isu-authentication.html?toc=2.1.1) in the Workday documentation.

To configure a Workday Live Data Query connection:

1. In AWS Secrets Manager, create a secret with the following key/value pairs. Follow the steps in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the AWS Secrets Manager User Guide. Keep the secret name, `secretName`, for the next step.
   + `wd.authn.clientId` – Your OAuth 2.0 client ID.
   + `wd.authn.isu` – The user name of your Integration System User.
   + `wd.authn.accessTokenEndpoint` – Your Workday OAuth 2.0 token endpoint, for example `https://{{host}}/ccx/oauth2/{{tenant}}/token`.
   + `wd.authn.privateKey` – Your PEM-formatted private key, including the BEGIN and END PRIVATE KEY lines.
**Note**  
The key names are reserved. Enter them exactly as shown. The private key must keep its line breaks. If you create the secret as JSON, encode each line break in the private key as `\n`.

1. Create an IAM role that AWS Glue can assume, with permission to read `secretName`. Use the following trust policy:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "glue.amazonaws.com"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "123456789012"
                   }
               }
           }
       ]
   }
   ```

   Attach a permissions policy that allows `secretsmanager:GetSecretValue` on your secret. If you want to use this role for your AWS Glue jobs too, also attach the [AWSGlueServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole) managed policy. You can use the following policy statement:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:secretName-AbCdEf"
           }
       ]
   }
   ```

1. In the AWS Glue console, create the connection from AWS Glue Studio:

   1. In the navigation pane, choose **Visual ETL**, then choose **Visual ETL** to create a job.

   1. Under **Sources**, choose **Workday Live Data Query**.

   1. For the AWS Glue connection, choose an existing Workday Live Data Query connection or create a new one.

   1. On the **Create Workday Live Data Query connection** page, under **Connection access**, provide the following:
      + For **Host**, provide your Workday Data Service host name. This is usually the same host as your token endpoint, for example `services1.wd12.myworkday.com`.
      + For **Port**, provide `443`.
      + (Optional) Select **EnforceSSL** to enforce SSL.
      + (Optional) For **JDBC URL Parameters**, provide additional Workday driver parameters as `key1=value1;key2=value2`. Leave this empty unless your Workday administrator gives you a specific setting.
      + For **IAM Role ARN**, choose the role from step 2.

   1. Under **Authentication**, for **AWS Secret**, choose **Select secret from this account** and choose `secretName`, or choose **Manually enter secret ARN**. The secret must contain `wd.authn.accessTokenEndpoint`, `wd.authn.clientId`, `wd.authn.isu`, and `wd.authn.privateKey`.

   1. (Optional) Choose **Test connection**. On success, the console shows **Connection test successful**.

   1. Choose **Next**.

   1. Enter a name for the connection and choose **Create connection**. Keep the connection name, `connectionName`, for the next step.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`. If your job uses a different role than the connection, also grant that role `secretsmanager:GetSecretValue` on `secretName`. The job role reads the secret directly; the connection's role doesn't cover it.

1. If you want AWS Glue to connect to Workday from your VPC, configure network options for the connection with the AWS CLI or the AWS Glue API. For more information, see the following section. Also attach the following permissions policy to the IAM role:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeVpcs",
                   "ec2:DescribeSubnets",
                   "ec2:DescribeSecurityGroups",
                   "ec2:CreateNetworkInterface",
                   "ec2:DescribeNetworkInterfaces",
                   "ec2:DeleteNetworkInterface"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

   The subnet must be able to reach AWS STS, AWS Secrets Manager, and your Workday Data Service host and token endpoint on port 443, for example through a NAT gateway.

1. In your AWS Glue job, use `connectionName`. In a visual job, choose it in the Workday Live Data Query source node. In a script job, provide it as an **Additional network connection** in the job configuration.

## Configuring Workday Live Data Query connections with the AWS CLI
<a name="workday-ldq-configuring-connections-cli"></a>

You can create connections using the AWS CLI. Replace the example values with your own.

Save your Workday credentials in a file named `workday-ldq-secret.json`:

```
{
    "wd.authn.clientId": "your-client-id",
    "wd.authn.isu": "your-isu-user-name",
    "wd.authn.accessTokenEndpoint": "https://your-workday-host/ccx/oauth2/your-tenant/token",
    "wd.authn.privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...\n-----END PRIVATE KEY-----"
}
```

Create the secret:

```
aws secretsmanager create-secret \
    --name workday-ldq-secret \
    --secret-string file://workday-ldq-secret.json \
    --region us-east-1
```

Save the connection definition in a file named `workday-ldq-connection.json`:

```
{
    "Name": "workday-ldq-conn1",
    "ConnectionType": "WORKDAYLDQ",
    "ConnectionProperties": {
        "HOST": "your-workday-data-service-host",
        "PORT": "443",
        "ROLE_ARN": "arn:aws:iam::123456789012:role/glue-role"
    },
    "AuthenticationConfiguration": {
        "AuthenticationType": "CUSTOM",
        "SecretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:workday-ldq-secret-AbCdEf"
    },
    "ValidateCredentials": true,
    "ValidateForComputeEnvironments": [
        "SPARK"
    ]
}
```

Create the connection:

```
aws glue create-connection \
    --connection-input file://workday-ldq-connection.json \
    --region us-east-1
```

On success, the command returns `"CreateConnectionStatus": "READY"`. When `ValidateCredentials` is `true`, AWS Glue gets an access token from your Workday token endpoint and runs a test query against your Workday Data Service host before creating the connection. If the test fails, the connection isn't created and the error is returned. When `ValidateCredentials` is `false`, the connection is created without testing. We recommend that you set it to `true`.

To connect from your VPC, add `PhysicalConnectionRequirements` to the connection definition:

```
"PhysicalConnectionRequirements": {
    "SubnetId": "subnet-0123456789abcdef0",
    "SecurityGroupIdList": [
        "sg-0123456789abcdef0"
    ],
    "AvailabilityZone": "us-east-1a"
}
```

With network options, AWS Glue tests the connection from your subnet, and `create-connection` returns `"CreateConnectionStatus": "IN_PROGRESS"`. The test can take several minutes. Check the status with the following command and read `Status` (`READY` on success):

```
aws glue get-connection \
    --name workday-ldq-conn1 \
    --region us-east-1
```

Jobs that use the connection run in your subnet. The security group must allow workers to communicate.

To use the same connection with Amazon Athena, add `"ATHENA"` to `ValidateForComputeEnvironments` and provide the Athena connection properties, such as a spill bucket. For more information, see [Amazon Athena Workday Live Data Query connector](https://docs.aws.amazon.com/athena/latest/ug/connectors-workday-ldq.html) in the Amazon Athena User Guide.

The following table describes the Workday Live Data Query connection properties.


**Workday Live Data Query connection properties**  

| Property | Required | Description | 
| --- | --- | --- | 
| HOST | Yes | Your Workday Data Service host name. | 
| PORT | Yes | The port number. Use 443. | 
| ROLE\_ARN | Yes, for AWS Glue ETL | The IAM role AWS Glue assumes to read your secret and, if you configure network options, to create network interfaces. | 
| ENFORCE\_SSL | No | Whether AWS Glue enforces SSL. The default is false. In the console, this is the EnforceSSL option. Connections to Workday on port 443 use TLS whether or not you set this. | 
| JDBC\_PARAMS | No | Additional Workday driver parameters as key1=value1;key2=value2. In the console, this is the JDBC URL Parameters field. | 