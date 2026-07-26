The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Access control for the AWS Marketplace Compliance API

You can use the AWS Marketplace Compliance API to manage seller compliance in AWS Marketplace. However, first
make sure your user or role can access the API functionality that you want to call.

Use AWS Identity and Access Management (IAM) to create users and roles and assign policies that grant limited
permissions to end users. The policies define the actions that the user or role can take on
your resources through the AWS Marketplace Compliance API.

###### Note

To sell products on AWS Marketplace, your AWS account must be set up as a seller account. For
more details about becoming an AWS Marketplace seller, see [Getting started as a
seller](../userguide/user-guide-for-sellers.md "../userguide/user-guide-for-sellers.md") in the _AWS Marketplace Seller Guide_.

###### Topics

- [Allowing actions with AWS managed policies](#compliance-allowing-actions-with-managed-policies "#compliance-allowing-actions-with-managed-policies")
- [Allowing actions on all resources](#compliance-allowing-actions-on-all-resources "#compliance-allowing-actions-on-all-resources")
- [Allowing actions on specific resources](#compliance-allowing-actions-on-specific-resources "#compliance-allowing-actions-on-specific-resources")
- [Allowing actions with specific aws:ResourceTag condition key](#compliance-allowing-actions-with-resource-tag "#compliance-allowing-actions-with-resource-tag")
- [Managing tags on resources](#compliance-managing-tags-on-resources "#compliance-managing-tags-on-resources")
- [Granting permission to manage tags on resources](#compliance-grant-permission-manage-tags "#compliance-grant-permission-manage-tags")
- [Granting permission to manage tags on resources only when those resources have specific tags](#compliance-grant-permission-manage-tags-specific-tags "#compliance-grant-permission-manage-tags-specific-tags")
- [Requiring tags when starting invoice submission tasks](#compliance-requiring-tags-when-starting-tasks "#compliance-requiring-tags-when-starting-tasks")
- [Requiring tags when starting tax compliance profile change tasks](#compliance-requiring-tags-when-starting-tcp-tasks "#compliance-requiring-tags-when-starting-tcp-tasks")
- [Verification evidence operations](#compliance-verification-verification-evidence-operations "#compliance-verification-verification-evidence-operations")

## Allowing actions with AWS managed policies

You can use policies that are managed by AWS to grant permissions to your user or
role.

To work with invoice submissions on AWS Marketplace, you can use the
`AWSMarketplaceSellerFullAccess` IAM managed policy, which includes full
access to the AWS Marketplace Compliance API actions in addition to its other permissions. For more
information, see [Policies
and permissions for AWS Marketplace sellers](../userguide/detailed-management-portal-permissions.md "../userguide/detailed-management-portal-permissions.md") and [AWS managed policies for
AWS Marketplace sellers](../userguide/security-iam-awsmanpol.md "../userguide/security-iam-awsmanpol.md") in the _AWS Marketplace Seller
Guide_.

Alternatively, you can create your own IAM policies to have more granular control than
is available in AWS managed policies. Use the following topics to create your own IAM
policies.

## Allowing actions on all resources

Resources are objects that the actions can act upon. The Compliance API has the following
resource types:

- **InvoiceSubmissionTask** – An invoice
  submission task tracks the processing of a seller-submitted invoice in AWS Marketplace.
- **IssuedTaxInvoice** – A tax invoice that AWS Marketplace
  issued on behalf of a seller.
- **VerificationEvidence** – Contains verification
  data for a specific verification category and
  subject being verified.
- **TaxComplianceProfile** – A tax compliance
  profile that represents a seller's compliance configuration for a specific
  jurisdiction.
- **TaxComplianceProfileChangeTask** – A task that
  tracks the asynchronous processing of a tax compliance profile create or update
  request.

To allow a user or role full access to invoice submission task operations, you can add
the following IAM policy. With this policy, the user or role can use all invoice
submission task actions on all resources (`"*"`).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartInvoiceSubmissionTask",
        "aws-marketplace:GetInvoiceSubmissionTask",
        "aws-marketplace:ListInvoiceSubmissionTasks",
        "aws-marketplace:ListPayables"
      ],
      "Resource": "*"
    }
  ]
}
```

To allow a user or role full access to issued tax invoice operations, you can add the
following IAM policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ListIssuedTaxInvoices",
        "aws-marketplace:GetIssuedTaxInvoice"
      ],
      "Resource": "*"
    }
  ]
}
```

To allow a user or role full access to verification operations, you can add
the following IAM policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:CreateVerificationEvidence",
        "aws-marketplace:UpdateVerificationEvidence",
        "aws-marketplace:GetVerificationEvidence",
        "aws-marketplace:ListVerificationEvidence",
        "aws-marketplace:StartVerification",
        "aws-marketplace:GetVerification",
        "aws-marketplace:ListVerifications"
      ],
      "Resource": "*"
    }
  ]
}
```

To allow a user or role full access to tax compliance profile operations, you can add
the following IAM policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartTaxComplianceProfileChangeTask",
        "aws-marketplace:ListTaxComplianceProfileChangeTasks",
        "aws-marketplace:GetTaxComplianceProfile",
        "aws-marketplace:ListTaxComplianceProfiles"
      ],
      "Resource": "*"
    }
  ]
}
```

For information about all actions available for the Compliance API, see [Actions,
resources, and condition keys for AWS Marketplace Compliance](../../../service-authorization/latest/reference/list_awsmarketplacecompliance.md "../../../service-authorization/latest/reference/list_awsmarketplacecompliance.md") in the _Service Authorization Reference_.

## Allowing actions on specific resources

You can use resource-level permissions to allow actions on a specific resource instead of
all resources. You do this by specifying the Amazon Resource Name (ARN) of the resource in
the `Resource` of the IAM policy.

The following example allows the `GetInvoiceSubmissionTask` action on a
specific invoice submission task.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetInvoiceSubmissionTask"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:`123456789012`:catalog/`example-catalog`/invoice-submission-task/`example-task-id`"
      ]
    }
  ]
}
```

The following example allows the `GetIssuedTaxInvoice` action on a specific
issued tax invoice.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetIssuedTaxInvoice"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:`123456789012`:catalog/`AWSMarketplace`/issued-tax-invoice/`example-invoice-id`"
      ]
    }
  ]
}
```

The following example allows the `GetVerificationEvidence` action on a
specific verification evidence resource.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetVerificationEvidence"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:`123456789012`:verification-type/business-verification/verification-evidence/`evidence-a1b2c3d4e5f6g`"
      ]
    }
  ]
}
```

The following example allows the `GetTaxComplianceProfile` action on a
specific tax compliance profile.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetTaxComplianceProfile"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:`123456789012`:tax-compliance-profile/`tcp-a1b2c3d4e5f6g`"
      ]
    }
  ]
}
```

## Allowing actions with specific aws:ResourceTag condition key

You can allow actions on resources based on their tags without having to specify
individual ARNs. Adding tags to resources allows you to control access to those resources
based on their tags.

For example, the following IAM policy allows the
`GetInvoiceSubmissionTask` action on any invoice submission task resource
(`"*"`) that has a tag key of `product-team` and tag value of
`team-xyz`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetInvoiceSubmissionTask"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

Similarly, the following IAM policy allows the `GetIssuedTaxInvoice` action
on any issued tax invoice resource (`"*"`) that has a tag key of
`Department` and tag value of `Tax`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetIssuedTaxInvoice"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Department": "Tax"
        }
      }
    }
  ]
}
```

The following IAM policy allows the `GetVerificationEvidence` action on
any verification evidence resource (`"*"`) that has a tag key of
`Department` and tag value of `Compliance`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetVerificationEvidence"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Department": "Compliance"
        }
      }
    }
  ]
}
```

Similarly, the following IAM policy allows the
`GetTaxComplianceProfile` action on any tax compliance profile resource
(`"*"`) that has a tag key of `Department` and tag value of
`Tax`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetTaxComplianceProfile"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Department": "Tax"
        }
      }
    }
  ]
}
```

## Managing tags on resources

You can add, list, and remove tags from existing Compliance API resources such as
invoice submission tasks, issued tax invoices, and tax compliance profiles.

### Add tags to resources

To add tags to a resource, use the `TagResource` API action.

**Request**

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
  "ResourceArn": "string",
  "Tags": [
    {
      "Key": "string",
      "Value": "string"
    }
  ]
}
```

Request parameters include:

- ResourceArn (String) – (Required) ARN of the resource.
- Tags (Array of objects) – (Required) A list of objects specifying each tag
  key and value. Number of objects allowed: 1–50.

  - Key (String) – (Required) Name of the tag. Regex pattern:
    `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`. Character length:
    1–128.
  - Value (String) – (Required) Value of the tag. Regex pattern:
    `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`. Character length:
    0–256.

### Remove tags from resources

To remove a tag or list of tags from a resource, use the
`UntagResource` API action.

**Request**

```
POST /UntagResource HTTP/1.1
Content-type: application/json

{
  "ResourceArn": "string",
  "TagKeys": [
    "string"
  ]
}
```

Request parameters include:

- ResourceArn (String) – (Required) ARN of the resource.
- TagKeys (Array of strings) – (Required) A list of key names of tags to be
  removed.

### List all tags on a resource

To list all tags on a resource, use the
`ListTagsForResource` API action.

**Request**

```
POST /ListTagsForResource HTTP/1.1
Content-type: application/json

{
  "ResourceArn": "string"
}
```

**Response**

```
{
  "ResourceArn": "string",
  "Tags": [
    {
      "Key": "string",
      "Value": "string"
    }
  ]
}
```

## Granting permission to manage tags on resources

To allow a user or role to add, remove, and list tags on all Compliance API resources,
they need the following IAM policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:TagResource",
        "aws-marketplace:UntagResource",
        "aws-marketplace:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

## Granting permission to manage tags on resources only when those resources have specific tags

You can allow a user or role to add, remove, and list tags on Compliance API resources
that have specific tags. The following IAM policy allows those actions on any resource
(`"*"`) that has a tag key of
`product-team` and tag value of `team-xyz`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:TagResource",
        "aws-marketplace:UntagResource",
        "aws-marketplace:ListTagsForResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

## Requiring tags when starting invoice submission tasks

You can enforce tagging when invoice submission tasks are created by using the
`aws:RequestTag` and `aws:TagKeys` condition keys with the
`StartInvoiceSubmissionTask` action.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartInvoiceSubmissionTask"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/product-team": "team-xyz"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "product-team"
          ]
        }
      }
    }
  ]
}
```

## Requiring tags when starting tax compliance profile change tasks

You can enforce tagging when tax compliance profile change tasks are created by using the
`aws:RequestTag` and `aws:TagKeys` condition keys with the
`StartTaxComplianceProfileChangeTask` action.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartTaxComplianceProfileChangeTask"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/RequiresApproval": "true"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "RequiresApproval"
          ]
        }
      }
    }
  ]
}
```

## Verification evidence operations

The AWS Marketplace Compliance API provides operations for managing verification evidence
and verification processes. You can use IAM policies to control access to these
operations.

### IAM actions for verification operations

The following IAM actions are available for verification operations. All actions use
the `aws-marketplace` namespace.

**Evidence management actions**

- `aws-marketplace:CreateVerificationEvidence` – Create new
  verification evidence.
- `aws-marketplace:UpdateVerificationEvidence` – Update existing
  verification evidence.
- `aws-marketplace:GetVerificationEvidence` – Get details of
  verification evidence.
- `aws-marketplace:ListVerificationEvidence` – List verification
  evidence resources.

**Verification process actions**

- `aws-marketplace:StartVerification` – Submit evidence and
  enable data sharing.
- `aws-marketplace:GetVerification` – Get detailed verification
  status.
- `aws-marketplace:ListVerifications` – List all verification
  statuses.

### Resource type

The **VerificationEvidence** resource contains
verification data for a specific verification category and
subject being verified. The ARN format for this resource is:

```
arn:aws:aws-marketplace:`region`:`account-id`:verification-type/`type-value`/verification-evidence/`evidence-id`
```

The following is an example ARN for business verification:

`arn:aws:aws-marketplace:us-east-1:123456789012:verification-type/business-verification/verification-evidence/evidence-a1b2c3d4e5f6g`

### Using the VerificationType condition key

The `aws-marketplace:VerificationType` condition key filters verification
process operations by type. This condition key applies to the following actions:

- `StartVerification`
- `GetVerification`
- `ListVerifications`

Valid values for this condition key are:

- `BusinessVerification`

###### Note

Evidence management operations (`CreateVerificationEvidence`,
`UpdateVerificationEvidence`, `GetVerificationEvidence`,
`ListVerificationEvidence`) do not use this condition key because the
verification type is already encoded in the resource ARN.

### Allowing actions with AWS managed policies

The `AWSMarketplaceSellerFullAccess` IAM managed policy includes all
seven verification permissions in addition to its other permissions. For more information, see
[AWS managed policies for
AWS Marketplace sellers](../userguide/security-iam-awsmanpol.md "../userguide/security-iam-awsmanpol.md") in the _AWS Marketplace Seller
Guide_.

### Allowing full access to all verification operations

To allow a user or role full access to all verification operations, you can add the
following IAM policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:CreateVerificationEvidence",
        "aws-marketplace:UpdateVerificationEvidence",
        "aws-marketplace:GetVerificationEvidence",
        "aws-marketplace:ListVerificationEvidence",
        "aws-marketplace:StartVerification",
        "aws-marketplace:GetVerification",
        "aws-marketplace:ListVerifications"
      ],
      "Resource": "*"
    }
  ]
}
```

### Allowing read-only access to business verification evidence

To allow a user or role read-only access to business verification evidence, you can
use ARN-based filtering to restrict access to a specific verification type.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetVerificationEvidence",
        "aws-marketplace:ListVerificationEvidence"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:*:`123456789012`:verification-type/business-verification/verification-evidence/*"
      ]
    }
  ]
}
```

### Restricting verification process operations by type

To restrict verification process operations to a specific verification type, use the
`aws-marketplace:VerificationType` condition key. The following example allows
verification process operations only for business verification.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartVerification",
        "aws-marketplace:GetVerification",
        "aws-marketplace:ListVerifications"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws-marketplace:VerificationType": "BusinessVerification"
        }
      }
    }
  ]
}
```

### Allowing actions on specific verification evidence resources

To allow actions on specific verification evidence resources, specify the ARN of the
resource in the `Resource` element of the IAM policy. The following example
allows all evidence management actions on a specific verification evidence resource.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:GetVerificationEvidence",
        "aws-marketplace:UpdateVerificationEvidence"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:`123456789012`:verification-type/business-verification/verification-evidence/`evidence-id`"
      ]
    }
  ]
}
```
