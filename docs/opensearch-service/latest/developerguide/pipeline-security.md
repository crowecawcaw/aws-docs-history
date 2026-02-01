# Configuring VPC access for Amazon OpenSearch Ingestion

pipelines

You can access your Amazon OpenSearch Ingestion pipelines using an interface VPC endpoint. A
VPC is a virtual network that's dedicated to your AWS account. It's logically isolated
from other virtual networks in the AWS Cloud. Accessing a pipeline through a VPC endpoint
enables secure communication between OpenSearch Ingestion and other services within the VPC
without the need for an internet gateway, NAT device, or VPN connection. All traffic remains
securely within the AWS Cloud.

OpenSearch Ingestion establishes this private connection by creating an _interface endpoint_, powered by AWS PrivateLink. We create an endpoint network
interface in each subnet that you specify during pipeline creation. These are
requester-managed network interfaces that serve as the entry point for traffic destined for
the OpenSearch Ingestion pipeline. You can also choose to create and manage the interface
endpoints yourself.

Using a VPC allows you to enforce data flow through your OpenSearch Ingestion pipelines within
the boundaries of the VPC, rather than over the public internet. Pipelines that aren't
within a VPC send and receive data over public-facing endpoints and the internet.

A pipeline with VPC access can write to public or VPC OpenSearch Service domains, and to public or VPC
OpenSearch Serverless collections.

###### Topics

- [Considerations](#pipeline-vpc-considerations "#pipeline-vpc-considerations")
- [Limitations](#pipeline-vpc-limitations "#pipeline-vpc-limitations")
- [Prerequisites](#pipeline-vpc-prereqs "#pipeline-vpc-prereqs")
- [Configuring VPC access for a pipeline](#pipeline-vpc-configure "#pipeline-vpc-configure")
- [Self-managed VPC endpoints](#pipeline-vpc-self-managed "#pipeline-vpc-self-managed")
- [Service-linked role for VPC access](#pipeline-vpc-slr "#pipeline-vpc-slr")

## Considerations

Consider the following when you configure VPC access for a pipeline.

- A pipeline doesn't need to be in the same VPC as its sink. You also don't need
  to establish a connection between the two VPCs. OpenSearch Ingestion takes care of
  connecting them for you.
- You can only specify one VPC for your pipeline.
- Unlike with public pipelines, a VPC pipeline must be in the same AWS Region
  as the domain or collection sink that it's writing to.
  You can configure an S3 source for the pipeline in order to write cross-region.
- You can choose to deploy a pipeline into one, two, or three subnets of your
  VPC. The subnets are distributed across the same Availability Zones that your
  Ingestion OpenSearch Compute Units (OCUs) are deployed in.
- If you only deploy a pipeline in one subnet and the Availability Zone goes
  down, you won't be able to ingest data. To ensure high availability, we
  recommend that you configure pipelines with two or three subnets.
- Specifying a security group is optional. If you don't provide a security
  group, OpenSearch Ingestion uses the default security group that is specified in the
  VPC.

## Limitations

Pipelines with VPC access have the following limitations.

- You can't change a pipeline's network configuration after you create it. If
  you launch a pipeline within a VPC, you can't later change it to a public
  endpoint, and vice versa.
- You can either launch your pipeline with an interface VPC endpoint or a
  public endpoint, but you can't do both. You must choose one or the other when
  you create a pipeline.
- After you provision a pipeline with VPC access, you can't move it to a
  different VPC, and you can't change its subnets or security group
  settings.
- If your pipeline writes to a domain or collection sink that uses VPC access,
  you can't go back later and change the sink (VPC or public) after the pipeline
  is created. You must delete and recreate the pipeline with a new sink. You can
  still switch from a public sink to a sink with VPC access.
- You can't provide [cross-account ingestion access](configure-client.md#configure-client-cross-account "configure-client.md#configure-client-cross-account") to VPC pipelines.

## Prerequisites

Before you can provision a pipeline with VPC access, you must do the
following:

- **Create a VPC**

To create your VPC, you can use the Amazon VPC console, the AWS CLI, or one
of the AWS SDKs. For more information, see [Working with VPCs](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md") in
the _Amazon VPC User Guide_. If you already have
a VPC, you can skip this step.

- **Reserve IP addresses**

OpenSearch Ingestion places an _elastic network interface_
in each subnet that you specify during pipeline creation. Each network interface
is associated with an IP address. You must reserve one IP address per subnet for
the network interfaces.

## Configuring VPC access for a pipeline

You can enable VPC access for a pipeline within the OpenSearch Service console or using the
AWS CLI.

You configure VPC access during [pipeline
creation](creating-pipeline.md#create-pipeline "creating-pipeline.md#create-pipeline"). Under **Source network options**, choose
**VPC access** and configure the following settings:

| Setting                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint management**    | Choose whether you want to create your VPC endpoints<br>yourself, or have OpenSearch Ingestion create them for<br>you.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **VPC**                    | Choose the ID of the virtual private cloud (VPC) that you want to<br>use. The VPC and pipeline must be in the same AWS Region.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Subnets**                | Choose one or more subnets. OpenSearch Service places a VPC endpoint and<br>elastic network interfaces in the subnets.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Security groups**        | Choose one or more VPC security groups that allow your required<br>application to reach the OpenSearch Ingestion pipeline on the ports (80 or<br>443) and protocols (HTTP or HTTPs) exposed by the pipeline.                                                                                                                                                                                                                                                                                                                                                               |
| **VPC attachment options** | If your source requires cross-VPC communication, such as<br>Amazon DocumentDB, self-managed OpenSearch, or Confluent Kafka,<br>OpenSearch Ingestion creates Elastic Network Interfaces (ENIs) in<br>the subnets that you specify in order to connect to these<br>sources. OpenSearch Ingestion uses ENIs in each Availability Zone<br>to reach the specified sources. The \*_Attach to<br>VPC_<br>• option connects the OpenSearch Ingestion data<br>plane VPC to your specified VPC.<br>Select a CIDR reservation for the managed VPC to deploy<br>the network interface. |

To configure VPC access using the AWS CLI, specify the
`--vpc-options` parameter:

```
aws osis create-pipeline \
  --pipeline-name `vpc-pipeline` \
  --min-units 4 \
  --max-units 10 \
  --**vpc-options** SecurityGroupIds={`sg-12345678`,`sg-9012345`},SubnetIds=`subnet-1212234567834asdf` \
  --pipeline-configuration-body "file://`pipeline-config.yaml`"
```

## Self-managed VPC endpoints

When you create a pipeline, you can use endpoint management to create a pipeline with
self-managed endpoints or service-managed endpoints. Endpoint management is optional,
and defaults to endpoints managed by OpenSearch Ingestion.

To create a pipeline with a self-managed VPC endpoint in the AWS Management Console, see [Creating pipelines with the OpenSearch Service console](creating-pipeline.md#create-pipeline-console "creating-pipeline.md#create-pipeline-console"). To create a pipeline with a
self-managed VPC endpoint in the AWS CLI, you can use the `--vpc-options`
parameter in the [create-pipeline](../../../cli/latest/reference/osis/create-pipeline.md "../../../cli/latest/reference/osis/create-pipeline.md") command:

```
--vpc-options SubnetIds=subnet-abcdef01234567890,VpcEndpointManagement=CUSTOMER
```

You can create an endpoint to your pipeline yourself when you specify your endpoint
service. To find your endpoint service, use the [get-pipeline](../../../cli/latest/reference/osis/get-pipeline.md "../../../cli/latest/reference/osis/get-pipeline.md") command,
which returns a response similar to the following:

```
"vpcEndpointService" : "com.amazonaws.osis.us-east-1.pipeline-id-1234567890abcdef1234567890",
"vpcEndpoints" : [
  {
    "vpcId" : "vpc-1234567890abcdef0",
    "vpcOptions" : {
      "subnetIds" : [ "subnet-abcdef01234567890", "subnet-021345abcdef6789" ],
      "vpcEndpointManagement" : "CUSTOMER"
    }
  }
```

Use the `vpcEndpointService` from the response to create a VPC endpoint
with the AWS Management Console or AWS CLI.

If you use self-managed VPC endpoints, you must enable the DNS attributes
`enableDnsSupport` and `enableDnsHostnames` in your VPC. Note
that if you have a pipeline with a self-managed endpoint that you [stop and
restart](pipeline--stop-start.md "pipeline--stop-start.md"), you must recreate the VPC endpoint in your account.

## Service-linked role for VPC access

A [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") is a unique type of IAM role that delegates
permissions to a service so that it can create and manage resources on your behalf. If
you choose a service-managed VPC endpoint, OpenSearch Ingestion requires a service-linked
role called **AWSServiceRoleForAmazonOpenSearchIngestionService** to access your VPC,
create the pipeline endpoint, and place network interfaces in a subnet of your VPC.

If you choose a self-managed VPC endpoint, OpenSearch Ingestion requires a service-linked
role called **AWSServiceRoleForOpensearchIngestionSelfManagedVpce**. For more
information on these roles, their permissions, and how to delete them, see [Using service-linked roles to create OpenSearch Ingestion
pipelines](slr-osis.md "slr-osis.md").

OpenSearch Ingestion automatically creates the role when you create an ingestion pipeline.
For this automatic creation to succeed, the user creating the first pipeline in an
account must have permissions for the `iam:CreateServiceLinkedRole` action.
To learn more, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_. You can view the role in the AWS Identity and Access Management (IAM) console
after it's created.
