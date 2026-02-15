# Creating a VPC for your AWS PCS

cluster

You can create an Amazon Virtual Private Cloud (Amazon VPC) for your clusters within AWS Parallel Computing Service (AWS PCS).

Use Amazon VPC to launch VPC resources into a virtual network that you've
defined. This virtual network closely resembles a traditional network that you might operate in
your own data center. However, it comes with the benefits of using the scalable infrastructure of
Amazon Web Services. We recommend that you have a thorough understanding of the Amazon VPC service before
deploying production VPC clusters. For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the author visual
mode._Amazon VPC User Guide_.

An PCS cluster, nodes, and supporting resources (such as file systems and directory
services) are deployed within your Amazon VPC. If you want to use an existing Amazon VPC with PCS,
it must meet the requirements described in [AWS PCS VPC and subnet requirements
and considerations](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md") . This topic describes how to create a
VPC that meets PCS requirements using an AWS–provided CloudFormation template. Once
you've deployed a template, you can view the resources created by the template to know exactly
what resources it created, and the configuration of those resources.

## Prerequisites

To create an Amazon VPC for PCS, you must have the necessary IAM permissions to
create Amazon VPC resources. These resources are VPCs, subnets, security groups, route tables and
routes, and internet and NAT gateways. For more information, see [Create a VPC with a public subnet](../../../vpc/latest/userguide/vpc-policy-examples.md#vpc-public-subnet-iam "../../../vpc/latest/userguide/vpc-policy-examples.md#vpc-public-subnet-iam") in the _Amazon VPC User Guide_. To review the
full list for Amazon EC2, see [Actions, resources, and
condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md") in the _Service Authorization Reference_.

## Create an Amazon VPC

Create a VPC by copy and pasting the appropriate URL for the AWS Region where you will use
PCS. You may also download the CloudFormation template and upload it yourself to the
[CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").

- **US East (N. Virginia) (us-east-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **US East (Ohio) (us-east-2)**

```
https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **US West (Oregon) (us-west-2)**

```
https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Asia Pacific (Mumbai) (ap-south-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Asia Pacific (Singapore) (ap-southeast-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Asia Pacific (Sydney) (ap-southeast-2)**

```
https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Asia Pacific (Tokyo) (ap-northeast-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Europe (Frankfurt) (eu-central-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Europe (Ireland) (eu-west-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Europe (London) (eu-west-2)**

```
https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Europe (Paris) (eu-west-3)**

```
https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Europe (Stockholm) (eu-north-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **AWS GovCloud (US-East) (us-gov-east-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=us-gov-east-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **AWS GovCloud (US-West) (us-gov-west-1)**

```
https://console.aws.amazon.com/cloudformation/home?region=us-gov-west-1#/stacks/create/review?stackName=hpc-networking&templateURL=https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

- **Template only**

```
https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

###### To create an Amazon VPC for PCS

1. Open the template in the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").

###### Note

These are pre-populated in the template so that you can simply leave them as the default
values. 2. Under **Provide a stack name**, then **Stack name**, enter
`hpc-networking`. 3. Under **parameters**, enter the following details:

    1. Under **VPC**, then **CidrBlock**, enter
     `10.3.0.0/16`
    2. Under **Subnets A**:


    	1. Then **CidrPublicSubnetA**, enter `10.3.0.0/20`
    	2. Then **CidrPrivateSubnetA**, enter `10.3.128.0/20`
    3. Under **Subnets B**:


    	1. Then **CidrPublicSubnetB**, enter `10.3.16.0/20`
    	2. Then **CidrPrivateSubnetA**, enter  `10.3.144.0/20`
    4. Under **Subnets C**:


    	1. For **ProvisionSubnetsC**, select `True`.


    	###### Note

    	If you are creating a VPC in a Region that has less than three Availability Zones,
    	 this option will be ignored if set to `True`.
    	2. Then **CidrPublicSubnetB**, enter `10.3.32.0/20`
    	3. Then **CidrPrivateSubnetA**, enter `10.3.160.0/20`

4. Under **Capabilities**, check the box for **I acknowledge that
   AWS CloudFormation might create IAM resources**.

Monitor the status of the CloudFormation stack. When it reaches `CREATE_COMPLETE`, the VPC
resource are ready for you to use.

###### Note

To see all the resources the CloudFormation template created, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation"). Choose the
`hpc-networking` stack and then choose the **Resources**
tab.
