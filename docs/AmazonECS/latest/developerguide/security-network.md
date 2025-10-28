# Network security best practices for Amazon ECS

Network security is a broad topic that encompasses several subtopics. These include
encryption-in-transit, network segmentation and isolation, firewalling, traffic routing,
and observability.

## Encryption in transit

Encrypting network traffic prevents unauthorized users from intercepting and
reading data when that data is transmitted across a network. With Amazon ECS, network
encryption can be implemented in any of the following ways.

- **Using Nitro instances:**

By default, traffic is automatically encrypted between the following Nitro
instance types: C5n, G4, I3en, M5dn, M5n, P3dn, R5dn, and R5n. Traffic isn't
encrypted when it's routed through a transit gateway, load balancer, or
similar intermediary.

    + [Encryption in transit](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit")
    + [What's new announcement from 2019](https://aws.amazon.com/about-aws/whats-new/2019/10/introducing-amazon-ec2-m5n-m5dn-r5n-and-r5dn-instances-featuring-100-gbps-of-network-bandwidth/ "https://aws.amazon.com/about-aws/whats-new/2019/10/introducing-amazon-ec2-m5n-m5dn-r5n-and-r5dn-instances-featuring-100-gbps-of-network-bandwidth/")
    + [This talk from
     re:Inforce 2019](https://youtu.be/oqHLLbOoxDg?si=Us1YhSiY4deXLFA7 "https://youtu.be/oqHLLbOoxDg?si=Us1YhSiY4deXLFA7")

- **Using Server Name Indication (SNI) with an Application Load Balancer:**

The Application Load Balancer (ALB) and Network Load Balancer (NLB) support Server Name Indication (SNI). By using
SNI, you can put multiple secure applications behind a single
listener. For this, each has its own TLS certificate. We recommend
that you provision certificates for the load balancer using AWS Certificate Manager
(ACM) and then add them to the listener's certificate list. The AWS load
balancer uses a smart certificate selection algorithm with SNI. If
the hostname that's provided by a client matches a single certificate in the
certificate list, the load balancer chooses that certificate. If a hostname
that's provided by a client matches multiple certificates in the list, the
load balancer selects a certificate that the client can support. Examples
include self-signed certificate or a certificate generated through the
ACM.

    + [SNI with Application Load Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md#https-listener-certificates "../../../elasticloadbalancing/latest/application/create-https-listener.md#https-listener-certificates")
    + [SNI with Network Load Balancer](../../../elasticloadbalancing/latest/network/create-listener.md "../../../elasticloadbalancing/latest/network/create-listener.md")

- **End-to-end encryption with TLS
  certificates:**

This involves deploying a TLS certificate with the task. This can
either be a self-signed certificate or a certificate from a trusted
certificate authority. You can obtain the certificate by referencing a
secret for the certificate. Otherwise, you can choose to run a container
that issues a Certificate Signing Request (CSR) to ACM and then mounts the resulting secret to a
shared volume.

    + [Maintaining transport layer security all the way to your
     containers using the Network Load Balancer with Amazon ECS part 1](https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-using-the-network-load-balancer-with-amazon-ecs/ "https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-using-the-network-load-balancer-with-amazon-ecs/")
    + [Maintaining Transport Layer Security (TLS) all the way to your container part 2:
     Using AWS Private Certificate Authority](https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-part-2-using-aws-certificate-manager-private-certificate-authority/ "https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-part-2-using-aws-certificate-manager-private-certificate-authority/")

## Task networking

The following recommendations are in consideration of how Amazon ECS works. Amazon ECS
doesn't use an overlay network. Instead, tasks are configured to operate in
different network modes. For example, tasks that are configured to use
`bridge` mode acquire a non-routable IP address from a Docker network
that runs on each host. Tasks that are configured to use the `awsvpc`
network mode acquire an IP address from the subnet of the host. Tasks that are
configured with `host` networking use the host's network interface.
`awsvpc` is the preferred network mode. This is because it's the only
mode that you can use to assign security groups to tasks. It's also the only mode
that's available for AWS Fargate tasks on Amazon ECS.

### Security

groups for tasks

We recommend that you configure your tasks to use the `awsvpc`
network mode. After you configure your task to use this mode, the Amazon ECS agent
automatically provisions and attaches an Elastic Network Interface (ENI) to the task. When the
ENI is provisioned, the task is enrolled in an AWS security group. The
security group acts as a virtual firewall that you can use to control inbound
and outbound traffic.

If you use a custom firewall with tasks or services, add an outbound rule to allow
traffic for the Amazon ECS agent management endpoints
("`ecs-a-*.`region`.amazonaws.com`"),
telemetry endpoints
("`ecs-t-*.`region`.amazonaws.com`"), and
the Service Connect Envoy management endpoints
("`ecs-sc.`region`.api.aws`").

## AWS PrivateLink and Amazon ECS

AWS PrivateLink is a networking technology that allows you to create private
endpoints for different AWS services, including Amazon ECS. The endpoints are required
in sandboxed environments where there is no Internet Gateway (IGW) attached to the Amazon VPC and no
alternative routes to the Internet. Using AWS PrivateLink ensures that calls to the
Amazon ECS service stay within the Amazon VPC and do not traverse the internet. For
instructions on how to create AWS PrivateLink endpoints for Amazon ECS and other related
services, see [Amazon ECS interface Amazon VPC
endpoints](vpc-endpoints.md "vpc-endpoints.md").

###### Important

AWS Fargate tasks don't require an AWS PrivateLink endpoint for Amazon ECS.

Amazon ECR and Amazon ECS both support endpoint policies. These policies allow you to refine
access to a service's APIs. For example, you could create an endpoint policy for
Amazon ECR that only allows images to be pushed to registries in particular AWS
accounts. A policy like this could be used to prevent data from being exfiltrated
through container images while still allowing users to push to authorized Amazon ECR
registries. For more information, see [Use
VPC endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies").

The following policy allows all AWS principals in your account to perform all
actions against only your Amazon ECR repositories:

```
{
  "Statement": [
    {
      "Sid": "LimitECRAccess",
      "Principal": "*",
      "Action": "*",
      "Effect": "Allow",
      "Resource": "arn:aws:ecr:`region`:`account_id`:repository/*"
    },
  ]
}

```

You can enhance this further by setting a condition that uses the new
`PrincipalOrgID` property. This prevents pushing and pulling of
images by an IAM principal that isn't part of your AWS Organizations. For more information,
see [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid").

We recommended applying the same policy to both the
`com.amazonaws.`region`.ecr.dkr` and the
`com.amazonaws.`region`.ecr.api`
endpoints.

## Container agent

settings

The Amazon ECS container agent configuration file includes several environment
variables that relate to network security. `ECS_AWSVPC_BLOCK_IMDS` and
`ECS_ENABLE_TASK_IAM_ROLE_NETWORK_HOST` are used to block a task's
access to Amazon EC2 metadata. `HTTP_PROXY` is used to configure the agent to
route through a HTTP proxy to connect to the internet. For instructions on
configuring the agent and the Docker runtime to route through a proxy, see [HTTP Proxy
Configuration](http_proxy_config.md "http_proxy_config.md").

###### Important

These settings aren't available when you use AWS Fargate.

## Network security recommendations

We recommend that you do the following when setting up your Amazon VPC, load balancers,
and network.

### Use

network encryption where applicable with Amazon ECS

You should use network encryption where applicable. Certain compliance
programs, such as PCI DSS, require that you encrypt data in transit if the
data contains cardholder data. If your workload has similar requirements,
configure network encryption.

Modern browsers warn users when connecting to insecure sites. If your service
is fronted by a public facing load balancer, use TLS/SSL to encrypt the traffic
from the client's browser to the load balancer and re-encrypt to the backend if
warranted.

### Use

`awsvpc` network mode and security groups to
control traffic between tasks and other resources in Amazon ECS

You should use `awsvpc` network mode and security groups when you
need to control traffic between tasks and between tasks and other network
resources. If your service is behind an ALB, use security groups to only
allow inbound traffic from other network resources using the same security group
as your ALB. If your application is behind an NLB, configure the
task's security group to only allow inbound traffic from the Amazon VPC CIDR range
and the static IP addresses assigned to the NLB.

Security groups should also be used to control traffic between tasks and other
resources within the Amazon VPC such as Amazon RDS databases.

### Create Amazon ECS clusters in separate Amazon VPCs when network traffic needs to be

strictly isolated

You should create clusters in separate Amazon VPCs when network traffic needs
to be strictly isolated. Avoid running workloads that have strict security
requirements on clusters with workloads that don't have to adhere to those
requirements. When strict network isolation is mandatory, create clusters in
separate Amazon VPCs and selectively expose services to other Amazon VPCs using Amazon VPC
endpoints. For more information, see [VPC endpoints](../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints "../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints").

### Configure AWS PrivateLink

endpoints when warranted for Amazon ECS

You should configure AWS PrivateLink endpoints when warranted. If your
security policy prevents you from attaching an Internet Gateway (IGW) to your Amazon VPCs,
configure AWS PrivateLink endpoints for Amazon ECS and other services such as Amazon ECR,
AWS Secrets Manager, and Amazon CloudWatch.

### Use Amazon VPC Flow Logs to analyze

the traffic to and from long-running tasks in Amazon ECS

You should use Amazon VPC Flow Logs to analyze the traffic to and from long-running
tasks. Tasks that use `awsvpc` network mode get their own ENI.
Doing this, you can monitor traffic that goes to and from individual tasks using
Amazon VPC Flow Logs. A recent update to Amazon VPC Flow Logs (v3), enriches the logs with
traffic metadata including the vpc ID, subnet ID, and the instance ID. This
metadata can be used to help narrow an investigation. For more information, see
[Amazon VPC Flow
Logs](../../../vpc/latest/userguide/flow-logs.md#flow-logs-basics "../../../vpc/latest/userguide/flow-logs.md#flow-logs-basics").

###### Note

Because of the temporary nature of containers, flow logs might not always
be an effective way to analyze traffic patterns between different containers
or containers and other network resources.
