# Configure VPC connectivity for a data source

Some data sources run on private resources that are not reachable over the public
internet, such as an on-premises Confluence Data Center instance that you front with an
internal load balancer in your VPC. To crawl these data sources, you create a VPC
configuration. Amazon Bedrock uses the configuration to provision a private network path into your
VPC and reach the resource.

A VPC configuration is a reusable resource on your knowledge base. You create it once,
then reference it by ID from one or more data sources. When you create a data source that
needs private connectivity, you select an existing VPC configuration or create a new
one.

###### Note

When Amazon Bedrock provisions a VPC configuration, it assumes an AWS Identity and Access Management (IAM) role
associated with your knowledge base to create a small set of networking resources in
your account. Every resource that Amazon Bedrock creates is tagged
`ManagedBy=VPCProxyService`, and the role can act only on resources that
carry that tag. See [Knowledge base IAM role permissions](#kb-managed-vpc-configuration-role "#kb-managed-vpc-configuration-role").

## What you provide

To create a VPC configuration, you provide the following:

VPC configuration inputs| Input | Why it is needed |
| --- | --- |
| A VPC and one or more subnets | Where Amazon Bedrock places the network entry point (a private gateway) into<br>your VPC. You provide 1–6 subnets from the chosen VPC. |
| A resource target and port | The private IP address or DNS name (and port) of the resource you<br>want to reach. |
| A knowledge base IAM role | Amazon Bedrock assumes this role to provision the networking resources in<br>your account. See [Knowledge base IAM role permissions](#kb-managed-vpc-configuration-role "#kb-managed-vpc-configuration-role"). |

You do not provide security groups. Amazon Bedrock uses your VPC's default security group for
the gateway. Make sure that the default security group's outbound (egress) rules
allow reaching your target on the requested port. See [Egress from the default security group](#kb-managed-vpc-configuration-egress "#kb-managed-vpc-configuration-egress").

## Network requirements

Amazon Bedrock reaches your resource through a private gateway that is created with private
network interfaces only (no public IP address). The gateway reaches your target over
your VPC's private (local) network and cannot reach public IP addresses. Your
resource target must be privately reachable from inside your VPC:

- An internal load balancer (`scheme: internal`) whose DNS name
  resolves to private addresses (for example,
  `10.`x``,
 `172.`x``, or
  `192.168.`x``).
- A private IP address, or a private DNS name that resolves to a private
  in-VPC address.

An internet-facing load balancer is not supported. An internet-facing load balancer
returns its public IP addresses even to in-VPC DNS queries, and the private gateway
cannot reach those addresses. If your resource is currently exposed only through an
internet-facing load balancer, create (or point at) an internal load balancer in the
same VPC and use its DNS name as the resource target.

## Create a VPC configuration

Console

###### To add a VPC configuration

1. In the data source configuration, under **VPC
   configuration**, choose **Add VPC
   configuration**. If a suitable configuration already
   exists, select it instead to reuse it across data
   sources.
2. (Optional) Enter a **Name** and
   **Description** for the configuration.
3. For **VPC ID**, select the VPC to use for
   connectivity.
4. For **Subnet IDs**, select one or more subnets
   from the chosen VPC.
5. For **Resource target**, enter the hostname or
   IP address of your resource (for example,
   `10.0.1.50` or
   `confluence.internal.example.com`).
6. For **Port**, enter the port number to connect
   on (for example, `443` or `8090`).
7. For **Protocol**, choose **HTTPS**
   or **HTTP**.
8. For **Resolution mode**, choose how the resource
   target address is resolved:

   - **Public** – The resource target
     is a publicly resolvable hostname or IP address.
   - **In VPC** – The resource target
     is resolvable only within your VPC. This is the common
     case for internal resources.

9. (Optional) For **Host header**, enter the
   `Host` header value to send with requests. Set this
   only if your resource (or an upstream router) routes by the HTTP
   `Host` header.
10. (Required for HTTPS) For **TLS server name**,
    enter the expected TLS certificate identity (Subject Alternative
    Name) for the resource. A single leftmost wildcard is allowed (for
    example, `*.example.com`).
11. Choose **Create**.

API
To create a VPC configuration, send a
`CreateVpcConfiguration` request. All operations are scoped to
a knowledge base through the `knowledgeBaseId` path parameter;
the request body does not include an account ID or role ARN, because Amazon Bedrock
resolves those from the knowledge base.

```
POST /knowledgebases/`knowledgeBaseId`/vpcconfigurations/
```

The request body uses the following fields.

CreateVpcConfiguration fields| Field | Required | Description |
| --- | --- | --- |
| `vpcId` | Yes | The ID of the VPC. Matches<br>`^vpc-[a-zA-Z0-9]+$`, up to 64<br>characters. |
| `subnetIds` | Yes | 1–6 subnet IDs from the specified VPC. Each<br>matches `^subnet-[a-zA-Z0-9]+$`. |
| `resourceTarget` | Yes | The IPv4 address or DNS name of the resource (1–255<br>characters). See [Resource target restrictions](#kb-managed-vpc-configuration-target "#kb-managed-vpc-configuration-target"). |
| `port` | Yes | The port to connect on (1–65535). |
| `protocol` | Yes | `HTTP` or `HTTPS`. |
| `resolutionMode` | Yes | `PUBLIC` or `IN_VPC`. Use<br>`IN_VPC` when the target resolves only inside<br>your VPC. |
| `tlsServerName` | Conditional | Required when `protocol` is<br>`HTTPS`. The hostname matched against the<br>resource's TLS certificate (up to 253 characters). A<br>single leftmost wildcard is allowed. Must not include a<br>port. |
| `hostHeader` | No | The HTTP `Host` header value to send (up to<br>255 characters). Set only if your resource routes by the<br>`Host` header. |
| `name` | No | A human-readable name (1–128 characters). |
| `description` | No | A description (up to 512 characters). |
| `clientToken` | No | An idempotency token. |

Creation is asynchronous. `CreateVpcConfiguration` returns a
`202` response with a `vpcConfigurationId` and a
status of `CREATING`. Poll `GetVpcConfiguration`
until the status is `CREATED` (or `CREATE_FAILED`,
in which case `statusMessage` names the cause). Use
`ListVpcConfigurations` to list configurations and
`DeleteVpcConfiguration` to remove one.

###### Note

If you create multiple configurations in the same VPC with the same
set of subnets, they share one gateway. A different set of subnets
provisions a separate gateway.

## Protocol, TLS server name, and host header

These three settings are the most commonly misconfigured. Use the following
guidance to choose the right values.

`protocol`

Choose `HTTP` to invoke the resource over plaintext HTTP, or
`HTTPS` to invoke it over TLS.

`tlsServerName`

Required when `protocol` is `HTTPS`. This is the
server name matched against your resource's TLS certificate Subject
Alternative Names during invocation. Set it to the hostname that your
certificate is issued for (for example,
`app.internal.example.com`). A single leftmost wildcard is
allowed (for example, `*.example.com`). If the resource is
reached by IP address but presents a certificate for a name, set
`tlsServerName` to that name. If the certificate does not
match, invocation fails the TLS identity check. This value must be a
hostname without a port.

`hostHeader`

Optional, and an application-layer concern that is independent of
`tlsServerName`. Set it only if your resource, or an upstream
router or ingress, routes by the HTTP `Host` header and that
host differs from what you would otherwise send. If your resource serves a
single site and does not route by `Host`, leave it
unset.

`resolutionMode`

Choose `PUBLIC` when the resource target is a publicly
resolvable name or a public IP address. Choose `IN_VPC` when
the resource target resolves only inside your VPC (private DNS or private
IP address), which is the common case for internal resources. A literal
private IP target (for example, `10.0.5.20`) works under either
mode, because there is no DNS name to resolve.

## Resource target restrictions

Amazon Bedrock validates `resourceTarget` when you create the configuration to
prevent the service from being directed at itself or at internal infrastructure. The
following targets are rejected:

- Loopback addresses (`127.0.0.0/8`, `::1`) and
  `localhost`.
- Link-local addresses (`169.254.0.0/16`, `fe80::/10`),
  including the instance metadata endpoint
  `169.254.169.254`.
- Wildcard or any-local addresses (`0.0.0.0`, `::`) and
  the `0.0.0.0/8` block.
- Multicast addresses.
- IPv6 literals. The gateway is provisioned IPv4-only, so IP targets must be a
  dotted-quad IPv4 address.

DNS names are allowed. Validation does not resolve them, so the target must still be
reachable from your gateway subnets.

## Egress from the default security group

Because Amazon Bedrock uses your VPC's default security group for the gateway, that security
group's egress rules must permit reaching `resourceTarget` on
`port`. If the default security group is locked down, creation fails
quickly with a clear message rather than timing out later. Before you create the
configuration, make sure an egress rule allows traffic from the gateway subnets to the
target and port.

## Knowledge base IAM role permissions

Amazon Bedrock assumes the IAM role associated with your knowledge base to provision and
later tear down the networking resources in your account. The role must grant the
create and delete permissions below, as well as the read permissions that make
retried deletes idempotent. Every resource that Amazon Bedrock creates is tagged
`ManagedBy=VPCProxyService`, and the destructive permissions are gated on
that tag, so the role can act only on resources that this feature created.

- **Create** –
  `vpc-lattice:CreateResourceGateway`,
  `vpc-lattice:CreateResourceConfiguration`,
  `vpc-lattice:TagResource`,
  `vpc-lattice:PutResourcePolicy`,
  `ram:CreateResourceShare`, `ram:TagResource`,
  `ram:AssociateResourceShare`, and
  `iam:CreateServiceLinkedRole` (one-time, for the VPC Lattice
  service-linked role).
- **Delete** –
  `vpc-lattice:DeleteResourceGateway`,
  `vpc-lattice:DeleteResourceConfiguration`, and
  `ram:DeleteResourceShare`.
- **Read (validation and idempotency)** –
  `vpc-lattice:GetResourceGateway`,
  `vpc-lattice:GetResourceConfiguration`,
  `ram:GetResourceShares`, `ec2:DescribeSubnets`,
  `ec2:DescribeSecurityGroups`, and
  `ec2:DescribeVpcs`.

###### Important

Grant both `vpc-lattice:GetResourceGateway` and
`vpc-lattice:GetResourceConfiguration`. Because the delete permissions
are tag-scoped, deleting an already-deleted resource returns an access-denied
error rather than a not-found error. Amazon Bedrock uses these untagged read permissions to
tell an already-deleted resource (treated as success) from a genuine permissions
problem. Without them, a retried delete after a partial failure can get
stuck.

The following example policy grants the required permissions. Replace
`region` and `accountId` with your
values.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VpcProxyCreateTagged",
            "Effect": "Allow",
            "Action": [
                "vpc-lattice:CreateResourceGateway",
                "vpc-lattice:CreateResourceConfiguration",
                "vpc-lattice:TagResource"
            ],
            "Resource": [
                "arn:aws:vpc-lattice:`region`:`accountId`:resourcegateway/*",
                "arn:aws:vpc-lattice:`region`:`accountId`:resourceconfiguration/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/ManagedBy": "VPCProxyService",
                    "aws:ResourceTag/ManagedBy": "VPCProxyService"
                },
                "ForAllValues:StringEquals": { "aws:TagKeys": ["ManagedBy"] }
            }
        },
        {
            "Sid": "VpcProxyPutResourcePolicy",
            "Effect": "Allow",
            "Action": "vpc-lattice:PutResourcePolicy",
            "Resource": [
                "arn:aws:vpc-lattice:`region`:`accountId`:resourceconfiguration/*"
            ],
            "Condition": {
                "StringEquals": { "aws:ResourceTag/ManagedBy": "VPCProxyService" }
            }
        },
        {
            "Sid": "VpcProxyRamCreate",
            "Effect": "Allow",
            "Action": "ram:CreateResourceShare",
            "Resource": "*",
            "Condition": {
                "StringEquals": { "aws:RequestTag/ManagedBy": "VPCProxyService" },
                "StringEqualsIfExists": {
                    "ram:RequestedResourceType": "vpc-lattice:ResourceConfiguration"
                }
            }
        },
        {
            "Sid": "VpcProxyRamAssociate",
            "Effect": "Allow",
            "Action": "ram:AssociateResourceShare",
            "Resource": "*",
            "Condition": {
                "StringEquals": { "aws:ResourceTag/ManagedBy": "VPCProxyService" }
            }
        },
        {
            "Sid": "VpcProxyRamTagOnCreate",
            "Effect": "Allow",
            "Action": "ram:TagResource",
            "Resource": [
                "arn:aws:ram:`region`:`accountId`:resource-share/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/ManagedBy": "VPCProxyService",
                    "aws:ResourceTag/ManagedBy": "VPCProxyService"
                },
                "ForAllValues:StringEquals": { "aws:TagKeys": ["ManagedBy"] }
            }
        },
        {
            "Sid": "VpcProxyDeleteTagged",
            "Effect": "Allow",
            "Action": [
                "vpc-lattice:DeleteResourceConfiguration",
                "vpc-lattice:DeleteResourceGateway"
            ],
            "Resource": [
                "arn:aws:vpc-lattice:`region`:`accountId`:resourcegateway/*",
                "arn:aws:vpc-lattice:`region`:`accountId`:resourceconfiguration/*"
            ],
            "Condition": {
                "StringEquals": { "aws:ResourceTag/ManagedBy": "VPCProxyService" }
            }
        },
        {
            "Sid": "VpcProxyRamDeleteTagged",
            "Effect": "Allow",
            "Action": "ram:DeleteResourceShare",
            "Resource": [
                "arn:aws:ram:`region`:`accountId`:resource-share/*"
            ],
            "Condition": {
                "StringEquals": { "aws:ResourceTag/ManagedBy": "VPCProxyService" },
                "StringLike": { "ram:ResourceShareName": "vpc-proxy-share-*" }
            }
        },
        {
            "Sid": "VpcProxyGetResource",
            "Effect": "Allow",
            "Action": [
                "vpc-lattice:GetResourceConfiguration",
                "vpc-lattice:GetResourceGateway"
            ],
            "Resource": [
                "arn:aws:vpc-lattice:`region`:`accountId`:resourcegateway/*",
                "arn:aws:vpc-lattice:`region`:`accountId`:resourceconfiguration/*"
            ]
        },
        {
            "Sid": "VpcProxyRamGetResourceShares",
            "Effect": "Allow",
            "Action": "ram:GetResourceShares",
            "Resource": "*"
        },
        {
            "Sid": "VpcProxyEc2Describe",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VpcProxyLatticeServiceLinkedRole",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": [
                "arn:aws:iam::`accountId`:role/aws-service-role/vpc-lattice.amazonaws.com/*"
            ],
            "Condition": {
                "StringEquals": { "iam:AWSServiceName": "vpc-lattice.amazonaws.com" }
            }
        }
    ]
}
```

## Lifecycle

- A VPC configuration transitions through `CREATING` to
  `CREATED`, or to `CREATE_FAILED`. When you delete it, the
  status is `DELETING`, or `DELETE_FAILED`.
- Creation and deletion are asynchronous. Poll
  `GetVpcConfiguration` to track progress. On failure,
  `statusMessage` names the actionable cause, such as a missing
  permission.
- Deletion is idempotent. A partially completed delete converges when you
  retry it.
