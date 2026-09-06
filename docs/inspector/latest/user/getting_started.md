

# Getting started with Amazon Inspector
<a name="getting_started"></a>

 This section provides information to consider before activating Amazon Inspector and a getting started tutorial describing how to activate Amazon Inspector and view your [findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html) in the Amazon Inspector console and with the Amazon Inspector API. 

**Topics**
+ [Before activating Amazon Inspector](#tutorial_before)
+ [Getting started tutorial: Activating Amazon Inspector](getting_started_tutorial.md)

## Before activating Amazon Inspector
<a name="tutorial_before"></a>

 Before activating Amazon Inspector, consider the following: 

**Amazon Inspector is a Regional service**  
 Your data is stored in the AWS Region where you activate Amazon Inspector. Repeat the steps in the first part of the [getting started tutorial](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html#getting-started-tutorial) for all AWS Regions where you plan to use Amazon Inspector. 

**Amazon Inspector creates the service-linked roles AWSServiceRoleForAmazonInspector2 and AWSServiceRoleForAmazonInspector2Agentless**  
 A [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is a role in AWS Identity and Access Management (IAM) that's linked to an AWS servce. [AWSServiceRoleForAmazonInspector2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonInspector2AgentlessServiceRolePolicy.html) and [AWSServiceRoleForAmazonInspector2Agentless](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonInspector2ServiceRolePolicy.html) allow Amazon Inspector to access AWS services required to perform security assessments. 

**IAM identities with administrator permissions can enable Amazon Inspector**  
 Protect your credentials by creating users with [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) or [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html). This helps you make sure users only have the permissions required to manage Amazon Inspector. For more information, see [AWS managed policy: AmazonInspectorFullAccess](https://docs.aws.amazon.com/inspector/latest/user/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonInspector2FullAccess). 

**Hybrid scanning is automatically enabled**  
 Hybrid scanning includes [agent-based scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html#agent-based) and [agentless scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html#agentless). By default, Amazon Inspector uses these scan methods on all eligible Amazon EC2 instances. For more information, see [Scanning Amazon EC2 instances with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html). 

**Amazon ECR scanning and Lambda function scanning doesn't require the SSM agent**  
 Agent-based scanning uses [the SSM agent](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html#agent-based) to collect software inventory. Agentless scanning uses Amazon EBS snapshots to collect software inverntory. 

**Note**  
 By default, the SSM agent is already installed in Amazon EC2 instances based on Amazon Machine Images. However, you might need to activate the SSM agent manually in some cases. For more information, see [Working with the SSM agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) in the *AWS Systems Manager User Guide*. 

**Monthly costs are based on workloads scanned**  
 For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/). 

**Multi-account enablement with AWS Organizations**  
 For organizations using [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), Amazon Inspector supports both delegated administrator management and organization policy-based enablement. Organization policies provide centralized governance with automatic enablement for new accounts. For detailed instructions on both approaches, see [Getting started tutorial: Activating Amazon Inspector](getting_started_tutorial.md). 