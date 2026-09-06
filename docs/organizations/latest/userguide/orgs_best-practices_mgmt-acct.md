

# Best practices for the management account
<a name="orgs_best-practices_mgmt-acct"></a>

Follow these recommendations to help protect the security of the management account in AWS Organizations. These recommendations assume that you also adhere to the [best practice of using the root user only for those tasks that truly require it](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html).

**Topics**
+ [Limit who has access to the management account](#bp_mgmt-acct_limit-access)
+ [Review and track who has access](#bp_mgmt-acct_review-access)
+ [Use the management account only for tasks that ***require*** the management account](#bp_mgmt-acct_use-mgmt)
+ [Avoid deploying workloads to the organization’s management account](#bp_mgmt-acct_avoid-deploying)
+ [Prevent inadvertent account departures and closures with an SCP](#bp_mgmt-acct_default-controls)
+ [Delegate responsibilities outside the management account for decentralization](#bp_mgmt-acct_)

## Limit who has access to the management account
<a name="bp_mgmt-acct_limit-access"></a>

The management account is key to all the mentioned administrative tasks such as account management, policies, integration with other AWS services, consolidated billing, and so on. Therefore, you should restrict and limit access to the management account only to those admin users who need rights to make changes to the organization. 

## Review and track who has access
<a name="bp_mgmt-acct_review-access"></a>

To make sure that you maintain access to the management account, periodically review the personnel within your business who have access to the email address, password, MFA, and phone number associated with it. Align your review with existing business procedures. Add a monthly or quarterly review of this information to verify that only the correct people have access. Ensure that the process to recover or reset access to the root user credentials is not reliant on any specific individual to complete. All processes should address the prospect of people being unavailable.

## Use the management account only for tasks that ***require*** the management account
<a name="bp_mgmt-acct_use-mgmt"></a>

We recommend that you use the management account and its users and roles for tasks that must be performed only by that account. Store all of your AWS resources in other AWS accounts in the organization and keep them out of the management account. One important reason to keep your resources in other accounts is because Organizations service control policies (SCPs) do not work to restrict any users or roles in the management account. Separating your resources from your management account also helps you to understand the charges on your invoices.

For a list of tasks that must be called from the management account, see [Operations you can call from only the organization's management account ](https://docs.aws.amazon.com/organizations/latest/APIReference/action-reference.html#actions-management-account).

## Avoid deploying workloads to the organization’s management account
<a name="bp_mgmt-acct_avoid-deploying"></a>

Privileged operations can be performed within an organization’s management account, and SCPs do not apply to the management account. That's why you should limit the cloud resources and data contained in the management account to only those that must be managed in the management account. 

## Prevent inadvertent account departures and closures with an SCP
<a name="bp_mgmt-acct_default-controls"></a>

Member accounts can leave your organization or close themselves, which can disrupt governance, billing, and security controls. We recommend that you attach an SCP at the root of your organization that denies the `organizations:LeaveOrganization` and `account:CloseAccount` actions to prevent member accounts from performing these actions without approval from the management account or a delegated administrator.

AWS Organizations organizations created through the AWS Management Console after July 10, 2026 automatically receive this SCP at the root. If you created your organization using the AWS Command Line Interface (AWS CLI), AWS SDKs, or CloudFormation, or if your organization was created before this date, you must create and attach this SCP manually. For the policy example and more information about these controls, see [Default security controls in AWS Organizations](orgs_security_default_controls.md). For instructions on configuring SCPs, see [Enabling a policy type](enable-policy-type.md), [Creating organization policies with AWS Organizations](orgs_policies_create.md), and [Attaching organization policies with AWS Organizations](orgs_policies_attach.md).

## Delegate responsibilities outside the management account for decentralization
<a name="bp_mgmt-acct_"></a>

Where possible, we recommend delegating responsibilities and services outside the management account. Provide your teams with permissions in their own accounts to manage the needs of the organization, without requiring access to the management account. In addition, you can register multiple delegated administrators for services that support this functionality such as AWS Service Catalog for sharing software across the organization, or CloudFormation StackSets for authoring and deploying stacks.

For more information, see [Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html), [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html), and [AWS services that you can use with AWS Organizations](orgs_integrate_services_list.md) for suggestions on registering member accounts as delegated administrator for various AWS services.

For more information about setting up delegated admins, see [Enabling a delegated admin account for AWS Account Management](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-delegated-admin.html) and [Delegated administrator for AWS Organizations](orgs_delegate_policies.md). 