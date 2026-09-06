

# Verifying Amazon ECS stopped task connectivity
<a name="verify-connectivity"></a>

There are times when a task stops because of a network connectivity issue. It might be an intermittent issue, but it is most likely caused because the task cannot connect to an endpoint. 

## Testing the task connectivity
<a name="test-network"></a>

You can use `AWSSupport-TroubleshootECSTaskFailedToStart` runbook to test the task connectivity. When you use the runbook, you need the following resource information:
+ The task ID

  Use the ID of the most recent failed task.
+ The cluster that the task was in

For information about how to use the runbook, see [`AWSSupport-TroubleshootECSTaskFailedToStart`](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootecstaskfailedtostart.html) in the *AWS Systems Manager Automation runbook reference*.

The runbook analyzes the task. You can view the results in the **Output** section for the following issues that can prevent a task from starting: 
+ Network connectivity to the configured container registry
+ VPC endpoint connectivity
+ Security group rule configuration

## Fixing VPC endpoint issues
<a name="fix-vpc-endpoints"></a>

When the `AWSSupport-TroubleshootECSTaskFailedToStart` runbook result indicates the VPC endpoint issue, check the following configuration:
+ The VPC where you create the endpoint and the VPC endpoint need to use Private DNS.
+ Make sure that you have a AWS PrivateLink endpoint for the service that the task cannot connect to in the same VPC as the task. For more information see one of the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html)
+ Configure an outbound rule for the task subnet which allows HTTPS on port 443 DNS (TCP) traffic. For more information, see [Configure security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon Elastic Compute Cloud User Guide*.
+ If you use a custom name domain server, then confirm the DNS query's settings. The query must have outbound access on port 53, and use UDP and TCP protocol. Also, it must have HTTPS access on port 443. For more information, see [Coonfigure security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html#add-remove-security-group-rules) in the *Amazon Elastic Compute Cloud User Guide*.
+ If the subnet has a network ACL, the following ACL rules are required:
  + An outbound rule that allows traffic that allows traffic on ports 1024-65535.
  + An inbound rule that allows TCP traffic on port 443.

  For information about how to configure rules, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

## Fixing network issues
<a name="fix-network-issues"></a>

When the `AWSSupport-TroubleshootECSTaskFailedToStart` runbook result indicates a network issue, check the following configuration:

### Tasks that use awsvpc network mode in a public subnet
<a name="fix-network-issues-fargate-public"></a>

Perform the following configuration based on the runbook:
+ For tasks in public subnets, specify **ENABLED** for **Auto-assign public IP** when launching the task. For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md).
+ You need a gateway to handle internet traffic. The route table for the task subnet needs to have a route for traffic to the gateway.

  For more information, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes) in the* Amazon Virtual Private Cloud User Guide*.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html)
+ If the task subnet has a network ACL, the following ACL rules are required:
  + An outbound rule that allows traffic on ports 1024-65535.
  + An inbound rule that allows TCP traffic on port 443.

  For information about how to configure rules, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

### Tasks that use awsvpc network mode in a private subnet
<a name="fix-network-issues-fargate-private"></a>

Perform the following configuration based on the runbook:
+ Choose **DISABLED** for **Auto-assign public IP** when launching the task.
+  Configure a NAT gateway in your VPC to route requests to the internet. For more information, see [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*. 
+ The route table for the task subnet needs to have a route for traffic to the NAT gateway.

  For more information, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes) in the* Amazon Virtual Private Cloud User Guide*.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html)
+ If the task subnet has a network ACL, the following ACL rules are required:
  + An outbound rule that allows traffic on ports 1024-65535.
  + An inbound rule that allows TCP traffic on port 443.

  For information about how to configure rules, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

### Tasks that don't use awsvpc network mode in a public subnet
<a name="fix-network-issues-ec2-public"></a>

Perform the following configuration based on the runbook:
+ Choose **Turn on** for **Auto assign IP** under **Networking for Amazon EC2 instances** when you create the cluster.

  This option assigns a public IP address to the instance primary network interface.
+ You need a gateway to handle internet traffic. The route table for the instance subnet needs to have a route for traffic to the gateway.

  For more information, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes) in the* Amazon Virtual Private Cloud User Guide*.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html)
+ If the instance subnet has a network ACL, the following ACL rules are required:
  + An outbound rule that allows traffic on ports 1024-65535.
  + An inbound rule that allows TCP traffic on port 443.

  For information about how to configure rules, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

### Tasks that don't use awsvpc network mode in a private subnet
<a name="fix-network-issues-fargate-private"></a>

Perform the following configuration based on the runbook:
+ Choose **Turn off** for **Auto assign IP** under **Networking for Amazon EC2 instances** when you create the cluster.
+  Configure a NAT gateway in your VPC to route requests to the internet. For more information, see [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*. 
+ The route table for the instance subnet needs to have a route for traffic to the NAT gateway.

  For more information, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes) in the* Amazon Virtual Private Cloud User Guide*.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html)
+ If the task subnet has a network ACL, the following ACL rules are required:
  + An outbound rule that allows traffic on ports 1024-65535.
  + An inbound rule that allows TCP traffic on port 443.

  For information about how to configure rules, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.