# AMS Accelerate accounts

AMS Accelerate is the AMS operations plan that can operate AWS infrastructure supporting
workloads. You can benefit from AMS Accelerate operational services such as monitoring and
alerting, incident management, security management, and backup management, without going
through a new migration, experiencing downtime, or changing how you use AWS. AMS Accelerate
also offers an optional patch add-on for EC2 based workloads that require regular
patching.

With AMS Accelerate you have the freedom to use, configure, and deploy all AWS services
natively, or with your preferred tools. You will use your preferred access and change
mechanisms while AMS consistently applies proven practices that help scale your team,
optimize costs, increase security and efficiency, and improve resiliency.

###### Note

AMS Accelerate accounts in AMS Advanced do not have AMS change management (RFCs) or the
AMS Advanced console. Instead, they have the AMS Accelerate console and functionality.

Accelerate accounts can only be provisioned from your AMS multi-account landing zone Management account.
Accelerate offers different operational capabilities. To learn more see the
[Accelerate service description](../accelerate-guide/acc-sd.md "../accelerate-guide/acc-sd.md").

- You will continue to enjoy some of the features from the multi-account landing zone (MALZ) core
  accounts such as centralized logging, single billing, Config Aggregator in the
  security account and SCPs.
- AMS Accelerate does not provide some AMS Advanced services like EPS, Access management,
  Change management and provisioning. We recommend you follow the next steps to gain
  access and configure the transit gateway (TGW).
  For more details about Accelerate, see
  [What is Accelerate](../accelerate-guide/what-is-acc.md "../accelerate-guide/what-is-acc.md").

## Creating your Accelerate account

To create an Accelerate account, follow the steps outlined here
[Create an Accelerate account](../ctref/deployment-managed-management-account-create-accelerate-account.md#deployment-managed-management-account-create-accelerate-account-info "../ctref/deployment-managed-management-account-create-accelerate-account.md#deployment-managed-management-account-create-accelerate-account-info").

## Accessing your Accelerate account

After you provision an Accelerate account in your multi-account landing zone (MALZ) account, a role with
[Administrative access](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") permissions,
`AccelerateDefaultAdminRole`, is in the account for you to assume.

To access the new Accelerate account:

1. Log into the IAM console for the management account with the `CustomerDefaultAssumeRole` role.
2. In the IAM console, on the navigation bar, choose your username.
3. Choose **Switch Role**. If this is the first time choosing this option, a page appears with more information.
   After reading it, choose **Switch Role**. If you clear your browser cookies, this page can appear again.
4. On the **Switch Role** page, type the Accelerate account ID and the name of the role to assume:
   `AccelerateDefaultAdminRole`.

Now that you have access, you can create new IAM Roles to continue to access your
environment. If you would like to leverage SAML Federation for your Accelerate account, see
[Enabling
SAML 2.0 federated users to access the AWS Management Console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md").

## Connecting your Accelerate account with Transit Gateway

AMS does not manage the network setup of an Accelerate account. You have the
option of managing your own network using AWS APIs (see
[Networking Solutions](https://aws.amazon.com/solutionspace/networking/ "https://aws.amazon.com/solutionspace/networking/"))
or connecting to the MALZ network managed by AMS, using the existing Transit Gateway (TGW) deployed in AMS MALZ.

###### Note

You can only have a VPC attached to the TGW if the Accelerate account is in the same AWS Region. For more information see
[Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md").

To add your Accelerate account to Transit Gateway, request a new route using the
[Deployment | Managed landing zone | Networking account | Add static route](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") (ct-3r2ckznmt0a59) change type, include this information:

- **Blackhole**: True to indicate that the route's target isn't available. Do this when the traffic for the static route is to
  be dropped by the Transit Gateway. False to route the traffic to the specified TGW attachment ID. Default value is false.
- **DestinationCidrBlock**: The IPV4 CIDR range used for destination matches. Routing decisions are based on the most specific
  match. Example: 10.0.2.0/24.
- **TransitGatewayAttachmentId**: The TGW Attachment ID that will serve as the route table target. If **Blackhole**
  is false, this parameter is required, otherwise leave this parameter blank. Example: tgw-attach-04eb40d1e14ec7272.
- **TransitGatewayRouteTableId**: The ID of the TGW route table. Example: tgw-rtb-06ddc751c0c0c881c.

Create routes in the TGW route tables to connect to this VPC:

1. By default this VPC will not be able to communicate with any of the other VPCs in your MALZ network.
2. Decide with your solutions architect what VPCs you want this Accelerate VPC to communicate with.
3. Submit a
   [Deployment | Managed landing zone | Networking account | Add static route](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") (ct-3r2ckznmt0a59) change type, include this information:
   - **Blackhole**: True to indicate that the route's target isn't available. Do this when the traffic for the static route is to
     be dropped by the Transit Gateway. False to route the traffic to the specified TGW attachment ID. Default value is false.
   - **DestinationCidrBlock**: The IPV4 CIDR range used for destination matches. Routing decisions are based on the most specific
     match. Example: 10.0.2.0/24.
   - **TransitGatewayAttachmentId**: The TGW Attachment ID that will serve as the route table target. If **Blackhole**
     is false, this parameter is required, otherwise leave this parameter blank. Example: tgw-attach-04eb40d1e14ec7272.
   - **TransitGatewayRouteTableId**: The ID of the TGW route table. Example: tgw-rtb-06ddc751c0c0c881c.

**Connecting a new Accelerate account VPC to the AMS Multi-Account Landing
Zone network (creating a TGW VPC attachment)**:

1. In your multi-account landing zone Networking account, open the
   [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateways**. Record the TGW ID of the transit gateway you see.
3. In your Accelerate account, open the
   [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
4. In the navigation pane, choose **Transit Gateway Attachments** > **Create Transit Gateway Attachment**. Make these choices:
   - For the **Transit Gateway ID**, choose the transit gateway ID you recorded in Step 2.
   - For **Attachment type**, choose **VPC**.
   - Under **VPC Attachment**, optionally type a name for **Attachment name tag**.
   - Choose whether to enable **DNS Support** and **IPv6 Support**.
   - For **VPC ID**, choose the VPC to attach to the transit gateway. This VPC must have at least one subnet associated with it.
   - For **Subnet IDs**, select one subnet for each Availability Zone to be used by the transit gateway to route traffic.
     You must select at least one subnet. You can select only one subnet per Availability Zone.

5. Choose **Create attachment**. Record the ID of the newly created TGW Attachment.

**Associating the TGW attachment to a route table**:

1. Decide which TGW route table you want to associate the VPC with. We recommend creating a new application route table for Accelerate account
   VPCs using Deployment | Managed landing zone | Networking account | Create transit gateway route table (ct-3dscwaeyi6cup) change type.
2. Submit a
   [Management | Managed landing zone | Networking account | Associate TGW attachment](../ctref/management-managed-networking-account-associate-tgw-attachment.md "../ctref/management-managed-networking-account-associate-tgw-attachment.md") (ct-3nmhh0qr338q6)
   RFC on the Networking account to associate the VPC or TGW attachment to the route table you select.

**Create routes in the TGW route tables to connect to this VPC**:

1. By default, this VPC will not be able to communicate with any of the other VPCs in your multi-account landing zone network.
2. Decide with your solutions architect what VPCs you want this Accelerate account VPC to communicate with.
3. Submit a
   [Deployment | Managed landing zone | Networking account | Add static route](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") (ct-3r2ckznmt0a59) RFC against the networking account
   to create the TGW routes you need.

**Configuring your VPC Route tables to point at the AMS multi-account landing zone transit gateway**:

1. Decide with your solutions architect what traffic you want to send to the AMS Multi-Account Landing Zone transit gateway.
2. Submit a
   [Deployment | Managed landing zone | Networking account | Add static route](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") (ct-3r2ckznmt0a59) RFC against the networking account to create
   the TGW routes you need.
