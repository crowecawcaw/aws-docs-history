# AWS Private CA VPC endpoints (AWS PrivateLink)

You can create a private connection between your VPC and AWS Private CA by configuring
an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md"), a technology for privately accessing AWS Private CA API
operations. AWS PrivateLink routes all network traffic between your VPC and
AWS Private CA through the Amazon network, avoiding exposure on the open internet.
Each VPC endpoint is represented by one or more [elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") with
private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to AWS Private CA without an
internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances
in your VPC don't need public IP addresses to communicate with the AWS Private CA
API.

To use AWS Private CA through your VPC, you must connect from an instance that is
inside the VPC. Alternatively, you can connect your private network to your VPC by
using an AWS Virtual Private Network (Site-to-Site VPN) or Direct Connect. For information about Site-to-Site VPN, see [VPN Connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the
_Amazon VPC User Guide_. For information about
Direct Connect, see [Creating a
Connection](../../../directconnect/latest/UserGuide/dedicated_connection.md#create-connection "../../../directconnect/latest/UserGuide/dedicated_connection.md#create-connection") in the _Direct Connect User Guide_.

AWS Private CA does not require the use of AWS PrivateLink, but we recommend it as an
additional layer of security. For more information about AWS PrivateLink and VPC
endpoints, see [Accessing Services Through AWS PrivateLink](../../../vpc/latest/userguide/privatelink-access-aws-services.md "../../../vpc/latest/userguide/privatelink-access-aws-services.md").

## Considerations for AWS Private CA

VPC endpoints

Before you set up interface VPC endpoints for AWS Private CA, be aware of the
following considerations:

- AWS Private CA might not support VPC endpoints in some Availability
  Zones. When you create a VPC endpoint, first check support in the
  management console. Unsupported Availability Zones are marked "Service
  not supported in this Availability Zone."
- VPC endpoints do not support cross-Region requests. Ensure that you
  create your endpoint in the same Region where you plan to issue your API
  calls to AWS Private CA.
- VPC endpoints only support Amazon provided DNS through Amazon Route 53. If
  you want to use your own DNS, you can use conditional DNS forwarding.
  For more information, see [DHCP Options Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  in the _Amazon VPC User Guide_.
- The security group attached to the VPC endpoint must allow incoming
  connections on port 443 from the private subnet of the VPC.

AWS Private CA API currently supports VPC endpoints in the following
AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Canada West (Calgary)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Europe (Zurich)
- Israel (Tel Aviv)
- Middle East (Bahrain)
- Middle East (UAE)
- South America (São Paulo)

## Creating the VPC endpoints for

AWS Private CA

You can create a VPC endpoint for the AWS Private CA service using either the
VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") or the AWS Command Line Interface. For more information, see the
[Creating an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") procedure in the _Amazon VPC User Guide_. AWS Private CA supports making
calls to all of its API operations inside your VPC.

If you have enabled private DNS host names for the endpoint, then the default
AWS Private CA endpoint now resolves to your VPC endpoint. For a comprehensive
list of default service endpoints, see [Service Endpoints and
Quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md").

If you have not enabled private DNS host names, Amazon VPC provides a DNS
endpoint name that you can use in the following format:

```
`vpc-endpoint-id`.acm-pca.`region`.vpce.amazonaws.com
```

###### Note

The value `region` represents the Region
identifier for an AWS Region supported by AWS Private CA, such as
`us-east-2` for the US East (Ohio) Region. For a list of
AWS Private CA, see [AWS Certificate
Manager Private Certificate Authority Endpoints and
Quotas](../../../general/latest/gr/pca.md "../../../general/latest/gr/pca.md").

For more information, see [AWS Private CA VPC endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.

## Create a VPC endpoint policy for

AWS Private CA

You can create a policy for Amazon VPC endpoints for AWS Private CA to specify the
following:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC Guide_.

###### Example – VPC endpoint policy for AWS Private CA actions

When attached to an endpoint, the following policy grants access for all
principals to the AWS Private CA actions `IssueCertificate`,
`DescribeCertificateAuthority`, `GetCertificate`,
`GetCertificateAuthorityCertificate`,
`ListPermissions`, and `ListTags`. The resource in
each stanza is a private CA. The first stanza authorizes the creation of
end-entity certificates using the specified private CA and certificate
template. If you don't want to control the template being used, the
`Condition` section is not needed. However, removing this
allows all principals to create CA certificates as well as end-entity
certificates.

```
{
      "Statement":[
         {
            "Principal":"*",
            "Effect":"Allow",
            "Action":[
               "acm-pca:IssueCertificate"
            ],
            "Resource":[
               "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
            ],
            "Condition":{
               "StringEquals":{
                  "acm-pca:TemplateArn":"arn:aws:acm-pca:::template/EndEntityCertificate/V1"
               }
            }
         },
         {
            "Principal":"*",
            "Effect":"Allow",
            "Action":[
               "acm-pca:DescribeCertificateAuthority",
               "acm-pca:GetCertificate",
               "acm-pca:GetCertificateAuthorityCertificate",
               "acm-pca:ListPermissions",
               "acm-pca:ListTags"
            ],
            "Resource":[
               "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`"
            ]
         }
      ]
   }
```
