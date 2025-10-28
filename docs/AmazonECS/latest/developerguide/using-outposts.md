# Amazon Elastic Container Service on AWS Outposts

AWS Outposts enables native AWS services, infrastructure, and operating models in
on-premises facilities. In AWS Outposts environments, you can use the same AWS APIs, tools, and
infrastructure that you use in the AWS Cloud.

Amazon ECS on AWS Outposts is ideal for low-latency workloads that need to be run in close proximity
to on-premises data and applications.

For more information about AWS Outposts, see the [_AWS Outposts User
Guide_](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md").

## Considerations

The following are considerations of using Amazon ECS on AWS Outposts:

- Amazon Elastic Container Registry, AWS Identity and Access Management, and Network Load Balancer run in the AWS Region, not on AWS Outposts.
  This will increase latencies between these services and the containers.
- AWS Fargate is not available on AWS Outposts.

The following are network connectivity considerations for AWS Outposts:

- If network connectivity between your AWS Outposts and its AWS Region is lost,
  your clusters will continue to run. However, you cannot create new clusters or
  take new actions on existing clusters until connectivity is restored. In case of
  instance failures, the instance will not be automatically replaced. The CloudWatch Logs
  agent will be unable to update logs and event data.
- We recommend that you provide reliable, highly available, and low latency
  connectivity between your AWS Outposts and its AWS Region.

## Prerequisites

The following are prerequisites for using Amazon ECS on AWS Outposts:

- You must have installed and configured an Outpost in your on-premises data
  center.
- You must have a reliable network connection between your Outpost and its AWS
  Region.

## Overview of cluster creation on AWS Outposts

The following is an overview of the configuration:

1. Create a role and policy with rights on AWS Outposts.
2. Create an IAM instance profile with rights on AWS Outposts.
3. Create a VPC, or use an existing one that is in the same
   Region as your AWS Outposts.
4. Create a subnet or use an existing one that is associated with the
   AWS Outposts.

This is the subnet where the container instances run. 5. Create a security group for the container instances in your cluster. 6. Create an Amazon ECS cluster. 7. Define the Amazon ECS container agent environment variables to launch the instance
into the cluster. 8. Run a container.

For detailed information about how to integrate Amazon ECS with AWS Outposts, see [Extend Amazon ECS across two AWS Outposts racks](https://community.aws/content/2k5wK9P1oSC9I4ZzuSLWynsiJaa/extend-amazon-ecs-across-two-outposts-racks "https://community.aws/content/2k5wK9P1oSC9I4ZzuSLWynsiJaa/extend-amazon-ecs-across-two-outposts-racks").

The following example creates an Amazon ECS cluster on an AWS Outposts.

1. Create a role and policy with rights on AWS Outposts.

The `role-policy.json` file is the policy document that contains
the effect and actions for resources. For information about the file format, see
[PutRolePolicy](../../../IAM/latest/APIReference/API_PutRolePolicy.md "../../../IAM/latest/APIReference/API_PutRolePolicy.md")
in the _IAM API Reference_

```
aws iam create-role –-role-name `ecsRole` \
    --assume-role-policy-document file://ecs-policy.json
aws iam put-role-policy --role-name `ecsRole` --policy-name `ecsRolePolicy` \
    --policy-document file://role-policy.json
```

2. Create an IAM instance profile with rights on AWS Outposts.

```
aws iam create-instance-profile --instance-profile-name `outpost`
aws iam add-role-to-instance-profile --instance-profile-name `outpost` \
    --role-name `ecsRole`
```

3. Create a VPC.

```
aws ec2 create-vpc --cidr-block `10.0.0.0/16`
```

4. Create a subnet associated with your AWS Outposts.

```
aws ec2 create-subnet \
    --cidr-block `10.0.3.0/24` \
    --vpc-id `vpc-xxxxxxxx` \
    --outpost-arn arn:aws:outposts:`us-west-2`:123456789012:outpost/`op-xxxxxxxxxxxxxxxx` \
    --availability-zone-id `usw2-az1`
```

5. Create a security group for the container instances, specifying the proper
   CIDR range for the AWS Outposts. (This step is different for AWS Outposts.)

```
aws ec2 create-security-group --group-name `MyOutpostSG`
aws ec2 authorize-security-group-ingress --group-name `MyOutpostSG` --protocol tcp \
    --port 22 --cidr `10.0.3.0/24`
aws ec2 authorize-security-group-ingress --group-name `MyOutpostSG` --protocol tcp \
    --port 80 --cidr `10.0.3.0/24`
```

6. Create the Cluster.
7. Define the Amazon ECS container agent environment variables to launch the instance
   into the cluster created in the previous step and define any tags you want to
   add to help identify the cluster (for example, `Outpost` to indicate
   that the cluster is for an Outpost).

```
#! /bin/bash
cat << ‘EOF’ >> /etc/ecs/ecs.config
ECS_CLUSTER=MyCluster
ECS_IMAGE_PULL_BEHAVIOR=prefer-cached
ECS_CONTAINER_INSTANCE_TAGS={“environment”: ”Outpost”}
EOF
```

###### Note

In order to avoid delays caused by pulling container images from Amazon ECR in
the Region, use image caches. To do this, each time a task is run, configure
the Amazon ECS agent to default to using the cached image on the instance itself
by setting `ECS_IMAGE_PULL_BEHAVIOR` to
`prefer-cached`. 8. Create the container instance, specifying the VPC and subnet for the AWS Outposts
where this instance should run and an instance type that is available on the
AWS Outposts. (This step is different for AWS Outposts.)

The `userdata.txt` file contains the user data the instance can use
to perform common automated configuration tasks and even run scripts after the
instance starts. For information about the file for API calls, see [Run
commands on your Linux instance at launch](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md") in the _Amazon EC2 User Guide_.

```
aws ec2 run-instances --count 1 --image-id `ami-xxxxxxxx` --instance-type `c5.large` \
    --key-name `aws-outpost-key` –-subnet-id `subnet-xxxxxxxxxxxxxxxxx` \
    --iam-instance-profile Name `outpost` --security-group-id `sg-xxxxxx` \
    --associate-public-ip-address --user-data `file://userdata.txt`
```

###### Note

This command is also used when adding additional instances to the cluster.
Any containers deployed in the cluster will be placed on that specific
AWS Outposts.
