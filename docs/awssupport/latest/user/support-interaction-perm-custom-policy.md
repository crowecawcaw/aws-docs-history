

# Option 2: Create a custom policy with minimum required permissions
<a name="support-interaction-perm-custom-policy"></a>

You can explicitly allow-list specific actions instead of using wildcards. The following are the required permissions for support interactions, case creation, and case management:

```
                
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "support:AddAttachmentsToSet",
        "support:AddCommunicationToCase",
        "support:CreateCase",
        "support:DescribeAttachment",
        "support:DescribeCaseAttributes",
        "support:DescribeCases",
        "support:DescribeCommunication",
        "support:DescribeCommunications",
        "support:DescribeCreateCaseOptions",
        "support:DescribeIssueTypes",
        "support:DescribeServices",
        "support:DescribeSeverityLevels",
        "support:DescribeSupportedLanguages",
        "support:DescribeSupportLevel",
        "support:GetInteraction",
        "support:InitiateCallForCase",
        "support:ListInteractionEntries",
        "support:ListInteractions",
        "support:InitiateChatForCase",
        "support:PutCaseAttributes",
        "support:ResolveCase",
        "support:ResolveInteraction",
        "support:SearchForCases",
        "support:StartInteraction",
        "support:UpdateInteraction",
        "support-console:GetAccountState",
        "support-console:GetAccountGovCloudEnabled",
        "support-console:GetCaseDraft",
        "support-console:CreateCaseDraft",
        "support-console:DeleteCaseDraft",
        "support-console:GetBanner",
        "support-console:DescribeDynamicHelp",
        "support-console:CreateContact"
      ],
      "Resource": "*"
    }
  ]
}
```

For AWS DevOps Agent permissions required by your IAM identity, attach the following AWS managed policies:
+ `AIDevOpsAgentFullAccess`. Provides full access to DevOps Agent management actions.
+ `AIDevOpsAgentAccessPolicy`. Required to create the agent space.
+ `AIDevOpsOperatorAppAccessPolicy`. Required to enable Operator App access.

For the full list of actions, see [DevOps Agent IAM permissions](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html) in the *AWS DevOps Agent User Guide*.

Your IAM identity needs `iam:PassRole` on the `DevOpsAgentRole-AgentSpace` and `DevOpsAgentRole-WebappAdmin` roles so that the Support Center Console can pass these roles to DevOps Agent when creating them on your behalf during first-time setup. For investigations on Amazon Elastic Kubernetes Service clusters, your IAM identity also needs `eks:DescribeAccessEntry`, `eks:CreateAccessEntry`, and `eks:AssociateAccessPolicy` so that the Support Center Console can create the read-only access entry on the target cluster. For more information about access entries, see [Grant IAM users access to Kubernetes with Amazon EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon Elastic Kubernetes Service User Guide*.

**Note**  
Using a custom policy requires ongoing maintenance as AWS Support releases new features. For more information about the Support Center Console API operations, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md). For more information about each of the Support API operations, see [Manage access to AWS Support Center](accessing-support.md).