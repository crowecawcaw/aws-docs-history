NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Troubleshooting launch errors

Use the information in this section to troubleshoot launch errors.

###### Topics

- [Do I need to recreate the entire launch
  template for every version?](#Solving-Communication-Problems1 "#Solving-Communication-Problems1")
- [Error - AccessDeniedException - Must be admin user](#error-admin-user "#error-admin-user")
- [VPCIdNotSpecified error](#Troubleshooting-vpc-error "#Troubleshooting-vpc-error")
- [Error: Failed to connect using HTTP channel](#Error-Failed-to-connect-using-HTTP-channel "#Error-Failed-to-connect-using-HTTP-channel")
- [Could not take up-to-date snapshot. Launching from snapshot taken on...](#up-to-date-snapshot "#up-to-date-snapshot")

## Do I need to recreate the entire launch

template for every version?

When you save a new template version, it is tagged as the latest version. However, for a
multitude of reasons, AWS Application Migration Service (AWS MGN) uses the version marked as the default for its
purposes. So in order to actually have AWS MGN recognize the changes you make, you need to go
into the template itself, and change the default version to the version you have just
updated.

1. Create the new template version.
2. Select the launch template in the success message, and then select **Actions** and choose **Set default version**.
3. From the drop down menu select the latest version, and then choose **Set as default version**.

## Error - AccessDeniedException - Must be admin user

If you receive an AccessDeniedException error when attempting to log into AWS Application Migration Service (AWS MGN) for the first
time and set up your replication settings template, it means that you are not the administrator
of your AWS Account and therefore cannot initialize AWS MGN. You must be the Admin user of your AWS
Account to initialize AWS MGN. [Learn more about
initializing MGN.](mandatory-setup.md "mandatory-setup.md")

## VPCIdNotSpecified error

The EC2 launch template does not automatically set a specific Subnet. As such, EC2 will
attempt to launch in a Subnet within the default VPC. If you have removed your default VPC, EC2
will fail to launch any instance for which there is no valid Subnet specified. Ensure that you
specify a subnet if that is the case, or AWS Application Migration Service instance launch will fail. You may see the
VPCIdNotSpecified error if:

- A default subnet/VPC is not selected in the EC2 launch template.
- An incorrect target subnet is specified in the EC2 launch template.
- the EC2 launch template with the correct subnet settings is not set as the
  default.

## Error: Failed to connect using HTTP channel

This error mostly occurs when the conversion server is unable to communicate with the necessary AWS Endpoints for [staging area communication.](Network-Requirements.md#Communication-TCP-443-Staging "Network-Requirements.md#Communication-TCP-443-Staging")

- Check if any network changes were made in the staging area that could affect the conversion server reaching the AWS Endpoints (firewall settings, DNS settings, security group settings, route table settings, and access control list settings).
- Test TCP Port 443 connectivity with a test instance from the staging area subnet, to the [required endpoints.](Network-Requirements.md#Communication-TCP-443-Staging "Network-Requirements.md#Communication-TCP-443-Staging")
- If the issue persists after confirming network connectivity please [create a case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") with AWS Premium Support for further investigation.

## Could not take up-to-date snapshot. Launching from snapshot taken on...

When a test or cutover instance is launched, AWS Application Migration Service (AWS MGN) will attempt to create the latest consistent snapshot of the source server. AWS MGN will wait for all the snapshots to become available and once they are ready, will proceed with the launch workflow.

If you see a timeout message when launching a test or cutover instance, it means the snapshot creation timed out. In this case, AWS MGN will use the latest successful snapshot for that source server to launch the instance. This ensures you can still launch an instance, but the instance will only contain data current up to the timestamp specified in the message.

To launch a test or cutover instance with the most up-to-date data, determine why the latest snapshot could not be created. Common causes include the source server not having a "Healthy" status, or backlog/lag.

Also check the CloudTrail Event History for errors on the CreateSnapshot and DescribeSnapshot API calls, which can prevent timely EBS snapshot creation. Resolving these underlying issues will allow successful creation of up-to-date snapshots for test and cutover instances.
