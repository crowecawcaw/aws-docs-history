

# iam-policy-no-statements-with-full-access
<a name="iam-policy-no-statements-with-full-access"></a>

Checks if AWS Identity and Access Management (IAM) policies that you create grant permissions to all actions on individual AWS resources. The rule is NON\_COMPLIANT if any customer managed IAM policy allows full access to at least 1 AWS service. 

**Context**: Following the principle of least privilege, it is recommended to limit the permitted actions in your IAM policies when granting permissions to AWS services. This approach helps ensure that you only grant the necessary permissions by specifying the exact actions required, avoiding the use of unrestricted wildcards for a service, such as `ec2:*`.

In some cases, you might want to permit multiple actions with a similar prefix, such as [DescribeFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html) and [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html). In these cases, you can add a suffixed wildcard to the common prefix (for example, `ec2:Describe*`). Grouping related actions can help avoid hitting [IAM policy size limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html).

This rule will return COMPLIANT if you use prefixed actions with a suffixed wildcard (for example, `ec2:Describe*`). This rule will only return NON\_COMPLIANT if you use unrestricted wildcards (for example, `ec2:*`).

**Note**  
This rule only evaluates customer managed policies. This rule does NOT evaluate inline policies or AWS managed policies. For more information on the difference, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.



**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_FULL\_ACCESS

**Resource Types:** AWS::IAM::Policy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

excludePermissionBoundaryPolicy (Optional)Type: boolean  
Boolean flag to exclude the evaluation of IAM policies used as permissions boundaries. If set to 'true', the rule will not include permissions boundaries in the evaluation. Otherwise, all IAM policies in scope are evaluated when value is set to 'false.' Default value is 'false'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d939c27"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).