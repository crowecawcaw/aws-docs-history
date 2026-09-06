

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Tag subnets for EKS Auto Mode
<a name="tag-subnets-auto"></a>

If you use the load balancing capability of EKS Auto Mode, you need to add AWS tags to your VPC subnets.

## Background
<a name="_background"></a>

These tags identify subnets as associated with the cluster, and more importantly if the subnet is public or private.

Public subnets have direct internet access via an internet gateway. They are used for resources that need to be publicly accessible such as load balancers.

Private subnets do not have direct internet access and use NAT gateways for outbound traffic. They are used for internal resources such as EKS nodes that don’t need public IPs.

To learn more about NAT gateways and Internet gateways, see [Connect your VPC to other networks](https://docs.aws.amazon.com/vpc/latest/userguide/extend-intro.html) in the Amazon Virtual Private Cloud (VPC) User Guide.

## Requirement
<a name="_requirement"></a>

At this time, subnets used for load balancing by EKS Auto Mode are required to have one of the following tags.

### Public subnets
<a name="_public_subnets"></a>

Public subnets are used for internet-facing load balancers. These subnets must have the following tags:


| Key | Value | 
| --- | --- | 
|  `kubernetes.io/role/elb`  |  `1` or `` | 

### Private subnets
<a name="_private_subnets"></a>

Private subnets are used for internal load balancers. These subnets must have the following tags:


| Key | Value | 
| --- | --- | 
|  `kubernetes.io/role/internal-elb`  |  `1` or `` | 

## Procedure
<a name="_procedure"></a>

Before you begin, identify which subnets are public (with Internet Gateway access) and which are private (using NAT Gateway). You’ll need permissions to modify VPC resources.

### AWS Management Console
<a name="auto-tag-subnets-console"></a>

1. Open the Amazon VPC console and navigate to **Subnets**.

1. Select the subnet to tag.

1. Choose the **Tags** tab and select **Add tag**.

1. Add the appropriate tag:
   + For public subnets: Key=`kubernetes.io/role/elb` 
   + For private subnets: Key=`kubernetes.io/role/internal-elb` 

1. Set **Value** to `1` or leave empty.

1. Save and repeat for remaining subnets.

### AWS CLI
<a name="shared_aws_cli"></a>

For public subnets:

```
aws ec2 create-tags \
    --resources subnet-ID \
    --tags Key=kubernetes.io/role/elb,Value=1
```

For private subnets:

```
aws ec2 create-tags \
    --resources subnet-ID \
    --tags Key=kubernetes.io/role/internal-elb,Value=1
```

Replace `subnet-ID` with your actual subnet ID.