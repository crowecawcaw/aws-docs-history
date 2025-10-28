# Cross-account access roles for Reachability Analyzer

When you enable trusted access for Reachability Analyzer, we use AWS CloudFormation StackSets to deploy the
IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess IAM role to all
member accounts in the organization. This role allows the management account and delegated
administrator accounts to specify resources from member accounts in path analyses.

Reachability Analyzer creates the custom IAM role automatically when you turn on trusted access using
the Network Manager console. We strongly recommend that you use the console to turn on trusted access, as
alternate approaches require an advanced level of expertise and are more prone to
error.

Deregistering a delegated administrator removes it from the account list so that
it can no longer assume this custom IAM role. If you turn off trusted access, we
delete the StackSets.

## IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess

This IAM policy role enables cross-account read-only access to resources
through role switching. For more information, see
[AmazonEC2ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess") and
[AWSDirectConnectReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess") in the IAM console.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables Console Access role
Resources:
  ConsoleRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Principal:
            AWS:
            - arn:aws:iam::`management-account-id`:root
            - arn:aws:iam::`delegated-admin-1-account-id`:root
            - arn:aws:iam::`delegated-admin-2-account-id`:root
          Action:
          - sts:AssumeRole
      Path: "/"
      ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess
      - arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
      - arn:aws:iam::aws:policy/AmazonVPCReachabilityAnalyzerPathComponentReadPolicy
```

## Manage IAM role deployments

If you make changes to your role policies, or if you've updated a self-managed
role, you can deploy the updated policy to the accounts in your organization.

With a self-managed deployment, you are responsible for attaching the
required policies and managing the trust relationship required for the
delegated administrator and management accounts to use cross-account
analyses.

## Troubleshoot self-managed role deployments

If the StackSets deployment to an account fails and the message is "IAM role
exists", delete the IAM role from the member account and then retry the role deployment in
the management account.

###### To retry the IAM role deployments

1. Sign in to the management account.
2. Open the Network Manager console at
   [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
3. From the navigation pane, choose **Reachability Analyzer**,
   **Settings**.
4. Under **IAM role deployments status**, choose
   **Retry role deployment**. The deployments can take
   several minutes to complete, depending on the number of member accounts
   in your organization.

For a message other than "IAM role exists", open a case with AWS Support.
For more information, see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _Support User Guide_.
