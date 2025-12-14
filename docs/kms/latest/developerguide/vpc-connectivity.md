# Configure VPC endpoint service connectivity

Use the guidance in this section to create and configure the AWS resources and
related components that are required for an external key store that uses [VPC endpoint service connectivity](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity"). The
resources listed for this connectivity option are a supplement to the [resources required for all external key stores](create-xks-keystore.md#xks-requirements "create-xks-keystore.md#xks-requirements").
After you create and configure the required resources, you can [create your external key store](create-xks-keystore.md "create-xks-keystore.md").

You can locate your external key store proxy in your Amazon VPC or locate the proxy outside
of AWS and use your VPC endpoint service for communication.

Before you begin, [confirm that you need an external key
store](keystore-external.md#do-i-need-xks "keystore-external.md#do-i-need-xks"). Most customer can use KMS keys backed by AWS KMS key material.

###### Note

Some of the elements required for VPC endpoint service connectivity might be
included in your external key manager. Also, your software might have additional
configuration requirements. Before creating and configuring the AWS resources in
this section, consult your proxy and key manager documentation.

###### Topics

- [Requirements for VPC endpoint
  service connectivity](#xks-vpce-service-requirements "#xks-vpce-service-requirements")
- [Step 1: Create an Amazon VPC and subnets](#xks-create-vpc "#xks-create-vpc")
- [Step 2: Create a target group](#xks-target-group "#xks-target-group")
- [Step 3: Create a network load balancer](#xks-nlb "#xks-nlb")
- [Step 4: Create a VPC endpoint service](#xks-vpc-svc "#xks-vpc-svc")
- [Step 5: Verify your private DNS name
  domain](#xks-private-dns "#xks-private-dns")
- [Step 6: Authorize AWS KMS to connect to the
  VPC endpoint service](#xks-vpc-authorize-kms "#xks-vpc-authorize-kms")

## Requirements for VPC endpoint

service connectivity

If you choose VPC endpoint service connectivity for your external key store, the
following resources are required.

- An Amazon VPC that is connected to your external key manager. It must have at
  least two private [subnets](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") in two different Availability Zones.

You can use an existing Amazon VPC for your external key store, provided that
it [fulfills the requirements](#xks-vpc-requirements "#xks-vpc-requirements") for
use with an external key store. Multiple external key stores can share an
Amazon VPC, but each external key store must have its own VPC endpoint
service and private DNS name.

- An [Amazon VPC endpoint service powered by AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-share-your-services.md "../../../vpc/latest/privatelink/privatelink-share-your-services.md") with a [network load balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") and [target group](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md").

The endpoint service cannot require acceptance. Also, you must add AWS KMS
as an allowed principal. This allows AWS KMS to create interface endpoints so
it can communicate with your external key store proxy.

- A private DNS name for the VPC endpoint service that is unique in its
  AWS Region.

The private DNS name must be a subdomain of a higher-level public domain.
For example, if the private DNS name is
`myproxy-private.xks.example.com`, it must be a subdomain of a
public domain such as `xks.example.com` or
`example.com`.

You must [verify ownership](#xks-private-dns "#xks-private-dns") of the
DNS domain for private DNS name.

- A TLS certificate issued by a [supported
  public certificate authority](https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities "https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities") for your external key store proxy.

The subject common name (CN) on the TLS certificate must match the private
DNS name. For example, if the private DNS name is
`myproxy-private.xks.example.com`, the CN on the TLS certificate
must be `myproxy-private.xks.example.com` or `*.xks.example.com`.

- To minimize network latency, create your AWS components in the [supported AWS Region](keystore-external.md#xks-regions "keystore-external.md#xks-regions") that is closest to
  your [external key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm"). If possible,
  choose a Region with a network round-trip time (RTT) of 35 milliseconds or
  less.

For all requirements for an external key store, see the [Assemble the prerequisites](create-xks-keystore.md#xks-requirements "create-xks-keystore.md#xks-requirements").

## Step 1: Create an Amazon VPC and subnets

VPC endpoint service connectivity requires an Amazon VPC that is connected to your
external key manager with at least two private subnets. You can create an Amazon VPC or
use an existing Amazon VPC that fulfills the requirements for external key stores. For
help with creating a new Amazon VPC, see [Create a VPC](../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC "../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC") in
the _Amazon Virtual Private Cloud User Guide_.

### Requirements for your Amazon VPC

The Amazon VPC endpoint service must have the following properties to work with
external key stores.

- Must be in a [supported Region](keystore-external.md#xks-regions "keystore-external.md#xks-regions") as
  your external key store.
- Requires at least two private subnets, each in a different
  Availability Zone.
- The private IP address range of your Amazon VPC must not overlap with the
  private IP address range of the data center hosting your [external key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm").
- All components must use IPv4.

You have many options for connecting the Amazon VPC to your external key store
proxy. Choose an option that meets your performance and security needs. For a
list, see [Connect your VPC to other
networks](../../../vpc/latest/userguide/extend-intro.md "../../../vpc/latest/userguide/extend-intro.md") and [Network-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md"). For more details, see
[Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"), and the [AWS Site-to-Site VPN User Guide](../../../vpn/latest/s2svpn.md "../../../vpn/latest/s2svpn.md").

### Creating an Amazon VPC for your external key

store

Use the following instructions to create the Amazon VPC for your external key
store. An Amazon VPC is required only if you choose the [VPC endpoint service connectivity](choose-xks-connectivity.md "choose-xks-connectivity.md")
option. You can use an existing Amazon VPC that fulfills the requirements for an
external key store.

Follow the instructions in the [Create a VPC, subnets, and other VPC resources](../../../vpc/latest/userguide/working-with-vpcs.md#create-vpc-and-other-resources "../../../vpc/latest/userguide/working-with-vpcs.md#create-vpc-and-other-resources") topic using the
following required values. For other fields, accept the default values and provide names as requested.

| Field                              | Value                                                                                                                                                                                                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IPv4 CIDR block                    | Enter the IP addresses for your VPC. The private IP address<br>range of your Amazon VPC must not overlap with the private IP address<br>range of the data center hosting your [external key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm"). |
| Number of Availability Zones (AZs) | 2 or more                                                                                                                                                                                                                                                                  |
| Number of public subnets           | None are required (0)                                                                                                                                                                                                                                                      |
| Number of private subnets          | One for each AZ                                                                                                                                                                                                                                                            |
| NAT gateways                       | None are required.                                                                                                                                                                                                                                                         |
| VPC endpoints                      | None are required.                                                                                                                                                                                                                                                         |
| Enable DNS hostnames               | Yes                                                                                                                                                                                                                                                                        |
| Enable DNS resolution              | Yes                                                                                                                                                                                                                                                                        |

Be sure to test your VPC communication. For example, if your external key
store proxy is not located in your Amazon VPC, create an Amazon EC2 instance in your
Amazon VPC, verify that the Amazon VPC can communicate with your external key store
proxy.

### Connecting the VPC to the external key

manager

Connect the VPC to the data center that hosts your external key manager using
any of the [network connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md") that Amazon VPC supports. Ensure that the
Amazon EC2 instance in the VPC (or the external key store proxy, if it is in the
VPC), can communicate with the data center and the external key manager.

## Step 2: Create a target group

Before you create the required VPC endpoint service, create its required
components, a network load balancer (NLB) and a target group. The network load
balancer (NLB) distributes requests among multiple healthy targets, any of which can
service the request. In this step, you create a target group with at least two hosts
for your external key store proxy, and register your IP addresses with the target
group.

Follow the instructions in the [Configure a target group](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md#configure-target-group "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md#configure-target-group") topic using the following required values.
For other fields, accept the default values and provide names as requested.

| Field                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Target type                    | IP addresses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Protocol                       | TCP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Port                           | 443                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| IP address type                | IPv4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VPC                            | Choose the VPC where you will create the VPC endpoint service for<br>your external key store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Health check protocol and path | Your health check protocol and path will differ with your<br>external key store proxy configuration. Consult the<br>documentation for your external key manager or external key<br>store proxy.For general information about configuring<br>health checks for your target groups, see [Health checks<br>for your target groups](../../../elasticloadbalancing/latest/network/target-group-health-checks.md "../../../elasticloadbalancing/latest/network/target-group-health-checks.md") in the _Elastic Load Balancing User Guide for Network Load<br>Balancers_. |
| Network                        | Other private IP address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IPv4 address                   | The private addresses of your external key store proxy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ports                          | 443                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Step 3: Create a network load balancer

The network load balancer distributes the network traffic, including requests from
AWS KMS to your external key store proxy, to the configured targets.

Follow the instructions in the [Configure a load balancer and a listener](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md#configure-load-balancer "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md#configure-load-balancer") topic to configure and add a
listener and create a load balancer using the following required values.
For other fields, accept the default values and provide names as requested.

| Field                      | Value                                                                                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scheme                     | Internal                                                                                                                                             |
| IP address type            | IPv4                                                                                                                                                 |
| Network mapping            | Choose the VPC where you will create the VPC endpoint service<br>for your external key store.                                                        |
| Mapping                    | Choose both of the availability zones (at least two) that you<br>configured for your VPC subnets. Verify the subnet names and private<br>IP address. |
| Protocol                   | TCP                                                                                                                                                  |
| Port                       | 443                                                                                                                                                  |
| Default action: Forward to | Choose the [target group](#xks-target-group "#xks-target-group")<br>for your network load balancer.                                                  |

## Step 4: Create a VPC endpoint service

Typically, you create an endpoint to a service. However, when you create a VPC
endpoint service, you are the provider, and AWS KMS creates an endpoint to your
service. For an external key store, create a VPC endpoint service with the network
load balancer that you created in the previous step. The VPC endpoint service can be
in the same AWS account as your external key store or a different
AWS account.

Multiple external key stores can share an Amazon VPC, but each external key store must
have its own VPC endpoint service and private DNS name.

Follow the instructions in the [Create an endpoint service](../../../vpc/latest/privatelink/create-endpoint-service.md#create-endpoint-service-nlb "../../../vpc/latest/privatelink/create-endpoint-service.md#create-endpoint-service-nlb") topic to create your VPC endpoint service
with the following required values. For other fields, accept the default values and provide names as requested.

| Field                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Load balancer type         | Network                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Available load balancers   | Choose the [network load balancer](#xks-nlb "#xks-nlb")<br>that you created in the previous step.If your new load<br>balancer does not appear in the list, verify that its state is<br>active. It might take a few minutes for the load balancer state<br>to change from provisioning to active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Acceptance required        | False. Uncheck the check box._Do not<br>require acceptance_. AWS KMS cannot connect to the<br>VPC endpoint service without a manual acceptance. If acceptance<br>is required, attempts to [create the external key store](create-xks-keystore.md "create-xks-keystore.md") fail with an<br>`XksProxyInvalidConfigurationException`<br>exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Enable private DNS name    | Associate a private DNS name with the service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Private DNS name           | Enter a private DNS name that is unique in its AWS Region.<br>The private DNS name must be a subdomain of a higher level<br>public domain. For example, if the private DNS name is<br>`myproxy-private.xks.example.com`, it must be a<br>subdomain of a public domain such as<br>`xks.example.com` or<br>`example.com`.This private DNS name must<br>match the subject common name (CN) in the TLS certificate<br>configured on your external key store proxy. For example, if the<br>private DNS name is `myproxy-private.xks.example.com`, the<br>CN on the TLS certificate must be<br>`myproxy-private.xks.example.com` or<br>`*.xks.example.com`.If the certificate and private<br>DNS name do not match, attempts to connect an external key store<br>to its external key store proxy fail with a connection error<br>code of `XKS_PROXY_INVALID_TLS_CONFIGURATION`. For<br>details, see [General configuration errors](xks-troubleshooting.md#fix-xks-gen-configuration "xks-troubleshooting.md#fix-xks-gen-configuration"). |
| Supported IP address types | IPv4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Step 5: Verify your private DNS name

domain

When you create your VPC endpoint service, its domain verification status is
`pendingVerification`. Before using the VPC endpoint service to
create an external key store, this status must be `verified`. To verify
that you own the domain associated with your private DNS name, you must create a TXT
record in a public DNS server.

For example, if the private DNS name for your VPC endpoint service is
`myproxy-private.xks.example.com`, you must create a TXT record in a
public domain, such as `xks.example.com` or `example.com`,
whichever is public. AWS PrivateLink looks for the TXT record first on
`xks.example.com` and then on `example.com`.

###### Tip

After you add a TXT record, it might take a few minutes for the
**Domain verification status** value to change from
`pendingVerification` to `verify`.

To begin, find the verification status of your domain using either of the
following methods. Valid values are `verified`,
`pendingVerification`, and `failed`.

- In the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc"), choose
  **Endpoint services**, and choose your endpoint
  service. In the detail pane, see **Domain verification
  status**.
- Use the [DescribeVpcEndpointServiceConfigurations](../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.md") operation. The
  `State` value is in the
  `ServiceConfigurations.PrivateDnsNameConfiguration.State`
  field.

If the verification status is not `verified`, follow the instructions
in the [Domain
ownership verification](../../../vpc/latest/privatelink/manage-dns-names.md#verify-domain-ownership "../../../vpc/latest/privatelink/manage-dns-names.md#verify-domain-ownership") topic to add a TXT record to your domain's DNS
server and verify that the TXT record is published. Then check your verification
status again.

You are not required to create an A record for the private DNS domain name. When
AWS KMS creates an interface endpoint to your VPC endpoint service, AWS PrivateLink
automatically creates a hosted zone with the required A record for the private
domain name in the AWS KMS VPC. For external key stores with VPC endpoint service
connectivity, this happens when you [connect
your external key store](xks-connect-disconnect.md "xks-connect-disconnect.md") to its external key store proxy.

## Step 6: Authorize AWS KMS to connect to the

VPC endpoint service

See the following procedures for managing your Amazon VPC endpoint service permissions.
Each step depends on your connectivity and configuration between your external key
store, VPC endpoint service, and AWS account.

Same AWS account
When your VPC endpoint service is owned by the same AWS account as
your external key store, you must add AWS KMS to the **Allow
principals** list for your VPC endpoint service. This
allows AWS KMS to create interface endpoints to your VPC endpoint service.
If AWS KMS is not an allowed principal, attempts to create an external key
store will fail with an
`XksProxyVpcEndpointServiceNotFoundException`
exception.

Follow the instructions in the [Manage permissions](../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions "../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions") topic in the _AWS PrivateLink Guide_. Use the following required
value.

| Field       | Value                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| AWS KMS ARN | `cks.kms.`<region>`.amazonaws.com`For<br>example,<br>`cks.kms.us-east-1.amazonaws.com` |

Cross AWS account
When your VPC endpoint service is owned by another AWS account you
must add both AWS KMS and your account to the **Allow
principals** list. This allows AWS KMS and your external key
store to create interface endpoints to your VPC endpoint service. If
AWS KMS is not an allowed principal, attempts to create an external key
store will fail with an
`XksProxyVpcEndpointServiceNotFoundException`
exception. You'll need to provide the AWS account ARN where
the external key store resides.

Follow the instructions in the [Manage permissions](../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions "../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions") topic in the _AWS PrivateLink Guide_. Use the following required
value.

| Field           | Value                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| AWS KMS ARN     | `cks.kms.`<region>`.amazonaws.com`For<br>example,<br>`cks.kms.us-east-1.amazonaws.com`                         |
| AWS account ARN | `arn:aws:iam::`111122223333`:role/`role_name``For<br>example,<br>`arn:aws:iam::`123456789012`:role/`cks_role`` |

**Next**: [Create an external key store](create-xks-keystore.md "create-xks-keystore.md")
