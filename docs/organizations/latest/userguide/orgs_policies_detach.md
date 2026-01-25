# Detaching organization policies with AWS Organizations

This topic describes how to detach policies with AWS Organizations. A _policy_
defines the controls that you want to apply to a group of AWS accounts.

###### Topics

- [Detach policies](#detach_policy "#detach_policy")

## Detach policies with AWS Organizations

###### Minimum permissions

To detach a policy from the organization root, OU, or account, you must have
permission to run the following action:

- `organizations:DetachPolicy`

###### Note

You can't detach the last authorization policy (SCP or RCP) from a root, an OU, or
an account. There must be at least one SCP and RCP attached to every root, OU, and
account at all times.

Service control policies (SCPs)
You can detach an SCP by either navigating to the policy or to the
root, OU, or account that you want to detach the policy from.

###### To detach an SCP by navigating to the root, OU, or account

it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the SCP that you want to detach, and then
   choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached SCPs is updated. The policy change
caused by detaching the SCP takes effect immediately. For
example, detaching an SCP immediately affects the
permissions of IAM users and roles in the formerly
attached account or accounts under the formerly attached
organization root or OU.

###### To detach an SCP by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page, choose the name of the policy
   that you want to detach from a root, OU, or account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached SCPs is updated. The policy change
caused by detaching the SCP takes effect immediately. For
example, detaching an SCP immediately affects the
permissions of IAM users and roles in the formerly
attached account or accounts under the formerly attached
organization root or OU.

Resource control policies (RCPs)
You can detach an RCP by either navigating to the policy or to the
root, OU, or account that you want to detach the policy from. After
you detach an RCP from an entity, that RCP no longer applies to any
resources that were affected by the now detached entity.

###### Note

**You cannot detach the
`RCPFullAWSAccess` policy**

The `RCPFullAWSAccess` policy is automatically
attached to the root, every OU, and every account in your
organization. You cannot detach this policy.

###### To detach an RCP by navigating to the root, OU, or account

it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the RCP that you want to detach, and then
   choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached RCPs is updated. The policy change
caused by detaching the RCP takes effect immediately. For
example, detaching an RCP immediately affects the
permissions of IAM users and roles in the formerly
attached account or accounts under the formerly attached
organization root or OU.

###### To detach an RCP by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Resource control policy** page,
   choose the name of the policy that you want to detach from a
   root, OU, or account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached RCPs is updated. The policy change
caused by detaching the RCP takes effect immediately. For
example, detaching an RCP immediately affects the
permissions of IAM users and roles in the formerly
attached account or accounts under the formerly attached
organization root or OU.

Declarative policies
You can detach a declarative policy by either navigating to the
policy or to the root, OU, or account that you want to detach the
policy from.

###### To detach a declarative policy by navigating to the root, OU,

or account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the declarative policy that you want to
   detach, and then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached declarative policies is updated. The
policy change takes effect immediately.

###### To detach a declarative policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page,
   choose the name of the policy that you want to detach from a
   root, OU, or account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached declarative policies is updated. The
policy change takes effect immediately.

Backup policies
You can detach a backup policy by either navigating to the policy
or to the root, OU, or account that you want to detach the policy
from.

###### To detach a backup policy by navigating to the root, OU, or

account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the backup policy that you want to detach,
   and then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached backup policies is updated. The
policy change takes effect immediately.

###### To detach a backup policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page, choose the name of the
   policy that you want to detach from a root, OU, or
   account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached backup policies is updated. The
policy change takes effect immediately.

Tag policies
You can detach a tag policy by either navigating to the policy or
to the root, OU, or account that you want to detach the policy
from.

###### To detach a tag policy by navigating to the root, OU, or

account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the tag policy that you want to detach, and
   then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached tag policies is updated. The policy
change takes effect immediately.

###### To detach a tag policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page, choose the name of the policy
   that you want to detach from a root, OU, or account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached tag policies is updated. The policy
change takes effect immediately.

Chat applications policies
You can detach a chat applications policy by either navigating to
the policy or to the root, OU, or account that you want to detach
the policy from.

###### To detach a chat applications policy by navigating to the

root, OU, or account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the chat applications policy that you want to
   detach, and then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached chat applications policies is
updated. The policy change takes effect immediately.

###### To detach a chat applications policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page, choose the name of the
   policy that you want to detach from a root, OU, or
   account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached chat applications policies is
updated. The policy change takes effect immediately.

AI services opt-out policies
You can detach an AI services opt-out policy by either navigating
to the policy or to the root, OU, or account that you want to detach
the policy from.

###### To detach an AI services opt-out policy by navigating to the

root, OU, or account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the AI services opt-out policy that you want
   to detach, and then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached AI services opt-out policies is
updated. The policy change takes effect immediately.

###### To detach an AI services opt-out policy by navigating to the

policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose the name of the
   policy that you want to detach from a root, OU, or
   account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached AI services opt-out policies is
updated. The policy change takes effect immediately.

Security Hub policies
You can detach a Security Hub policy by either navigating to the policy
or to the root, OU, or account that you want to detach the policy
from.

###### To detach a Security Hub policy by navigating to the root, OU, or

account it's attached to

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page navigate to the Root, OU, or account
   that you want to detach a policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want. Choose the
   name of the Root, OU, or account.
3. On the **Policies** tab, choose the radio
   button next to the Security Hub policy that you want to detach, and
   then choose **Detach**.
4. In the confirmation dialog box, choose **Detach
   policy**.

The list of attached Security Hub policies is updated. The policy
change takes effect immediately.

###### To detach a Security Hub policy by navigating to the policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose the name of the
   policy that you want to detach from a root, OU, or
   account.
3. On the **Targets** tab, choose the radio
   button next to the root, OU, or account that you want to
   detach the policy from. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU or account that you want.
4. Choose **Detach**.
5. In the confirmation dialog box, choose
   **Detach**.

The list of attached Security Hub policies is updated. The policy
change takes effect immediately.

**To attach a policy**

The following code examples show how to use `DetachPolicy`.

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
    /// Shows how to detach a policy from an AWS Organizations organization,
    /// organizational unit, or account.
    /// </summary>
    public class DetachPolicy
    {
        /// <summary>
        /// Initializes the Organizations client object and uses it to call
        /// DetachPolicyAsync to detach the policy.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var policyId = "p-00000000";
            var targetId = "r-0000";

            var request = new DetachPolicyRequest
            {
                PolicyId = policyId,
                TargetId = targetId,
            };

            var response = await client.DetachPolicyAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully detached policy with Policy Id: {policyId}.");
            }
            else
            {
                Console.WriteLine("Could not detach the policy.");
            }
        }
    }



```

- For API details, see
  [DetachPolicy](../../../goto/DotNetSDKV3/organizations-2016-11-28/DetachPolicy.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/DetachPolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To detach a policy from a root, OU, or account**

The following example shows how to detach a policy from an OU:

```
`aws organizations detach-policy --target-id `ou-examplerootid111-exampleouid111` --policy-id `p-examplepolicyid111``

```

- For API details, see
  [DetachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def detach_policy(policy_id, target_id, orgs_client):
    """
    Detaches a policy from a target.

    :param policy_id: The ID of the policy to detach.
    :param target_id: The ID of the resource where the policy is currently attached.
    :param orgs_client: The Boto3 Organizations client.
    """
    try:
        orgs_client.detach_policy(PolicyId=policy_id, TargetId=target_id)
        logger.info("Detached policy %s from target %s.", policy_id, target_id)
    except ClientError:
        logger.exception(
            "Couldn't detach policy %s from target %s.", policy_id, target_id
        )
        raise




```

- For API details, see
  [DetachPolicy](../../../goto/boto3/organizations-2016-11-28/DetachPolicy.md "../../../goto/boto3/organizations-2016-11-28/DetachPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples").

```
    TRY.
        lo_org->detachpolicy(
          iv_policyid = iv_policy_id
          iv_targetid = iv_target_id ).
        MESSAGE 'Policy detached from target.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to detach the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgtargetnotfoundex.
        MESSAGE 'The specified target does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotattex.
        MESSAGE 'The policy is not attached to the target.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [DetachPolicy](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

The policy change takes effect immediately, affecting the permissions of IAM
users and roles and resources, if applicable, in the attached account or all
accounts under the attached root or OU.
