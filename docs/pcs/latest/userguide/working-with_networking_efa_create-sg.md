# Create a security group to support EFA

communications

AWS CLI
You can use the following AWS CLI command to create a security group that supports EFA. The
command outputs a security group ID. Make the following replacements:

- `region-code` – Specify the AWS Region
  where you use AWS PCS, such as `us-east-1`.
- `vpc-id` – Specify the ID of the VPC that
  you use for AWS PCS.
- `efa-group-name` – Provide your chosen
  name for the security group.

```
aws ec2 create-security-group \
    --group-name `efa-group-name` \
    --description "Security group to enable EFA traffic" \
    --vpc-id `vpc-id` \
    --region `region-code`
```

Use the following commands to attach inbound and outbound security group rules. Make the
following replacement:

- `efa-secgroup-id` – Provide the ID of the
  EFA security group you just created.

```
aws ec2 authorize-security-group-ingress \
    --group-id `efa-secgroup-id` \
    --protocol -1 \
    --source-group `efa-secgroup-id`

aws ec2 authorize-security-group-egress \
    --group-id `efa-secgroup-id` \
    --protocol -1 \
    --source-group `efa-secgroup-id`
```

CloudFormation template
You can use a CloudFormation template to create a security group that supports EFA.
Download the template from the following URL, then upload it into the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/enable_efa/assets/efa-sg.yaml
```

With the template open in the AWS CloudFormation console, enter the following options.

- Under **Provide a stack name**
  - Under **Stack name**, enter a name such as
    `efa-sg-stack`.

- Under **Parameters**
  - Under **SecurityGroupName**, enter a name such as
    `efa-sg`.
  - Under **VPC**, select the VPC where you will use AWS PCS.

Finish creating the CloudFormation stack and monitor its status. When it reaches
`CREATE_COMPLETE` the EFA security group is ready for use.
