

# AWSManagedSignUpAdminAccess
<a name="AWSManagedSignUpAdminAccess"></a>

**Description**: Grants AWS permission to complete signup for AWS managed accounts.

`AWSManagedSignUpAdminAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSManagedSignUpAdminAccess-how-to-use"></a>

You can attach `AWSManagedSignUpAdminAccess` to your users, groups, and roles.

## Policy details
<a name="AWSManagedSignUpAdminAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: July 20, 2026, 19:27 UTC 
+ **Edited time:** July 20, 2026, 19:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSManagedSignUpAdminAccess`

## Policy version
<a name="AWSManagedSignUpAdminAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSManagedSignUpAdminAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PaymentWidgetPermissions",
      "Effect" : "Allow",
      "Action" : [
        "payments:CreatePaymentInstrument",
        "payments:GetPaymentInstrument",
        "payments:GetPaymentStatus",
        "payments:ListPaymentPreferences",
        "payments:ListTagsForResource",
        "payments:MakePayment",
        "payments:TagResource",
        "payments:UntagResource",
        "payments:UpdatePaymentInstrument",
        "payments:UpdatePaymentPreferences"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "BillingPermissions",
      "Effect" : "Allow",
      "Action" : [
        "billing:GetSellerOfRecord"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AccountPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account:GetContactInformation"
      ],
      "Resource" : "arn:aws:account::*:account"
    },
    {
      "Sid" : "InvoicingPermissions",
      "Effect" : "Allow",
      "Action" : [
        "invoicing:GetInvoicePDF"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "TaxWidgetPermissions",
      "Effect" : "Allow",
      "Action" : [
        "tax:BatchPutTaxRegistration",
        "tax:DeleteTaxRegistration",
        "tax:GetTaxRegistration",
        "tax:GetTaxRegistrationDocument",
        "tax:ListTaxRegistrations",
        "tax:PutTaxRegistration"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CustomerVerificationWidgetPermissions",
      "Effect" : "Allow",
      "Action" : [
        "customer-verification:CreateCustomerVerificationDetails",
        "customer-verification:CreateUploadUrls",
        "customer-verification:GetCustomerVerificationDetails",
        "customer-verification:GetCustomerVerificationEligibility",
        "customer-verification:UpdateCustomerVerificationDetails"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSManagedSignUpAdminAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)