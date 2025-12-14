# Deleting organization policies with AWS Organizations

When you no longer need a policy and after you detach it from all organizational units
(OUs) and accounts, you can delete it.

This topic describes how to delete policies with AWS Organizations. A _policy_
defines the controls that you want to apply to a group of AWS accounts.

###### Topics

- [Delete policies](#delete_policy "#delete_policy")

## Delete policies with AWS Organizations

When you sign in to your organization's management account, you can delete a policy
that you no longer need in your organization.

Before you can delete a policy, you must first detach it from all attached
entities.

###### Note

- You can't delete any AWS managed SCP such as the SCP named
  `FullAWSAccess`.
- You can't delete any AWS managed RCP such as the RCP named
  `RCPFullAWSAccess`.

###### Minimum permissions

To delete a policy, you need permission to run the following action:

- `organizations:DeletePolicy`

Service control policies (SCPs)

###### To delete an SCP

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page, choose the name of the SCP that
   you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Resource control policies (RCPs)

###### To delete an RCP

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Resource control policies](https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy")** page, choose the name of the RCP that
   you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Declarative policies

###### To delete a declarative policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page,
   choose the name of the policy that you want to
   delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Backup policies

###### To delete a backup policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page, choose the name of the
   backup policy that you want to delete.
3. You must first detach the backup policy that you want to
   delete from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Tag policies

###### To delete a tag policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the \***\*[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page\*\*, choose the
   policy that you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that's shown in the
   **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Chat applications policies

###### To delete a chat applications policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page, choose the name of the
   policy that you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

AI services opt-out policies

###### To delete an AI services opt-out policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose the name of the
   policy that you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

Security Hub CSPM policies

###### To delete a Security Hub CSPM policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose the name of the
   policy that you want to delete.
3. You must first detach the policy that you want to delete
   from all roots, OUs, and accounts. Choose the
   **Targets** tab, choose the radio
   button next to each root, OU, or account that is shown in
   the **Targets** list, and then choose
   **Detach**. In the confirmation dialog
   box, choose **Detach**. Repeat until you
   remove all targets.
4. Choose **Delete** at the top of the
   page.
5. On the confirmation dialog box, enter the name of the
   policy, and then choose **Delete**.

**To delete an a policy**

The following code examples show how to use `DeletePolicy`.

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
    /// Deletes an existing AWS Organizations policy.
    /// </summary>
    public class DeletePolicy
    {
        /// <summary>
        /// Initializes the Organizations client object and then uses it to
        /// delete the policy with the specified policyId.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var policyId = "p-00000000";

            var request = new DeletePolicyRequest
            {
                PolicyId = policyId,
            };

            var response = await client.DeletePolicyAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully deleted Policy: {policyId}.");
            }
            else
            {
                Console.WriteLine($"Could not delete Policy: {policyId}.");
            }
        }
    }



```

- For API details, see
  [DeletePolicy](../../../goto/DotNetSDKV3/organizations-2016-11-28/DeletePolicy.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/DeletePolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete a policy**

The following example shows how to delete a policy from an organization. The example assumes that you previously detached the policy from all entities:

```
`aws organizations delete-policy --policy-id `p-examplepolicyid111``

```

- For API details, see
  [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def delete_policy(policy_id, orgs_client):
    """
    Deletes a policy.

    :param policy_id: The ID of the policy to delete.
    :param orgs_client: The Boto3 Organizations client.
    """
    try:
        orgs_client.delete_policy(PolicyId=policy_id)
        logger.info("Deleted policy %s.", policy_id)
    except ClientError:
        logger.exception("Couldn't delete policy %s.", policy_id)
        raise




```

- For API details, see
  [DeletePolicy](../../../goto/boto3/organizations-2016-11-28/DeletePolicy.md "../../../goto/boto3/organizations-2016-11-28/DeletePolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.
