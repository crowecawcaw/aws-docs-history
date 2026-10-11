

# Troubleshooting AWS Secrets Manager
<a name="troubleshoot"></a>

Use the information here to help you diagnose and fix issues that you might encounter when you're working with Secrets Manager.

For issues related to rotation, see [Troubleshoot AWS Secrets Manager rotation](troubleshoot_rotation.md).

**Topics**
+ ["Access denied" messages](#troubleshoot_general_access-denied-service)
+ ["Access denied" for temporary security credentials](#troubleshoot_general_access-denied-temp-creds)
+ [Changes I make aren't always immediately visible.](#troubleshoot_general_eventual-consistency)
+ ["Connection reset by peer" errors](#troubleshoot_general_connection-reset)
+ ["Cannot generate a data key with an asymmetric KMS key" when creating a secret](#asymmetrical-key)
+ [An AWS CLI or AWS SDK operation can't find my secret from a partial ARN](#ARN_secretnamehyphen)
+ [This secret is managed by an AWS service, and you must use that service to update it.](#troubleshoot-service-linked-secrets)
+ [Python module import fails when using `Transform: AWS::SecretsManager-2024-09-16`](#troubleshoot-python-import)
+ [My managed external secret is not rotating](#troubleshoot-mes-not-rotating)

## "Access denied" messages
<a name="troubleshoot_general_access-denied-service"></a>

When you make an API call such as GetSecretValue or CreateSecret to Secrets Manager, you must have IAM permissions to make that call. You should also ensure you're making these API calls in the AWS account and AWS Region where the secret is located. When you use the console, the console makes the same API calls on your behalf, so you must also have IAM permissions. An administrator can grant permissions by attaching an IAM policy to your IAM user, or to a group that you're a member of. If the policy statements that grant those permissions include any conditions, such as time-of-day or IP address restrictions, you also must meet those requirements when you send the request. For information about viewing or modifying policies for an IAM user, group, or role, see [Working with Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide*. For information about permissions required for Secrets Manager, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md).

If you're signing API requests manually, without using the [AWS SDKs](http://aws.amazon.com/tools/), verify you correctly [signed the request](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html).

## "Access denied" for temporary security credentials
<a name="troubleshoot_general_access-denied-temp-creds"></a>

Verify the IAM user or role you're using to make the request has the correct permissions. Permissions for temporary security credentials derive from an IAM user or role. This means the permissions are limited to those granted to the IAM user or role. For more information about how permissions for temporary security credentials are determined, see [Controlling Permissions for Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access.html) in the *IAM User Guide*.

Verify that your requests are signed correctly and that the request is well-formed. For details, see the [toolkit](http://aws.amazon.com/tools/) documentation for your chosen SDK, or [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.

Verify that your temporary security credentials haven't expired. For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*. 

For information about permissions required for Secrets Manager, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md).

## Changes I make aren't always immediately visible.
<a name="troubleshoot_general_eventual-consistency"></a>

Secrets Manager uses a distributed computing model called [eventual consistency](https://wikipedia.org/wiki/Eventual_consistency). Any change that you make in Secrets Manager (or other AWS services) takes time to become visible from all possible endpoints. Some of the delay results from the time it takes to send the data from server to server, from replication zone to replication zone, and from region to region around the world. Secrets Manager also uses caching to improve performance, but in some cases this can add time. The change might not be visible until the previously cached data times out.

Design your global applications to account for these potential delays. Also, ensure that they work as expected, even when a change made in one location isn't instantly visible at another.

For more information about how some other AWS services are affected by eventual consistency, see:
+ [Managing data consistency](https://docs.aws.amazon.com/redshift/latest/dg/managing-data-consistency.html) in the *Amazon Redshift Database Developer Guide*
+ [Amazon S3 Data Consistency Model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Introduction.html#ConsistencyModel) in the *Amazon Simple Storage Service User Guide*
+ [Ensuring Consistency When Using Amazon S3 and Amazon EMR for ETL Workflows](https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/) in the AWS Big Data Blog
+ [Amazon EC2 Eventual Consistency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/query-api-troubleshooting.html#eventual-consistency) in the *Amazon EC2 API Reference*

## "Connection reset by peer" errors
<a name="troubleshoot_general_connection-reset"></a>

When you call Secrets Manager, you might occasionally receive a *connection reset by peer* error. This happens when the server closes a TCP connection that your client is using or attempting to use. To manage capacity and maintain availability, AWS services, including Secrets Manager, can close connections at any time.

This most often affects idle keep-alive connections that your application reuses, but it can also affect newly established connections. Occasional resets are a normal part of connection lifecycle management. They don't indicate a problem with your secret or your account.

The AWS SDKs manage a connection pool and retry these errors on a new connection by default, so you don't usually need to take any action. If you encounter these errors, do the following:
+ Verify that you're using a current version of the AWS SDK or AWS CLI. Make sure you haven't turned off the default retry behavior. For more information, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.
+ If you manage HTTP connections directly instead of using an AWS SDK, retry the request on a new connection. Read operations such as `GetSecretValue` are idempotent and safe to retry.
+ Cache secret values on the client instead of calling Secrets Manager on every use. Caching reduces the number of connections your application opens and improves resilience to transient network errors. For more information, see [Use caching to retrieve secrets](best-practices.md#best-practices-caching).

If these errors persist over a sustained period, the cause is likely something other than routine connection cycling. To identify the cause, check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status) for Secrets Manager events in your AWS Region. Also verify your network path to the service endpoint, including any VPC endpoint, proxy, firewall, or DNS configuration. If the problem continues, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

## "Cannot generate a data key with an asymmetric KMS key" when creating a secret
<a name="asymmetrical-key"></a>

Secrets Manager uses a [symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks) associated with a secret to generate a data key for each secret value. You can't use an asymmetric KMS key. Verify you are using a symmetric encryption KMS key instead of an asymmetric KMS key. For instructions, see [Identifying asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html).

## An AWS CLI or AWS SDK operation can't find my secret from a partial ARN
<a name="ARN_secretnamehyphen"></a>

In many cases, Secrets Manager can find your secret from part of an ARN rather than the full ARN. However, if your secret's name ends in a hyphen followed by six characters, Secrets Manager might not be able to find the secret from only part of an ARN. Instead, we recommend that you use the complete ARN or the name of the secret.

**More details**

Secrets Manager includes six random characters at the end of the secret name to help ensure that the secret ARN is unique. If the original secret is deleted, and then a new secret is created with the same name, the two secrets have different ARNs because of these characters. Users with access to the old secret don't automatically get access to the new secret because the ARNs are different.

Secrets Manager constructs an ARN for a secret with Region, account, secret name, and then a hyphen and six more characters, as follows:

```
arn:aws:secretsmanager:us-east-2:111122223333:secret:{{SecretName}}-abcdef
```

If your secret name ends with a hyphen and six characters, using only part of the ARN can appear to Secrets Manager as though you are specifying a full ARN. For example, you might have a secret named `MySecret-abcdef` with the ARN

`arn:aws:secretsmanager:us-east-2:111122223333:secret:MySecret-abcdef-nutBrk`

If you call the following operation, which only uses part of the secret ARN, then Secrets Manager might not find the secret. 

```
$ aws secretsmanager describe-secret --secret-id arn:aws:secretsmanager:us-east-2:111122223333:secret:MySecret-abcdef
```

## This secret is managed by an AWS service, and you must use that service to update it.
<a name="troubleshoot-service-linked-secrets"></a>

If you encounter this message while trying to modify a secret, the secret can only be updated by using the managing service listed in the message. For more information, see [AWS Secrets Manager secrets managed by other AWS services](service-linked-secrets.md).

To determine who manages a secret, you can review the secret name. Secrets managed by other services are prefixed with the ID of that service. Or, in the AWS CLI, call [describe-secret](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/describe-secret.html), and then review the field `OwningService`. 

## Python module import fails when using `Transform: AWS::SecretsManager-2024-09-16`
<a name="troubleshoot-python-import"></a>

If you're using the Transform: `AWS::SecretsManager-2024-09-16` and encounter Python module import failures when your rotation Lambda function runs, the issue is likely caused by an incompatible `Runtime` value. With this transform version, AWS CloudFormation manages the runtime version, code, and shared object files for you. You don't need to manage these yourself. 

## My managed external secret is not rotating
<a name="troubleshoot-mes-not-rotating"></a>

If a [Secrets managed by third party applications](managed-external-secrets.md) does not rotate as expected, Secrets Manager records the details in a `RotationFailed` event in AWS CloudTrail. This event includes specific information about why the rotation failed. Review the most recent `RotationFailed` event for the secret to identify the cause. For more information about viewing Secrets Manager events in CloudTrail, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md).

The following are common causes of rotation failures for managed external secrets:
+ **Invalid credentials.** The credentials stored in the secret, or in the admin secret if you use one, are no longer valid or don't have permission to rotate the secret in the partner application. Verify that the secret value contains the correct fields in the format the integration partner requires, and that the credentials are still active in the partner application. For the required fields for each partner, see [Integration Partners](mes-partners.md).
+ **Blocked network access to the external resource.** The partner application blocks the Secrets Manager managed external secrets rotation traffic. If your external resource restricts inbound access by IP address, you must allowlist the IP ranges that rotation calls originate from. Add the AWS-managed prefix list `com.amazonaws.{{region}}.secretsmanager-managed-external-secrets`, where {{region}} is the AWS Region where your secret exists, to your ingress rules. Using the managed prefix list ensures your ingress rules automatically stay current as the underlying IP ranges change. For more information, see [AWS-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) in the *Amazon VPC User Guide*.

  If you prefer to reference the prefix list programmatically, you can use the [GetManagedPrefixListEntries](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetManagedPrefixListEntries.html) API to list the IPs that need to be allowlisted. You should periodically refresh your ingress rules with this prefix list to keep them current.

For more information about managed external secrets rotation, see [Rotate Secrets Manager managed external secrets](rotate-secrets_external.md). For security and permissions details, including the managed prefix list, see [Security and permissions](mes-security.md).