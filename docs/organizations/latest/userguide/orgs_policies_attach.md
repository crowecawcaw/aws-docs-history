# Attaching organization policies with AWS Organizations

This topic describes how to attach policies with AWS Organizations. A _policy_
defines the controls that you want to apply to a group of AWS accounts.

###### Topics

- [Attach policies](#attach_policy "#attach_policy")

## Attach policies with AWS Organizations

###### Minimum permissions

To attach policies, you must have permission to run the following action:

- `organizations:AttachPolicy`

###### Minimum permissions

To attach an authorization policy (SCP or RCP) to a root, OU, or account, you need
permission to run the following action:

- `organizations:AttachPolicy` with a `Resource`
  element in the same policy statement that includes "\*" or the Amazon
  Resource Name (ARN) of the specified policy and the ARN of the root, OU, or
  account that you want to attach the policy to

Service control policies (SCPs)
You can attach an SCP by either navigating to the policy or to the
root, OU, or account that you want to attach the policy to.

###### To attach an SCP by navigating to the root, OU, or

account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   check box next to the root, OU, or account that you want to
   attach an SCP to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Service control policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached SCPs on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately, affecting the permissions of IAM users and
roles in the attached account or all accounts under the
attached root or OU.

###### To attach an SCP by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page, choose the name of the policy
   that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached SCPs on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately, affecting the permissions of IAM users and
roles in the attached account or all accounts under the
attached root or OU.

Resource control policies (RCPs)
You can attach an RCP by either navigating to the policy or to the
root, OU, or account that you want to attach the policy to.

###### To attach an RCP by navigating to the root, OU, or

account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   check box next to the root, OU, or account that you want to
   attach an RCP to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Resource control policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached RCPs on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately, affecting the permissions of resources in the
attached account or all accounts under the attached root or
OU.

###### To attach an RCP by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Resource control policy** page,
   choose the name of the policy that you want to
   attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached RCPs on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately, affecting the permissions of resources in the
attached account or all accounts under the attached root or
OU.

Declarative policies
You can attach a declarative policy by either navigating to the
policy or to the root, OU, or account that you want to attach the
policy to.

###### To attach a declarative policy by navigating to the root, OU,

or account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Declarative policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached declarative policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach a declarative policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page,
   choose the name of the policy that you want to
   attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached declarative policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

Backup policies
You can attach a backup policy by either navigating to the policy
or to the root, OU, or account that you want to attach the policy
to.

###### To attach a backup policy by navigating to the root, OU, or

account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Backup policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached backup policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach a backup policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page, choose the name of the
   policy that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached backup policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

Tag policies
You can attach a tag policy by either navigating to the policy or
to the root, OU, or account that you want to attach the policy
to.

###### To attach a tag policy by navigating to the root, OU, or

account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Tag policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached tag policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach a tag policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page, choose the name of the policy
   that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached tag policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

Chat applications policies
You can attach a chat applications policy by either navigating to
the policy or to the root, OU, or account that you want to attach
the policy to.

###### To attach a chat applications policy by navigating to the

root, OU, or account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Chat applications policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached chat applications policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach a chat applications policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page, choose the name of the
   policy that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached chat applications policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

AI services opt-out policies
You can attach an AI services opt-out policy by either navigating
to the policy or to the root, OU, or account that you want to attach
the policy to.

###### To attach an AI services opt-out policy by navigating to the

root, OU, or account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **AI service opt-out policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached AI services opt-out policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach an AI services opt-out policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose the name of the
   policy that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached AI services opt-out policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

Security Hub policies
You can attach a Security Hub policy by either navigating to the policy
or to the root, OU, or account that you want to attach the policy
to.

###### To attach a Security Hub policy by navigating to the root, OU, or

account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, navigate to and then choose the
   name of the root, OU, or account that you want to attach a
   policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
3. In the **Policies** tab, in the entry for
   **Security Hub policies**, choose
   **Attach**.
4. Find the policy that you want and choose **Attach
   policy**.

The list of attached Security Hub policies on the
**Policies** tab is updated to include
the new addition. The policy change takes effect
immediately.

###### To attach a Security Hub policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose the name of the
   policy that you want to attach.
3. On the **Targets** tab, choose
   **Attach**.
4. Choose the radio button next to the root, OU, or account
   that you want to attach the policy to. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
5. Choose **Attach policy**.

The list of attached Security Hub policies on the
**Targets** tab is updated to include
the new addition. The policy change takes effect
immediately.

**To attach a policy**

The following code examples show how to use `AttachPolicy`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Shows how to attach an AWS Organizations policy to an organization,
    /// an organizational unit, or an account.
    /// </summary>
    public class AttachPolicy
    {
        /// <summary>
        /// Initializes the Organizations client object and then calls the
        /// AttachPolicyAsync method to attach the policy to the root
        /// organization.
        /// </summary>
        public static async Task Main()
        {
            IAmazonOrganizations client = new AmazonOrganizationsClient();
            var policyId = "p-00000000";
            var targetId = "r-0000";

            var request = new AttachPolicyRequest
            {
                PolicyId = policyId,
                TargetId = targetId,
            };

            var response = await client.AttachPolicyAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully attached Policy ID {policyId} to Target ID: {targetId}.");
            }
            else
            {
                Console.WriteLine("Was not successful in attaching the policy.");
            }
        }
    }



```

- For API details, see
  [AttachPolicy](../../../goto/DotNetSDKV3/organizations-2016-11-28/AttachPolicy.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/AttachPolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To attach a policy to a root, OU, or account**

**Example 1**

The following example shows how to attach a service control policy (SCP) to an OU:

```
`aws organizations attach-policy
 --policy-id `p-examplepolicyid111`
 --target-id `ou-examplerootid111-exampleouid111``

```

**Example 2**

The following example shows how to attach a service control policy directly to an account:

```
`aws organizations attach-policy
 --policy-id `p-examplepolicyid111`
 --target-id `333333333333``

```

- For API details, see
  [AttachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def attach_policy(policy_id, target_id, orgs_client):
    """
    Attaches a policy to a target. The target is an organization root, account, or
    organizational unit.

    :param policy_id: The ID of the policy to attach.
    :param target_id: The ID of the resources to attach the policy to.
    :param orgs_client: The Boto3 Organizations client.
    """
    try:
        orgs_client.attach_policy(PolicyId=policy_id, TargetId=target_id)
        logger.info("Attached policy %s to target %s.", policy_id, target_id)
    except ClientError:
        logger.exception(
            "Couldn't attach policy %s to target %s.", policy_id, target_id
        )
        raise




```

- For API details, see
  [AttachPolicy](../../../goto/boto3/organizations-2016-11-28/AttachPolicy.md "../../../goto/boto3/organizations-2016-11-28/AttachPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

The policy change takes effect immediately, affecting the permissions of IAM
users and roles in the attached account or all accounts under the attached root
or OU
