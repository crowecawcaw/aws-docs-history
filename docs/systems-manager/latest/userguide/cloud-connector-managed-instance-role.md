

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Managed instance role
<a name="cloud-connector-managed-instance-role"></a>

The managed instance role is the IAM role that SSM Agent assumes on each Azure virtual machine after it's installed and registered. The role grants the agent the permissions it needs to call the Systems Manager service from the VM. Unlike the other three roles, this is not created on your behalf. You select an existing role during the connector setup wizard, or let the wizard create the recommended role `AmazonEC2RunCommandRoleForManagedInstances` with the `AmazonSSMManagedInstanceCore` AWS managed policy attached.

For information about creating this role and the policies you can attach to it, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md). Cloud Connector activations use the same role pattern as hybrid activations.