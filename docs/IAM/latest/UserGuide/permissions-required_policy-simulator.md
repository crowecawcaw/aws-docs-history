

# Permissions for using the policy simulator
<a name="permissions-required_policy-simulator"></a>

The permissions you need depend on whether you use the AWS CLI or AWS API, or the IAM console, and which mode you use.

------
#### [ Console ]

You need permission to call `iam:GetContextKeysForCustomPolicy` to use the IAM policy simulator on the console.

Additional permissions you need depend on the mode. In Principal mode you need additional read permissions to list the identities in your account and read their attached policies. To reduce what you have to grant, use Custom mode if you only need to test policies that you paste in.

**Custom mode**  
To use Custom mode, where you paste in the policies you want to test, you also need `iam:SimulateCustomPolicy`

**Principal mode**  
To use Principal mode, where the console loads and displays the identities and policies in your account, you need the common permission plus the following. This is the larger set, because the console has to discover identities and read their attached policies.

Simulate:
+ `iam:SimulatePrincipalPolicy`

Listing identities:
+ `iam:ListUsers`, `iam:ListRoles`, `iam:ListGroups`
+ `iam:ListGroupsForUser`

Listing attached policies:
+ `iam:ListPolicies`, `iam:ListUserPolicies`, `iam:ListRolePolicies`, `iam:ListGroupPolicies`
+ `iam:ListAttachedUserPolicies`, `iam:ListAttachedRolePolicies`, `iam:ListAttachedGroupPolicies`

Getting policy documents:
+ `iam:GetPolicyVersion`, `iam:GetUserPolicy`, `iam:GetRolePolicy`, `iam:GetGroupPolicy`

Getting permissions boundaries:
+ `iam:GetUser`, `iam:GetRole`

**Additional permissions for Principal mode to simulate resource-based policies**  
To include a resource's policy in a Principal mode simulation, add the read permission for that resource type:
+ `s3:GetBucketPolicy`, `sns:GetTopicAttributes`, `sqs:GetQueueUrl`, `sqs:GetQueueAttributes`, `glacier:GetVaultAccessPolicy`

For example policies that grant access to the simulator, see [Example policies: AWS Identity and Access Management (IAM)](access_policies_examples.md#policy_library_IAM).

------
#### [ AWS CLI and AWS API ]

For the AWS CLI and AWS API, you need only the permission to call the simulation action for the type of policy you want to test. If you use `iam:GetContextKeysForCustomPolicy` and `iam:GetContextKeysForPrincipalPolicy` to discover the context keys first, also grant permissions to these actions. For security reasons, the actions are split into the following two modes. Grant only the permissions that match what you want to simulate.

**To simulate policies that you pass directly to the API as strings (custom policies)**  

+ `iam:SimulateCustomPolicy`
+ `iam:GetContextKeysForCustomPolicy` (only if you use the context-key discovery step)

These actions let you test policies that are not yet attached to a user, user group, or role. You pass the policies as strings, and they are used only in the simulation.

**To simulate policies that are attached to an IAM user, user group, role, or resource**  

+ `iam:SimulatePrincipalPolicy`
+ `iam:GetContextKeysForPrincipalPolicy` (only if you use the context-key discovery step)

------

Because these actions can reveal the permissions assigned to other IAM entities, consider restricting who can call them. For example, to give a user named Bob permission to simulate a policy assigned to a user named Alice, give Bob access to the resource `arn:aws:iam::777788889999:user/alice`.

To view an example policy that allows using the policy simulator API for attached and unattached policies in the current AWS account, see [IAM: Access the policy simulator API](reference_policies_examples_iam_policy-sim.md). To view an example policy scoped to users with a specific path, see [IAM: Access the policy simulator API based on user path](reference_policies_examples_iam_policy-sim-path.md).