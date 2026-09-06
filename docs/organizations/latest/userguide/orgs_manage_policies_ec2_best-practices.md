

# Best practices for using EC2 policies
<a name="orgs_manage_policies_ec2_best-practices"></a>

AWS recommends the following best practices for using EC2 policies.

## Leverage readiness assessments
<a name="bp-EC2-readiness"></a>

Use the EC2 policy *account status report* to assess the current status of all attributes supported by EC2 policies for the accounts in scope. You can choose the accounts and organizational units (OUs) to include in the report scope, or choose an entire organization by selecting the root.

This report helps you assess readiness by providing a Region breakdown and if the current state of an attribute is *uniform across accounts* (through the `numberOfMatchedAccounts`) or *inconsistent* (through the `numberOfUnmatchedAccounts`). You can also see the *most frequent value*, which is the configuration value that is most frequently observed for the attribute.

The choice to attach a EC2 policy for enforcing a baseline configuration depends on your specific use case.

For more information and an illustrative example, see [Account status report for EC2 policies](orgs_manage_policies_ec2.md#orgs_manage_policies_ec2-account-status-report).

## Start small and then scale
<a name="bp-ec2-rules"></a>

To simplify debugging, start with a test policy. Validate the behavior and impact of each change before making the next change. This approach reduces the number of variables you have to account for when an error or unexpected result occurs.

For example, you can start with a test policy attached to a single account in a noncritical test environment. After you have confirmed that it works to your specifications, you can then incrementally move the policy up the organization structure to more accounts and more organizational units (OUs).

## Establish review processes
<a name="bp-ec2-review"></a>

Implement processes to monitor for new EC2 attributes, evaluate policy exceptions, and make adjustments to maintain alignment with your organizational security and operational requirements.

## Validate changes using `DescribeEffectivePolicy`
<a name="bp-ec2-workflow"></a>

After you make a change to an EC2 policy, check the effective policies for representative accounts below the level where you made the change. You can [view the effective policy by using the AWS Management Console](orgs_manage_policies_effective.md), or by using the [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) API operation or one of its AWS CLI or AWS SDK variants. Ensure that the change you made had the intended impact on the effective policy.

## Communicate and train
<a name="bp-ec2-train"></a>

Ensure your organizations understand the purpose and impact of your EC2 policies. Provide clear guidance on the expected behaviors and how to handle failures due to policy enforcement.