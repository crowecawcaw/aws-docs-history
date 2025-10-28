# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS Parallel Computing Service (AWS PCS) gives another service to the
resource. Use `aws:SourceArn` if you want only one resource to be associated with
the cross-service access. Use `aws:SourceAccount` if you want to allow any
resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3
bucket ARN, you must use both global condition context keys to limit permissions.

The value of `aws:SourceArn` must be a cluster ARN.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in AWS PCS to prevent
the confused deputy problem.

```
{
"Version": "2012-10-17",
  "Statement": {
"Sid": "ConfusedDeputyPreventionExamplePolicy",
    "Effect": "Allow",
    "Principal": {
      "Service": "pcs.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
      "ArnLike": {
        "aws:SourceArn": [
          "arn:aws:pcs:us-east-1:123456789012:cluster/*"
        ]
      },
      "StringEquals": {
        "aws:SourceAccount": "123456789012"
      }
    }
  }
}
```

## IAM role for Amazon EC2 instances provisioned as part of a compute node group

AWS PCS automatically orchestrates Amazon EC2 capacity for each of the configured compute node groups in a cluster. When creating a compute node group, users must provide an IAM instance profile through the `iamInstanceProfileArn` field. The instance profile specifies the permissions associated with the provisioned EC2 instances. AWS PCS accepts any role that has `AWSPCS` as role name prefix or `/aws-pcs/` as part of the role path. The `iam:PassRole` permission is required on the IAM identity (user or role) that creates or updates a compute node group. When a user calls the `CreateComputeNodeGroup` or `UpdateComputeNodeGroup` API actions, AWS PCS checks to see if the user is allowed to perform the `iam:PassRole` action.

The following example policy grants permissions to pass only IAM roles whose name begins with `AWSPCS`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/AWSPCS*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "ec2.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```
