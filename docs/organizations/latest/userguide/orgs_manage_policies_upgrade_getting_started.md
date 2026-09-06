

# Getting started with upgrade rollout policies
<a name="orgs_manage_policies_upgrade_getting_started"></a>

Follow these steps to implement upgrade rollout policies in your organization. Each step links to detailed information to help you complete the implementation successfully.

## Before you begin
<a name="orgs_manage_policies_upgrade_getting_started_prerequisites"></a>

Ensure you have the following:
+ Administrative access to AWS Organizations
+ Resources in supported AWS services (such as Aurora or Amazon Relational Database Service)
+ Necessary IAM permissions configured

## Implementation steps
<a name="orgs_manage_policies_upgrade_getting_started_steps"></a>

1. [Enable upgrade rollout policies for your organization.](enable-policy-type.md)

1. [Understand how upgrade rollout policies work.](orgs_manage_policies_upgrade_rollout.md#orgs_manage_policies_upgrade_rollout_how_work)
   + Identify development, testing, and production environments
   + Determine which resources should be upgraded first, second, and last
   + Document your tagging strategy for resource identification

1.  [Create a upgrade rollout policy](orgs_policies_create.md#create-upgrade-rollout-policy-procedure): 
   + Define the default rollout order (organizational unit or account level)
   + Specify resource targeting using tags
   + Configure any policy exclusions

1. [Attach an upgrade rollout policy to a single member account that you can use for testing.](orgs_policies_attach.md): 
   + Start with a test organizational unit
   + Verify policy inheritance
   + Confirm policy attachment status

1. Tag your resources according to your upgrade order strategy:
   + Apply tags to development resources for first upgrades
   + Tag testing resources for second-order upgrades
   + Designate production resources for last-order upgrades

1. Monitor and validate the policy:
   + Review upgrade order assignments
   + Verify policy effects on test resources

1. Test the upgrade process:
   + Wait for a service upgrade to become available
   + Monitor the upgrade progression through your environments
   + Verify that upgrades follow your specified order

1. Enable upgrade rollout policies for additional organizational units as needed

**Other information**
+ [Learn upgrade rollout policy syntax and see example policies](orgs_manage_policies_upgrade_syntax.md)