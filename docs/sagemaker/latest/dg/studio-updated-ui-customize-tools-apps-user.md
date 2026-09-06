

# Hide machine learning tools and applications on a user level
<a name="studio-updated-ui-customize-tools-apps-user"></a>

The following shows how to customize the applications and ML tools displayed in Studio on a user level. For more information, see [Hide machine learning tools and applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md).

This feature is not available if Studio Classic is set as your default experience. 

## Hide machine learning tools and applications on a user level instructions (console)
<a name="studio-updated-ui-customize-tools-apps-user-instructions-console"></a>

**To hide machine learning tools and applications Studio UI on a user level (console)**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. From the list of domains, choose the link to the domain you wish to edit.

1. On the **Domain details** page, choose the **User profiles** tab.

1. In the **User profiles** section, choose the link to the user profile you wish to edit.

1. Choose the **App Configurations** tab.

1. In the **SageMaker Studio** section, choose **Customize Studio UI**.

1. On the **Customize Studio UI** page you can hide applications and ML tools displayed in Studio by toggling them off. 

   Note that not all ML features are available in all regions.

1. Once you have reviewed your changes, choose **Save**. This will take you back to the user profile edit flow.

1. Choose **Save changes**. 

Once completed, you will see a green banner containing a success message at the top of the page.

## Hide machine learning tools and applications on a user level instructions (AWS CLI)
<a name="studio-updated-ui-customize-tools-apps-user-instructions-cli"></a>

**Note**  
To use this feature you may need to update to the latest AWS CLI version. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

You can use the AWS CLI to customize the applications and ML tools displayed in Studio on a user level, using [StudioWebPortalSettings](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StudioWebPortalSettings.html). Use `HiddenAppTypes` to hide applications and `HiddenMlTools` to hide ML tools. 

In the following example, SageMaker Canvas and Code Editor are being hidden for user {{userProfileName}} in the domain `{{domainId}}`.

```
aws sagemaker update-user-profile \
  --domain-id {{domainId}} \
  --user-profile-name {{userProfileName}} \
  --user-settings '{"StudioWebPortalSettings": {"HiddenAppTypes": ["Canvas", "CodeEditor"]}}'
```

Note that not all ML features are available in all AWS Regions.