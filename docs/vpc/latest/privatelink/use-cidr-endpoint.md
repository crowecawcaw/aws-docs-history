

# Access a network segment through a tunnel VPC endpoint
<a name="use-cidr-endpoint"></a>

You can access a network segment through a tunnel endpoint. A network segment is a set of CIDR ranges. It is shared as a resource configuration of type CIDR. A tunnel endpoint associates with exactly one CIDR-type resource configuration.

## Prerequisites
<a name="prerequisites-cidr-endpoints"></a>

To create a tunnel endpoint, you must meet the following prerequisites.
+ You must have a CIDR-type resource configuration that you created, or that another account created and shared with you through AWS RAM.
+ If a resource configuration is shared with you from another account, you must review and accept the resource share that contains the resource configuration. For more information, see [Accepting and rejecting invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html) in the *AWS RAM User Guide*.
+ The resource configuration must be attached to a resource gateway whose DNS resolution flag is set to `IN_VPC`.
+ Your consumer VPC must have subnets in Availability Zones that overlap the provider resource gateway's Availability Zones.
+ Your consumer compute must be able to encapsulate application traffic in GENEVE. The VNI must be set to `0`. The inner packet must be a layer 3 IP packet. This should ideally be done in its own routing context or network namespace.
+ Security groups on both the endpoint and the compute must allow UDP port 6081.

## Create a tunnel VPC endpoint
<a name="create-cidr-endpoint-aws"></a>

After you create a tunnel endpoint, you must describe its association to obtain the per-Availability Zone endpoint IP addresses, and then configure the GENEVE device and the tunnel nameserver on your compute.

**To create a tunnel endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. (Optional) Enter a name to make it easier to find and manage the endpoint.

1. For **Type**, choose the tunnel endpoint type.

1. For **Resource configurations**, select the CIDR resource configuration.

1. For **Network settings**, select the VPC from which you'll access the range.

1. For **Subnets**, select a subnet in each Availability Zone that overlaps the resource gateway's Availability Zones.

1. For **Security groups**, select a security group that allows UDP port 6081. If you do not specify a security group, we associate the default security group for the VPC.

1. Choose **Create endpoint**.

The following [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) command creates a tunnel endpoint for a CIDR resource configuration:

```
aws ec2 create-vpc-endpoint \
    --vpc-endpoint-type Tunnel \
    --vpc-id {{vpc-1a2b3c4d}} \
    --subnet-ids {{subnet-1a2b3c4d}} \
    --ip-address-type ipv4 \
    --resource-configuration-arn arn:aws:vpc-lattice:{{us-east-1}}:111122223333:resourceconfiguration/{{rcfg-1234567890abcdefg}}
```

**To create a tunnel endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)