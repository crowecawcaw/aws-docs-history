# Step 1: Enable and configure AWS Security Incident Response

The onboarding process takes approximately 10 to 15 minutes per AWS organization. For a walkthrough, see the [Getting Started video](getting-started.md "getting-started.md").

###### Note

You can also perform these steps using the API/AWS CLI. For instructions, see [Enable Security Incident Response and configure your incident response team using the API/CLI](enable-sir-using-cli.md "enable-sir-using-cli.md").

## Before you begin

Confirm the following before you start:

- You have access to your AWS Organizations management account.
- Your AWS Organizations has **All Features** enabled. Consolidated billing alone isn't sufficient.
- Your service control policies (SCPs) don't block the creation of service-linked roles or prevent the use of AWS Security Incident Response actions. If your organization uses restrictive SCPs, verify that they allow the `security-ir:*` actions and the `iam:CreateServiceLinkedRole` action for the Security Incident Response service principal.
- You have identified which account to use as your central membership account. This is the account where you configure membership details, manage your incident response team, and create and manage security cases. We recommend choosing an account that your incident responders already have access to, since they communicate with the Security Incident Response Engineering team and manage active cases. For guidance on structuring your security accounts, see [Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md") in _AWS Prescriptive Guidance_.
- You have sufficient IAM permissions to administer AWS Security Incident Response. For details, see [AWS Security Incident Response managed policies](aws-managed-policies.md "aws-managed-policies.md").

For guidance on preparing your environment with detection services (GuardDuty, Security Hub CSPM, CloudTrail) and third-party EDR integrations, see [Onboarding prerequisites](onboarding-prerequisites.md "onboarding-prerequisites.md").

## Sign up and choose your membership account

1. Sign in to the AWS Management Console using your AWS Organizations management account, then open the [AWS Security Incident Response console](https://console.aws.amazon.com/security-ir "https://console.aws.amazon.com/security-ir") and choose **Sign up**.
2. Designate which account in your organization serves as the central membership account. You have two options:

   - **Use a delegated administrator account (recommended)** — Administrative tasks and case management are located in the delegated administrator account. We recommend using the same delegated administrator that you use for other AWS security and compliance services. Provide the 12-digit delegated administrator account ID, then sign in to that account to proceed. For more information, see [Considerations and
     recommendations](considerations_important.md "considerations_important.md").
   - **Use the currently signed-in account** — The current account becomes the central membership account. Individuals in your organization access the service through this account to create, access, and manage active and resolved cases.

3. After you choose an account, sign in to it to continue with the following configuration steps.

## Configure membership details and account scope

After you sign in to your membership account, you configure how your membership is set up and which accounts it covers.

1. **Select your AWS Region.** Choose the Region where your membership and cases are stored. You can't change this after initial registration.

###### Note

AWS Security Incident Response still monitors findings from all [supported commercial AWS Regions](supported-configs.md "supported-configs.md"). 2. **Define your account scope.** Choose to enable AWS Security Incident Response for your entire AWS organization or for specific organizational units (OUs). You can select coverage at the OU level, but not at the individual account level. Your choice determines how coverage behaves over time:

    * **Full organization:** Your membership covers all member accounts in the organization. Coverage updates automatically as you add or remove accounts.
    * **Specific OUs:** Your membership covers all accounts under the selected OUs, including accounts in sub-OUs. Coverage updates automatically as you add or remove accounts from those OUs.

To learn more about best practices for organizing accounts into OUs, see [Organizing your AWS environment using multiple accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md"). 3. **Provide your incident response contacts.** Supply a primary and secondary contact. These contacts are automatically included as part of your incident response team. At minimum, two contacts must exist for a membership. 4. **Optional settings.** You can enter a name for the membership and define tags to help track AWS costs and search for resources.

## Review service permissions and enable proactive response

Before completing signup, the console displays the permissions that AWS Security Incident Response requires. By signing up, you confirm that the service can:

- Create service-linked roles to access the OUs and accounts in your organization.
- Access and review logs (such as VPC Flow Logs, CloudTrail management events, and S3 CloudTrail events) to expedite investigation and response.
- Ingest alerts from Amazon GuardDuty and AWS Security Hub CSPM, apply suppression rules, and automatically escalate critical findings. This includes creating suppression filters and escalation cases in your accounts.

Select the confirmation checkbox to acknowledge these permissions, then choose **Sign up**. For more information on how proactive response works, see [Proactive response and alert triaging](proactive-response-alert-triaging.md "proactive-response-alert-triaging.md").

## Configure containment actions

After you complete signup, you can optionally configure containment actions to pre-authorize Security Incident Response Engineering to act on your behalf during active incidents. For details on supported containment actions and how to configure them, see [Contain](contain.md "contain.md").
