• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with associations using

IAM

State Manager, a tool in AWS Systems Manager, uses [targets](systems-manager-state-manager-targets-and-rate-controls.md#systems-manager-state-manager-targets-and-rate-controls-about-targets "systems-manager-state-manager-targets-and-rate-controls.md#systems-manager-state-manager-targets-and-rate-controls-about-targets") to choose which instances you configure your associations with.
Originally, associations were created by specifying a document name
(`Name`) and instance ID (`InstanceId`). This created an
association between a document and an instance or managed node. Associations used to
be identified by these parameters. These parameters are now deprecated, but they're
still supported. The resources `instance` and
`managed-instance` were added as resources to actions with
`Name` and `InstanceId`.

AWS Identity and Access Management (IAM) policy enforcement behavior depends on the type of resource
specified. Resources for State Manager operations are only enforced based on the
passed-in request. State Manager doesn't perform a deep check for the properties of
resources in your account. A request is only validated against policy resources if
the request parameter contains the specified policy resources. For example, if you
specify an instance in the resource block, the policy is enforced if the request
uses the `InstanceId` parameter. The `Targets` parameter for
each resource in the account isn't checked for that `InstanceId`.

Following are some cases with confusing behavior:

- [DescribeAssociation](../APIReference/API_DescribeActivations.md "../APIReference/API_DescribeActivations.md"), [DeleteAssociation](../APIReference/API_DeleteAssociation.md "../APIReference/API_DeleteAssociation.md"), and [UpdateAssociation](../APIReference/API_UpdateAssociation.md "../APIReference/API_UpdateAssociation.md") use `instance`,
  `managed-instance`, and `document` resources to
  specify the deprecated way of referring to associations. This includes all
  associations created with the deprecated `InstanceId`
  parameter.
- [CreateAssociation](../APIReference/API_CreateAssociation.md "../APIReference/API_CreateAssociation.md"), [CreateAssociationBatch](../APIReference/API_CreateAssociationBatch.md "../APIReference/API_CreateAssociationBatch.md"), and [UpdateAssociation](../APIReference/API_UpdateAssociation.md "../APIReference/API_UpdateAssociation.md") use `instance` and
  `managed-instance` resources to specify the deprecated way of
  referring to associations. This includes all associations created with the
  deprecated `InstanceId` parameter. The `document`
  resource type is part of the deprecated way of referring to associations and
  is an actual property of an association. This means you can construct IAM
  policies with `Allow` or `Deny` permissions for both
  `Create` and `Update` actions based on document
  name.
  For more information about using IAM policies with Systems Manager, see [Identity and access management for
  AWS Systems Manager](security-iam.md "security-iam.md") or [Actions, resources, and condition keys for AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md "../../../service-authorization/latest/reference/list_awssystemsmanager.md") in the
  _Service Authorization Reference_.
