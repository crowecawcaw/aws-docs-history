

# Identity and Access Management for AWS Billing

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Billing resources. IAM is an AWS service that you can use with no additional charge.

To start activating access to the Billing console, see [IAM tutorial: grant access to the Billing console](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html) in the *IAM User Guide*.

## User types and billing permissions
<a name="security_iam_audience"></a>

This table summarizes the default actions that are permitted in Billing for each type of billing user.


**User types and billing permissions**  

| User type | Description | Billing permissions | 
| --- | --- | --- | 
| Account owner | The person or entity in whose name your account is set up as. |  +  Has full control of all Billing and Cost Management resources. <br />+  Receives a monthly invoice of AWS charges.    | 
| User | A person or application defined as a user in an account by an account owner or administrative user. Accounts can contain multiple users. |  +  Has permissions explicitly granted to the user or a group that includes the user.  <br />+  Can be granted permission to view Billing and Cost Management console pages. For more information, see [Overview of managing access permissions](control-access-billing.md).  <br />+  Can't close accounts.   | 
| Organization management account owner | The person or entity associated with an AWS Organizations management account. The management account pays for AWS usage that is incurred by a member account in an organization.  |  +  Has full control of all Billing and Cost Management resources for the management account only.  <br />+  Receives a monthly invoice of AWS charges for the management account and member accounts.  <br />+  Views the activity of member accounts in the billing reports for the management account.   | 
| Organization member account owner | The person or entity associated with an AWS Organizations member account. The management account pays for AWS usage that is incurred by a member account in an organization.  |  +  Doesn't have permission to review any usage reports or account activity except for its own. Doesn't have access to usage reports or account activity for other member accounts in the organization or for the management account.  <br />+  Doesn't have permission to view billing reports. <br />+  Has permission to update account information only for its own account. Can't access other member accounts or the management account.    | 

## Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting AWS Billing identity and access](security_iam_troubleshoot.md))
+ **Service administrator** - determine user access and submit permission requests (see [How AWS Billing works with IAM](security_iam_service-with-iam.md))
+ **IAM administrator** - write policies to manage access (see [Identity-based policy with AWS Billing](security_iam_id-based-policy-examples.md))

## Authenticating with identities
<a name="security_iam_authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

### AWS account root user
<a name="security_iam_authentication-rootuser"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

### Federated identity
<a name="security_iam_authentication-federated"></a>

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A *federated identity* is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

### IAM users and groups
<a name="security_iam_authentication-iamuser"></a>

An *[IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)* is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*.

An [*IAM group*](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html) in the *IAM User Guide*.

### IAM roles
<a name="security_iam_authentication-iamrole"></a>

An *[IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)* is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Managing access using policies
<a name="security_iam_access-manage"></a>

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the *IAM User Guide*.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based policies
<a name="security_iam_access-manage-id-based-policies"></a>

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

Identity-based policies can be *inline policies* (embedded directly into a single identity) or *managed policies* (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html) in the *IAM User Guide*.

### Resource-based policies
<a name="security_iam_access-manage-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Other policy types
<a name="security_iam_access-manage-other-policies"></a>

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:
+ **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
+ **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the *AWS Organizations User Guide*.
+ **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide*.

### Multiple policy types
<a name="security_iam_access-manage-multiple-policies"></a>

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

## Identity-based policy examples
<a name="sec-policies"></a>

Two identities need Data Hub permissions: the person who creates datasets and the role AWS FinOps Agent uses to read them.

<a name="sec-admin-policy"></a>**Permissions to create and manage datasets.** This policy lets the IAM user or role it is attached to create, change, delete, and tag datasets from the Data Hub page in the AWS Billing and Cost Management console. Add these actions to a policy attached to that person's IAM user or role, such as your AWS FinOps Agent admin setup policy. AWS does not provide a managed policy for these actions during public preview, so you add them to a policy yourself.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ManageDataHubDatasets",
            "Effect": "Allow",
            "Action": [
                "bcm-data-hub:CreateDataset",
                "bcm-data-hub:ListDatasets",
                "bcm-data-hub:GetDataset",
                "bcm-data-hub:GetDatasetSchema",
                "bcm-data-hub:UpdateDataset",
                "bcm-data-hub:DeleteDataset",
                "bcm-data-hub:TagResource",
                "bcm-data-hub:UntagResource",
                "bcm-data-hub:ListTagsForResource"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ReadBillingViews",
            "Effect": "Allow",
            "Action": [
                "billing:ListBillingViews",
                "billing:GetBillingView"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ReadOrganization",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListDelegatedAdministrators"
            ],
            "Resource": "*"
        }
    ]
}
```

`bcm-data-hub:CreateDataset` creates a dataset. Without it, **Create dataset** fails and no dataset is provisioned, so AWS FinOps Agent, even when connected to Data Hub, answers at the service and account level. `bcm-data-hub:ListDatasets` and `bcm-data-hub:GetDataset` list and open datasets. Without them, you cannot see or open your datasets on the Data Hub page or in the Data Hub card in AWS FinOps Agent setup. `bcm-data-hub:GetDatasetSchema` returns a dataset's schema, `bcm-data-hub:UpdateDataset` changes its name, and `bcm-data-hub:DeleteDataset` deletes it. `bcm-data-hub:TagResource`, `bcm-data-hub:UntagResource`, and `bcm-data-hub:ListTagsForResource` add, remove, and list its tags.

**Permissions to read and query a dataset.** This policy is for the agent's role. This policy does not let the role create or delete a dataset, because the person who creates datasets does that. An organization-wide agent needs nothing here, because the agent reads through `AWSServiceRoleForFinOpsAgent`, which AWS maintains. A single-account agent reads its own account's dataset with that account's agent role, and you have two options.
+ **Option 1: let the agent creation wizard attach the policy, recommended.** The `FinOpsAgentAgentPolicy` AWS managed policy already carries the Data Hub read and query actions, and the wizard attaches it to the agent role for you, so you do not write or attach a policy. AWS keeps the policy current as Data Hub adds actions. The person who creates the dataset needs the policy under [Permissions to create and manage datasets](#sec-admin-policy), attached to their own IAM user or role.
+ **Option 2: write the policy yourself.** Choose this when your IAM administrator manages permissions centrally and a console wizard is not allowed to attach policies, or when you want the agent role scoped to a single dataset rather than carrying the managed policy. Use the JSON below and attach it to the agent role. `ListQueryExecutions` takes `*` and lists every query in the account from every principal, each with its SQL, so the role sees other callers' queries. Replace the account ID and the dataset identifier with the ones in your dataset's ARN. Because you own this policy, you also add any action Data Hub introduces later. The [AWS FinOps Agent IAM setup guide](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up.html) defines the agent role.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadAndQueryOneDataset",
            "Effect": "Allow",
            "Action": [
                "bcm-data-hub:GetDataset",
                "bcm-data-hub:StartQueryExecution",
                "bcm-data-hub:GetQueryExecution",
                "bcm-data-hub:GetQueryExecutionResults",
                "bcm-data-hub:CancelQueryExecution"
            ],
            "Resource": "arn:aws:bcm-data-hub:us-east-1:111122223333:dataset/cost_usage-8rp5oclq6g674xnt808hitr2x"
        },
        {
            "Sid": "DiscoverDatasetsAndQueries",
            "Effect": "Allow",
            "Action": [
                "bcm-data-hub:ListDatasets",
                "bcm-data-hub:ListQueryExecutions",
                "bcm-data-hub:GetDatasetSchema"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
To limit an action to one dataset, use the dataset's ARN as the resource. Three actions do not apply to a single dataset, `ListDatasets`, `ListQueryExecutions`, and `GetDatasetSchema`, so they take `*` as the resource and do not accept a dataset ARN. `CreateDataset` has no dataset ARN yet, because AWS generates the identifier when it creates the dataset, so use `arn:aws:bcm-data-hub:us-east-1:111122223333:dataset/*`. See [Identity and Access Management for AWS Billing](security-iam.md).

For how to create a policy from a JSON document, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. When you write one, follow [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), which covers starting from AWS managed policies and narrowing toward least privilege.

## Denying Data Hub access with a service control policy
<a name="sec-scp"></a>

To stop member accounts creating datasets, deny `bcm-data-hub:CreateDataset` in a service control policy attached to the organizational units or accounts you want restricted. Reads are unaffected, so an organization-wide agent in the delegated administrator account keeps answering from the dataset the management account holds. An agent in a restricted account keeps querying a dataset that account already has.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyDataHubDatasetCreation",
            "Effect": "Deny",
            "Action": "bcm-data-hub:CreateDataset",
            "Resource": "*"
        }
    ]
}
```

Service control policies do not apply to the management account, so the management account denies creation across every member account and still creates the organization-wide dataset. During public preview the management account is the only account that can create an organization-wide dataset in any case.

To stop an account from reaching Data Hub at all, deny every `bcm-data-hub` action instead.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyDataHub",
            "Effect": "Deny",
            "Action": "bcm-data-hub:*",
            "Resource": "*"
        }
    ]
}
```

**Warning**  
A service control policy that denies `bcm-data-hub` actions stops roles in member accounts from creating or managing datasets. The service control policy does not stop an organization-wide agent from reading a dataset, because service control policies do not apply to a service-linked role.