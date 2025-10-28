# Using service-linked roles for

RTB Fabric

AWS RTB Fabric uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to RTB Fabric. Service-linked roles are predefined by RTB Fabric and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up RTB Fabric easier because you don't have to
manually add the necessary permissions. RTB Fabric defines the permissions of its
service-linked roles, and unless defined otherwise, only RTB Fabric can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your RTB Fabric resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for RTB Fabric

RTB Fabric uses the service-linked role named `AWSServiceRoleForRTBFabric` –
A service-linked role required for AWS RTB Fabric to access your network interface resources and deliver metrics. `AWSServiceRoleForRTBFabric` uses managed policy [RTBFabricServiceRolePolicy](security-iam-awsmanpol.md#aws-managed-policy-RTBFabricServiceRolePolicy "security-iam-awsmanpol.md#aws-managed-policy-RTBFabricServiceRolePolicy").

The AWSServiceRoleForRTBFabric service-linked role trusts the following services to assume the
role:

- `rtbfabric.amazonaws.com`

The role permissions policy allows RTB Fabric to complete the
following actions on the specified resources:

- Action: `ec2:CreateNetworkInterface` on subnets and security groups
- Action: `ec2:CreateNetworkInterface` on network interfaces with the `RTBFabricManaged:true` tag
- Action: `ec2:CreateNetworkInterfacePermission` on network interfaces tagged with `RTBFabricManaged:true`
- Action: `ec2:DeleteNetworkInterface` and `ec2:DetachNetworkInterface` on network interfaces tagged with `RTBFabricManaged:true`
- Action: `ec2:CreateTags` on network interfaces during creation
- Action: `ec2:Describe*` on EC2 resources for network interface management
- Action: `cloudwatch:PutMetricData` to the `AWS/RTBFabric` namespace

The complete permissions policy for this role is available in the [AWS Managed Policy Reference](../../../aws-managed-policy/latest/reference/RTBFabricServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/RTBFabricServiceRolePolicy.md"). For information about policy updates, see [AWS managed policy updates](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for RTB Fabric

You don't need to manually create a service-linked role. When you
create an RTB application for the first time (CreateRequesterRtbApp or CreateResponderRtbApp) in the AWS Management Console, the AWS CLI, or the AWS API, RTB Fabric creates
the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create an RTB application for the first time (CreateRequesterRtbApp or CreateResponderRtbApp),
RTB Fabric creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**RTB Fabric** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `rtbfabric.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for RTB Fabric

RTB Fabric does not allow you to edit the AWSServiceRoleForRTBFabric service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for RTB Fabric

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the RTB Fabric service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete RTB Fabric resources used by the AWSServiceRoleForRTBFabric

1. Delete all RTB applications in your account. You must delete both requester and responder gateways before you can delete the service-linked role. You can use either the console or the CLI:
   1. **Console method:** For instructions on deleting requester gateways, see [Deleting a requester gateway](../../../requester-rtb-applications.md#delete-requester-rtb-application "../../../requester-rtb-applications.md#delete-requester-rtb-application"). For instructions on deleting responder gateways, see [Deleting a responder gateway](../../../responder-rtb-applications.md#delete-responder-rtb-application "../../../responder-rtb-applications.md#delete-responder-rtb-application").
   2. **CLI method:** Use the `DeleteRequesterGateway` or `DeleteResponderGateway` API to delete RTB gateways. Replace the example gateway ID with your gateway ID:

   ```
   aws rtbfabric delete-requester-gateway --gateway-id `rtb-gw-abc123xyz789`
   ```

   The response returns a status of `DELETING`:

   ```
   {
   "gatewayId": "rtb-gw-abc123xyz789",
   "status": "DELETING"
   }
   ```

   Repeat this command for each RTB application in your account.

2. After deleting all RTB applications, wait for RTB Fabric to automatically clean up the network interfaces tagged with `RTBFabricManaged:true`. This process can take up to 20 minutes.
3. Verify that no RTB applications or RTB Fabric-managed network interfaces remain in your account:
   1. Open the RTB Fabric console and verify that no RTB applications are listed.
   2. Open the [Network Interfaces page](https://console.aws.amazon.com/ec2/home#NetworkInterfaces "https://console.aws.amazon.com/ec2/home#NetworkInterfaces") of the Amazon EC2 console.
   3. In the search box, enter `tag:RTBFabricManaged:true` to filter for RTB Fabric-managed network interfaces.
   4. Verify that no network interfaces appear in the results.

###### Note

RTBFabric only deletes the network interface if no other RTBFabric configuration is using that network interface. If you have multiple RTBFabric configurations using the same subnet and security group combination, the network interface will remain until all configurations are removed.

###### Note

RTBFabric relies on the service-linked role permissions to delete network interfaces. Do not delete the AWSServiceRoleForRTBFabric role before RTBFabric completes the network interface cleanup, or the cleanup may fail.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForRTBFabric service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for RTB Fabric service-linked roles

RTB Fabric supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
