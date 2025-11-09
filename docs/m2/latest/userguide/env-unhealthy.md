AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Troubleshooting error: Environment unhealthy

This page describes how you can resolve your error when you receive a notification that one
of your AWS Mainframe Modernization environments are unhealthy.

- Engine: AWS Blu Age and Rocket Software (formerly Micro Focus)
- Component: environments
  If you receive a notification that says one of your AWS Mainframe Modernization environments has become unhealthy,
  this applies to you. You are notified through one of these sources:

- The unhealthy environment status is shown in your AWS Mainframe Modernization console.
- Email notification about the unhealthy environment status from AWS Health.
- You see a related event from AWS Mainframe Modernization in your AWS Health dashboard, under **Your account health**.

## Common cause

The error occurs when the resources in your AWS account associated with the AWS Mainframe Modernization
environment is inaccessible. A common reason for this issue is that the resources related to the
environment are being modified or deleted.

## Resolution

For specific guidance, use the error code provided in the email from **AWS Health**, or through your **AWS Mainframe Modernization console**.

Error code:

- **`Storage unreachable`**

This error indicates that the attached storage (Amazon Elastic File System or Amazon FSx file systems) for
the environment has failed to mount correctly. To check details about unhealthy environment,
complete the following steps:

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/").
2. Select the unhealthy environment, and choose **Configuration**.
3. Choose **Attached Storage** to view the storage resources
   associated with this environment.
4. Check the network-related configurations, such as the security group, subnet, and Amazon VPC
   associated with the storage. If these configurations are incorrect, try to restore them to
   solve this issue.

###### Note

If the storage has been deleted, the environment can't be recovered. In this case,
you should consider deleting the unhealthy environment.
