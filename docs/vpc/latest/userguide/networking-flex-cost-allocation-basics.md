

# How Networking Flexible Cost Allocation works

Before you start: Networking Flexible Cost Allocation (FCA) writes its cost breakdown to your AWS Cost and Usage Report. Make sure your AWS Cost and Usage Report includes [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html), and that the management account or a standalone account has turned on **Networking flexible cost allocation** in Cost Management preferences. You then create a policy and associate it with your resources in the Amazon VPC console, with the AWS CLI, or with AWS CloudFormation. For how to turn on the preference, see [Turning on the data in your Cost and Usage Reports](networking-flex-cost-allocation-work-with.md#networking-flex-cost-allocation-turn-on). This section describes the concepts. To create and apply a policy, see [Working with Networking Flexible Cost Allocation](networking-flex-cost-allocation-work-with.md).

## Policies and associations
<a name="networking-flex-cost-allocation-concepts"></a>

FCA uses the following concepts.

### Policy
<a name="networking-flex-cost-allocation-concept-policy"></a>

Defines what to allocate. A policy applies to one resource type (NAT gateway, Amazon EC2 instance, or VPC peering connection), and specifies the cost dimensions to allocate and the reporting granularity. A policy has a description and can have tags.

### Association
<a name="networking-flex-cost-allocation-concept-association"></a>

Applies a policy to a resource. You can associate a policy with specific resources, or with an account, VPC, or subnet. When you associate a policy with an account, VPC, or subnet, it applies to every resource of the policy's resource type in that scope, including resources that exist now and resources that you create while the association is active. If a policy is associated with both a specific resource and a broader scope that contains it, the association with the specific resource applies.

### Dimension
<a name="networking-flex-cost-allocation-concept-dimension"></a>

The charge to allocate. The `data-transfer` dimension allocates data transfer charges. The `data-processing` dimension allocates data processing charges and is available only for NAT gateways.

### Reporting granularity
<a name="networking-flex-cost-allocation-concept-granularity"></a>

The level at which allocated usage is itemized. You specify one value for each policy.

The following reporting granularities are available for all resource types. They are listed from most specific to least specific.
+ `eni` – The network interface that generated the usage.
+ `ec2` – The Amazon EC2 instance that generated the usage.
+ `subnet` – The subnet.
+ `vpc` – The VPC.
+ `account` – The AWS account.
+ `cidr` – A label that you define for an IP address range, such as `10.0.1.0/24`.

Some resource types support additional granularities. For example, VPC peering connections also support `peering-id`. For the dimensions and granularities that each resource type supports, see the page for that resource type. If FCA can't resolve a flow at the granularity that you specify, it itemizes the usage at the next less specific level that it can resolve.

### Resource that generates the usage
<a name="networking-flex-cost-allocation-concept-resource"></a>

The resource on the other side of the traffic that the shared resource handles. For a NAT gateway, this is the resource that sends traffic through the NAT gateway and receives the responses. For an Amazon EC2 instance or a VPC peering connection, this is the peer that exchanges data with it. The policy attributes usage in both directions to this resource and identifies it at the policy's reporting granularity.

### Showback
<a name="networking-flex-cost-allocation-concept-showback"></a>

Turns allocation on or off for a policy. Showback is turned on by default. When showback is turned off, the policy and its associations remain; however, FCA doesn't itemize the usage. You can turn showback off and on again when you modify the policy, without removing the associations. Showback doesn't change who pays. The charges remain with the account that owns the shared resource.