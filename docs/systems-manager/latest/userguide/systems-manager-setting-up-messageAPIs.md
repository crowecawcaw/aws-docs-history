• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Reference: ec2messages,

ssmmessages, and other API operations

If you monitor API operations, you might see calls to the following operations:

- `ec2messages:AcknowledgeMessage`
- `ec2messages:DeleteMessage`
- `ec2messages:FailMessage`
- `ec2messages:GetEndpoint`
- `ec2messages:GetMessages`
- `ec2messages:SendReply`
- `ssmmessages:CreateControlChannel`
- `ssmmessages:CreateDataChannel`
- `ssmmessages:OpenControlChannel`
- `ssmmessages:OpenDataChannel`
- `ssm:DescribeDocumentParameters`
- `ssm:DescribeInstanceProperties`
- `ssm:GetCalendar`
- `ssm:GetManifest`
- `ssm:ListInstanceAssociations`
- `ssm:PutCalendar`
- `ssm:PutConfigurePackageResult`
- `ssm:RegisterManagedInstance`
- `ssm:RequestManagedInstanceRoleToken`
- `ssm:UpdateInstanceAssociationStatus`
- `ssm:UpdateInstanceInformation`
- `ssm:UpdateManagedInstancePublicKey`
  These are special operations used by AWS Systems Manager, as described in the rest of this
  topic.

## Agent-related API operations

(`ssmmessages` and `ec2messages` endpoints)

###### ssmmessages API operations

Systems Manager uses the `ssmmessages` endpoint for the following types of API
operations:

- Operations from Systems Manager Agent (SSM Agent) to the Systems Manager service in the cloud.
- Operations from SSM Agent to Session Manager, a tool in AWS Systems Manager, in the cloud. This
  endpoint is required to create and delete session channels with the Session Manager service
  in the cloud. Additionally, if connectivity is allowed, SSM Agent receives
  `Command` documents through this Amazon Message Gateway
  Service. If connectivity is not allowed, SSM Agent receives
  `Command` documents through the Amazon Message Delivery
  Service. For more information, see [Actions, resources, and condition keys for Amazon Message Gateway
  Service](../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md "../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md").

###### Note

If the `ssmmessages:OpenControlChannel` permission is removed from
policies attached to your IAM instance profile or IAM service role,SSM Agent
on the managed node loses connectivity to the Systems Manager service in the cloud.
However, it can take up to 1 hour for a connection to be terminated after the
permission is removed. This is the same behavior as when the IAM instance role
or IAM service role is deleted.

Note that the `ssmmessages:OpenControlChannel` permission is
included in the managed policy [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md"), which is used in the instructions for
[creating an IAM instance profile](setup-instance-permissions.md#instance-profile-add-permissions "setup-instance-permissions.md#instance-profile-add-permissions") for EC2 instances and for [creating an IAM service role](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md") for non-EC2 instances.

- Operations from Run Command.

###### ec2messages API operations

`ec2messages:*` API operations are made to the Amazon
Message Delivery Service endpoint. Systems Manager uses this endpoint for API
operations from Systems Manager Agent (SSM Agent) to the Systems Manager service in the cloud.

###### Important

`ec2messages:*` API operations are supported only in
AWS Regions that launched before 2024. In Regions launched in 2024 and later, only
`ssmmessages:*` API operations are supported.

###### Endpoint connection precedence

Beginning with version 3.3.40.0 of SSM Agent, Systems Manager began using the
`ssmmessages:*` endpoint (Amazon Message Gateway Service)
whenever available instead of the `ec2messages:*` endpoint
(Amazon Message Delivery Service).

If you provide access to `ssmmessages:*` in your AWS Identity and Access Management (IAM) permission
policies, SSM Agent connects to the `ssmmessages:*` endpoint, even if your IAM
instance profile is configured to allow both endpoints. This includes policies for [IAM instance profiles](setup-instance-permissions.md#instance-profile-add-permissions "setup-instance-permissions.md#instance-profile-add-permissions") and [IAM service roles](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md") you have created
yourself, and for IAM instance profiles created by the [Quick Setup Host management configuration](quick-setup-host-management.md "quick-setup-host-management.md") and
[Default Host
Management Configuration](quick-setup-default-host-management-configuration.md "quick-setup-default-host-management-configuration.md").

If you have provided permissions for both endpoints and monitor API operations using, for
example, CloudWatch Metrics, you will see no calls to `ec2messages:*`.

For AWS Regions launched before 2024: You can safely remove `ec2messages:*` permissions from your policies at this time.

###### Endpoint connection failover

For AWS Regions launched before 2024 only: If your IAM instance profile does not
provide permissions for `ssmmessages:*` at the time the agent starts, but
only `ec2messages:*`, SSM Agent connects to the `ec2messages:*` endpoint. If you have both
`ssmmessages:*` and `ec2messages:*` at the time
SSM Agent starts, but remove `ssmmessages:*` after the agent starts, SSM Agent
soon switches the connection to the `ec2messages:*` endpoint.
For Regions launched in 2024 and later, only the `ssmmessages:*` endpoint is
supported.

For more information about the `ssmmessages` and `ec2messages:*` endpoints, see the following topics in the _AWS Service Authorization Reference_.

- [Actions, resources, and condition keys for Amazon Message Gateway
  Service](../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md "../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md") (`ssmmessages`).
- [Actions, resources, and condition keys for Amazon Message Delivery
  Service](../../../service-authorization/latest/reference/list_amazonmessagedeliveryservice.md "../../../service-authorization/latest/reference/list_amazonmessagedeliveryservice.md") (`ec2messages:*`)

## `ssm:*` namespace instance-related API

operations

`DescribeDocumentParameters`

Systems Manager runs this API operation to render specific nodes in the Amazon EC2
console. Results of the `DescribeDocumentParameters` operation
are displayed in the Documents node.

`DescribeInstanceProperties`

Systems Manager runs this API operations to render specific nodes in the Amazon EC2
console. Results of the `DescribeInstanceProperties` operation are displayed in the
Fleet Manager node.

`GetCalendar`

Systems Manager runs this API operation to render Change Calendar type documents in the
Change Calendar console.

`GetManifest`

SSM Agent runs this API operation to determine system requirements for
installing or updating a specified version of an [AWS Systems Manager Distributor](distributor.md "distributor.md") package. This is a legacy API operation
and not available in AWS Regions launched after 2017.

`ListInstanceAssociations`

SSM Agent runs this API operation to see if a new State Manager association is
available. This API operation is required for State Manager to function.

`PutCalendar`

Systems Manager runs this API operation to update Change Calendar type documents in the
Change Calendar console.

`PutConfigurePackageResult`

SSM Agent runs this API operation to publish installation error and latency
metrics for public Distributor packages to the package owner’s
account.

`RegisterManagedInstance`

SSM Agent runs this API operation for the following scenarios:

- To register an on-premises server or virtual machine (VM) with
  Systems Manager as a managed instance using an activation code and ID.
- To register AWS IoT Greengrass Version 2 credentials.

This operation is also called by Amazon EC2 instances running SSM Agent version
3.1.x or later.

`RequestManagedInstanceRoleToken`

SSM Agent runs this API operation to retrieve temporary credentials to
access the managed node.

`UpdateInstanceAssociationStatus`

SSM Agent runs this API operation to update an association. This API
operation is required for State Manager, a tool in AWS Systems Manager, to function.

`UpdateInstanceInformation`

SSM Agent calls the Systems Manager service in the cloud every 5 minutes to provide
heartbeat information. This call is necessary to maintain a heartbeat with
the agent so that the service knows the agent is functioning as expected.

`UpdateManagedInstancePublicKey`

SSM Agent runs this API operation to provide the public key after rotating
the key pair on the managed node. The public key is used to authenticate the
requests, signed with the private key, to get temporary credentials from
Systems Manager.

## ssm:\* namespace other

API operations

`ExecuteApi`

Systems Manager delegated administrators who manage OpsItems in OpsCenter require
access to this API action so they can view related resource details about
OpsItems across multiple AWS accounts. Specifically, this API gives a
delegated administrator permission to view the following OpsItem details in the
AWS Management Console: the OpsItem description, tags, CloudFormation template, AWS Config changes,
CloudWatch Logs alarms, and AWS CloudTrail events. For more information about working with
OpsItems across accounts, see [(Optional)
Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md "OpsCenter-getting-started-multiple-accounts.md"). For more
information about related resource details for OpsItems, see [Adding
related resources to an OpsItem](OpsCenter-working-with-OpsItems-adding-related-resources.md "OpsCenter-working-with-OpsItems-adding-related-resources.md").
