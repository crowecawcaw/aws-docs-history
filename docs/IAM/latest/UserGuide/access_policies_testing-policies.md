# IAM policy testing with the IAM policy

simulator

For more information about how and why to use IAM policies, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md").

**You can access the IAM Policy Simulator Console at: [https://policysim.aws.amazon.com/](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/")**

###### Important

The policy simulator results can differ from your live AWS environment. We recommend
that you check your policies against your live AWS environment after testing using the
policy simulator to confirm that you have the desired results. For more information, see [How the IAM policy simulator
works](#policies_policy-simulator-how-it-works "#policies_policy-simulator-how-it-works").

With the IAM policy simulator, you can test and troubleshoot identity-based policies and
IAM permissions boundaries. Here are some common things you can do with the policy
simulator:

- Test identity-based policies that are attached to IAM users, IAM groups, or roles in
  your AWS account. If more than one policy is attached to the user, user group, or role,
  you can test all the policies, or select individual policies to test. You can test which
  actions are allowed or denied by the selected policies for specific resources.
- Test and troubleshoot the effect of [permissions boundaries](access_policies_boundaries.md "access_policies_boundaries.md") on IAM entities. You can only simulate one permissions
  boundary at a time.
- Test the effects of resource-based policies on IAM users that are attached to AWS
  resources, such as Amazon S3 buckets, Amazon SQS queues, Amazon SNS topics, or Amazon Glacier vaults. To use a
  resource-based policy in the policy simulator for IAM users, you must include the resource
  in the simulation. You must also select the checkbox to include that resource's policy in
  the simulation.

###### Note

Simulation of resource-based policies isn't supported for IAM roles.

- If your AWS account is a member of an organization in [AWS Organizations](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md"), then you can test the impact of service control policies (SCPs) on your
  identity-based policies.

###### Note

The policy simulator doesn't evaluate SCPs that have any conditions.

- Test new identity-based policies that are not yet attached to a user, user group, or
  role by typing or copying them into the policy simulator. These are used only in the
  simulation and are not saved. You can't type or copy a resource-based policy in the policy
  simulator.
- Test identity-based policies with selected services, actions, and resources. For
  example, you can test to ensure that your policy allows an entity to perform the
  `ListAllMyBuckets`, `CreateBucket`, and `DeleteBucket`
  actions in the Amazon S3 service on a specific bucket.
- Simulate real-world scenarios by providing context keys, such as an IP address or date,
  that are included in `Condition` elements in the policies being tested.

###### Note

The policy simulator doesn't simulate tags provided as input if the identity-based
policy in the simulation doesn't have a `Condition` element that explicitly
checks for tags.

- Identify which specific statement in identity-based policy results in allowing or
  denying access to a particular resource or action.

###### Topics

- [How the IAM policy simulator
  works](#policies_policy-simulator-how-it-works "#policies_policy-simulator-how-it-works")
- [Permissions required for using the
  IAM policy simulator](#permissions-required_policy-simulator "#permissions-required_policy-simulator")
- [Using the IAM policy simulator
  (console)](#policies_policy-simulator-using "#policies_policy-simulator-using")
- [Using the IAM policy simulator (AWS CLI and
  AWS API)](#policies-simulator-using-api "#policies-simulator-using-api")

## How the IAM policy simulator

works

The policy simulator evaluates statements in the identity-based policy and the inputs that
you provide during simulation. The policy simulator results can differ from your live AWS
environment. We recommend that you check your policies against your live AWS environment
after testing using the policy simulator to confirm that you have the desired results.

The policy simulator differs from the live AWS environment in the following ways:

- The policy simulator does not make an actual AWS service request, so you can safely
  test requests that might make unwanted changes to your live AWS environment. The policy
  simulator doesn't consider real context key values in production.
- Because the policy simulator does not simulate running the selected actions, it cannot
  report any response to the simulated request. The only result returned is whether the
  requested action would be allowed or denied.
- If you edit a policy in the policy simulator, these changes affect only the policy
  simulator. The corresponding policy in your AWS account remains unchanged.
- You can't test service control policies (SCPs) with any conditions.
- The policy simulator doesn't support simulation for resource control policies
  (RCPs).
- The policy simulator doesn't support simulation for IAM roles and users for
  cross-account access.

###### Note

The IAM policy simulator doesn't determine which services support [global condition keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md") for
authorization. For example, the policy simulator doesn't identify that a service doesn't
support [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys").

## Permissions required for using the

IAM policy simulator

You can use the policy simulator console or the policy simulator API to test policies. By
default, console users can test policies that are not yet attached to a user, user group, or
role by typing or copying those policies into the policy simulator. These policies are used
only in the simulation and do not disclose sensitive information. API users must have
permissions to test unattached policies. You can allow console or API users to test policies
that are attached to IAM users, IAM groups, or roles in your AWS account. To do so, you
must provide permission to retrieve those policies. In order to test resource-based policies,
users must have permission to retrieve the resource's policy.

For examples of console and API policies that allow a user to simulate policies, see [Example policies: AWS Identity and Access Management (IAM)](access_policies_examples.md#policy_library_IAM "access_policies_examples.md#policy_library_IAM").

### Permissions required for

using the policy simulator console

You can allow users to test policies that are attached to IAM users, IAM groups, or
roles in your AWS account. To do so, you must provide your users with permissions to
retrieve those policies. In order to test resource-based policies, users must have
permission to retrieve the resource's policy.

To view an example policy that allows using the policy simulator console for policies
that are attached to a user, user group, or role, see [IAM: Access the policy
simulator console](reference_policies_examples_iam_policy-sim-console.md "reference_policies_examples_iam_policy-sim-console.md").

To view an example policy that allows using the policy simulator console only for those
users with a specific path, see [IAM: Access the
policy simulator console based on user path](reference_policies_examples_iam_policy-sim-path-console.md "reference_policies_examples_iam_policy-sim-path-console.md").

To create a policy to allow using the policy simulator console for only one type of
entity, use the following procedures.

###### To allow console users to simulate policies for users

Include the following actions in your policy:

- `iam:GetGroupPolicy`
- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `iam:GetUser`
- `iam:GetUserPolicy`
- `iam:ListAttachedUserPolicies`
- `iam:ListGroupsForUser`
- `iam:ListGroupPolicies`
- `iam:ListUserPolicies`
- `iam:ListUsers`

###### To allow console users to simulate policies for IAM groups

Include the following actions in your policy:

- `iam:GetGroup`
- `iam:GetGroupPolicy`
- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `iam:ListAttachedGroupPolicies`
- `iam:ListGroupPolicies`
- `iam:ListGroups`

###### To allow console users to simulate policies for roles

Include the following actions in your policy:

- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `iam:GetRole`
- `iam:GetRolePolicy`
- `iam:ListAttachedRolePolicies`
- `iam:ListRolePolicies`
- `iam:ListRoles`

To test resource-based policies, users must have permission to retrieve the resource's
policy.

###### To allow console users to test resource-based policies in an Amazon S3 bucket

Include the following action in your policy:

- `s3:GetBucketPolicy`

For example, the following policy uses this action to allow console users to simulate a
resource-based policy in a specific Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetBucketPolicy",
 "Resource":"arn:aws:s3:::`bucket-name`/*"
 }
 ]
 }`

```

### Permissions required for using

the policy simulator API

The policy simulator API operations [GetContextKeyForCustomPolicy](../APIReference/API_GetContextKeyForCustomPolicy.md "../APIReference/API_GetContextKeyForCustomPolicy.md") and [SimulateCustomPolicy](../APIReference/API_SimulateCustomPolicy.md "../APIReference/API_SimulateCustomPolicy.md") allow you to
test policies that are not yet attached to a user, user group, or role. To test such
policies, you pass the policies as strings to the API. These policies are used only in the
simulation and do not disclose sensitive information. You can also use the API to test
policies that are attached to IAM users, IAM groups, or roles in your AWS account. To
do that, you must provide users with permissions to call [GetContextKeyForPrincipalPolicy](../APIReference/API_GetContextKeyForPrincipalPolicy.md "../APIReference/API_GetContextKeyForPrincipalPolicy.md") and [SimulatePrincipalPolicy](../APIReference/API_SimulatePrincipalPolicy.md "../APIReference/API_SimulatePrincipalPolicy.md").

To view an example policy that allows using the policy simulator API for attached and
unattached policies in the current AWS account, see [IAM: Access the policy simulator
API](reference_policies_examples_iam_policy-sim.md "reference_policies_examples_iam_policy-sim.md").

To create a policy to allow using the policy simulator API for only one type of policy,
use the following procedures.

###### To allow API users to simulate policies passed directly to the API as strings

Include the following actions in your policy:

- `iam:GetContextKeysForCustomPolicy`
- `iam:SimulateCustomPolicy`

###### To allow API users to simulate policies attached to IAM users, IAM groups, roles,

or resources

Include the following actions in your policy:

- `iam:GetContextKeysForPrincipalPolicy`
- `iam:SimulatePrincipalPolicy`

For example, to give a user named Bob permission to simulate a policy that is assigned
to a user named Alice, give Bob access to the following resource:
`arn:aws:iam::777788889999:user/alice`.

To view an example policy that allows using the policy simulator API only for those
users with a specific path, see [IAM: Access the policy
simulator API based on user path](reference_policies_examples_iam_policy-sim-path.md "reference_policies_examples_iam_policy-sim-path.md").

## Using the IAM policy simulator

(console)

By default, users can test policies that are not yet attached to a user, user group, or
role by typing or copying those policies into the policy simulator console. These policies are
used only in the simulation and do not disclose sensitive information.

###### To test a policy that is not attached to a user, user group, or role (console)

1. Open the IAM policy simulator console at: [https://policysim.aws.amazon.com/](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/").
2. In the **Mode:** menu at the top of the page, choose **New
   Policy**.
3. In the **Policy Sandbox**, choose **Create New
   Policy**.
4. Type or copy a policy into the policy simulator, and use the policy simulator as
   described in the following steps.

After you have permission to use the IAM Policy Simulator Console, you can use the
policy simulator to test an IAM user, user group, role, or resource policy.

###### To test a policy that is attached to a user, user group, or role (console)

1. Open the IAM policy simulator console at [https://policysim.aws.amazon.com/](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/").

###### Note

To sign in to the policy simulator as an IAM user, use your unique sign-in URL to
sign in to the AWS Management Console. Then go to [https://policysim.aws.amazon.com/](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/"). For more
information about signing in as an IAM user, see [How IAM users sign in to AWS](id_users_sign-in.md "id_users_sign-in.md").

The policy simulator opens in **Existing Policies** mode and lists
the IAM users in your account under **Users, Groups, and
Roles**. 2. Choose the option that is appropriate to your task:

| To test this:                                                                                                                                                                                                                                                                                              | Do this:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A policy attached to a user                                                                                                                                                                                                                                                                                | Choose **Users** in the **Users, Groups, and Roles** list. Then choose the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| A policy attached to a user group                                                                                                                                                                                                                                                                          | Choose **Groups** in the **Users, Groups, and Roles** list. Then choose the user group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| A policy attached to a role                                                                                                                                                                                                                                                                                | Choose **Roles** in the **Users, Groups, and Roles** list. Then choose the role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| A policy attached to a resource                                                                                                                                                                                                                                                                            | See [Step 9](#polsimstep-respol "#polsimstep-respol").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| A custom policy for a user, user group, or role                                                                                                                                                                                                                                                            | Choose **Create New Policy**. In the new **Policies** pane, type or paste a policy and then choose **Apply**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ###### Tip To test a policy that is attached to user group, you can launch the IAM policy simulator directly from the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"): In the navigation pane, choose **User groups**. Choose the name of the group that you want to test a policy on, and then choose the **Permissions** tab. Choose **Simulate**. To test a customer managed policy that is attached to a user: In the navigation pane, choose **Users**. Choose the name of the user that you want to test a policy on. Then choose the **Permissions** tab and expand the policy that you want to test. On the far right, choose **Simulate policy**. The **IAM Policy Simulator** opens in a new window and displays the selected policy in the **Policies** pane. 3. (Optional) If your account is a member of an organization in [AWS Organizations](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md"), then select the checkbox next to **AWS Organizations SCPs** to include SCPs in your simulated evaluation. SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU). The SCP limits permissions for entities in member accounts. If an SCP blocks a service or action, then no entity in that account can access that service nor perform that action. This is true even if an administrator explicitly grants permissions to that service or action through an IAM or resource policy. If your account is not a member of an organization, then the checkbox does not appear. 4. (Optional) You can test a policy that is set as a [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for an IAM entity (user or role), but not for IAM groups. If a permissions boundary policy is currently set for the entity, it appears in the **Policies** pane. You can set only one permissions boundary for an entity. To test a different permissions boundary, you can create a custom permissions boundary. To do this, choose **Create New Policy**. A new **Policies** pane opens. In the menu, choose **Custom IAM Permissions Boundary Policy**. Enter a name for the new policy and type or copy a policy into the space below. Choose **Apply** to save the policy. Next, choose **Back** to return to the original **Policies** pane. Then select the checkbox next to the permissions boundary you want to use for the simulation. 5. (Optional) You can test only a subset of policies attached to a user, user group, or role. To do so, in the **Policies** pane clear the checkbox next to each policy that you want to exclude. 6. Under **Policy Simulator**, choose **Select service** and then choose the service to test. Then choose **Select actions** and select one or more actions to test. Although the menus show the available selections for only one service at a time, all the services and actions that you have selected appear in **Action Settings and Results**. 7. (Optional) If any of the policies that you choose in [Step 2](#polsimstep-selectid "#polsimstep-selectid") and [Step 5](#polsimstep-polsubset "#polsimstep-polsubset") include conditions with [AWSglobal condition keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md"), then supply values for those keys. You can do this by expanding the **Global Settings** section and typing values for the key names displayed there. ###### Warning If you leave the value for a condition key empty, then that key is ignored during the simulation. In some cases, this results in an error, and the simulation fails to run. In other cases, the simulation runs, but the results might not be reliable. In those cases, the simulation does not match the real-world conditions that include a value for the condition key or variable. 8. (Optional) Each selected action appears in the **Action Settings and Results** list with **Not simulated** shown in the **Permission** column until you actually run the simulation. Before you run the simulation, you can configure each action with a resource. To configure individual actions for a specific scenario, choose the arrow to expand the action's row. If the action supports resource-level permissions, you can type the [Amazon Resource Name (ARN)](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns") of the specific resource whose access you want to test. By default, each resource is set to a wildcard (\*). You can also specify a value for any [condition context keys](reference_policies_actions-resources-contextkeys.md "reference_policies_actions-resources-contextkeys.md"). As noted previously, keys with empty values are ignored, which can cause simulation failures or unreliable results. 1. Choose the arrow next to the action name to expand each row and configure any additional information required to accurately simulate the action in your scenario. If the action requires any resource-level permissions, you can type the [Amazon Resource Name (ARN)](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns") of the specific resource that you want to simulate access to. By default, each resource is set to a wildcard (\*). 2. If the action supports resource-level permissions but does not require them, then you can choose **Add Resource** to select the resource type that you want to add to the simulation. 3. If any of the selected policies include a `Condition` element that references a context key for this action's service, then that key name is displayed under the action. You can specify the value to be used during the simulation of that action for the specified resource.###### Actions that require different groups of resource types Some actions require different resource types under different circumstances. Each group of resource types is associated with a scenario. If one of these applies to your simulation, select it and the policy simulator requires the resource types appropriate for that scenario. The following list shows each of the supported scenario options and the resources that you must define to run the simulation. Each of the following Amazon EC2 scenarios requires that you specify `instance`, `image`, and `security-group` resources. If your scenario includes an EBS volume, then you must specify that `volume` as a resource. If the Amazon EC2 scenario includes a virtual private cloud (VPC), then you must supply the `network-interface` resource. If it includes an IP subnet, then you must specify the `subnet` resource. For more information on the Amazon EC2 scenario options, see [Supported Platforms](../../../AWSEC2/latest/UserGuide/ec2-supported-platforms.md "../../../AWSEC2/latest/UserGuide/ec2-supported-platforms.md") in the _Amazon EC2 User Guide_. <br>• **EC2-VPC-InstanceStore** instance, image, security-group, network-interface <br>• **EC2-VPC-InstanceStore-Subnet** instance, image, security-group, network-interface, subnet <br>• **EC2-VPC-EBS** instance, image, security-group, network-interface, volume <br>• **EC2-VPC-EBS-Subnet** instance, image, security-group, network-interface, subnet, volume 9. (Optional) If you want to include a resource-based policy in your simulation, then you must first select the actions that you want to simulate on that resource in [Step 6](#polsimstep-service "#polsimstep-service"). Expand the rows for the selected actions, and type the ARN of the resource with a policy that you want to simulate. Then select **Include Resource Policy** next to the **ARN** text box. The IAM policy simulator currently supports resource-based policies from only the following services: Amazon S3 (resource-based policies only; ACLs are not currently supported), Amazon SQS, Amazon SNS, and unlocked Amazon Glacier vaults (locked vaults are not currently supported). 10. Choose **Run Simulation** in the upper-right corner. The **Permission** column in each row of **Action Settings and Results** displays the result of the simulation of that action on the specified resource. 11. To see which statement in a policy explicitly allowed or denied an action, choose the **`N` matching statement(s)** link in the **Permissions** column to expand the row. Then choose the **Show statement** link. The **Policies** pane shows the relevant policy with the statement that affected the simulation result highlighted. ###### Note If an action is _implicitly_ denied—that is, if the action is denied only because it is not explicitly allowed—the **List** and **Show statement** options are not displayed. ### Troubleshooting IAM policy simulator console messages The following table lists the informational and warning messages you might encounter when using the IAM policy simulator. The table also provides steps you can take to resolve them. |
| Message                                                                                                                                                                                                                                                                                                    | Steps to resolve                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| This policy has been edited. Changes will not be saved to your account.                                                                                                                                                                                                                                    | **No action required.** This message is informational. If you edit an existing policy in the IAM policy simulator, your change does not affect your AWS account. The policy simulator allows you to make changes to policies for testing purposes only.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Cannot get the resource policy. Reason: `detailed error message`                                                                                                                                                                                                                                           | The policy simulator is not able to access a requested resource-based policy. Ensure that the specified resource ARN is correct and that the user running the simulation has permission to read the resource's policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| One or more policies require values in the simulation settings. The simulation might fail without these values.                                                                                                                                                                                            | This message appears if the policy you are testing contains condition keys or variables but you have not provided any values for these keys or variables in **Simulation Settings**. To dismiss this message, choose **Simulation Settings**, Then enter a value for each condition key or variable.                                                                                                                                                                                                                                                                                                                                                                                       |
| You have changed policies. These results are no longer valid.                                                                                                                                                                                                                                              | This message appears if you have changed the selected policy while results are displayed in the **Results** pane. Results shown in the **Results** pane are not updated dynamically. To dismiss this message, choose **Run Simulation** again to display new simulation results based on the changes made in the **Policies** pane.                                                                                                                                                                                                                                                                                                                                                        |
| The resource you typed for this simulation does not match this service.                                                                                                                                                                                                                                    | This message appears if you have typed an Amazon Resource Name (ARN) in the **Simulation Settings** pane that does not match the service that you chose for the current simulation. For example, this message appears if you specify an ARN for an Amazon DynamoDB resource but you chose Amazon Redshift as the service to simulate. To dismiss this message, do one of the following: <br>• Remove the ARN from the box in the **Simulation Settings** pane. <br>• Choose the service that matches the ARN that you specified in **Simulation Settings**.                                                                                                                                |
| This action belongs to a service that supports special access control mechanisms in addition to resource-based policies, such as Amazon S3 ACLs or Amazon Glacier vault lock policies. The policy simulator does not support these mechanisms, so the results can differ from your production environment. | **No action required.** This message is informational. In the current version, the policy simulator evaluates policies attached to users and IAM groups, and can evaluate resource-based policies for Amazon S3, Amazon SQS, Amazon SNS, and Amazon Glacier. The policy simulator does not support all access control mechanisms supported by other AWS services.                                                                                                                                                                                                                                                                                                                          |
| DynamoDB FGAC is currently not supported.                                                                                                                                                                                                                                                                  | **No action required.** This informational message refers to _fine-grained access control_. Fine-grained access control is the ability to use IAM policy conditions to determine who can access individual data items and attributes in DynamoDB tables and indexes. It also refers to the actions that can be performed on these tables and indexes. The current version of the IAM policy simulator does not support this type of policy condition. For more information on DynamoDB fine-grained access control, see [Fine-Grained Access Control for DynamoDB](../../../amazondynamodb/latest/developerguide/FGAC_DDB.md "../../../amazondynamodb/latest/developerguide/FGAC_DDB.md"). |
| You have policies that do not comply with the policy syntax. You can use policy validation to review recommended updates to your policies.                                                                                                                                                                 | This message appears at the top of the policy list if you have policies that do not comply with the IAM policy grammar. In order to simulate these policies, review the policy validation options at [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md") to identify and fix these policies.                                                                                                                                                                                                                                                                                                                                                |
| This policy must be updated to comply with the latest policy syntax rules.                                                                                                                                                                                                                                 | This message is displayed if you have policies that do not comply with the IAM policy grammar. In order to simulate these policies, review the policy validation options at [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md") to identify and fix these policies.                                                                                                                                                                                                                                                                                                                                                                         | ## Using the IAM policy simulator (AWS CLI and AWS API) Policy simulator commands typically require calling API operations to do two things: 1. Evaluate the policies and return the list of context keys that they reference. You need to know what context keys are referenced so that you can supply values for them in the next step. 2. Simulate the policies, providing a list of actions, resources, and context keys that are used during the simulation. For security reasons, the API operations have been broken into two groups: <br>• API operations that simulate only policies that are passed directly to the API as strings. This set includes [GetContextKeysForCustomPolicy](../APIReference/API_GetContextKeysForCustomPolicy.md "../APIReference/API_GetContextKeysForCustomPolicy.md") and [SimulateCustomPolicy](../APIReference/API_SimulateCustomPolicy.md "../APIReference/API_SimulateCustomPolicy.md"). <br>• API operations that simulate the policies that are attached to a specified IAM user, user group, role, or resource. Because these API operations can reveal details of permissions assigned to other IAM entities, you should consider restricting access to these API operations. This set includes [GetContextKeysForPrincipalPolicy](../APIReference/API_GetContextKeysForPrincipalPolicy.md "../APIReference/API_GetContextKeysForPrincipalPolicy.md") and [SimulatePrincipalPolicy](../APIReference/API_SimulatePrincipalPolicy.md "../APIReference/API_SimulatePrincipalPolicy.md"). For more information about restricting access to API operations, see [Example policies: AWS Identity and Access Management (IAM)](access_policies_examples.md#policy_library_IAM "access_policies_examples.md#policy_library_IAM"). In both cases, the API operations simulate the effect of one or more policies on a list of actions and resources. Each action is paired with each resource and the simulation determines whether the policies allow or deny that action for that resource. You can also provide values for any context keys that your policies reference. You can get the list of context keys that the policies reference by first calling [`GetContextKeysForCustomPolicy`](../APIReference/API_GetContextKeysForCustomPolicy.md "../APIReference/API_GetContextKeysForCustomPolicy.md") or [`GetContextKeysForPrincipalPolicy`](../APIReference/API_GetContextKeysForPrincipalPolicy.md "../APIReference/API_GetContextKeysForPrincipalPolicy.md"). If you don't provide a value for a context key, the simulation still runs. But the results might not be reliable because the policy simulator cannot include that context key in the evaluation. ###### To get the list of context keys (AWS CLI, AWS API) Use the following to evaluate a list of policies and return a list of context keys that are used in the policies. <br>• AWS CLI: [`aws iam get-context-keys-for-custom-policy`](../../../cli/latest/reference/iam/get-context-keys-for-custom-policy.md "../../../cli/latest/reference/iam/get-context-keys-for-custom-policy.md") and [`aws iam get-context-keys-for-principal-policy`](../../../cli/latest/reference/iam/get-context-keys-for-principal-policy.md "../../../cli/latest/reference/iam/get-context-keys-for-principal-policy.md") <br>• AWS API: [`GetContextKeysForCustomPolicy`](../APIReference/API_GetContextKeysForCustomPolicy.md "../APIReference/API_GetContextKeysForCustomPolicy.md") and [`GetContextKeysForPrincipalPolicy`](../APIReference/API_GetContextKeysForPrincipalPolicy.md "../APIReference/API_GetContextKeysForPrincipalPolicy.md") ###### To simulate IAM policies (AWS CLI, AWS API) Use the following to simulate IAM policies to determine a user's effective permissions. <br>• AWS CLI: [`aws iam simulate-custom-policy`](../../../cli/latest/reference/iam/simulate-custom-policy.md "../../../cli/latest/reference/iam/simulate-custom-policy.md") and [`aws iam simulate-principal-policy`](../../../cli/latest/reference/iam/simulate-principal-policy.md "../../../cli/latest/reference/iam/simulate-principal-policy.md") <br>• AWS API: [`SimulateCustomPolicy`](../APIReference/API_SimulateCustomPolicy.md "../APIReference/API_SimulateCustomPolicy.md") and [`SimulatePrincipalPolicy`](../APIReference/API_SimulatePrincipalPolicy.md "../APIReference/API_SimulatePrincipalPolicy.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
