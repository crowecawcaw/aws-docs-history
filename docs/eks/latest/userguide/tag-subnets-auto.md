**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Tag subnets for EKS Auto Mode

If you use the load balancing capability of EKS Auto Mode, you need to add AWS tags to your VPC subnets.

## Background

These tags identify subnets as associated with the cluster, and more importantly if the subnet is public or private.

Public subnets have direct internet access via an internet gateway. They are used for resources that need to be publicly accessible such as load balancers.

Private subnets do not have direct internet access and use NAT gateways for outbound traffic. They are used for internal resources such as EKS nodes that don’t need public IPs.

To learn more about NAT gateways and Internet gateways, see [Connect your VPC to other networks](../../../vpc/latest/userguide/extend-intro.md "../../../vpc/latest/userguide/extend-intro.md") in the Amazon Virtual Private Cloud (VPC) User Guide.

## Requirement

At this time, subnets used for load balancing by EKS Auto Mode are required to have one of the following tags.

### Public subnets

Public subnets are used for internet-facing load balancers. These subnets must have the following tags:

| Key                      | Value     |
| ------------------------ | --------- |
| `kubernetes.io/role/elb` | `1` or `` |

### Private subnets

Private subnets are used for internal load balancers. These subnets must have the following tags:

| Key                               | Value     |
| --------------------------------- | --------- |
| `kubernetes.io/role/internal-elb` | `1` or `` |

## Procedure

Before you begin, identify which subnets are public (with Internet Gateway access) and which are private (using NAT Gateway). You’ll need permissions to modify VPC resources.

### AWS Management Console

1. Open the Amazon VPC console and navigate to Subnets
2. Select the subnet to tag
3. Choose the Tags tab and select Add tag
4. Add the appropriate tag:
   - For public subnets: Key=`kubernetes.io/role/elb`
   - For private subnets: Key=`kubernetes.io/role/internal-elb`

5. Set Value to `1` or leave empty
6. Save and repeat for remaining subnets

### AWS CLI

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
