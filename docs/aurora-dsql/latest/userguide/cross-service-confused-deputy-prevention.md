

# Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that Amazon Aurora DSQL gives another service to the resource. Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if you are specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcard characters (`*`) for the unknown portions of the ARN. For example, `arn:aws:{{dsql}}:*:{{123456789012}}:*`. 

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3 bucket ARN, you must use both global condition context keys to limit permissions. 

The value of `aws:SourceArn` must be the ARN of the Aurora DSQL resource that the service role acts on behalf of.

The following example shows how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in Aurora DSQL to prevent the confused deputy problem.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": {
    "Sid": "ConfusedDeputyPreventionExamplePolicy",
    "Effect": "Allow",
    "Principal": {
      "Service": "backup.amazonaws.com"
    },
    "Action": "dsql:GetCluster",
    "Resource": [
      "arn:aws:dsql:*:{{123456789012}}:cluster/*"
    ],
    "Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:backup:*:{{123456789012}}:*"
      },
      "StringEquals": {
        "aws:SourceAccount": "{{123456789012}}"
      }
    }
  }
}
```

------

## CDC stream service role
<a name="cross-service-confused-deputy-cdc"></a>

Change data capture (CDC) streams require an IAM service role that Aurora DSQL assumes to write CDC records to your target. When you create this role, use `aws:SourceAccount` and `aws:SourceArn` conditions in the trust policy to ensure that only CDC streams in your account can assume the role.

Set `aws:SourceArn` to the stream ARN pattern for the cluster that uses the role. Because Aurora DSQL hasn't assigned the stream identifier when you create the stream, use a wildcard for the stream portion of the ARN:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DSQLAssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "dsql.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your-account-id}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}/stream/*"
                }
            }
        }
    ]
}
```

After you create a stream, you can tighten `aws:SourceArn` to the exact stream ARN if the role serves a single stream. For a full explanation of the trust policy and permissions policy for CDC service roles, see [Configuring IAM](cdc-iam.md).