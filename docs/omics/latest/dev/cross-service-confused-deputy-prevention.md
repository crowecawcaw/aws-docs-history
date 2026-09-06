

# Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

 The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it shouldn't otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

 We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that AWS HealthOmics gives another service to the resource. 

To prevent the confused deputy problem in roles assumed by HealthOmics, set the value of `aws:SourceArn` to `arn:aws:omics:{{region}}:{{accountNumber}}:*` in the role's trust policy. The wildcard (`*`) applies the condition for all HealthOmics resources. 

 The following trust relationship policy grants HealthOmics access to your resources and uses the `aws:SourceArn` and `aws:SourceAccount` global condition context keys to prevent the confused deputy problem. Use this policy when you create a role for HealthOmics. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "omics.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{123456789012}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:omics:{{us-east-1}}:{{123456789012}}:*"
        }
      }
    }
  ]
}
```

------