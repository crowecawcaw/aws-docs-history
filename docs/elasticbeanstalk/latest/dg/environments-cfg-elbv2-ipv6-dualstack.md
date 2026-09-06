

# Configuring dual-stack Elastic Beanstalk load balancers
<a name="environments-cfg-elbv2-ipv6-dualstack"></a>

You can enable your Elastic Beanstalk environments to serve both IPv4 and IPv6 protocols with dual-stack configured load balancers. When you create a load balanced environment, the infrastructure defaults to IPv4. You can select to create new environments with dual-stack configuration or update existing IPv4-only environments to dual-stack.

To enable your environment's load balancers to serve both IPv6 and IPv4 network traffic set the `IpAddressType` option in the [aws:elbv2:loadbalancer](command-options-general.md#command-options-general-elbv2) namespace to *dualstack*.

**Note**  
Elastic Beanstalk only supports dual-stack protocols for Application Load Balancers and Network Load Balancers. It does not support dual-stack for environments that use Classic Load Balancers or single instance environments.

## Amazon VPC prerequisites
<a name="environments-cfg-elbv2-ipv6-dualstack.prereqs"></a>

Before you configure your load balancer in your Elastic Beanstalk environment, you must first complete some configuration steps with Amazon VPC:

1. Associate an IPv6 CIDR block with your environment’s VPC.

1. Associate IPv6 CIDR blocks to all of the VPC’s subnets.

1. (Optional) If your environment exchanges network traffic with components outside of the VPC, it has route tables that specify which networks your VPC can communicate with. In this case you must update the VPC route tables to enable IPv6 traffic. 

You can complete these prerequisite configurations with either the Amazon VPC console or AWS CLI commands. The topics that follow will guide you and direct you to the *Amazon VPC User Guide* and the *AWS CLI command reference* for more details.

**Note**  
After you complete the VPC configuration, wait several minutes for the changes to propagate before configuring dual-stack for your load balancer. If you encounter VPC or subnet configuration errors during dual-stack setup, wait a few minutes for the VPC configuration to propagate and try the dual-stack configuration again.

### Complete VPC prerequisites using the console
<a name="environments-cfg-elbv2-ipv6-dualstack.prereqs.console"></a>

The *Amazon VPC User Guide* provides detailed steps to complete these prerequisite tasks.

1. See [Step 1: Associate an IPv6 CIDR block with your VPC and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html#vpc-migrate-ipv6-cidr) in the *Amazon VPC User Guide*. 

   This step provides two procedures that you must complete:
   + Associate an IPv6 CIDR block with your VPC.
   + Associate an IPv6 CIDR block with your VPC subnets.

1. (Optional) If your environment exchanges network traffic with components outside of the VPC, it has route tables that specify which networks your VPC can communicate with. In this case you must update the VPC route tables to enable IPv6 traffic. To complete this configuration see [Step 2: Update your route tables](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html#vpc-migrate-ipv6-routes) in the *Amazon VPC User Guide*.

### Complete VPC prerequisites using the AWS CLI
<a name="environments-cfg-elbv2-ipv6-dualstack.prereqs.cli"></a>

You can use the AWS CLI to complete and verify the prerequisite configurations.

1. Associate an IPv6 CIDR block with your environment’s VPC.

   1. Use the [associate-vpc-cidr-block](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-vpc-cidr-block.html) command to associate a CIDR block with your VPC.

   1. Use the [describe-vpcs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpcs.html) command to verify your VPC configurations.

   

     
**Example commands**  

   ```
   # Associate an Amazon-provided IPv6 CIDR block with your VPC
   aws ec2 associate-vpc-cidr-block \
       --vpc-id {{vpc-12345678}} \
       --region {{us-east-1}}  \
       --amazon-provided-ipv6-cidr-block
   
   # Verify the IPv6 CIDR block association
   aws ec2 describe-vpcs \
       --vpc-ids {{vpc-12345678}} \
       --region {{us-east-1}}  \
       --query {{'Vpcs[0].Ipv6CidrBlockAssociationSet'}}
   ```

1. Associate IPv6 CIDR blocks to all of the VPC’s subnets.

   1. Use the [associate-subnet-cidr-block](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-subnet-cidr-block.html) command to associate a CIDR block with your subnet.

   1. Use the [describe-subnets](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-subnets.html) command to verify your subnet configurations.

   

     
**Example commands**  

   ```
   # List all subnets in your VPC
   aws ec2 describe-subnets \
       --region {{us-east-1}}  \
       --filters {{"Name=vpc-id,Values=vpc-12345678"}} \
       --query {{'Subnets[].{SubnetId:SubnetId,AvailabilityZone:AvailabilityZone}'}}
   
   # Associate IPv6 CIDR block with each subnet
   aws ec2 associate-subnet-cidr-block \
       --subnet-id {{subnet-12345678}} \
       --region {{us-east-1}}  \
       --ipv6-cidr-block {{2001:db8::/64}}
   
   # Verify IPv6 CIDR block association for all subnets
   aws ec2 describe-subnets \
       --region {{us-east-1}}  \
       --filters {{"Name=vpc-id,Values=vpc-12345678"}} \
       --query {{'Subnets[].{SubnetId:SubnetId,Ipv6CidrBlock:Ipv6CidrBlockAssociationSet[0].Ipv6CidrBlock}'}}
   ```

1.  (Optional) If your environment exchanges network traffic with components outside of the VPC, it has route tables that specify which networks your VPC can communicate with. In this case you must update the VPC route tables to enable IPv6 traffic. 

   1. Use the [create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html) command to add a route in a route table within the VPC.

   1. Use the [describe-route-tables](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-route-tables.html) command to verify your route tables.

   

     
**Example commands**  

   ```
   # Add IPv6 route to Internet Gateway for public subnets
   aws ec2 create-route \
       --route-table-id {{rtb-12345678}} \
       --destination-ipv6-cidr-block {{::/0}} \
       --gateway-id {{igw-12345678}}  \
       --region {{us-east-1}}
   
   # Add IPv6 route to NAT Gateway for private subnets (if applicable)
   aws ec2 create-route \
       --route-table-id {{rtb-87654321}} \
       --destination-ipv6-cidr-block {{::/0}} \
       --nat-gateway-id {{nat-12345678}} \
       --region {{us-east-1}}
   
   # Verify routes
   aws ec2 describe-route-tables \
       --route-table-ids {{rtb-12345678}} \
       --region {{us-east-1}} \
       --query {{'RouteTables[0].Routes'}}
   ```

## Configuring dual-stack for your Elastic Beanstalk load balancer
<a name="environments-cfg-elbv2-ipv6-dualstack.enable"></a>

After your VPC prerequisite configuration is set up for your environment, you can configure the load balancer with the dual-stack option, so it can serve both the IPv4 and IPv6 protocols. You can use the Elastic Beanstalk console, the AWS CLI, configuration files in `.ebextensions`, and the AWS SDK to configure the load balancer to serve dual-stack traffic.

### Using the console
<a name="environments-cfg-elbv2-ipv6-dualstack.enable.console"></a>

You can use the Elastic Beanstalk console to configure dual-stack for your environment's load balancer.

**Note**  
This configuration depends on the timing of data propagation at several points. Consider the following timing requirements when you configure your load balancer and test the changes.  
*VPC configuration time.* After you complete the VPC configuration described in [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs), wait several minutes for the changes to propagate before you follow these procedures. If you encounter VPC or subnet configuration errors during dual-stack setup, wait a few minutes and try the configuration steps again.  
*DNS propagation time.* After you set the `IpAddressType` option to *dualstack*, wait several minutes for the changes to propagate before you test. Route 53 DNS propagation can take 1–2 minutes to complete. During this time, you might experience issues when testing communication from a client to your application if you're initiating requests using the IPv6 protocol.

**Creating new environment: To configure your load balancer for dual-stack support**

1. Launch the Elastic Beanstalk console and begin the steps to create a new environment. After you set the required fields **Service role** and **EC2 instance profile** in the **Configure service access** page, continue with the steps in this procedure to set your load balancer to dual-stack configuration. For more information to get started, see [Creating an Elastic Beanstalk environment](using-features.environments.md). 

1. From **Configure service access** select **Next**.

1. The **Set up networking, database, and tags** page displays. 

   If you completed the [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs) described in the previous section, then you've already set up the required VPC and subnets. In this case, skip this step along with its sub-steps to move on to select the VPC.

   1. To configure the VPC and subnets you can select **Create VPC** to navigate to the VPC console. Follow the steps in [Complete VPC prerequisites using the console](#environments-cfg-elbv2-ipv6-dualstack.prereqs.console).

   1.  Allow several minutes for the VPC updates to propagate, then return to the Elastic Beanstalk console and select refresh to continue with the next step. 

       If you encounter VPC or subnet configuration errors in the remaining steps, wait a few minutes to allow time for the VPC configuration to propagate and try the steps again. 

1. On the **Set up networking, database, and tags** page select a value from the **VPC** dropdown that has an associated IPv6 CIDR block. 

   After you select a VPC the **Instance subnets** will populate with the VPC subnets.

1. Select one or more **Instance subnets**, then select **Next**.

1. The **Configure instance traffic and scaling** page displays. 

   In **Load balancer network settings** select **Enable** for **Dualstack (IPv4 & IPv6).**

1. Select the **Load balancer type**. Both **Application load balancer** or **Network load balancer** support *dualstack*.

1. You can continue to configure other load balancer options on the current console page. For more information about load balancer options and configuration, see the other topics in this chapter.

1. Continue with the steps to complete the configuration and creation of your environment. For more information, see [Creating an Elastic Beanstalk environment](using-features.environments.md).



**Existing environment: To configure your load balancer for dual-stack support**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Network and database** configuration category, choose **Edit**.

1. If you completed the [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs) described in the previous section, then you've already set up the required VPC and subnets. In this case, skip this step along with its sub-steps to move on to select the VPC.

   1. To configure the VPC and subnets you can select **Create VPC** to navigate to the VPC console. Follow the steps in [Complete VPC prerequisites using the console](#environments-cfg-elbv2-ipv6-dualstack.prereqs.console).

   1.  Allow several minutes for the VPC updates to propagate, then return to the Elastic Beanstalk console and select refresh to continue with the next step. 

       If you encounter VPC or subnet configuration errors in the remaining steps, wait a few minutes to allow time for the VPC configuration to propagate and try the steps again. 

1. In the **Network and database** page select a value from the **VPC** dropdown that has an associated IPv6 CIDR block. 

   After you select a VPC the **Instance subnets** will populate with the VPC subnets.

1. Select one or more **Instance subnets**.

1. To save the changes choose **Apply** at the bottom of the page.

1. In the **Instance traffic and scaling** configuration category, choose **Edit**.

1. In **Load balancer network settings** select to **Enable** for **Dualstack (IPv4 & IPv6).**

1. To save the changes choose **Apply** at the bottom of the page.

### Using the AWS CLI
<a name="environments-cfg-elbv2-ipv6-dualstack.enable.cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to configure your environment's load balancers to serve both IPv6 and IPv4 network traffic. This section provides examples of the [create-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-environment.html) and [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) commands with the [aws:elbv2:loadbalancer](command-options-general.md#command-options-general-elbv2) namespace.

**Note**  
This configuration depends on the timing of data propagation at several points. Consider the following timing requirements when you configure your load balancer and test the changes.  
*VPC configuration time.* After you complete the VPC configuration described in [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs), wait several minutes for the changes to propagate before you run these commands to configure your load balancer for dual-stack. If you encounter VPC or subnet configuration errors during dual-stack setup, wait a few minutes and try the commands again.  
*DNS propagation time.* After you set the `IpAddressType` option to *dualstack*, wait several minutes for the changes to propagate before you test. Route 53 DNS propagation can take 1–2 minutes to complete. During this time, you might experience issues when testing communication from a client to your application if you're initiating requests using the IPv6 protocol.

 

**Example of create-environment with dualstack configuration (namespace options inline)**  

```
aws elasticbeanstalk create-environment \
--region {{us-east-1}} \
--application-name {{my-app}} \
--environment-name {{my-env}} \
--solution-stack-name {{"64bit Amazon Linux 2 v3.4.0 running Python 3.8"}} \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=aws-elasticbeanstalk-ec2-role \
Namespace=aws:elbv2:loadbalancer,OptionName=IpAddressType,Value={{dualstack}}
```



As an alternative, use an `options.json` file to specify the namespace options instead of including them inline. The following example command demonstrates the [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) command.

**Example of update-environment with dualstack configuration (namespace options in `options.json` file)**  

```
aws elasticbeanstalk update-environment \
--region {{us-east-1}} \
--application-name {{my-app}} \
--environment-name {{my-env}} \
--solution-stack-name {{"64bit Amazon Linux 2 v3.4.0 running Python 3.8"}} \
--option-settings \ file://options.json
```

**Example**  

```
### example options.json ###
[
  {
    "Namespace": "aws:elbv2:loadbalancer",
    "OptionName": "IpAddressType",
    "Value": "{{dualstack}}"
  }
]
```



The following example updates an existing environment to set the `IpAddressType` option to *IPv4*.

**Note**  
This example `update-environment` command is useful if you need to roll back your environment configuration from dual-stack to IPv4.

**Example of update-environment to set IpAddressType to IPv4**  

```
aws elasticbeanstalk update-environment \
--region {{us-east-1}} \
--application-name {{my-app}} \
--environment-name {{my-env}} \
--solution-stack-name {{"64bit Amazon Linux 2 v3.4.0 running Python 3.8"}} \
--option-settings \
Namespace=aws:elbv2:loadbalancer,OptionName=IpAddressType,Value={{ipv4}}
```

### Using .ebextensions configuration files
<a name="environments-cfg-elbv2-ipv6-dualstack.enable.ebx"></a>

You can use Elastic Beanstalk [configuration files](ebextensions.md) to enable your environment's load balancers to serve both IPv6 and IPv4 network traffic. Set the `IpAddressType` option in the [aws:elbv2:loadbalancer](command-options-general.md#command-options-general-elbv2) namespace to *dualstack*.

**Note**  
This configuration depends on the timing of data propagation at several points. Consider the following timing requirements when you configure your load balancer and test the changes.  
*VPC configuration time.* After completing the VPC configuration described in [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs), allow several minutes for the VPC changes to propagate before applying the `.ebextensions`configurations. If you encounter VPC or subnet configuration errors during this configuration setup wait a few minutes and try again.  
*DNS propagation time.* After you set the `IpAddressType` option to *dualstack*, wait several minutes for the changes to propagate before you test. Route 53 DNS propagation can take 1–2 minutes to complete. During this time, you might experience issues when testing communication from a client to your application if you're initiating requests using the IPv6 protocol.

**Example .ebextensions/options.config for load balancer dualstack configuration ([shorthand syntax](ebextensions-optionsettings.md#ebextensions-optionsettings.title))**  

```
option_settings:
  aws:elbv2:loadbalancer:
    IpAddressType: {{dualstack}}
```

**Example .ebextensions/options.config for load balancer dualstack configuration ([standard syntax](ebextensions-optionsettings.md#ebextensions-optionsettings.title))**  

```
option_settings:
  - namespace: aws:elbv2:loadbalancer
    option_name: IpAddressType
    value: {{dualstack}}
```

### Using the AWS SDK
<a name="environments-cfg-elbv2-ipv6-dualstack.enable.sdk"></a>

You can configure dual-stack using the [AWS SDKs](https://docs.aws.amazon.com/code-library/). Similar to the `update-environment` and `create-environment` AWS CLI commands mentioned in the previous section, you can use the [CreateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html) and [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) API actions. Use the `OptionSettings` request parameter to specify the options of the [aws:elbv2:loadbalancer](command-options-general.md#command-options-general-elbv2) namespace.

**Note**  
This configuration depends on the timing of data propagation at several points. Consider the following timing requirements when you configure your load balancer and test the changes.  
*VPC configuration time.* After you complete the VPC configuration described in [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs), allow several minutes for the changes to propagate before you run your programs to configure the load balancer for dual-stack. If you encounter VPC or subnet configuration errors during dual-stack setup, wait a few minutes and try running the programs for dual-stack configuration again.  
*DNS propagation time.* After you set the `IpAddressType` option to *dualstack*, wait several minutes for the changes to propagate before you test. Route 53 DNS propagation can take 1–2 minutes to complete. During this time, you might experience issues when testing communication from a client to your application if you're initiating requests using the IPv6 protocol.

## Troubleshooting
<a name="environments-cfg-elbv2-ipv6-dualstack.troubleshooting"></a>

**Try Amazon Q Developer CLI for AI-assisted troubleshooting**  
 Amazon Q Developer CLI can help you troubleshoot environment issues quickly. The Q CLI provides solutions by checking environment status, reviewing events, analyzing logs, and asking clarifying questions. For more information and detailed walkthroughs, see [Troubleshooting Elastic Beanstalk Environments with Amazon Q Developer CLI ](https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/) in the AWS blogs.

This section provides guidance for troubleshooting issues with your load balancer dual-stack configuration.

**Event:** *VPC {{vpc\_id}} does not have IPv6 CIDR blocks configured. IPv6 CIDR blocks are required for dualstack load balancer. Please associate an IPv6 CIDR block with your VPC before using dualstack mode.*

Your VPC and all of the subnets must have IPv6 CIDR blocks associated with them. This is one of the VPC prerequisites that you must complete before configuring your load balancer for dualstack support. For more information to complete this task see [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs) earlier in this topic.

 **Event:** *One or more subnets for VPC {{vpc\_id}} do not have IPv6 CIDR blocks configured. IPv6 CIDR blocks are required for the subnets used with dualstack load balancer. Please associate IPv6 CIDR blocks with all required subnets before using dualstack mode.* 

All of the subnets for your VPC must have IPv6 CIDR blocks associated with them. This is one of the VPC prerequisites that you must complete before configuring your load balancer for dualstack support. For more information to complete this task see [Amazon VPC prerequisites](#environments-cfg-elbv2-ipv6-dualstack.prereqs) earlier in this topic.

 **Error:** *The `IpAddressType` option can only be applied on Elastic Beanstalk environments configured with an Application Load Balancer or Network Load Balancer.* 

This message indicates that your Elastic Beanstalk environment may be a single instance environment or that it may be using a Classic Load Balancer. Only environments configured with an Application Load Balancer or Network Load Balancer can configure `IpAddressType`.