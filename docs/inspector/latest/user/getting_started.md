# Getting started with Amazon Inspector

This section provides information to consider before activating Amazon Inspector and a getting started tutorial describing how to activate Amazon Inspector and view your [findings](findings-understanding.md "findings-understanding.md") in the Amazon Inspector console and with the Amazon Inspector API.

###### Topics

- [Before activating Amazon Inspector](#tutorial_before "#tutorial_before")
- [Getting started tutorial: Activating Amazon Inspector](getting_started_tutorial.md "getting_started_tutorial.md")

## Before activating Amazon Inspector

Before activating Amazon Inspector, consider the following:

###### Amazon Inspector is a Regional service

Your data is stored in the AWS Region where you activate Amazon Inspector.
Repeat the steps in the first part of the [getting started tutorial](getting_started_tutorial.md#getting-started-tutorial "getting_started_tutorial.md#getting-started-tutorial") for all AWS Regions where you plan to use Amazon Inspector.

###### Amazon Inspector creates the service-linked roles AWSServiceRoleForAmazonInspector2 and AWSServiceRoleForAmazonInspector2Agentless

A [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is a role in AWS Identity and Access Management (IAM) that's linked to an AWS servce.
[AWSServiceRoleForAmazonInspector2](../../../aws-managed-policy/latest/reference/AmazonInspector2AgentlessServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonInspector2AgentlessServiceRolePolicy.md") and [AWSServiceRoleForAmazonInspector2Agentless](../../../aws-managed-policy/latest/reference/AmazonInspector2ServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonInspector2ServiceRolePolicy.md") allow Amazon Inspector to access AWS services required to perform security assessments.

###### IAM identities with administrator permissions can enable Amazon Inspector

Protect your credentials by creating users with [IAM](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") or [AWS IAM Identity Center](../../../singlesignon/latest/userguide/users-groups-provisioning.md "../../../singlesignon/latest/userguide/users-groups-provisioning.md").
This helps you make sure users only have the permissions required to manage Amazon Inspector.
For more information, see [AWS managed policy: AmazonInspectorFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2FullAccess").

###### Hybrid scanning is automatically enabled

Hybrid scanning includes [agent-based scanning](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") and [agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless").
By default, Amazon Inspector uses these scan methods on all eligible Amazon EC2 instances.
For more information, see [Scanning Amazon EC2 instances with Amazon Inspector](scanning-ec2.md "scanning-ec2.md").

###### Amazon ECR scanning and Lambda function scanning doesn't require the SSM agent

Agent-based scanning uses [the SSM agent](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") to collect software inventory.
Agentless scanning uses Amazon EBS snapshots to collect software inverntory.

###### Note

By default, the SSM agent is already installed in Amazon EC2 instances based on Amazon Machine Images.
However, you might need to activate the SSM agent manually in some cases.
For more information, see [Working with the SSM agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the _AWS Systems Manager User Guide_.

###### Monthly costs are based on workloads scanned

For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/ "https://aws.amazon.com/inspector/pricing/").
