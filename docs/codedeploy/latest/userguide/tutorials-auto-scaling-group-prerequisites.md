# Prerequisites

To follow along in this tutorial:

- Complete all of the steps in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"), including setting up and
  configuring the AWS CLI and creating an IAM instance profile
  (`CodeDeployDemo-EC2-Instance-Profile`) and a service
  role (`CodeDeployDemo`). A
  _service role_ is a special type of IAM role that gives
  a service permission to act on your behalf.
- If you create your Amazon EC2 Auto Scaling group with a launch template, you must add the
  following permissions:

      + `ec2:RunInstances`
      + `ec2:CreateTags`
      + `iam:PassRole`

  For more information, see [Step 2: Create a service
  role](getting-started-create-service-role.md "getting-started-create-service-role.md"), [Creating a
  launch template for an Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/create-launch-template.md "../../../autoscaling/ec2/userguide/create-launch-template.md"), and [Launch template support](../../../autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.md") in the _Amazon EC2 Auto Scaling User Guide_.

- Create and use a revision that is compatible with an Ubuntu Server instance and
  CodeDeploy. For your revision, you can do one of the following:
  - Create and use the sample revision in [Step 2: Create
    a sample application revision](tutorials-on-premises-instance-2-create-sample-revision.md "tutorials-on-premises-instance-2-create-sample-revision.md") in the [Tutorial: Deploy an application to an
    on-premises instance with CodeDeploy (Windows Server, Ubuntu Server, or Red Hat Enterprise Linux)](tutorials-on-premises-instance.md "tutorials-on-premises-instance.md") tutorial.
  - Create a revision on your own, see [Working with application revisions for CodeDeploy](application-revisions.md "application-revisions.md").

- Create a Security Group named `CodeDeployDemo-AS-SG` with
  the following **Inbound rule**:

      + Type: HTTP
      + Source: Anywhere

  This is required to view your application and verify deployment success. For
  information on how to create a Security Group, see [Creating a security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group") in the _Amazon EC2 user
  guide_.
