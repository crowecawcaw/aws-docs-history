# Policy templates

Policy templates are a new IAM construct designed for defining temporary permissions that partners request in customers' accounts. Like regular IAM policies, they define permissions using statements with Effect, Action, Resource, and Condition elements. The key difference is that policy templates include parameters (such as @{bucketName}) that are replaced with actual values when you create a delegation request.

## How Policy Templates Work

As part of the onboarding process, you register your policy templates with AWS. AWS assigns each template a unique ARN that you reference when creating delegation requests.

When you create a delegation request, you specify:

- The policy template ARN
- Parameter values to substitute into the template

AWS combines the template with your parameter values to generate a standard IAM policy. Customers review this final rendered policy when approving your delegation request, seeing exactly what permissions will be granted.

###### Note

The final rendered policy has a maximum size limit of 2048 characters.

Here's a simple example showing how template substitution works.

Policy Template:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::@{bucketName}/*"
        }
    ]
}
```

Parameters Provided in Delegation Request:

```
{
    "Name": "bucketName",
    "Values": ["customer-data-bucket"],
    "Type": "String"
}
```

Final rendered policy (what customers see):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::customer-data-bucket/*"
        }
    ]
}
```

## Template Syntax

Policy templates use two key features to provide flexibility: parameter substitution and conditional statements. Parameter substitution allows you to define placeholders in your template that are replaced with actual values when creating a delegation request. Conditional statements allow you to include or exclude entire policy statements based on parameter values.

### Parameter Substitution and Types

Use the @{parameterName} syntax to define parameters in your policy template. When creating a delegation request, you must specify the type for each parameter.

#### String

A single value that is substituted directly into the template.

Template:

```
"Resource": "arn:aws:s3:::@{bucketName}/*"
```

Parameters:

```
{
    "Name": "bucketName",
    "Values": ["my-bucket"],
    "Type": "String"
}
```

Rendered result:

```
"Resource": "arn:aws:s3:::my-bucket/*"
```

#### StringList

Multiple values that generate multiple resource entries. When a StringList parameter is used in a resource ARN, it expands to create separate resource entries for each value.

Template:

```
"Resource": "arn:aws:s3:::@{bucketNames}/*"
```

Parameters:

```
{
    "Name": "bucketNames",
    "Values": ["bucket-1", "bucket-2"],
    "Type": "StringList"
}
```

Rendered result:

```
"Resource": [
    "arn:aws:s3:::bucket-1/*",
    "arn:aws:s3:::bucket-2/*"
]
```

#### Cross-Product Behavior

When multiple parameters are used in the same resource ARN, StringList parameters create a cross-product of all combinations.

Template:

```
"Resource": "arn:aws:s3:::@{bucketNames}/@{prefix}/*"
```

Parameters:

```
[
    {
        "Name": "bucketNames",
        "Values": ["bucket-1", "bucket-2"],
        "Type": "StringList"
    },
    {
        "Name": "prefix",
        "Values": ["data"],
        "Type": "String"
    }
]
```

Rendered result:

```
"Resource": [
    "arn:aws:s3:::bucket-1/data/*",
    "arn:aws:s3:::bucket-2/data/*"
]
```

### Conditional Statements

Use the @Enabled directive to conditionally include or exclude entire statements based on parameter values.

Syntax:

- @Enabled: "parameterName" - Include the statement when parameter value is "True"
- @Enabled: "!parameterName" - Include the statement when parameter value is NOT "True" (negation)

Template:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "*"
        },
        {
            "@Enabled": "ENABLE_S3_WRITE",
            "Effect": "Allow",
            "Action": ["s3:PutObject"],
            "Resource": "arn:aws:s3:::@{bucketName}/*"
        }
    ]
}
```

Parameters (when ENABLE_S3_WRITE is "True"):

```
[
    {
        "Name": "bucketName",
        "Values": ["my-bucket"],
        "Type": "String"
    },
    {
        "Name": "ENABLE_S3_WRITE",
        "Values": ["True"],
        "Type": "String"
    }
]
```

Rendered result:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject"],
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}
```

Parameters (when ENABLE_S3_WRITE is "False"):

```
[
    {
        "Name": "bucketName",
        "Values": ["my-bucket"],
        "Type": "String"
    },
    {
        "Name": "ENABLE_S3_WRITE",
        "Values": ["False"],
        "Type": "String"
    }
]
```

Rendered result:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": "*"
        }
    ]
}
```

When ENABLE_S3_WRITE is set to "True", the conditional statement is included. When set to "False", the statement is excluded from the rendered policy.

## Additional Examples

The following examples demonstrate common patterns for using policy templates in temporary delegation. They focus on creating IAM roles with permission boundaries for long-term access and show different strategies for scoping permissions to specific resources. These examples illustrate how to balance flexibility with security by using techniques such as ARN prefixes, resource tagging, and permission boundary updates.

### Example 1: Granting Long-Term Access to Specific Resources

The following permission boundary is submitted as "SQSAccessorBoundary" for "partner.com":

```
{
    "Effect": "Allow",
    "Action": [
        "sqs:DeleteMessage",
        "sqs:ReceiveMessage",
        "sqs:SendMessage"
    ],
    "Resource": "arn:aws:sqs:*:*:*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
}
```

###### Note

This includes a same-account condition to avoid granting access to queues in other accounts with open resource policies. A direct reference to the customer's account ID cannot be included because the boundary is shared across all customers and cannot be templated.

Since this is the first version of this policy, its ARN is arn:aws:iam::partner:policy/partner.com/SQSAccessorBoundary_20250115

The following policy template is submitted for temporary access permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:ListQueues"
            ],
            "Resource": "arn:aws:sqs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:PutRolePermissionsBoundary",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::@{AccountId}:role/partner.com/SQSAccessor",
            "Condition": {
                "StringEquals": {
                    "iam:PermissionsBoundary": "arn:aws:iam::partner:policy/partner.com/SQSAccessorBoundary_20250115"
                }
            }
        }
    ]
}
```

### Example 2: Using ARN Prefixes

The permission boundary can specify a resource ARN prefix to limit access:

```
"Resource": "arn:aws:sqs:*:@{AccountId}:PartnerPrefix*"
```

This limits access to only the resources with that prefix, reducing the scope of accessible resources.

### Example 3: Using Tags for Resource Access Control

You can tag resources during temporary delegated access and rely on those tags for long-term access control.

Permission boundary allowing access to tagged resources:

```
{
    "Effect": "Allow",
    "Action": [
        "sqs:DeleteMessage",
        "sqs:ReceiveMessage",
        "sqs:SendMessage"
    ],
    "Resource": "arn:aws:sqs:*:*:*",
    "Condition": {
        "Null": {
            "aws:ResourceTag/ManagedByPartnerDotCom": "false"
        },
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
}
```

Policy template to tag new queues on creation:

```
{
    "Effect": "Allow",
    "Action": [
        "sqs:CreateQueue",
        "sqs:TagQueue"
    ],
    "Resource": "arn:aws:sqs:*:*:*",
    "Condition": {
        "Null": {
            "aws:RequestTag/ManagedByPartnerDotCom": "false"
        }
    }
}
```

Policy template to tag pre-existing queues and create the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:TagQueue"
            ],
            "Resource": "arn:aws:sqs:*:@{AccountId}:@{QueueName}",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "ManagedByPartnerDotCom"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:PutRolePermissionsBoundary",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::@{AccountId}:role/partner.com/SQSAccessor",
            "Condition": {
                "StringEquals": {
                    "iam:PermissionsBoundary": "arn:aws:iam::partner:policy/partner.com/SQSAccessorBoundary_20250115"
                }
            }
        }
    ]
}
```

This approach allows customers to explicitly confirm which specific resources can be accessed long-term.

### Example 4: Updating the Permission Boundary

To update a permission boundary, register a new version with a new date suffix and request permission to replace it.

Updated permission boundary with additional permission:

```
{
    "Effect": "Allow",
    "Action": [
        "sqs:DeleteMessage",
        "sqs:PurgeQueue",
        "sqs:ReceiveMessage",
        "sqs:SendMessage"
    ],
    "Resource": "arn:aws:sqs:*:*:*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
}
```

As the second version, this policy has the ARN: arn:aws:iam::partner:policy/partner.com/SQSAccessorBoundary_2025_01_20

Policy template to update the permission boundary on the existing role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePermissionsBoundary"
            ],
            "Resource": "arn:aws:iam::@{AccountId}:role/partner.com/SQSAccessor",
            "Condition": {
                "StringEquals": {
                    "iam:PermissionsBoundary": "arn:aws:iam::partner:policy/partner.com/SQSAccessorBoundary_2025_01_20"
                }
            }
        }
    ]
}
```

Customers must approve this delegation request to update the permission boundary on the existing role.
