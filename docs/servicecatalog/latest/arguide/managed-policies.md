# AWS managed polices

We recommend that you use AWS Service Catalog AppRegistry managed policies to add permissions to identies.
For more information see [IAM identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

You could create customer managed policies.
However, creating these types of polcies requires product expertise and time.
Managed policies are designed to help you get started quickly because they provide permissions for common use cases.
For more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update managed policies.
The permissions in these policies cannot be changed.
To support new features, services periodically add permissions to managed policies.
These updates effect all identities where you can find managed policies.
Services typically update these policies during feature launches or when new operations become available.
Services don't remove permissions from managed policies, so updates don't break existing permissions.

In addition, AWS supports managed policies for job functions that extend multiple services.
For example, the `ReadOnlyAccess` policy provides read-only access to all services and resources.
When services launch new features, AWS adds read-only permissions for new operations and resources.
For a list of job functions and their descriptions, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWSServiceCatalogAppRegistryFullAccess

AppRegistry provides you with `AWSServiceCatalogAppRegistryFullAccess`, an AWS managed policy that grants you full access to AppRegistry capabilities.

In this version of the policy, AppRegistry adds the resource group permissions `resource-groups:AssociateResource` and `resource-groups:DisassociateResource`, which allow you to call the resource groups for the AppRegistry `AssociateResource` and `DisassociateResource` APIs.

###### Note

You can use the AppRegistry `AssociateResource` and `DisassociateResource` APIs to add and remove resources associated with [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").
For more information, see [AssociateResource](../dg/API_app-registry_AssociateResource.md "../dg/API_app-registry_AssociateResource.md") and [DisassociateResource](../dg/API_app-registry_DisassociateResource.md "../dg/API_app-registry_DisassociateResource.md") in the _AWS Service Catalog AppRegistry Developer Guide_.

AppRegistry also adds the permission `tag:GetResources`, which allows you to return all tagged resources.
All tagged resources with defined tag keys and values can be included as resources for applications.

###### Permissions details

- **CloudFormation** – Allows AppRegistry to update a stack in CloudFormation.
- **Resource Groups** – Allows AppRegistry to create resource groups, return information about resource groups, delete resource groups, tag resource groups, return lists of tags associated with resource groups, remove tags from resource groups, retrieve resource tag information, and retrieve service configurations associated with resource groups.
- **IAM** – Allows AppRegistry to create an IAM role that's linked to a specific AWS service.

You can link to the following JSON policy in the IAM console or include it in your documentation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AppRegistryUpdateStackAndResourceGroupTagging",
 "Effect": "Allow",
 "Action": [
 "cloudformation:UpdateStack",
 "tag:GetResources"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "servicecatalog-appregistry.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AppRegistryResourceGroupsIntegration",
 "Effect": "Allow",
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:DeleteGroup",
 "resource-groups:GetGroup",
 "resource-groups:GetTags",
 "resource-groups:Tag",
 "resource-groups:Untag",
 "resource-groups:GetGroupConfiguration",
 "resource-groups:AssociateResource",
 "resource-groups:DisassociateResource"
 ],
 "Resource": "arn:aws:resource-groups:*:*:group/AWS_*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "servicecatalog-appregistry.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AppRegistryServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/servicecatalog-appregistry.amazonaws.com/AWSServiceRoleForAWSServiceCatalogAppRegistry*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "servicecatalog-appregistry.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AppRegistryOperations",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "servicecatalog:CreateApplication",
 "servicecatalog:GetApplication",
 "servicecatalog:UpdateApplication",
 "servicecatalog:DeleteApplication",
 "servicecatalog:ListApplications",
 "servicecatalog:AssociateResource",
 "servicecatalog:DisassociateResource",
 "servicecatalog:GetAssociatedResource",
 "servicecatalog:ListAssociatedResources",
 "servicecatalog:AssociateAttributeGroup",
 "servicecatalog:DisassociateAttributeGroup",
 "servicecatalog:ListAssociatedAttributeGroups",
 "servicecatalog:CreateAttributeGroup",
 "servicecatalog:UpdateAttributeGroup",
 "servicecatalog:DeleteAttributeGroup",
 "servicecatalog:GetAttributeGroup",
 "servicecatalog:ListAttributeGroups",
 "servicecatalog:SyncResource",
 "servicecatalog:ListAttributeGroupsForApplication",
 "servicecatalog:GetConfiguration",
 "servicecatalog:PutConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AppRegistryResourceTagging",
 "Effect": "Allow",
 "Action": [
 "servicecatalog:ListTagsForResource",
 "servicecatalog:UntagResource",
 "servicecatalog:TagResource"
 ],
 "Resource": "arn:aws:servicecatalog:*:*:*"
 }
 ]
}`

```

##

AWSServiceCatalogAppRegistryReadOnlyAccess

`AWSServiceCatalogAppRegistryReadOnlyAccess` is an AWS managed policy
that provides read-only access
to AppRegistry capabilites.
You can use this policy
to associate tag keys and values
with applications.

###### Note

All tagged resouces
with defined tag keys and values
can be included
as resources
for applications.

You can link
to this JSON policy
in the IAM console
or include it
in your documentation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:GetApplication",
 "servicecatalog:ListApplications",
 "servicecatalog:GetAssociatedResource",
 "servicecatalog:ListAssociatedResources",
 "servicecatalog:ListAssociatedAttributeGroups",
 "servicecatalog:GetAttributeGroup",
 "servicecatalog:ListAttributeGroups",
 "servicecatalog:ListTagsForResource",
 "servicecatalog:ListAttributeGroupsForApplication",
 "servicecatalog:GetConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy updates

The following table includes information about the updates to the `AWSServiceCatalogAppRegistryFullAccess` and `AWSServiceCatalogAppRegistryReadOnlyAccess` policies.

| Policy                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                    | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSServiceCatalogAppRegistryFullAccess](#full "#full") – Update to an existing policy                                                                  | Added the resource group permission `tag:GetResources`, which allows you to retrieve resource tag information.                                                                                                                                                                                                                                                 | December 07, 2023 |
| [AWSServiceCatalogAppRegistryFullAccess](#full "#full") – Update to an existing policy                                                                  | Added the resource group permissions `resource-groups:AssociateResource` and `resource-groups:DisassociateResource`, which allow you to call the resource groups for `AssociateResource` and `DisassociateResource`.                                                                                                                                           | November 13, 2023 |
| [AWSServiceCatalogAppRegistryFullAccess](#full "#full") – Update to an existing policy                                                                  | Added the following:<br>• `GetConfiguration` to retrieve a `TagKey` configuration from an account.<br>• `PutConfiguration` to associate a `TagKey` configuration with an account.<br>• The resource group actions `AssociateResource` and `DisassociateResource`, which are required to perform `AssociateResource` and `DisassociateResource` on a tag value. | November 17, 2022 |
| [AWSServiceCatalogAppRegistryReadOnlyAccess](#read-only "#read-only") – Update to an existing policy                                                    | Added `GetConfiguration` to retrieve a `TagKey` configuration from an account.                                                                                                                                                                                                                                                                                 | November 17, 2022 |
| [AWSServiceCatalogAppRegistryServiceRolePolicy](slr-appregistry.md#permissions-slr "slr-appregistry.md#permissions-slr") – Update to an existing policy | Updated `GetGroup` and `GetGroupConfiguration` permissions, which are required for AppRegistry to verify which service-linked resource groups exist in customer accounts.                                                                                                                                                                                      | October 24, 2022  |
| [AWSServiceCatalogAppRegistryFullAccess](#full "#full") – Update to an existing policy                                                                  | Added `ListAttributeGroupsForApplication` to list the details of all attribute groups associated with an application.                                                                                                                                                                                                                                          | June 15, 2022     |
| [AWSServiceCatalogAppRegistryReadOnlyAccess](#read-only "#read-only") – Update to an existing policy                                                    | Added `ListAttributeGroupsForApplication` to list the details of all attribute groups associated with an application.                                                                                                                                                                                                                                          | June 15, 2022     |
| [AWSServiceCatalogAppRegistryServiceRolePolicy](slr-appregistry.md "slr-appregistry.md") – Update to an existing policy                                 | Added permissions to tag AWS Resource Groups when AWS Resource Groups are created.                                                                                                                                                                                                                                                                             | August 24, 2021   |
| [AWSServiceCatalogAppRegistryFullAccess](#full "#full") – Update to an existing policy                                                                  | Added the following:<br>• `UpdateStack` permissions to perform `SyncResource`, which updates the tags on the AWS Service Catalog stack.<br>• `TagResource`, `ListTagForResources`, and `UntagResource` to perform tagging operations on resources.<br>• `GetAssociatedResource`, as part of the integration with AWS Resource Groups.                          | August 24, 2021   |
| [AWSServiceCatalogAppRegistryReadOnlyAccess](#read-only "#read-only") – Update to an existing policy                                                    | Added the following:<br>• `ListTagForResources` to list all of the tags on a resource.<br>• `GetAssociatedResource`, as part of the integration with AWS Resource Groups.                                                                                                                                                                                      | August 24, 2021   |
