# Hide machine learning

tools and applications on a domain level

The following shows how to use the console to customize the applications and ML tools
displayed in Studio on a domain level. For more information, see [Hide machine learning tools and
applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md "studio-updated-ui-customize-tools-apps.md").

This feature is not available if Amazon SageMaker Studio Classic is set as your default
experience.

###### To hide machine learning tools and applications Studio UI on a

domain level (console)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, choose the link to the domain you
   wish to edit.
5. On the **Domain details** page, choose the
   **App Configurations** tab.
6. In the **SageMaker Studio** section, choose
   **Customize Studio UI**.
7. On the **Customize Studio UI** page you can hide
   applications and ML tools displayed in Studio by toggling them off.

Note that not all ML features are available in all regions. 8. Once you have reviewed your changes, choose
**Save**.
Once completed, you will see a green banner containing a success message at
the top of the page.

###### Note

To use this feature you may need to update to the latest AWS CLI version.
For more information, see [Installing or
updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

You can use the AWS CLI to customize the applications and ML tools displayed in
Studio on a domain level, using [StudioWebPortalSettings](../APIReference/API_StudioWebPortalSettings.md "../APIReference/API_StudioWebPortalSettings.md"). Use `HiddenAppTypes` to hide
applications and `HiddenMlTools` to hide ML tools.

In the following example, SageMaker Canvas and Code Editor are being hidden for users in the
domain `domainId`.

```
aws sagemaker update-domain \
  --domain-id `domainId` \
  --default-user-settings '{"StudioWebPortalSettings": {"HiddenAppTypes": ["Canvas", "CodeEditor"]}}'
```

Note that not all ML features are available in all AWS Regions.
