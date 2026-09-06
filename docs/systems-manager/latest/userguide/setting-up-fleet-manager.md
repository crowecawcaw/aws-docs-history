

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up Fleet Manager
<a name="setting-up-fleet-manager"></a>

Before users in your AWS account can use Fleet Manager to monitor and manage your managed nodes, they must be granted the necessary permissions. In addition, any Amazon Elastic Compute Cloud (Amazon EC2) instances; AWS IoT Greengrass core devices; and on-premises servers, edge devices, and virtual machines (VMs) to be monitored and managed using Fleet Manager must be Systems Manager* managed nodes*. A managed node is any machine configured for use with Systems Manager in [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environments.

This means your nodes must meet certain prerequisites and be configured with the AWS Systems Manager Agent (SSM Agent).

Depending on the machine type, refer to one of the following topics to make sure your machines meet the requirements for managed nodes.
+ Amazon EC2 instances: [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md)
**Tip**  
You can also use Quick Setup to help you quickly configure your Amazon EC2 instances as managed instances in an individual account. If your business or organization uses AWS Organizations, you can also configure instances across multiple organizational units (OUs) and AWS Regions. For more information about using Quick Setup to configure managed instances, see [Set up Amazon EC2 host management using Quick Setup](quick-setup-host-management.md).
+ On-premises and other server types in the cloud: [Managing nodes in hybrid and multicloud environments with Systems Manager](systems-manager-hybrid-multicloud.md)
+ AWS IoT Greengrass (edge) devices: [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md)

**Topics**
+ [Controlling access to Fleet Manager](configuring-fleet-manager-permissions.md)