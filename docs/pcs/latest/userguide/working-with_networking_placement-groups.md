# Placement groups for EC2 instances in

AWS PCS

You can use a **placement group** to influence the placement of
EC2 instances to suit the needs of the workload that runs on them.

###### Placement group types

- Cluster – Packs instances close together in an
  Availability Zone to optimize for low-latency communication.
- Partition – Spreads instances across logical partitions to
  help maximize resilience.
- Spread – Strictly enforces that a small number of
  instances launch on distinct hardware, which can also help with resiliency.
  For more information, see [Placement groups for your Amazon EC2
  instances](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md") in the _Amazon Elastic Compute Cloud User Guide_.

We recommended you include a **cluster** placement group when
you configure an AWS PCS compute node group to use Elastic Fabric Adapter (EFA).

###### To create a cluster placement group that works with EFA

1. Create a placement group with the type **cluster** for the
   compute node group.
   - Use the following AWS CLI command:

   ```
   aws ec2 create-placement-group --strategy cluster --group-name `PLACEMENT-GROUP-NAME`
   ```

   - You can also use a CloudFormation template to create a placement group. For more
     information, see [Working with CloudFormation
     templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") in the _AWS CloudFormation User Guide_. Download the template
     from the following URL and upload it into the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").

   ```
   https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/enable_efa/assets/efa-placement-group.yaml
   ```

2. Include the placement group in the EC2 launch template for the AWS PCS compute node
   group.
