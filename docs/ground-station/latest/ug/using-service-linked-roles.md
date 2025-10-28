# Use service-linked roles for

Ground Station

AWS Ground Station uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Ground Station. Service-linked roles are predefined by Ground Station and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Ground Station easier because you don’t have to
manually add the necessary permissions. Ground Station defines the permissions of its
service-linked roles, and unless defined otherwise, only Ground Station can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

Ground Station

Ground Station uses the service-linked role named **AWSServiceRoleForGroundStationDataflowEndpointGroup** –
AWS GroundStation uses this service-linked role to invoke EC2 to find public IPv4 addresses.

The AWSServiceRoleForGroundStationDataflowEndpointGroup service-linked role trusts the following services to assume the
role:

- `groundstation.amazonaws.com`

The role permissions policy named AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy allows Ground Station to complete the following actions on the
specified resources:

- Action: `ec2:DescribeAddresses` on
  `all AWS resources (*)`

Action allows Ground Station to list all IPs associated with EIPs.

- Action: `ec2:DescribeNetworkInterfaces` on
  `all AWS resources (*)`

Action allows Ground Station to get information on the network interfaces associated with EC2 instances

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

Ground Station

You don't need to manually create a service-linked role. When you
create a DataflowEndpointGroup in the AWS CLI or the AWS API, Ground Station
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a DataflowEndpointGroup,
Ground Station creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**Data Delivery to Amazon EC2** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `groundstation.amazonaws.com` service name. For more
information, see [Creating a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for

Ground Station

Ground Station does not allow you to edit the AWSServiceRoleForGroundStationDataflowEndpointGroup service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

Ground Station

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained.

You can delete a service-linked role only after first deleting the DataflowEndpointGroups using the service-linked role.
This protects you from inadvertently revoking permissions to your DataflowEndpointGroups. If a service-linked role is used with
multiple DataflowEndpointGroups, you must delete all DataflowEndpointGroups that use the service-linked role before you can delete it.

###### Note

If the Ground Station service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete Ground Station resources used by the AWSServiceRoleForGroundStationDataflowEndpointGroup

- Delete DataflowEndpointGroups via the AWS CLI or the AWS API.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForGroundStationDataflowEndpointGroup
service-linked role. For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for

Ground Station service-linked roles

Ground Station supports using service-linked roles in all of the regions where the service is available. For more information, see [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Troubleshooting

`NOT_AUTHORIZED_TO_CREATE_SLR` - This indicates the role in your account that is being used to call the CreateDataflowEndpointGroup API does not have the `iam:CreateServiceLinkedRole` permission.
An administrator with the `iam:CreateServiceLinkedRole` permission must manually create the Service-Linked Role for your account.
