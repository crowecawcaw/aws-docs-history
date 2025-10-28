AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# AWS managed views

A _managed view_ is how other AWS services can access resource
information indexed by Resource Explorer for your AWS account or organization with your consent.

###### Topics

- [About managed views](#about-managed-views "#about-managed-views")
- [Listing managed views](listing-managed-views.md "listing-managed-views.md")
- [Deleting managed views](deleting-managed-views.md "deleting-managed-views.md")

## About managed views

Managed views can be updated or deleted only by the service that created the managed view.
An AWS service creates a managed view using [IAM forward access sessions
(FAS)](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") or a [service-linked role
(SLR)](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md").

Resource Explorer uses a [resource-based
policy](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to control access to the managed view. When an AWS service creates a
managed view, Resource Explorer attaches the resource-based policy to the view. This policy allows the
managing AWS service to use and delete the view and allows view's resource owners to list
and retrieve details about the view. The following is an example resource-based policy
attached to a managed view:

Managed views can only be updated or deleted by the service that created the managed view.
An AWS service creates a managed view using [IAM forward access sessions
(FAS)](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") or a [service-linked role
(SLR)](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md").

Resource Explorer uses a [resource-based
policy](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to control access to the managed view. When an AWS service creates a
managed view, Resource Explorer attaches the resource-based policy to the view. This policy allows the
managing AWS service to use and delete the view and allows view's resource owners to list
and retrieve details about the view. The following is an example resource-based policy
attached to a managed view:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`view_UUID`_ACCESS_TO_SERVICE_PRINCIPAL",
 "Effect": "Allow",
 "Principal": {
 "Service": "sampleservice.amazonaws.com"
 },
 "Action": [
 "resource-explorer-2:GetManagedView",
 "resource-explorer-2:Search"
 ],
 "Resource": "`arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Sid": "`view_UUID`_DENY_ACCESS_TO_NON_SERVICE_PRINCIPAL",
 "Effect": "Deny",
 "Principal": "*",
 "Condition": {
 "ForAllValues:StringNotEquals": {
 "aws:PrincipalServiceNamesList": [
 "sampleservice.amazonaws.com"
 ]
 }
 },
 "NotAction": [
 "resource-explorer-2:GetManagedView"
 ],
 "Resource": "`arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`"
 }
 ]
 }`

```

Managed views can only be deleted by the AWS service that manages them. Before the
managing service can delete the view, you may need to perform service-specific tasks to remove a
managed view from your account.

Resource Explorer managed views use the AWS Systems Manager `AWSManagedViewForSSM` unified console
resource, which allows Systems Manager to access resource information indexed by Resource Explorer for your
organization. If you want to delete the managed view, you must disable the unified console in
Systems Manager. For instructions, see [Disabling the Systems Manager unified console](../../../systems-manager/latest/userguide/systems-manager-disable-integrated-console.md "../../../systems-manager/latest/userguide/systems-manager-disable-integrated-console.md") in the _AWS Systems Manager User Guide_.
