# Solution deployment guide example

As a partner who is building a solution using Amazon WorkSpaces Core, it's your responsibility to
document how your customers can deploy your solution to their environments. We recommend that you
create a deployment guide, with the following suggested table of contents. Some topics might not
be relevant to your solution, so revise the topics as necessary.

It’s also a good practice to link to other AWS documentation where relevant. For example,
refer your customers to the [Amazon WorkSpaces Administration Guide](../../../workspaces/latest/adminguide/amazon-workspaces.md "../../../workspaces/latest/adminguide/amazon-workspaces.md")
for sections related to Bring Your Own License (BYOL) image import, directory setup, and virtual
private cloud (VPC) setup. Specific details of your deployment guide and steps will vary,
depending on the level of integration of your solution with the WorkSpaces API, and what steps
customers must take manually using the AWS Management Console or AWS Command Line Interface.

As a partner, you're responsible for hosting and publishing the deployment guides on your
website. Amazon WorkSpaces Core can link to these guides from the **WorkSpaces Core Partners**
section at [Amazon WorkSpaces Core](https://aws.amazon.com/workspaces/core/ "https://aws.amazon.com/workspaces/core/"), where customers can
easily find them.

Following is a suggested table of contents for an Amazon WorkSpaces Core solution deployment guide:

- Chapter 1: Introduction
- Chapter 2: Getting started
  - Overview
  - Setting up security groups
  - Configuring the directory services security group
  - Configuring a VPC

- Chapter 3: Installing <your service> in Amazon EC2
  - Required AWS permissions
  - Launching a connection broker instance
  - Upgrading the <your service> connection broker
  - Lauching a <your service> gateway instance
  - Obtaining your <your service> license

- Chapter 4: Preparing WorkSpaces Core images
- Chapter 5: Integrating with your AWS infrastructure
  - Connecting to your Amazon diretory services
  - Connecting to your Amazon WorkSpaces account
  - Attaching the <your service> gateway to a connection broker

- Chapter 6: Launching new workspaces
  - Loading users
  - Deploying new workspaces

- Chapter 7: Connecting users to WorkSpaces
  - Amazon WorkSpaces pools
  - Protocol plans
  - Power control plans
  - Release plans
  - Building user policies
  - Assigning policies to users
  - Testing your connection broker configuration
  - Connecting to WorkSpaces
