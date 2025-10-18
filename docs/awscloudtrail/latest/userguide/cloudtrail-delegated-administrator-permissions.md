# Required permissions to assign a delegated administrator

When assigning a CloudTrail delegated administrator, you must have the permissions to add and remove the delegated administrator in CloudTrail, as well as certain
 AWS Organizations API actions and IAM permissions listed in the following policy statement.

You can add the following statement to the end of an IAM policy to grant these permissions:


```
{
    "Sid": "Permissions",
    "Effect": "Allow",
    "Action": [
        "cloudtrail:RegisterOrganizationDelegatedAdmin",
        "cloudtrail:DeregisterOrganizationDelegatedAdmin",
        "organizations:RegisterDelegatedAdministrator",
        "organizations:DeregisterDelegatedAdministrator",
        "organizations:ListAWSServiceAccessForOrganization",
        "iam:CreateServiceLinkedRole",
        "iam:GetRole"
    ],
    "Resource": "*"
}
```

## Considerations when using condition keys with policy statements for delegated administrator permissions


You might consider using IAM global condition keys when adding policy statements to add and remove the delegated administrator in CloudTrail for additional security.
 When doing so, remember to include both service principal names (SPNs) to the condition. For example: 



```
{
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": [
            "context.cloudtrail.amazonaws.com",
            "cloudtrail.amazonaws.com"
          ]
        }
      },
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "*",
      "Effect": "Allow"
}
        
```

For more information, see [Identity and Access Management for AWS CloudTrail](security-iam.md "security-iam.md").
