# Get started tutorial

This tutorial walks you through the process of setting up and configuring VPC Route
Server to enable dynamic routing in your VPC. You'll learn how to create and configure
all the necessary components, establish BGP peering, and verify proper operation. The
tutorial covers everything from initial IAM setup through testing and cleanup.

Before beginning this tutorial, ensure you have:

- Administrative access to your AWS account
- A VPC with at least two subnets where you want to enable dynamic
  routing
- Network devices (like firewalls running on EC2 instances) that support BGP
  and can serve as route server peer devices
- Basic familiarity with BGP concepts and AWS networking
  The steps can be completed using either the AWS Management Console or AWS CLI. Both methods are provided for each step.

Estimated time to complete: 15-30 minutes

###### Steps

- [Step 1: Configure required IAM Role permissions](route-server-iam.md "route-server-iam.md")
- [Step 2: Create a route server](route-server-tutorial-create.md "route-server-tutorial-create.md")
- [Step 3: Associate route server with a VPC](route-server-tutorial-associate.md "route-server-tutorial-associate.md")
- [Step 4: Create route server endpoints](route-server-tutorial-create-endpoints.md "route-server-tutorial-create-endpoints.md")
- [Step 5: Enable route server propagation](route-server-tutorial-enable-prop.md "route-server-tutorial-enable-prop.md")
- [Step 6: Create route server peer](route-server-tutorial-create-peer.md "route-server-tutorial-create-peer.md")
- [Step 7: Initiate BGP sessions from the devices](route-server-tutorial-initiate-bgp.md "route-server-tutorial-initiate-bgp.md")
- [Step 8: Cleanup](route-server-tutorial-cleanup.md "route-server-tutorial-cleanup.md")
  The Amazon VPC Route Server tutorial is complete.
