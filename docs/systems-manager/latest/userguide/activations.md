

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS Systems Manager Hybrid Activations
<a name="activations"></a>

To configure non-EC2 machines for use with AWS Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environment, you create a *hybrid activation*. Non-EC2 machine types supported as managed nodes include the following:
+ Servers on your own premises (on-premises servers)
+ AWS IoT Greengrass core devices
+ AWS IoT and non-AWS edge devices
+ Virtual machines (VMs), including VMs in other cloud environments

When you run the [create-activation](https://docs.aws.amazon.com/cli/latest/reference/ssm/create-activation.html) command to start a hybrid activation process, you receive an activation code and ID in the command response. You then include the activation code and ID with the command to install SSM Agent on the machine, as described in step 3 of [Install SSM Agent on hybrid Linux nodes](hybrid-multicloud-ssm-agent-install-linux.md) and step 4 of [Install SSM Agent on hybrid Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md).

This activation process applies to all non-EC2 machine types *except* AWS IoT Greengrass core devices. For information about configuring AWS IoT Greengrass core devices for Systems Manager, see [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md).

**Note**  
Support isn't currently provided for non-EC2 macOS machines.

**Note**  
**Important:** Effective June 30, 2026, the advanced-instances tier has been removed. There is no longer a 1,000-instance limit for hybrid managed nodes, and you no longer need to enable a paid tier to use Session Manager on non-EC2 machines. Instead, starting September 30, 2026, Session Manager and Run Command use pay-as-you-go pricing when used on hybrid managed nodes.  
For more information about pricing, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).