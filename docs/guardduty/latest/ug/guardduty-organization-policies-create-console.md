

# Creating a policy in the console
<a name="guardduty-organization-policies-create-console"></a>

You create and manage GuardDuty policies from the delegated administrator account, on the **Organization policies** page in the GuardDuty console. Creating your first policy also enables the `GUARDDUTY_POLICY` policy type for your organization automatically.

**To create a GuardDuty policy**

1. Sign in to the GuardDuty console with the delegated administrator account.

1. In the navigation pane, choose **Organization policies**, then choose **Create policy**.

1. For **Step 1: Policy details**, enter a policy name and an optional description, then choose **Next**.

1. For **Step 2: Accounts**, choose where the policy is attached in your organization hierarchy, then choose **Next**:
   + **All organizational units and accounts** attaches the policy across the organization.
   + **Specific organizational units and accounts** attaches it to the entities you select.
   + **No organizational units or accounts** creates the policy without attaching it.

1. For **Step 3: Configuration details**, under **Capability selection**, select the protection plans this policy manages. Use **Enable all** or **Disable all** for a quick starting point, then adjust individual protection plans. Protection plans you do not select are not affected by this policy. Foundational threat detection must be enabled if you enable any other protection plan. Choose **Next**.

1. (Optional) For **Step 4: Regional overrides**, choose **Add regional override**, select one or more Regions, and set the configuration for those Regions. A regional override fully replaces the default configuration for the Region, so specify every protection plan you want managed there. Choose **Next**.

1. For **Step 5: Review and create**, review the policy details, accounts, default configuration, and any Regional overrides. To see the generated policy JSON, expand **Policy document**. Then choose **Create policy**.

You can review or edit the generated JSON at any step by expanding **Policy document**. For the policy structure, inheritance rules, and example policies, see [GuardDuty policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) in the AWS Organizations User Guide.