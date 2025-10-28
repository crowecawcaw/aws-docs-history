# Define security groups to control EMR Studio

network traffic

## About the EMR Studio security

groups

Amazon EMR Studio uses two security groups to control network traffic between
Workspaces in the Studio and an attached Amazon EMR cluster running on
Amazon EC2:

- An **engine security group** that uses port 18888 to
  communicate with an attached Amazon EMR cluster running on Amazon EC2.
- A **Workspace security group** associated with
  the Workspaces in a Studio. This security group includes an outbound
  HTTPS rule to allow the Workspace to route traffic to the internet and must
  allow outbound traffic to the internet on port 443 to enable linking Git repositories to
  a Workspace.

EMR Studio uses these security groups in addition to any security groups associated
with an EMR cluster attached to a Workspace.

You must create these security groups when you use the AWS CLI to create a Studio.

###### Note

You can customize the security groups for EMR Studio with rules tailored to your
environment, but you must include the rules noted on this page. Your Workspace
security group can't allow any inbound traffic, and the engine security group must allow
inbound traffic from the Workspace security group.

**Use the Default EMR Studio Security Groups**

When you use the Amazon EMR console, you can choose the following default security groups.
The default security groups are created by EMR Studio on your behalf, and include the
minimum required inbound and outbound rules for Workspaces in an EMR Studio.

- `DefaultEngineSecurityGroup`
- `DefaultWorkspaceSecurityGroupGit` or
  `DefaultWorkspaceSecurityGroupWithoutGit`

## Prerequisites

To create the security groups for EMR Studio, you need an Amazon Virtual Private Cloud (VPC) for the
Studio. You choose this VPC when you create the security groups. This should be the
same VPC that you specify when you create the Studio. If you plan to use Amazon
Amazon EMR on EKS with EMR Studio, choose the VPC for your Amazon EKS cluster worker
nodes.

## Instructions

Follow the instructions in [Creating a security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group") in the _Amazon EC2 User Guide for
Linux Instances_ to create an engine security group and a Workspace
security group in your VPC. The security groups must include the rules summarized in the
following tables.

When you create security groups for EMR Studio, note the IDs for both. You specify
each security group by ID when you create a Studio.

**Engine security group**

EMR Studio uses port 18888 to communicate with an attached cluster.

| Inbound rules | Type | Protocol | Port                                      | Destination                                                                           | Description                                                                                                         |
| ------------- | ---- | -------- | ----------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---- | -------- | ---- | ----------- | ----------- |
| TCP           | TCP  | 18888    | Your EMR Studio Workspace security group. | Allow traffic from any resources in the Workspace security group for EMR Studio.      | **Workspace security group** This security group is associated with the Workspaces in an EMR Studio. Outbound rules | Type | Protocol | Port | Destination | Description |
| ---           | ---  | ---      | ---                                       | ---                                                                                   |
| TCP           | TCP  | 18888    | Your EMR Studio engine security group.    | Allow traffic to any resources in the Engine security group for EMR Studio.           |
| HTTPS         | TCP  | 443      | 0.0.0.0/0                                 | Allow traffic to the internet to link publicly hosted Git repositories to Workspaces. |
