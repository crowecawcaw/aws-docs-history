

# Creating a Security Hub CSPM declarative policy in the console
<a name="orgs-policies-create-console"></a>

You create and manage Security Hub CSPM declarative policies from the delegated administrator account in the Security Hub console. Creating your first declarative policy also enables the `SECURITYHUB_CSPM_POLICY` policy type for your organization. If your organization uses central configuration, the console directs you to the import tool instead. For more information, see [Declarative policies and central configuration in Security Hub CSPM](orgs-policies-and-central-config.md).

You can also create Security Hub CSPM declarative policies by using the Organizations console, the AWS CLI, or the AWS SDKs. For more information, see [Getting started with Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_getting-started.html) in the *AWS Organizations User Guide*.

**To create a Security Hub CSPM declarative policy**

1. Sign in to the AWS Management Console by using the delegated administrator account. Then open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2](https://console.aws.amazon.com/securityhub/v2).

1. In the navigation pane, choose **Management**, and then choose **Configurations**.

1. In the **Configuration catalog**, choose **Posture management from AWS Security Hub CSPM**.

1. In the **Details** section, enter a name and an optional description for the declarative policy.

1. In the **Account selection** section, choose one of the following options:
   + **All organizational units and accounts** attaches the declarative policy to the organization root.
   + **Specific organizational units and accounts** attaches the declarative policy to the entities you select.
   + **No organizational units or accounts** creates the declarative policy without attaching it.

1. In the **Regions** section, choose the Regions where you want to enable Security Hub CSPM and the Regions where you want to disable it. To include new Regions automatically, select the option to include them. Regions that you don't select remain ungoverned.

1. In the **Standards** section, select the standards to enable. Standards that you don't select are disabled in governed Regions.

1. In the **Controls** section, choose whether controls in the selected standards are enabled or disabled by default, and then select any controls that are exceptions to that default.

1. (Optional) In the **Control parameters** section, customize parameter values for specific controls. Parameters that you don't customize use their default values.

1. (Optional) Choose **Add Regional override**, select one or more Regions, and set the standards, controls, and parameters for those Regions. A Regional override fully replaces the default configuration for the Region.

1. (Optional) Under **Advanced settings**, choose the inheritance operators that child declarative policies can use. For more information, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*.

1. (Optional) For **Resource tags**, add tags as key-value pairs.

1. Choose **Next**.

1. Review the declarative policy details, accounts, Regions, and configuration. To see the generated JSON, expand **Policy document**. Then choose **Create policy**.

You can review or edit the generated JSON at any step by expanding **Policy document**. For the declarative policy structure, inheritance rules, and example declarative policies, see [Security Hub CSPM policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_syntax.html) in the *AWS Organizations User Guide*.