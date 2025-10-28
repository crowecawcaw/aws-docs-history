# Best practices for using

declarative policies

AWS recommends the following best practices for using declarative policies.

## Leverage readiness assessments

Use the declarative policy _account status report_ to assess the
current status of all attributes supported by declarative policies for the accounts in
scope. You can choose the accounts and organizational units (OUs) to include in the
report scope, or choose an entire organization by selecting the root.

This report helps you assess readiness by providing a Region breakdown and if the
current state of an attribute is _uniform across accounts_ (through
the `numberOfMatchedAccounts`) or _inconsistent_ (through
the `numberOfUnmatchedAccounts`). You can also see the _most
frequent value_, which is the configuration value that is most frequently
observed for the attribute.

The choice to attach a declarative policy for enforcing a baseline configuration
depends on your specific use case.

For more information and an illustrative example, see [Account status
report for declarative policies](orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report "orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report").

## Start small and then scale

To simplify debugging, start with a test policy. Validate the behavior and impact of
each change before making the next change. This approach reduces the number of variables
you have to account for when an error or unexpected result occurs.

For example, you can start with a test policy attached to a single account in a
noncritical test environment. After you have confirmed that it works to your
specifications, you can then incrementally move the policy up the organization structure
to more accounts and more organizational units (OUs).

## Establish review processes

Implement processes to monitor for new declarative attributes, evaluate policy
exceptions, and make adjustments to maintain alignment with your organizational security
and operational requirements.

## Validate changes using

`DescribeEffectivePolicy`

After you make a change to a declarative policy, check the effective policies for
representative accounts below the level where you made the change. You can [view the effective policy by using the
AWS Management Console](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md"), or by using the [DescribeEffectivePolicy](../APIReference/API_DescribeEffectivePolicy.md "../APIReference/API_DescribeEffectivePolicy.md") API operation or one of its AWS CLI or AWS SDK
variants. Ensure that the change you made had the intended impact on the effective
policy.

## Communicate and train

Ensure your organizations understand the purpose and impact of your declarative
policies. Provide clear guidance on the expected behaviors and how to handle failures
due to policy enforcement.
