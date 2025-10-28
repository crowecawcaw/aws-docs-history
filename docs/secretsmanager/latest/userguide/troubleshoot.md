# Troubleshooting AWS Secrets Manager

Use the information here to help you diagnose and fix issues that you might encounter when
you're working with Secrets Manager.

For issues related to rotation, see [Troubleshoot AWS Secrets Manager rotation](troubleshoot_rotation.md "troubleshoot_rotation.md").

###### Topics

- ["Access denied" messages](#troubleshoot_general_access-denied-service "#troubleshoot_general_access-denied-service")
- ["Access denied" for temporary
  security credentials](#troubleshoot_general_access-denied-temp-creds "#troubleshoot_general_access-denied-temp-creds")
- [Changes I make aren't always
  immediately visible.](#troubleshoot_general_eventual-consistency "#troubleshoot_general_eventual-consistency")
- [“Cannot generate a data key with an asymmetric KMS key”
  when creating a secret](#asymmetrical-key "#asymmetrical-key")
- [An AWS CLI or AWS SDK operation can't find my secret
  from a partial ARN](#ARN_secretnamehyphen "#ARN_secretnamehyphen")
- [This secret is managed by an AWS service, and
  you must use that service to update it.](#troubleshoot-service-linked-secrets "#troubleshoot-service-linked-secrets")
- [Python module import fails when using Transform:
  AWS::SecretsManager-2024-09-16](#troubleshoot-python-import "#troubleshoot-python-import")

## "Access denied" messages

When you make an API call such as GetSecretValue or CreateSecret to Secrets Manager, you must have
IAM permissions to make that call. When you use the console, the console makes the same API
calls on your behalf, so you must also have IAM permissions. An administrator can grant
permissions by attaching an IAM policy to your IAM user, or to a group that you're a
member of. If the policy statements that grant those permissions include any conditions, such
as time-of-day or IP address restrictions, you also must meet those requirements when you send
the request. For information about viewing or modifying policies for an IAM user, group, or
role, see [Working with Policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md")
in the _IAM User Guide_. For information about permissions required for
Secrets Manager, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md "auth-and-access.md").

If you're signing API requests manually, without using the [AWS SDKs](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/"), verify you correctly [signed the request](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md").

## "Access denied" for temporary

security credentials

Verify the IAM user or role you're using to make the request has the correct
permissions. Permissions for temporary security credentials derive from an IAM user or role.
This means the permissions are limited to those granted to the IAM user or role. For more
information about how permissions for temporary security credentials are determined, see
[Controlling Permissions
for Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp_control-access.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access.md") in the _IAM User Guide_.

Verify that your requests are signed correctly and that the request is well-formed. For
details, see the [toolkit](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/") documentation for your
chosen SDK, or [Using
Temporary Security Credentials to Request Access to AWS Resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.

Verify that your temporary security credentials haven't expired. For more information, see
[Requesting Temporary Security
Credentials](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") in the _IAM User Guide_.

For information about permissions required for Secrets Manager, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md "auth-and-access.md").

## Changes I make aren't always

immediately visible.

Secrets Manager uses a distributed computing model called [eventual consistency](https://wikipedia.org/wiki/Eventual_consistency "https://wikipedia.org/wiki/Eventual_consistency"). Any
change that you make in Secrets Manager (or other AWS services) takes time to become visible from all
possible endpoints. Some of the delay results from the time it takes to send the data from
server to server, from replication zone to replication zone, and from region to region around
the world. Secrets Manager also uses caching to improve performance, but in some cases this can add
time. The change might not be visible until the previously cached data times out.

Design your global applications to account for these potential delays. Also, ensure that
they work as expected, even when a change made in one location isn't instantly visible at
another.

For more information about how some other AWS services are affected by eventual
consistency, see:

- [Managing data
  consistency](../../../redshift/latest/dg/managing-data-consistency.md "../../../redshift/latest/dg/managing-data-consistency.md") in the _Amazon Redshift Database Developer Guide_
- [Amazon S3 Data Consistency
  Model](../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel "../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel") in the _Amazon Simple Storage Service User Guide_
- [Ensuring Consistency When Using Amazon S3 and Amazon EMR for ETL Workflows](https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/ "https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/") in the AWS
  Big Data Blog
- [Amazon EC2
  Eventual Consistency](../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency "../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency") in the _Amazon EC2 API Reference_

## “Cannot generate a data key with an asymmetric KMS key”

when creating a secret

Secrets Manager uses a [symmetric encryption
KMS key](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") associated with a secret to generate a data key for each secret value. You
can't use an asymmetric KMS key. Verify you are using a symmetric encryption KMS key
instead of an asymmetric KMS key. For instructions, see [Identifying asymmetric
KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md").

## An AWS CLI or AWS SDK operation can't find my secret

from a partial ARN

In many cases, Secrets Manager can find your secret from part of an ARN rather than the full ARN.
However, if your secret's name ends in a hyphen followed by six characters, Secrets Manager might not be
able to find the secret from only part of an ARN. Instead, we recommend that you use the
complete ARN or the name of the secret.

**More details**

Secrets Manager includes six random characters at the end of the secret name to help ensure that the secret ARN is unique. If the original secret is deleted, and then a new secret is created with the same name, the two secrets have different ARNs because of these characters. Users with access to the old secret don't automatically get access to the new secret because the ARNs are different.

Secrets Manager constructs an ARN for a secret with Region, account, secret name, and then a hyphen
and six more characters, as follows:

```
arn:aws:secretsmanager:us-east-2:111122223333:secret:`SecretName`-abcdef
```

If your secret name ends with a hyphen and six characters, using only part of the ARN can
appear to Secrets Manager as though you are specifying a full ARN. For example, you might have a secret
named `MySecret-abcdef` with the ARN

`arn:aws:secretsmanager:us-east-2:111122223333:secret:MySecret-abcdef-nutBrk`

If you call the following operation, which only uses part of the secret ARN, then Secrets Manager
might not find the secret.

```
`$` `aws secretsmanager describe-secret --secret-id `arn:aws:secretsmanager:us-east-2:111122223333:secret:MySecret-abcdef``
```

## This secret is managed by an AWS service, and

you must use that service to update it.

If you encounter this message while trying to modify a secret, the secret can only be
updated by using the managing service listed in the message. For more information, see [AWS Secrets Manager secrets managed by other AWS services](service-linked-secrets.md "service-linked-secrets.md").

To determine who manages a secret, you can review the secret name. Secrets managed by
other services are prefixed with the ID of that service. Or, in the AWS CLI, call [describe-secret](../../../cli/latest/reference/secretsmanager/describe-secret.md "../../../cli/latest/reference/secretsmanager/describe-secret.md"), and then review the field `OwningService`.

## Python module import fails when using `Transform:

AWS::SecretsManager-2024-09-16`

If you're using the Transform: `AWS::SecretsManager-2024-09-16` and encounter
Python module import failures when your rotation Lambda function runs, the issue is likely caused by an
incompatible `Runtime` value. With this transform version, AWS CloudFormation manages the
runtime version, code, and shared object files for you. You don't need to manage these yourself.
