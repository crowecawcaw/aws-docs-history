

# Update a resource-based delegation policy with AWS Organizations
<a name="orgs-policy-delegate-update"></a>

From the management account, update a resource-based delegation policy for your organization and add a statement that specifies which member accounts can perform actions on policies. You can add multiple statements in the policy to denote a different set of permissions to member accounts.

**Important**  
Effective June 30, 2026, AWS Organizations no longer permits `NotAction` and `NotResource` elements in resource-based delegation policies. These elements are incompatible with the delegation allowlist model and can grant unintended access to organization management actions. Any attempt to create or update a delegation policy that contains `NotAction` or `NotResource` after this date is rejected with an error.  
Existing stored policies continue to function without interruption. Review your delegation policies and replace `NotAction` with an explicit `Action` list, and `NotResource` with an explicit `Resource` list.

**Minimum permissions**  
To update the resource-based delegation policy, you need permissions to run the following actions:  
`organizations:PutResourcePolicy`
`organizations:DescribeResourcePolicy` 
Additionally, you must grant roles and users in the delegated administrator account the corresponding IAM permissions to the required actions. Without IAM permissions, it is assumed that the calling principal doesn’t have the required permissions to manage AWS Organizations policies.

------
#### [ AWS Management Console ]

Add statements to the resource-based delegation policy in the AWS Management Console using one of the following methods: 
+ **JSON policy** – Paste and customize an example resource-based delegation policy to use in your account, or type your own JSON policy document in the JSON editor.
+ **Visual editor** – Construct a new delegation policy in the visual editor, which guides you in creating a delegation policy without having to write JSON syntax.

**Use the JSON policy editor to update a delegation policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. Choose **Settings**.

1. In the **Delegated administrator for AWS Organizations** section, choose **Edit** to update the Organizations delegation policy.

1. Enter a JSON policy document. For details about the IAM policy language, see [IAM JSON policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) reference.

1. Resolve any [security warnings, errors, or general warnings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) generated during policy validation, and then choose **Create policy**.

**Use the visual editor update a delegation policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. Choose **Settings**.

1. In the **Delegated administrator for AWS Organizations** section, choose **Edit** to update the Organizations delegation policy.

1. On the **Create Delegation policy** page, choose **Add new statement**.

1. Set **Effect** to `Allow`.

1. Add `Principal` to define the member accounts to which you want to delegate.

1. From the list of **Actions**, choose the actions you want to delegate. You can use **Filter actions** to narrow down the choices.

1. To specify if the delegated member account can attach policies to the organization root or organizational units (OUs), set `Resources`. You must also select `policy` as a resource type. You can specify resources in the following ways:
   + Choose **Add a resource** and construct the Amazon Resource Name (ARN) by following the prompts in the dialog box.
   + List resource ARNs manually in the editor. For more information about ARN syntax, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the AWS General Reference Guide. For information about using ARNs in the resource element of a policy, see [IAM JSON policy elements: Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html).

1. Choose **Add a condition** to specify other conditions, including the policy type you want to delegate. Choose the condition's **Condition key**, **Tag key**, **Qualifier**, and **Operator**, and then type a **Value**. When you're finished, choose **Add condition**. For more information about the **Condition** element, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the IAM JSON policy reference.

1. To add more permission blocks, choose **Add new statement**. For each block, repeat steps 5 through 9.

1. Resolve any security warnings, errors, or general warnings generated during [policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html), and then choose **Save policy**.

------
#### [ AWS CLI & AWS SDKs ]

**Create or update a delegation policy**  
You can use the following command to create or update a delegation policy: 
+ AWS CLI: [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/organizations/put-resource-policy.html)

  The following example creates or updates the delegation policy.

  ```
  $ aws organizations put-resource-policy --content
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "Fully_manage_backup_policies",
              "Effect": "Allow",
              "Principal": {
                  "AWS": "{{135791357913}}"
              },
              "Action": [
                  "organizations:DescribeOrganization",
                  "organizations:ListAccounts",
                  "organizations:CreatePolicy",
                  "organizations:DescribePolicy",
                  "organizations:UpdatePolicy",
                  "organizations:DeletePolicy",
                  "organizations:AttachPolicy",
                  "organizations:DetachPolicy"
              ],
              "Resource": [
                  "arn:aws:organizations::{{246802468024}}:root/o-{{abcdef}}/r-{{pqrstu}}",
                  "arn:aws:organizations::{{246802468024}}:ou/o-{{abcdef}}/*",
                  "arn:aws:organizations::{{246802468024}}:account/o-{{abcdef}}/*",
                  "arn:aws:organizations::{{246802468024}}:organization/policy/backup_policy/*",
              ],
              "Condition": {
                  "StringLikeIfExists": {
                      "organizations:PolicyType": [
                          "BACKUP_POLICY"
                      ]
                  }
              }
          }
      ]
  }
  ```
+ AWS SDK: [PutResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PutResourcePolicy.html)

------

**Supported delegation policy actions**  
The following actions are supported for delegation policy: 
+ `AttachPolicy`
+ `CreatePolicy`
+ `DeletePolicy`
+ `DescribeAccount`
+ `DescribeCreateAccountStatus`
+ `DescribeEffectivePolicy`
+ `DescribeHandshake`
+ `DescribeOrganization`
+ `DescribeOrganizationalUnit`
+ `DescribePolicy`
+ `DescribeResourcePolicy`
+ `DetachPolicy`
+ `DisablePolicyType`
+ `EnablePolicyType`
+ `ListAccounts`
+ `ListAccountsForParent`
+ `ListAWSServiceAccessForOrganization`
+ `ListChildren`
+ `ListCreateAccountStatus`
+ `ListDelegatedAdministrators`
+ `ListDelegatedServicesForAccount`
+ `ListHandshakesForAccount`
+ `ListHandshakesForOrganization`
+ `ListOrganizationalUnitsForParent`
+ `ListParents`
+ `ListPolicies`
+ `ListPoliciesForTarget`
+ `ListRoots`
+ `ListTagsForResource`
+ `ListTargetsForPolicy`
+ `TagResource`
+ `UntagResource`
+ `UpdatePolicy`

**Supported condition keys**  
Only condition keys supported by AWS Organizations can be used for delegation policy. For more information, see [Condition keys for AWS Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-policy-keys) in the *Service Authorization Reference*.