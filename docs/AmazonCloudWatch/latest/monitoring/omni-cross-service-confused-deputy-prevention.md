

# Cross-service confused deputy prevention
<a name="omni-cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that does not have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account.

We recommend using the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in resource policies to limit the permissions that CloudWatch Omni gives another service to the resource. Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

CloudWatch Omni assumes IAM roles in your account to read your telemetry, both during setup and during evaluation. To prevent it from being used as a confused deputy, restrict the roles you create so that they can only be assumed on your behalf.

**Setup and data-access roles**

The space operator role trusts the CloudWatch Omni service principal `cloudwatch.amazonaws.com`. When you set up a space in a single account, CloudWatch Omni creates this role and applies the following trust policy. If you supply your own role instead, give it the same trust policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "cloudwatch.amazonaws.com" },
      "Action": ["sts:AssumeRole", "sts:TagSession", "sts:SetSourceIdentity", "sts:SetContext"],
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "<YOUR_OWN_ACCOUNT_ID>" }
      }
    }
  ]
}
```

The `aws:SourceAccount` condition limits CloudWatch Omni to assuming this role on behalf of your own account.

**Dataset integration execution role**

Dataset integration reads your CloudWatch Logs data through a role that CloudWatch Logs assumes on your behalf. Because the calling service is CloudWatch Logs rather than CloudWatch Omni, this role's trust policy uses both `aws:SourceAccount` and `aws:SourceArn` to restrict the assumption to dataset integrations in your own account.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "logs.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "<YOUR_OWN_ACCOUNT_ID>" },
        "ArnLike": { "aws:SourceArn": "arn:aws:observabilityadmin:*:<YOUR_OWN_ACCOUNT_ID>:dataset-integration/*" }
      }
    }
  ]
}
```