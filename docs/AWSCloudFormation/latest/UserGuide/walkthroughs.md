# CloudFormation walkthroughs

This documentation provides a collection of walkthroughs designed to give you hands-on
practice with stack deployments.

- [Refer to resource outputs in another CloudFormation
  stack](walkthrough-crossstackref.md "walkthrough-crossstackref.md") – This walkthrough shows you
  how to reference outputs from one CloudFormation stack within another stack. Instead of
  including all resources in a single stack, you can create related AWS resources in
  separate stacks to create more modular and reusable templates.
- [Peer with a VPC in another
  AWS account](peer-with-vpc-in-another-account.md "peer-with-vpc-in-another-account.md") – This walkthrough
  guides you through the process of creating a Virtual Private Cloud (VPC) peering
  connection between two VPCs in different AWS accounts. VPC peering helps you route
  traffic between the VPCs and access resources as if they were part of the same
  network.
- [Create a scaled and load-balanced
  application](walkthrough-autoscaling.md "walkthrough-autoscaling.md")
  – Discover how to use CloudFormation to create a scalable and load-balanced
  application. This walkthrough covers creating an Auto Scaling group, a load balancer, and
  other related resources to ensure your application can handle varying traffic loads
  and maintain high availability.
- [Deploy applications on Amazon EC2](deploying.md "deploying.md")
  – Learn how to use CloudFormation to automatically install, configure, and start
  up your application on Amazon EC2 instances. This way, you can easily duplicate
  deployments and update existing installations without connecting directly to the
  instances.
- [Updating a stack](updating.stacks.md "updating.stacks.md") – Walk through a simple
  progression of updates to a running stack with CloudFormation.
- [Perform ECS blue/green deployments through CodeDeploy using
  CloudFormation](blue-green.md "blue-green.md") – Discover how to
  use CloudFormation to perform AWS CodeDeploy blue/green deployments on Amazon ECS. Blue/green
  deployments are a way to update your applications or services with minimal
  downtime.
