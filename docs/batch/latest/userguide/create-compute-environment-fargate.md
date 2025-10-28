# Tutorial: Create a managed compute

environment using Fargate resources

Complete the following steps to create a managed compute environment using AWS Fargate
resources.

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Compute environments**.
4. Choose **Create**.
5. Configure the compute environment.

###### Note

Compute environments for Windows containers on AWS Fargate jobs must at least one vCPU.

    1. For **Compute environment configuration**, choose
     **Fargate**.
    2. For **Name**, specify a unique name for your compute environment.
     The name can contain up to 128 characters in length. It can contain uppercase and
     lowercase letters, numbers, hyphens (-), and underscores (\_).
    3. For **Service role**, choose service-linked role that lets the
     AWS Batch service to make calls to the required AWS API operations on your behalf. For
     example, choose **AWSServiceRoleForBatch**. For more information, see
     [Using service-linked roles for
     AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md").
    4. (Optional) Expand **Tags**. To add a tag, choose **Add
     tag**. Then, enter a **Key** name and optional
     **Value**. Choose **Add tag**.
    5. Choose **Next page**.

6. In the **Instance configuration** section:
   1. (Optional) For **Use Fargate Spot capacity**, turn on Fargate
      Spot. For information about Fargate Spot, see [Using Amazon EC2 Spot
      and Fargate_SPOT](../../../AmazonECS/latest/bestpracticesguide/ec2-and-fargate-spot.md "../../../AmazonECS/latest/bestpracticesguide/ec2-and-fargate-spot.md").
   2. For **Maximum vCPUs**, choose the maximum number of vCPUs that
      your compute environment can scale out to, regardless of job queue demand.
   3. Choose **Next page**.

7. Configure networking.

###### Important

Compute resources need access to communicate with the Amazon ECS
service endpoint. This can be through an interface VPC endpoint or through your
compute resources having public IP addresses.

For more information about interface VPC endpoints, see [Amazon ECS Interface
VPC Endpoints (AWS PrivateLink)](../../../AmazonECS/latest/developerguide/vpc-endpoints.md "../../../AmazonECS/latest/developerguide/vpc-endpoints.md") in the
_Amazon Elastic Container Service Developer Guide_.

If you do not have an interface VPC endpoint configured and your compute
resources do not have public IP addresses, then they must use
network address translation (NAT) to provide this access. For more information,
see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_. For more information, see
[Create a VPC](create-a-vpc.md "create-a-vpc.md").

    1. For **Virtual Private Cloud (VPC) ID**, choose a VPC where you
     want to launch your instances.
    2. For **Subnets**, choose the subnets to use. By default, all
     subnets within the selected VPC are available.


    ###### Note

    AWS Batch on Fargate doesn't currently support Local Zones. For more
     information, see  [Amazon ECS clusters in Local Zones, Wavelength Zones, and AWS Outposts](../../../AmazonECS/latest/developerguide/cluster-regions-zones.md#clusters-local-zones "../../../AmazonECS/latest/developerguide/cluster-regions-zones.md#clusters-local-zones") in the
     *Amazon Elastic Container Service Developer Guide*.
    3. For **Security groups**, choose a security group to attach to
     your instances. By default, the default security group for your VPC is chosen.
    4. Choose **Next page**.

8. For **Review**, review the configuration steps. If you
   need to make changes, choose **Edit**. When you're finished,
   choose **Create compute environment**.
