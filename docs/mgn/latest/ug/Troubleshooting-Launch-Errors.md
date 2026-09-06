

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Troubleshooting launch errors
<a name="Troubleshooting-Launch-Errors"></a>

Use the information in this section to troubleshoot launch errors.

**Topics**
+ [Do I need to recreate the entire launch template for every version?](#Solving-Communication-Problems1)
+ [Error - AccessDeniedException - Must be admin user](#error-admin-user)
+ [VPCIdNotSpecified error](#Troubleshooting-vpc-error)
+ [Error: Failed to connect using HTTP channel](#Error-Failed-to-connect-using-HTTP-channel)
+ [Could not take up-to-date snapshot. Launching from snapshot taken on...](#up-to-date-snapshot)

## Do I need to recreate the entire launch template for every version?
<a name="Solving-Communication-Problems1"></a>

 When you save a new template version, it is tagged as the latest version. However, for a multitude of reasons, AWS Transform MGN uses the version marked as the default for its purposes. So to actually have MGN recognize the changes you make, you need to go into the template itself, and change the default version to the version you have just updated.

1. Create the new template version.

1. Select the launch template in the success message, and then select **Actions** and choose **Set default version**.

1. From the drop down menu select the latest version, and then choose **Set as default version**.

## Error - AccessDeniedException - Must be admin user
<a name="error-admin-user"></a>

If you receive an AccessDeniedException error when attempting to log into AWS Transform MGN for the first time and set up your replication settings template, it means that you are not the administrator of your AWS Account and therefore cannot initialize MGN. You must be the Admin user of your AWS Account to initialize MGN. [Learn more about initializing MGN.](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html) 

## VPCIdNotSpecified error
<a name="Troubleshooting-vpc-error"></a>

The EC2 launch template does not automatically set a specific Subnet. As such, EC2 will attempt to launch in a Subnet within the default VPC. If you have removed your default VPC, EC2 will fail to launch any instance for which there is no valid Subnet specified. Ensure that you specify a subnet if that is the case, or AWS Transform MGN instance launch will fail. You may see the VPCIdNotSpecified error if: 
+ A default subnet/VPC is not selected in the EC2 launch template.
+ An incorrect target subnet is specified in the EC2 launch template.
+ the EC2 launch template with the correct subnet settings is not set as the default.

## Error: Failed to connect using HTTP channel
<a name="Error-Failed-to-connect-using-HTTP-channel"></a>

This error mostly occurs when the conversion server is unable to communicate with the necessary AWS Endpoints for [staging area communication.](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-443-Staging)
+ Check if any network changes were made in the staging area that could affect the conversion server reaching the AWS Endpoints (firewall settings, DNS settings, security group settings, route table settings, and access control list settings).
+ Test TCP Port 443 connectivity with a test instance from the staging area subnet, to the [required endpoints.](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-443-Staging)
+ If the issue persists after confirming network connectivity, [create a case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) with AWS Premium Support for further investigation.

## Could not take up-to-date snapshot. Launching from snapshot taken on...
<a name="up-to-date-snapshot"></a>

When a test or cutover instance is launched, AWS Transform MGN will attempt to create the latest consistent snapshot of the source server. MGN will wait for all the snapshots to become available and once they are ready, will proceed with the launch workflow.

 If you see a timeout message when launching a test or cutover instance, it means the snapshot creation timed out. In this case, MGN will use the latest successful snapshot for that source server to launch the instance. This ensures you can still launch an instance, but the instance will only contain data current up to the timestamp specified in the message.

To launch a test or cutover instance with the most up-to-date data, determine why the latest snapshot could not be created. Common causes include the source server not having a "Healthy" status, or backlog/lag. 

Also check the CloudTrail Event History for errors on the CreateSnapshot and DescribeSnapshot API calls, which can prevent timely EBS snapshot creation. Resolving these underlying issues will allow successful creation of up-to-date snapshots for test and cutover instances.