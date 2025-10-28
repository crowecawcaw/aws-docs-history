# Create security groups for AWS PCS

AWS PCS relies on security groups to manage network traffic into and out of a cluster and
its compute node groups. For detailed information on this topic, see [Security group requirements
and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements "working-with_networking_sg.md#working-with_networking_sg-requirements").

In this step, you will use an CloudFormation template to create two security groups.

- A cluster security group, which enables communications between AWS PCS controller, compute
  nodes, and login nodes.
- An inbound SSH security group, which you can optionally add to your login nodes to support
  SSH access

## Create the security groups for AWS PCS

You can use a CloudFormation template to create the security groups. Use the following
URL to download the CloudFormation template, then upload the template in the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home#/stacks/create "https://console.aws.amazon.com/cloudformation/home#/stacks/create") to create a new
CloudFormation stack. For more information, see [Using the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md")
in the _AWS CloudFormation User Guide_.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/getting_started/assets/pcs-cluster-sg.yaml
```

With the template open in the AWS CloudFormation console, enter the following options. Note
that some options will be pre-populated in the template — you can simply leave them as the
default values.

- Under **Provide a stack name**
  - Under **Stack name**, enter:

  ```
  getstarted-sg
  ```

- Under **Parameters**
  - Under **VpcId**, choose the VPC where the name starts with
    `hpc-networking`.
  - (Optional) Under **ClientIpCidr**, enter a more restrictive IP range
    for the inbound SSH security group. We recommend that you restrict this with your own
    IP/subnet (x.x.x.x/32 for your own ip or x.x.x.x/24 for range. Replace x.x.x.x with your own
    PUBLIC IP. You can get your public IP using tools such as [https://ifconfig.co/](https://ifconfig.co/ "https://ifconfig.co/"))

Monitor the status of the CloudFormation stack. When it reaches
`CREATE_COMPLETE` the security group resources are ready.

There are two security groups created, with the names:

- `cluster-getstarted-sg` – this is the cluster security group
- `inbound-ssh-getstarted-sg` – this is a security group to allow inbound
  SSH access
