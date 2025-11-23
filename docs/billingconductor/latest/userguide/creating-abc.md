# Billing groups

When using Billing Conductor as a standalone service, a billing group is a set of accounts within your consolidated billing family that share a common end customer. This applies in the pro forma billing domain only. That end customer maintains the primary account, and can see the cost and usage that accrues across its group. Each billing group's pro forma usage is computed as its own consolidated billing family. Usage shares Reserved Instances and Savings Plans benefits only within the group, accrues volume tier discounts, and an [Always Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") offering. An account can only associate with one billing group during a billing period.

When using Billing Conductor with billing transfer, a billing group maps one-to-one with the AWS Organizations transferring its bills. Because of this one-to-one mapping, there are no changes to how reserved instances, Savings Plans, and volume discounts are calculated.

###### Note

For billing transfer billing groups, the primary account corresponds to the management account transferring its bill (bill source account). All linked accounts in the AWS Organizations must be included in the billing group because of the one-to-one mapping requirement.

###### Contents

- [Creating billing groups](create-billing-group.md "create-billing-group.md")
  - [Using Billing Conductor as a standalone service](create-billing-group.md#create-billing-group-standalone "create-billing-group.md#create-billing-group-standalone")
  - [Using Billing Conductor with billing transfer](create-billing-group.md#create-billing-group-tandem "create-billing-group.md#create-billing-group-tandem")

- [Viewing your billing group details](viewing-abc.md "viewing-abc.md")
  - [Viewing the billing group table](viewing-abc.md#table-billing-group "viewing-abc.md#table-billing-group")
  - [Viewing your pro forma configurations by billing group](viewing-abc.md#custom-pricing-view-proforma "viewing-abc.md#custom-pricing-view-proforma")
  - [Viewing your pro forma configurations by linked account](viewing-abc.md#view-proforma-linked-acct "viewing-abc.md#view-proforma-linked-acct")
  - [Viewing your billing details by custom pricing dimensions](viewing-abc.md#custom-pricing-view "viewing-abc.md#custom-pricing-view")

- [Configuring AWS CUR by billing group](configuring-abc.md "configuring-abc.md")
  - [Understanding the differences between AWS Billing Conductor AWS CUR and standard AWS CUR](configuring-abc.md#bp-standardCUR "configuring-abc.md#bp-standardCUR")
