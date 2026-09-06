

# Use Amazon SageMaker geospatial capabilities in Your Amazon Virtual Private Cloud
<a name="geospatial-notebooks-and-internet-access-vpc-requirements"></a>

**Note**  
Amazon SageMaker geospatial capabilities is no longer open to new customers. Offboard any previously saved jobs to Amazon S3 by using the [ExportEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html) and [ExportVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html) API operations.

The following topic gives information on how to use SageMaker notebooks with a SageMaker geospatial image in a Amazon SageMaker AI domain with VPC only mode. For more information on VPCs in Amazon SageMaker Studio Classic see [Choose an Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-vpc.html).

## `VPC only` communication with the internet
<a name="studio-notebooks-and-internet-access-vpc-geospatial"></a>

By default, SageMaker AI domain uses two Amazon VPC. One of the Amazon VPC is managed by Amazon SageMaker AI and provides direct internet access. You specify the other Amazon VPC, which provides encrypted traffic between the domain and your Amazon Elastic File System (Amazon EFS) volume.

You can change this behavior so that SageMaker AI sends all traffic over your specified Amazon VPC. If `VPC only` has been choosen as the network access mode during the SageMaker AI domain creation, the following requirements need to be considered to still allow usage of SageMaker Studio Classic notebooks within the created SageMaker AI domain.

## Requirements to use `VPC only` mode
<a name="studio-notebooks-and-internet-access-vpc-geospatial-requirements"></a>

**Note**  
In order to use the visualization components of SageMaker geospatial capabilities, the browser you use to access the SageMaker Studio Classic UI needs to be connected to the internet.

When you choose `VpcOnly`, follow these steps:

1. You must use private subnets only. You cannot use public subnets in `VpcOnly` mode.

1. Ensure your subnets have the required number of IP addresses needed. The expected number of IP addresses needed per user can vary based on use case. We recommend between 2 and 4 IP addresses per user. The total IP address capacity for a Studio Classic domain is the sum of available IP addresses for each subnet provided when the domain is created. Ensure that your estimated IP address usage does not exceed the capacity supported by the number of subnets you provide. Additionally, using subnets distributed across many availability zones can aid in IP address availability. For more information, see [VPC and subnet sizing for IPv4](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-sizing-ipv4).
**Note**  
You can configure only subnets with a default tenancy VPC in which your instance runs on shared hardware. For more information on the tenancy attribute for VPCs, see [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html).

1. Set up one or more security groups with inbound and outbound rules that together allow the following traffic:
   + [NFS traffic over TCP on port 2049](https://docs.aws.amazon.com/efs/latest/ug/network-access.html) between the domain and the Amazon EFS volume.
   + [TCP traffic within the security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html#sg-rules-other-instances). This is required for connectivity between the JupyterServer app and the KernelGateway apps. You must allow access to at least ports in the range `8192-65535`.

1. If you want to allow internet access, you must use a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-working-with) with access to the internet, for example through an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

1. If you don't want to allow internet access, [create interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) (AWS PrivateLink) to allow Studio Classic to access the following services with the corresponding service names. You must also associate the security groups for your VPC with these endpoints.
**Note**  
Currently, SageMaker geospatial capabilities are only supported in the US West (Oregon) Region.
   + SageMaker API : `com.amazonaws.us-west-2.sagemaker.api` 
   + SageMaker AI runtime: `com.amazonaws.us-west-2.sagemaker.runtime`. This is required to run Studio Classic notebooks with a SageMaker geospatial image.
   + Amazon S3: `com.amazonaws.us-west-2.s3`.
   + To use SageMaker Projects: `com.amazonaws.us-west-2.servicecatalog`.
   + SageMaker geospatial capabilities: `com.amazonaws.us-west-2.sagemaker-geospatial`

    If you use the [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/) to run remote training jobs, you must also create the following Amazon VPC endpoints.
   + AWS Security Token Service: `com.amazonaws.{{region}}.sts`
   + Amazon CloudWatch: `com.amazonaws.{{region}}.logs`. This is required to allow SageMaker Python SDK to get the remote training job status from Amazon CloudWatch.

**Note**  
For a customer working within VPC mode, company firewalls can cause connection issues with SageMaker Studio Classic or between JupyterServer and the KernelGateway. Make the following checks if you encounter one of these issues when using SageMaker Studio Classic from behind a firewall.  
Check that the Studio Classic URL is in your networks allowlist.
Check that the websocket connections are not blocked. Jupyter uses websocket under the hood. If the KernelGateway application is InService, JupyterServer may not be able to connect to the KernelGateway. You should see this problem when opening System Terminal as well. 