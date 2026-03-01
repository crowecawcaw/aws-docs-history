# Create a service that uses VPC Lattice

You can use either the AWS Management Console or the AWS CLI to create a service with VPC Lattice.

## Prerequisites

Before you start this tutorial, make sure that the following prerequisites are
met:

- The latest version of the AWS CLI is installed and configured. For more
  information, see [Installing the
  AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

- The steps described in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") are complete.
- Your IAM user has the required permissions specified in the [AmazonECS_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess") IAM policy
  example.

## Create a service that uses VPC Lattice with the AWS Management Console

Follow these steps to create a service with VPC Lattice using the AWS Management Console.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation page, choose **Clusters**.
3. On the **Clusters** page, choose the cluster to create the
   service in.
4. From the **Services** tab, choose
   **Create**.

If you've never created a service before, follow the steps found in [Creating an Amazon ECS service using the console](create-service-console-v2.md "create-service-console-v2.md"), then continue with
these steps when you reach the VPC Lattice section. 5. Choose to **Turn on VPC Lattice** by checking the button. 6. To use an existing role, for **ECS infrastructure role for
Amazon ECS**, choose one that you've already created to use when
creating the VPC Lattice target group. To create a new role, **Create ECS
infrastructure role**. 7. Choose the **VPC**.

The **VPC** depends on the networking mode you selected when
you registered your task definition. If you use the `host` or
`network` mode with EC2, choose your VPC.

For the `awsvpc` mode, the VPC is automatically selected based on
the VPC you chose under **Networking** and can't be
changed. 8. Under **Target Groups** choose the target group or groups.
You need to choose at least one target group and can have a maximum of five.
Choose **Add target group** to add additional target groups.
Choose the **Port name**, **Protocol**, and
**Port** for each target group you chose. To delete a
target group, choose **Remove**.

###### Note

    * If you want to add existing target groups, you need use the AWS CLI.
     For instructions on how to add target groups using the AWS CLI, see
     [register-targets](../../../cli/latest/reference/vpc-lattice/register-targets.md "../../../cli/latest/reference/vpc-lattice/register-targets.md")  in the*AWS Command Line Interface Reference*.
    * While a VPC Lattice service can have multiple target groups, each
     target group can only be added to one service.
    * To create a service in an IPv6-only configuration, choose target
     groups with an IP address type of `IPv6`.

9. At this point, you navigate to the VPC Lattice console to continue setting up.
   This is where you include your new target groups in the listener default action
   or in the rules of an existing VPC Lattice service.

For more information, see [Listener rules for your VPC
Lattice service](../../../vpc-lattice/latest/ug/listener-rules.md "../../../vpc-lattice/latest/ug/listener-rules.md").

###### Important

You need to allow the inbound rule `vpc-lattice` prefix to your
security group or tasks and health checks can fail.

## Create a service that uses VPC Lattice with the AWS CLI

Use the AWS CLI to create a service with VPC Lattice. Replace each `user input
 placeholder` with your own information.

1. Create a target group configuration file. The following example is named
   `tg-config.json`

```
{
    "ipAddressType": "IPV4",
    "port": 443,
    "protocol": "HTTPS",
    "protocolVersion": "HTTP1",
    "vpcIdentifier": "`vpc-f1663d9868EXAMPLE`"
}
```

2. Use the following command to create a VPC Lattice target group.

```
aws vpc-lattice create-target-group \
    --name my-lattice-target-group-ip \
    --type IP \
    --config file://`tg-config.json`
```

###### Note

To create a service in an IPv6-only configuration, create target groups
with an IP address type of `IPv6`. For more information, see
[create-target-group](../../../cli/latest/reference/vpc-lattice/create-target-group.md "../../../cli/latest/reference/vpc-lattice/create-target-group.md") in the
_AWS CLI Command Reference_.

Example output:

```
{
    "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE",
    "config": {
        "healthCheck": {
            "enabled": true,
            "healthCheckIntervalSeconds": 30,
            "healthCheckTimeoutSeconds": 5,
            "healthyThresholdCount": 5,
            "matcher": {
                "httpCode": "200"
            },
            "path": "/",
            "protocol": "HTTPS",
            "protocolVersion": "HTTP1",
            "unhealthyThresholdCount": 2
        },
        "ipAddressType": "IPV4",
        "port": 443,
        "protocol": "HTTPS",
        "protocolVersion": "HTTP1",
        "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
    },
    "id": "tg-0eaa4b9ab4EXAMPLE",
    "name": "my-lattice-target-group-ip",
    "status": "CREATE_IN_PROGRESS",
    "type": "IP"
}
```

3. The following JSON file named
   `ecs-service-vpc-lattice.json` is an example used
   to attach an Amazon ECS service to a VPC Lattice target group. The `portName`
   in the example below is the same one you defined in your task definition's
   `portMappings` property's `name` field.

```
{
    "serviceName": "`ecs-service-vpc-lattice`",
    "taskDefinition": "`ecs-task-def`",
        "vpcLatticeConfigurations": [
        {
            "targetGroupArn": "arn:aws:vpc-lattice:`us-west-2:123456789012`:targetgroup/`tg-0eaa4b9ab4EXAMPLE`",
            "portName": "`testvpclattice`",
            "roleArn": "arn:aws:iam::`123456789012`:role/ecsInfrastructureRoleVpcLattice"
        }
    ],
    "desiredCount": `5`,
    "role": "`ecsServiceRole`"
}
```

Use the following command to create an Amazon ECS service and attach it to the
VPC Lattice target group using the json example above.

```
aws ecs create-service \
    --cluster `clusterName` \
    --serviceName `ecs-service-vpc-lattice` \
    --cli-input-json file://`ecs-service-vpc-lattice.json`
```
