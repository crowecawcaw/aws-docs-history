# Policies and permissions for AWS Marketplace

sellers

AWS Marketplace provides a set of managed policies for use with the AWS Marketplace Management Portal. In addition, you can
use individual permissions to create your own AWS Identity and Access Management (IAM) policy.

You can also provide fine-grained access to the AWS Marketplace Management Portal for the
**Settings**, **Contact Us**, **File
Upload**, and **Insights** tabs. Fine-grained access enables you to
do the following:

- Grant other people permission to administer and use resources in your AWS account
  without sharing your password or access key.
- Grant granular permissions to multiple people for various resources. For example, you
  might allow some users access to view the **Settings** tab in the
  AWS Marketplace Management Portal. For other users, you might allow access to edit in the
  **Settings** and **Contact Us** tabs.

###### Note

For more information about policies and permissions in AWS Data Exchange for data products, see [Identity and
Access Management in AWS Data Exchange](../../../data-exchange/latest/userguide/auth-access.md "../../../data-exchange/latest/userguide/auth-access.md") in the _AWS Data Exchange User Guide_.

For more information about policies and permissions for AWS Marketplace buyers, see [Controlling access
to AWS Marketplace subscriptions](../buyerguide/buyer-iam-users-groups-policies.md "../buyerguide/buyer-iam-users-groups-policies.md") in the _AWS Marketplace Buyer Guide_.

## Policies for AWS Marketplace sellers

You can use the following managed policies to provide users with controlled access to the
AWS Marketplace Management Portal:

**`AWSMarketplaceSellerFullAccess`**

Allows full access to all of the pages in the AWS Marketplace Management Portal and other AWS services,
such as Amazon Machine Image (AMI) management.

**`AWSMarketplaceSellerProductsFullAccess`**

Allows full access to the [Products](https://aws.amazon.com/marketplace/management/products/ "https://aws.amazon.com/marketplace/management/products/") pages in the
AWS Marketplace Management Portal.

**`AWSMarketplaceSellerProductsReadOnly`**

Allows read-only access to the [Products](https://aws.amazon.com/marketplace/management/products/ "https://aws.amazon.com/marketplace/management/products/") pages in the
AWS Marketplace Management Portal.

###### Important

AWS Marketplace buyers can use managed policies to manage the subscriptions they purchase. The
names of the managed policies that you use with AWS Marketplace Management Portal start with
`AWSMarketplaceSeller`. When you search for policies in IAM, make sure to
search for policy names that start with `AWSMarketplaceSeller`. For more information about those policies, see the _AWS Managed Policy Reference_.

AWS Marketplace also provides specialized managed policies for specific scenarios. For a full
list of AWS managed policies for AWS Marketplace sellers and descriptions of what permissions they
provide, see [AWS managed policies for AWS Marketplace sellers](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Permissions for AWS Marketplace sellers

You can use the following permissions in IAM policies for the AWS Marketplace Management Portal:

**`aws-marketplace-management:PutSellerVerificationDetails`**

Allows access to start the Know Your Customer (KYC) process.

**`aws-marketplace-management:GetSellerVerificationDetails`**

Allows access to view the KYC status in the AWS Marketplace Management Portal.

**`aws-marketplace-management:PutBankAccountVerificationDetails`**

Allows access to start the [bank account verification](registration-process.md#completing-bank-account-verification "registration-process.md#completing-bank-account-verification") process.

**`aws-marketplace-management:GetBankAccountVerificationDetails`**

Allows access to view the bank account verification status in the AWS Marketplace Management Portal.

**`aws-marketplace-management:PutSecondaryUserVerificationDetails`**

Allows access to add secondary users in the AWS Marketplace Management Portal.

**`aws-marketplace-management:GetSecondaryUserVerificationDetails`**

Allows access to view the secondary user status in the AWS Marketplace Management Portal.

**`aws-marketplace-management:GetAdditionalSellerNotificationRecipients`**

Allows access to view email contacts for AWS Marketplace notifications.

**`aws-marketplace-management:PutAdditionalSellerNotificationRecipients`**

Allows access to update email contacts for AWS Marketplace notifications.

**`tax:PutTaxInterview`**

Allows access to take the [tax interview](registration-process.md#tax-info-for-sellers "registration-process.md#tax-info-for-sellers") in the AWS Marketplace Management Portal.

**`tax:GetTaxInterview`**

Allows access to view the tax interview status in the AWS Marketplace Management Portal.

**`tax:GetTaxInfoReportingDocument`**

Allows AWS Marketplace sellers to view and download tax documents (for example, 1099-K
forms) from the Tax dashboard

**`payments:CreatePaymentInstrument`**

Allows access to add a bank account to the AWS Marketplace Management Portal.

**`payments:GetPaymentInstrument`**

Allows access to view existing bank accounts in the AWS Marketplace Management Portal.

**`support:CreateCase`**

Allows access to create an AWS Marketplace case within the AWS Marketplace Management Portal.

**`aws-marketplace-management:viewSupport`**

Allows access to the [Customer Support Eligibility](https://aws.amazon.com/marketplace/management/support/ "https://aws.amazon.com/marketplace/management/support/") page in the AWS Marketplace Management Portal.

**`aws-marketplace-management:viewReports`**

Allows access to the [Reports](https://aws.amazon.com/marketplace/management/reports/ "https://aws.amazon.com/marketplace/management/reports/") page in the AWS Marketplace Management Portal.

**`aws-marketplace:ListEntities`**

Allows access to list objects in AWS Marketplace Management Portal. Required to access the [File Upload](https://aws.amazon.com/marketplace/management/product-load/ "https://aws.amazon.com/marketplace/management/product-load/"),
[Offers](https://aws.amazon.com/marketplace/management/offers "https://aws.amazon.com/marketplace/management/offers") and [Partners](https://aws.amazon.com/marketplace/management/partners "https://aws.amazon.com/marketplace/management/partners") pages in the
AWS Marketplace Management Portal.

###### Note

To allow access to view the **Settings** tab, you can use this
permission, the `ListEntity` permission, and the following Amazon Resource
Name (ARN):
`arn:{partition}:{aws-marketplace}:{region}:{account-id}:AWSMarketplace/Seller/{entity-id}`.

**`aws-marketplace:DescribeEntity`**

Allows access to view details of objects in AWS Marketplace Management Portal. Required to access the [File Upload](https://aws.amazon.com/marketplace/management/product-load/ "https://aws.amazon.com/marketplace/management/product-load/"),
[Offers](https://aws.amazon.com/marketplace/management/offers "https://aws.amazon.com/marketplace/management/offers"), [Partners](https://aws.amazon.com/marketplace/management/partners "https://aws.amazon.com/marketplace/management/partners"), and [Agreements](https://aws.amazon.com/marketplace/management/agreements "https://aws.amazon.com/marketplace/management/agreements") pages in
the AWS Marketplace Management Portal.

###### Note

To allow access to view the **Settings** tab, you can use this
permission, the `DescribeEntity` permission, and the following ARN:
`arn:{partition}:{aws-marketplace}:{region}:{account-id}:AWSMarketplace/Seller/*`.

**`aws-marketplace:StartChangeSet`**

Allows access to create product changes in AWS Marketplace Management Portal. Required to make changes in
the [File
Upload](https://aws.amazon.com/marketplace/management/product-load/ "https://aws.amazon.com/marketplace/management/product-load/"), [Offers](https://aws.amazon.com/marketplace/management/offers "https://aws.amazon.com/marketplace/management/offers"), [Partners](https://aws.amazon.com/marketplace/management/partners "https://aws.amazon.com/marketplace/management/partners"), and [Agreements](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md") pages in the AWS Marketplace Management Portal.

###### Note

To allow access to register as a seller in AWS Marketplace, you can use this permission, the
`catalog:ChangeType: "CreateSeller"` condition key, and the following
ARN:
`arn:{partition}:{aws-marketplace}:{region}:{account-id}:AWSMarketplace/Seller/{entity-id}`.

To allow access to update the seller profile in AWS Marketplace, you can use this
permission, the `catalog:ChangeType: "UpdateInformation"` condition key,
and the following ARN:
`arn:{partition}:{aws-marketplace}:{region}:{account-id}:AWSMarketplace/Seller/{entity-id}`.

To allow access to update disbursement preferences for Amazon Web Services, you can use this
permission, the `catalog:ChangeType: "UpdateDisbursementPreferences"`
condition key, and the following ARN:
`arn:{partition}:{aws-marketplace}:{region}:{account-id}:AWSMarketplace/Seller/{entity-id}`.

**`aws-marketplace:SearchAgreements`**

Allows viewing the high-level list of agreements on the [Agreements](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md")
page, and opportunities between ISVs and channel partners on the [Partners](channel-partner-offers.md "channel-partner-offers.md") page.

**`aws-marketplace:DescribeAgreement`**

Allows viewing of high-level agreement details on the
**Agreements** page, and opportunities between ISVs and channel
partners on the **Partners** page.

**`aws-marketplace:GetAgreementTerms`**

Allows viewing all agreement term details on the **Agreements**
page, and opportunities between ISVs and channel partners on the
**Partners** page.

**`aws-marketplace:GetSellerDashboard`**

Allows access to the dashboards on the **Insights** page in the
AWS Marketplace Management Portal.

**`aws-marketplace:ListAssessments`**

Allows access to view a list of assessments pending seller action.

**`aws-marketplace:DescribeAssessment`**

Allows access to view the details of assessments pending seller action.

###### Note

To enable a user to access the [Manage Products](https://aws.amazon.com/marketplace/management/products/ "https://aws.amazon.com/marketplace/management/products/") page, you
must use either the `AWSMarketplaceSellerProductsFullAccess` or
`AWSMarketplaceSellerProductsReadOnly` managed permissions.

You can combine the preceding permissions into a single IAM policy to grant the
permissions that you want. See the following examples.

## Example 1: Permissions to view the KYC

status

To grant permissions to view KYC status in the AWS Marketplace Management Portal, use a policy similar to the
following example.

To grant permissions to view the KYC status in the AWS Marketplace Management Portal, use a policy similar to the
following example.

JSON

```
`{"Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "aws-marketplace-management:GetSellerVerificationDetails"
 ],
 "Resource": ["*"]
 }]
}`

```

## Example 2: Permissions to create upgrades

and renewals for private offers

To grant permissions to view and use the **Agreements** page to create
upgrades and renewals for private offers, use a policy similar to the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:SearchAgreements",
 "aws-marketplace:DescribeAgreement",
 "aws-marketplace:GetAgreementTerms",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:StartChangeSet"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws-marketplace:PartyType": "Proposer"
 },
 "ForAllValues:StringEquals": {
 "aws-marketplace:AgreementType": [
 "PurchaseAgreement"
 ]
 }
 }
 }
 ]
}`

```

## Example 3: Permissions to access the Offers

page and create new private offers

To grant permissions to view and use the **Offers** page to view existing
private offers and create private offers, use a policy similar to the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:StartChangeSet"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Example 4: Permissions to access the Settings

page

To grant permissions to view and use the **Settings** page, use a policy
similar to the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:StartChangeSet"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:aws-marketplace:`us-east-1`:`111122223333`:AWSMarketplace/Seller/*"
 }
 ]
}`

```

## Example 5: Permissions to access the File Upload

page

To grant permissions to view and use the **File Upload** page, use a
policy similar to the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:StartChangeSet"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Using IAM groups

Alternatively, you can create separate IAM groups for granting access to each individual
page in the AWS Marketplace Management Portal. Users can belong to more than one group. So, if a user needs access to
more than one page, you can add the user to all of the appropriate groups. For example, create
one IAM group and grant that group permission to access the **Insights**
page, create another group and grant that group permission to access the **File
Upload** page, and so on. If a user needs permission to access both the
**Insights** page and the **File Upload** page, add the
user to both groups.

For more information about users and groups, see [IAM
Identities (users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.
