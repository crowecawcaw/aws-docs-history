

# Enable or disable blueprints

Enabling or disabling a resource blueprint controls whether that blueprint is available for deployment. You can enable or disable a blueprint either from the Amazon SageMaker Unified Studio domain management portal or from the Amazon SageMaker management console.

## Enabling or disabling blueprints from the domain management portal
<a name="enable-disable-blueprints-portal"></a>

Under each blueprint, you can see the AWS accounts that have access to it and its status. To view the account status, use the following procedure.

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. Choose **Blueprints**.

1. Choose a blueprint.

1. Choose the **Authorization** tab.

1. Choose an account.

1. In the **Account status** section, choose **Edit**.

1. For **Status**, choose **Enable for all projects** or **Disable**.

1. Choose **Save**.

In the accounts table, the **Account status** column shows one of the following values:
+ **Enabled for all projects** – the blueprint is enabled for use in projects created without a project profile, and the Tooling blueprint's category is ToolingLite.
+ **Enabled** – the blueprint is available for use both in projects created without a project profile and in projects created from a project profile.
+ **Disabled** – the blueprint can't be used to deploy resources in any project.

![The Edit account dialog in the Amazon SageMaker Unified Studio domain management portal, showing the Account status section with a Status choice of "Enable for all projects" (available in all projects, with or without a project profile) or "Disable" (not available in any project).](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-enable.png)


## Enabling or disabling blueprints from the Amazon SageMaker management console
<a name="enable-disable-blueprints-console"></a>

You can complete the following procedure to enable or disable blueprints in the Amazon SageMaker management console:

1. Navigate to the [Amazon SageMaker management console](https://console.aws.amazon.com/datazone), and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and choose the domain's name from the list. The name is a hyperlink.

1. On the domain's details page, navigate to the **Blueprints** tab. 

1. In the **Blueprints** tab, use the radio buttons to select the blueprints that you want to enable or disable and then choose the **Enable** or **Disable** buttons to perform the action.

**Important**  
When you enable a blueprint, by default, you are enabling it in the same region as your domain. When you are enabling blueprints for a project profile that is created and enabled in a different region from your domain, you must enable these blueprints in same region where this project profile is enabled (in addition to enabling this blueprint in the same region as your domain). You can do this via the **Regions** tab in the blueprint details page. This applies to all blueprints, including the Tooling blueprint. 