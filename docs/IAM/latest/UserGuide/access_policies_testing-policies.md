

# IAM policy testing with the IAM policy simulator
<a name="access_policies_testing-policies"></a>

With the IAM policy simulator, you can test identity-based policies, IAM permissions boundaries, service control policies (SCPs), and resource-based policies that you provide. You simulate how AWS would evaluate a request against those policies, without sending a real request to any AWS service. Each simulation returns a binary authorization outcome for every action and resource you test: the action is either allowed or denied. When the result is an allow or explicit deny, the simulator also shows you which policy produced that outcome, so you can understand and fix the cause.

For more information about how and why to use IAM policies, see [Policies and permissions in AWS Identity and Access Management](access_policies.md).

**Important**  
The policy simulator results can differ from your live AWS environment. We recommend that you check your policies against your live AWS environment after testing with the policy simulator to confirm that you have the desired results. For more information, see [How the IAM policy simulator works](#policies_policy-simulator-how-it-works).

The following screenshot shows the IAM policy simulator, where you select an identity and its policies and choose the actions and resources to test before running the simulation.

![The IAM policy simulator console in Principal mode.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policysim-console-screenshot-1.png)


**Topics**
+ [Policy simulator modes](#policies_policy-simulator-modes)
+ [What you can do with the policy simulator](#policies_policy-simulator-what-you-can-do)
+ [How the IAM policy simulator works](#policies_policy-simulator-how-it-works)
+ [How condition key evaluation works in the IAM policy simulator](#policies_policy-simulator-condition-keys)
+ [Permissions for using the policy simulator](permissions-required_policy-simulator.md)
+ [How to simulate policies](policies_policy-simulator-how-to.md)

## Policy simulator modes
<a name="policies_policy-simulator-modes"></a>

The policy simulator has two modes. Choose the mode that matches whether you want to test policies that already exist in your account, or policies that you are still drafting.

**Principal mode**  
In Principal mode, you test the policies that are already attached to an existing IAM user, role, or group. You choose one identity for the simulation, and the simulator evaluates the policies attached to that identity. You can also include or exclude custom identity policies or permissions boundaries to the simulation. Those additions are simulated as if attached to the principal, without actually being attached in IAM, so your account is unchanged.

**Custom mode**  
In Custom mode, you test one or more policies that you write or paste in. This is useful for checking a policy before you attach it. Custom policies are simulated on their own and are not saved to your account.

For detailed, step-by-step instructions on selecting a mode and running a simulation, see [How to simulate policies](policies_policy-simulator-how-to.md).

## What you can do with the policy simulator
<a name="policies_policy-simulator-what-you-can-do"></a>

Here are some common things you can do with the policy simulator. More detailed step-by-step guide and distinction between API and console behaviors can be found in [How to simulate policies](policies_policy-simulator-how-to.md).
+ Test identity-based policies, whether they are already attached to an IAM user, group, or role, or new policies that you write or paste in. For an attached identity with more than one policy, you can test all the policies together or select individual policies, and see which actions are allowed or denied for specific resources. New policies are evaluated as if they were attached to an identity, without actually attaching them in your account; they are used only in the simulation and are not saved to your account.
+ Test the effect of restrictive controls on access. You can simulate one permissions boundary at a time. If your AWS account is a member of an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/), you can also test the impact of service control policies (SCPs) on your identity-based policies. The simulator tells you whether an SCP allows or denies an action, but for security reasons it does not surface the matched statements from an SCP the way it does for other policy types.
+ Test the effect of a resource-based policy that you provide. Except in the console, the simulator does not retrieve a resource's policy for you. To include a resource-based policy in a simulation, you supply the policy along with the resource.
+ Test specific services, actions, and resources under real-world conditions, and identify what determines the outcome. For example, you can test whether a policy allows the `ListAllMyBuckets`, `CreateBucket`, and `DeleteBucket` actions in Amazon S3 on a specific bucket, and provide context keys such as an IP address or date that are referenced in `Condition` elements in the policies being tested. For each result, the simulator identifies which specific statement allows or denies access; matched statements can come from identity-based policies and from resource-based policies that you provide.

## How the IAM policy simulator works
<a name="policies_policy-simulator-how-it-works"></a>

When you run a simulation, the policy simulator evaluates the policies in scope for the request, any SCPs in scope, and the inputs that you provide, such as actions, resources, and context key values. In Custom mode you supply the policies directly. In Principal mode the simulator uses the policies attached to the identity you select, and you can include or exclude more policies to the simulation. The result is a binary outcome for each action and resource: allowed or denied.

The policy simulator differs from the live AWS environment in the following ways:
+ The policy simulator does not make an actual AWS service request, so you can safely test requests that might otherwise make unwanted changes to your live AWS environment. It does not use real context key values from production, and because the actions are not actually run, it returns no service response. The only result is whether each requested action would be allowed or denied.
+ If you edit a policy in the policy simulator, the change affects only the simulation. The corresponding policy in your AWS account remains unchanged.
+ The policy simulator evaluates SCPs, including condition keys and resource scoping in deny statements, but does not support resource control policies (RCPs). Simulation results can still differ from live behavior for some advanced configurations, such as VPC endpoint policies, role chaining, or multiple resource-based policies on a single resource.
+ Cross-account simulations return per-policy-type decisions (identity policy and resource policy) in `EvalDecisionDetails`.

## How condition key evaluation works in the IAM policy simulator
<a name="policies_policy-simulator-condition-keys"></a>

Many policies use `Condition` elements that depend on condition keys, such as `aws:RequestedRegion` or `aws:MultiFactorAuthPresent`. When you run a simulation, the policy simulator gets values for the condition keys from two sources: values that the simulator populates automatically, and values that you provide as simulation input. If a value does not satisfy a condition, the action is denied.

**Context that the simulator populates automatically**  
The simulator populates the following principal and organization context keys for the evaluation:
+ Principal context: `aws:PrincipalAccount`, `aws:PrincipalId`, `aws:PrincipalType`, `aws:Type`, `aws:UserId`, `aws:UserName`
+ Organization context: `aws:PrincipalOrgID`, `aws:PrincipalOrgMasterAccountId`, `aws:PrincipalOrgPaths`

Because these keys are populated for you, SCPs and other policies that use principal or organization conditions are evaluated correctly. You provide the values for all other condition keys that your policies reference. Review the `Condition` elements in the policies you are testing and supply values for any keys that are not in the list above.

**Global condition keys and service support**  
For identity-based policies and resource-based policies, the simulator does not determine which services support a given global condition key for authorization. For example, the simulator does not identify that a service does not support `aws:TagKeys`. In contrast, service control policies (SCPs) are evaluated with service-aware logic, including global condition keys such as `aws:RequestedRegion` and `aws:PrincipalAccount`. For more information about condition keys, see [AWS global condition context keys](reference_policies_condition-keys.md).

**Condition keys in service control policies (SCPs)**  
The simulator evaluates the condition keys and resource scoping in SCPs. How you supply values for those keys depends on how you run the simulation:
+ With the AWS CLI or AWS API, you can provide values for condition keys that are referenced by SCPs.
+ In the IAM console, you can only set values for condition keys that appear in your identity-based policies, permissions boundaries, or resource-based policies. If a condition key is referenced only by an SCP, you cannot set a value for it in the console. However, if the same condition key also appears in one of those other policies, the value you set is used across the entire evaluation, including the SCP.

For security reasons, SCP evaluation does not return missing context values. You still receive the allow or deny decision for the request.