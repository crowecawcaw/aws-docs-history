

# Create a service that uses VPC Lattice
<a name="ecs-vpc-lattice-create-service"></a>

You can use either the AWS Management Console or the AWS CLI to create a service with VPC Lattice.

## Prerequisites
<a name="create-ecs-vpc-lattice-prereqs"></a>

Before you start this tutorial, make sure that the following prerequisites are met:
+ The latest version of the AWS CLI is installed and configured. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
**Note**  
You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md).
+ The steps described in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md) are complete.
+ Your IAM user has the required permissions specified in the [AmazonECS\_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess) IAM policy example.

## Create a service that uses VPC Lattice with the AWS Management Console
<a name="ecs-lattice-create-console"></a>

Follow these steps to create a service with VPC Lattice using the AWS Management Console.

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation page, choose **Clusters**.

1. On the **Clusters** page, choose the cluster to create the service in.

1. From the **Services** tab, choose **Create**.

   If you've never created a service before, follow the steps found in [Creating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html), then continue with these steps when you reach the VPC Lattice section.

1. Choose to **Turn on VPC Lattice** by checking the button.

1. To use an existing role, for **ECS infrastructure role for Amazon ECS**, choose one that you've already created to use when creating the VPC Lattice target group. To create a new role, **Create ECS infrastructure role**.

1. Choose the **VPC**.

   The **VPC** depends on the networking mode you selected when you registered your task definition. If you use the `host` or `network` mode with EC2, choose your VPC. 

   For the `awsvpc` mode, the VPC is automatically selected based on the VPC you chose under **Networking** and can't be changed.

1. Under **Target Groups** choose the target group or groups. You need to choose at least one target group and can have a maximum of five. Choose **Add target group** to add additional target groups. Choose the **Port name**, **Protocol**, and **Port** for each target group you chose. To delete a target group, choose **Remove**.
**Note**  
If you want to add existing target groups, you need use the AWS CLI. For instructions on how to add target groups using the AWS CLI, see [register-targets ](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/register-targets.html) in the* AWS Command Line Interface Reference*.
While a VPC Lattice service can have multiple target groups, each target group can only be added to one service.
To create a service in an IPv6-only configuration, choose target groups with an IP address type of `IPv6`.

1. At this point, you navigate to the VPC Lattice console to continue setting up. This is where you include your new target groups in the listener default action or in the rules of an existing VPC Lattice service. 

   For more information, see [Listener rules for your VPC Lattice service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listener-rules.html).

**Important**  
You need to allow the inbound rule `vpc-lattice` prefix to your security group or tasks and health checks can fail. 

## Create a service that uses VPC Lattice with the AWS CLI
<a name="ecs-lattice-create-cli"></a>

Use the AWS CLI to create a service with VPC Lattice. Replace each {{user input placeholder}} with your own information.

1. Create a target group configuration file. The following example is named `tg-config.json`

   ```
   {
       "ipAddressType": "IPV4",
       "port": 443,
       "protocol": "HTTPS",
       "protocolVersion": "HTTP1",
       "vpcIdentifier": "{{vpc-f1663d9868EXAMPLE}}"
   }
   ```

1. Use the following command to create a VPC Lattice target group.

   ```
   aws vpc-lattice create-target-group \
       --name my-lattice-target-group-ip \
       --type IP \
       --config file://{{tg-config.json}}
   ```
**Note**  
To create a service in an IPv6-only configuration, create target groups with an IP address type of `IPv6`. For more information, see [create-target-group](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-target-group.html) in the *AWS CLI Command Reference*.

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

1. The following JSON file named {{ecs-service-vpc-lattice.json}} is an example used to attach an Amazon ECS service to a VPC Lattice target group. The `portName` in the following example is the same one you defined in your task definition's `portMappings` property's `name` field.

   ```
   {
       "serviceName": "{{ecs-service-vpc-lattice}}",
       "taskDefinition": "{{ecs-task-def}}",
           "vpcLatticeConfigurations": [
           {
               "targetGroupArn": "arn:aws:vpc-lattice:{{us-west-2:123456789012}}:targetgroup/{{tg-0eaa4b9ab4EXAMPLE}}",
               "portName": "{{testvpclattice}}",
               "roleArn": "arn:aws:iam::{{123456789012}}:role/ecsInfrastructureRoleVpcLattice"
           }
       ],
       "desiredCount": {{5}},
       "role": "{{ecsServiceRole}}"
   }
   ```

   Use the following command to create an Amazon ECS service and attach it to the VPC Lattice target group using the preceding JSON example.

   ```
   aws ecs create-service \
       --cluster {{clusterName}} \
       --serviceName {{ecs-service-vpc-lattice}} \
       --cli-input-json file://{{ecs-service-vpc-lattice.json}}
   ```