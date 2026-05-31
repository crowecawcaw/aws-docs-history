After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Setting up an Amazon FinSpace environment

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

An Amazon FinSpace environment is created from an AWS account. In this section, you sign up for an AWS account, create an administrator access, and create a FinSpace environment.

######

Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [(Optional) Attach managed policies for creating FinSpace environment](#optional-attach-managed-policies-for-creating-finspace-environment "#optional-attach-managed-policies-for-creating-finspace-environment")
- [Create an Amazon FinSpace environment](create-an-amazon-finspace-environment.md "create-an-amazon-finspace-environment.md")
- [Sample data bundles](sample-data-bundle.md "sample-data-bundle.md")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## (Optional) Attach managed policies for creating FinSpace environment

To create a FinSpace environment, the user performing the actions must have IAM permissions for `AdministratorAccess` or must have the FinSpace managed policy attached to their role. This step is optional if the user has `AdministratorAccess` permissions. Create and attach FinSpace managed policies to the account you used to create the FinSpace environment. These policies grant permissions to create the FinSpace environment and superusers in an AWS
account.

1. Create a managed policy on the JSON tab for FinSpace. For more information, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor").
2. Use the following managed policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "finspace:*"
 ],
 "Resource": "*"
 }
 ]
}`

```
