# Automatically rotating passwords for users

With AWS Secrets Manager, you can replace hardcoded credentials in your code (including passwords) with an API call to Secrets Manager to retrieve the secret programmatically.
This helps ensure that the secret can't be compromised by someone examining your code, because the secret simply isn't there.
Also, you can configure Secrets Manager to automatically rotate the secret for you according to a schedule that you specify.
This enables you to replace long-term secrets with short-term ones, which helps to significantly reduce the risk of compromise.

Using Secrets Manager, you can automatically rotate your ElastiCache for Redis OSS passwords (that is, secrets) using an AWS Lambda function that Secrets Manager provides.

For more information about AWS Secrets Manager, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md")

## How ElastiCache uses secrets

Valkey 7.2 and above have an equivalent feature set as Redis OSS 7.0. In Redis OSS 6, ElastiCache introduced [Role-Based Access Control (RBAC)](Clusters.md "Clusters.md") to secure the Valkey or Redis OSS cluster.
This feature allows certain connections to be limited in terms of the commands that can be executed and the keys that can be accessed.
With RBAC, while the customer creates a user with passwords, the password values need to be manually entered in plaintext and is visible to the operator.

With Secrets Manager, applications fetch the password from Secrets Manager rather than entering them manually and storing them in the application's configuration. For information on
how to do this, see [How ElastiCache users are associated with the secret](#How-User-Secrets-Manager-Associate "#How-User-Secrets-Manager-Associate").

There is a cost incurred for using secrets. For pricing information, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").

## How ElastiCache users are associated with the secret

Secrets Manager will keep a reference for the associated user in the secret’s `SecretString` field. There will be no reference to the secret from ElastiCache side.

```
{
    "password": "strongpassword",
    "username": "user1",
    "user_arn": "arn:aws:elasticache:us-east-1:xxxxxxxxxx918:user:user1" //this is the bond between the secret and the user
}
```

## Lambda rotation function

To enable Secrets Manager automatic password rotation, you will create a Lambda function that will interact with the [modify-user](../../../cli/latest/reference/elasticache/modify-user.md "../../../cli/latest/reference/elasticache/modify-user.md") API to update the user’s passwords.

For information on how this works, see [How rotation works](../../../secretsmanager/latest/userguide/rotating-secrets.md#rotate-secrets_how "../../../secretsmanager/latest/userguide/rotating-secrets.md#rotate-secrets_how").

###### Note

For some AWS services, to avoid the confused deputy scenario, AWS recommends that you use both the `aws:SourceArn` and
`aws:SourceAccount` global condition keys. However, if you include the `aws:SourceArn` condition in your rotation function policy,
the rotation function can only be used to rotate the secret specified by that ARN. We recommend that you include only the context key `aws:SourceAccount` so that you can use the rotation function for multiple secrets.

For any issues you may encounter, see [Troubleshoot AWS Secrets Manager rotation](../../../secretsmanager/latest/userguide/troubleshoot_rotation.md "../../../secretsmanager/latest/userguide/troubleshoot_rotation.md").

## How to create an ElastiCache user and associate it with Secrets Manager

The following steps illustrate how to create a user and associate it with Secrets Manager:

1. **Create an inactive user**

For Linux, macOS, or Unix:

```
aws elasticache create-user \
 --user-id user1 \
 --user-name user1 \
 --engine "REDIS" \
 --no-password \ // no authentication is required
 --access-string "*off* +get ~keys*" // this disables the user
```

For Windows:

```
aws elasticache create-user ^
 --user-id user1 ^
 --user-name user1 ^
 --engine "REDIS" ^
 --no-password ^ // no authentication is required
 --access-string "*off* +get ~keys*" // this disables the user
```

You will see a response similar to the following:

```
{
    "UserId": "user1",
    "UserName": "user1",
    "Status": "active",
    "Engine": "redis",
    "AccessString": "off ~keys* -@all +get",
    "UserGroupIds": [],
    "Authentication": {
        "Type": "no_password"
    },
    "ARN": "arn:aws:elasticache:us-east-1:xxxxxxxxxx918:user:user1"
}
```

2. **Create a Secret**

For Linux, macOS, or Unix:

```
aws secretsmanager create-secret \
--name production/ec/user1 \
--secret-string \
'{
   "user_arn": "arn:aws:elasticache:us-east-1:123456xxxx:user:user1",
    "username":"user1"
 }'
```

For Windows:

```
aws secretsmanager create-secret ^
--name production/ec/user1 ^
--secret-string ^
'{
   "user_arn": "arn:aws:elasticache:us-east-1:123456xxxx:user:user1",
    "username":"user1"
 }'
```

You will see a response similar to the following:

```
{
 "ARN": "arn:aws:secretsmanager:us-east-1:123456xxxx:secret:production/ec/user1-eaFois",
 "Name": "production/ec/user1",
 "VersionId": "aae5b963-1e6b-4250-91c6-ebd6c47d0d95"
}
```

3. **Configure a Lambda function to rotate your password**
   1. Sign in to the AWS Management Console and open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/")
   2. Choose **Functions** on the navigation pane and then choose the function you created. Choose the function name, not the checkbox to its left.
   3. Choose the **Configuration** tab.
   4. In **General configuration**, choose **Edit** and then set **Timeout** to at least 12 minutes.
   5. Choose **Save**.
   6. Choose **Environment variables** and then set the following:
      1. SECRETS_MANAGER_ENDPOINT – https://secretsmanager.`REGION`.amazonaws.com
      2. SECRET_ARN – The Amazon Resource Name (ARN) of the secret you created in Step 2.
      3. USER_NAME – Username of the ElastiCache user,
      4. Choose **Save**.

   7. Choose **Permissions**
   8. Under **Execution role**, choose the name of the Lambda function role to view on the IAM console.
   9. The Lambda function will need the following permission to modify the users and set the password:

   ElastiCache

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "elasticache:DescribeUsers",
    "elasticache:ModifyUser"
    ],
    "Resource": "arn:aws:elasticache:us-east-1:123456789012:user:user1"
    }
    ]
   }`

   ```

   Secrets Manager

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "secretsmanager:GetSecretValue",
    "secretsmanager:DescribeSecret",
    "secretsmanager:PutSecretValue",
    "secretsmanager:UpdateSecretVersionStage"
    ],
    "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:XXXX"
    },
    {
    "Effect": "Allow",
    "Action": "secretsmanager:GetRandomPassword",
    "Resource": "*"
    }
    ]
   }`

   ```

4. Set up Secrets Manager secret rotation
   1. **Using the AWS Management Console, see [Set up automatic rotation for AWS Secrets Manager secrets using the console](../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md "../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md")**

   For more information on setting up a rotation schedule, see [Schedule expressions in Secrets Manager rotation](../../../secretsmanager/latest/userguide/rotate-secrets_schedule.md "../../../secretsmanager/latest/userguide/rotate-secrets_schedule.md"). 2. **Using the AWS CLI, see [Set up automatic rotation for AWS Secrets Manager using the AWS Command Line Interface](../../../secretsmanager/latest/userguide/rotate-secrets-cli.md "../../../secretsmanager/latest/userguide/rotate-secrets-cli.md")**
