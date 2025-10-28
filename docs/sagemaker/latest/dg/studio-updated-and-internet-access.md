# Connect Amazon SageMaker Studio

in a VPC to External Resources

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

The following topic gives information on how to connect Amazon SageMaker Studio in a VPC
to external resources.

###### Topics

- [Default communication
  with the internet](#studio-notebooks-and-internet-access-default-setting "#studio-notebooks-and-internet-access-default-setting")
- [VPC only
  communication with the internet](#studio-notebooks-and-internet-access-vpc-only "#studio-notebooks-and-internet-access-vpc-only")

## Default communication

with the internet

By default, Amazon SageMaker Studio provides a network interface that allows communication
with the internet through a VPC managed by SageMaker AI. Traffic to AWS services like Amazon S3
and CloudWatch goes through an internet gateway, as does traffic that accesses the SageMaker AI
API and SageMaker AI runtime. Traffic between the domain and your Amazon EFS volume goes through
the VPC that you specified when you onboarded to the domain or called the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") API.

## `VPC only`

communication with the internet

To prevent SageMaker AI from providing internet access to Studio, you
can disable internet access by specifying the `VPC only` network access
type when you [onboard to Studio](onboard-vpc.md "onboard-vpc.md") or call the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md")
API. As a result, you won't be able to run Studio unless your VPC has
an interface endpoint to the SageMaker API and runtime, or a NAT gateway with internet
access, and your security groups allow outbound connections.

###### Note

The network access type can be changed after domain creation using the `--app-network-access-type` parameter of the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html") command.

### Requirements to use `VPC only` mode

When you choose `VpcOnly`, follow these steps:

1. You must use private subnets only. You cannot use public subnets in `VpcOnly` mode.
2. Ensure your subnets have the required number of IP addresses needed.
   The expected number of IP addresses needed per user can vary based on
   use case. We recommend between 2 and 4 IP addresses per user. The total
   IP address capacity for a domain is the sum of available IP
   addresses for each subnet provided when the domain is created. Ensure
   that your estimated IP address usage does not exceed the capacity
   supported by the number of subnets you provide. Additionally, using
   subnets distributed across many availability zones can aid in IP address
   availability. For more information, see [VPC and
   subnet sizing for IPv4](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4").

###### Note

You can configure only subnets with a default tenancy VPC in which
your instance runs on shared hardware. For more information on the
tenancy attribute for VPCs, see [Dedicated Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md"). 3. ###### Warning

When using `VpcOnly` mode, you partly own the networking configuration for the
domain. We recommend the security best practice of applying
least-privilege permissions to the inbound and outbound access that
security group rules provide. Overly permissive inbound rule
configurations could allow users with access to the VPC to interact
with the applications of other user profiles without
authentication.

Set up one or more security groups with inbound and outbound rules
that allow the following traffic:

    * [NFS traffic over TCP
     on port 2049](../../../efs/latest/ug/network-access.md "../../../efs/latest/ug/network-access.md") between the domain and the Amazon EFS
     volume.
    * [TCP traffic within the security group](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances"). This is
     required for connectivity between the Jupyter
     Server application and the Kernel
     Gateway applications. You must allow access to at
     least ports in the range `8192-65535`.

Create a distinct security group for each user profile and add inbound
access from that same security group. We do not recommend reusing a
domain-level security group for user profiles. If the domain-level
security group allows inbound access to itself, then all applications in
the domain would have access to all other applications in the
domain. 4. If you want to allow internet access, you must use a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with") with access to the internet, for example
through an [internet
gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md"). 5. If you don't want to allow internet access, [create interface
VPC endpoints](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") (AWS PrivateLink) to allow Studio to
access the following services with the corresponding service names. You
must also associate the security groups for your VPC with these
endpoints.

    * SageMaker API :
     `com.amazonaws.`region`.sagemaker.api`.
    * SageMaker AI runtime:
     `com.amazonaws.`region`.sagemaker.runtime`.
     This is required to run endpoint invocations.
    * Amazon S3:
     `com.amazonaws.`region`.s3`.
    * SageMaker Projects:
     `com.amazonaws.`region`.servicecatalog`.
    * SageMaker Studio: `aws.sagemaker.region.studio`.
    * Any other AWS services you require.

If you use the [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") to run remote training jobs, you must also create the following Amazon VPC endpoints.

    * AWS Security Token Service:
     `com.amazonaws.`region`.sts`
    * Amazon CloudWatch:
     `com.amazonaws.`region`.logs`.
     This is required to allow SageMaker Python SDK to get the remote
     training job status from Amazon CloudWatch.

6. If using the domain in `VpcOnly` mode from an on-premises
   network, establish private connectivity from the network of the host
   running Studio in the browser and the target Amazon VPC. This is required
   because the Studio UI invokes AWS endpoints using API calls with temporary
   AWS credentials. These temporary credentials are associated with the execution role of the logged user
   profile. If the domain is configured in `VpcOnly`
   mode in an on-premises network, the execution role might define IAM
   policy conditions that enforce the execution of AWS service API calls
   only through the configured Amazon VPC endpoints.This causes API calls
   executed from the Studio UI to fail. We recommend resolving this using
   an [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") or [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")connection.

###### Note

For a customer working within VPC mode, company firewalls can cause
connection issues with Studio or applications. Make the following
checks if you encounter one of these issues when using Studio from
behind a firewall.

- Verify that the Studio URL and URLs for all of your
  applications are in your network's allowlist. For example:

```
*.studio.`region`.sagemaker.aws
*.console.aws.a2z.com
```

- Verify that the websocket connections are not blocked. Jupyter
  uses websockets.

###### For more information

- [Security groups for
  your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
- [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md "interface-vpc-endpoint.md")
- [VPC with public and private subnets (NAT)](../../../vpc/latest/userguide/VPC_Scenario2.md "../../../vpc/latest/userguide/VPC_Scenario2.md")
