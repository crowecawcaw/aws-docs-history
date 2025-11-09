AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Troubleshooting error: Cannot access an application URL

This page describes how you can resolve your error when you can't access URL for a running
AWS Mainframe Modernization application.

- Engine: AWS Blu Age and Rocket Software (formerly Micro Focus)
- Component: applications
  If you can't access the URL for a running AWS Mainframe Modernization application that you created and deployed to
  an AWS Mainframe Modernization runtime environment, you might need to configure the inbound rules on the security group
  that you associated with the runtime environment.

## Common cause

When you create a runtime environment, the security group you provide, including the
default security group, must have inbound rules configured to allow traffic to the deployed
applications from outside the VPC, if you want to allow this type of access.

## Resolution

Check whether the Amazon VPC security group associated with the runtime environment allows
traffic to the environment on the appropriate application ports. To check the security group
rules, complete the following steps:

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/").
2. In the left navigation, choose **Environments**.
3. Choose the runtime environment that hosts the application you want to connect to.
4. Choose **Configurations**.
5. In **Security & Network**, choose the security group. The link opens
   the details of the security group in the Amazon VPC console.
6. If necessary, choose **Edit inbound rules** and add the following rule if not already present:

Type
Custom TCP

Port

8196 or the port that matches the listener properties specified in the application definition.
For more information, see [Step 2: Create the application definition](tutorial-runtime-ba.md#tutorial-runtime-ba-step2 "tutorial-runtime-ba.md#tutorial-runtime-ba-step2").

Source

The IP address from where you are calling the application.
You can choose **myIP** from the dropdown.
If you still have timeout issues, try choosing **Anywhere IPV4** or **Anywhere IPV6**.
Make sure to stop the application and start it again after you add the inbound rule on the security group.

For more information, see [Work
with security group rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-group-rules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-group-rules") in _Amazon VPC User Guide_.
