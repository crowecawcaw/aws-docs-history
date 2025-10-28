# Hide instance types

and images on a user level

###### Warning

Customizing a user profile is a permanent action. If custom settings are saved,
this user profile will overwrite the domain settings, and no longer dynamically
update with the domain in the future.

The following shows how to use the console to set rules to hide Amazon SageMaker AI instance
types and images from being displayed in the Amazon SageMaker Studio Classic UI on a _user level_. For more information, see [Hide instance types and
images in the Amazon SageMaker Studio UI](studio-updated-ui-customize-instances-images.md "studio-updated-ui-customize-instances-images.md").

This setting will take priority over the domain level settings.

The customize Studio UI feature is not available in Studio Classic.

###### To hide instance types and images Studio UI on a user level

(console)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, choose the link to the domain you
   wish to edit.
5. On the **Domain details** page, choose the
   **User profiles** tab.
6. In the **User profiles** section, choose the link to
   the user profile you wish to edit.
7. On the User details tab, you can view the rules applied to the user in
   the User profile rules section.
8. In the User profile rules section choose Manage rules.
9. On the Manage user profile rules page choose a Rule type.

Note that not all instance types and images are available in all
AWS Regions.

    1. If you choose **Instance type**, you can use
     the **Hide** action to hide SageMaker AI instance types
     you choose in the dropdown list under **Instance
     types**.
    2. If you choose **Image**, you can use the
     **Hide** action to hide SageMaker images you
     choose under the dropdown list under
     **Image**.

10. (Optional) Choose **+ Add new rule** to add more
    rules.
11. Once you have reviewed your changes, choose
    **Submit**.
    Once completed, you will see a green banner containing a success message at
    the top of the page.

###### Note

To use this feature you may need to update to the latest AWS CLI version.
For more information, see [Installing or
updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

You can use the AWS CLI to customize the applications and ML tools displayed in
Studio on a user level, using [StudioWebPortalSettings](../APIReference/API_StudioWebPortalSettings.md "../APIReference/API_StudioWebPortalSettings.md"). Use `HiddenInstanceTypes` to
hide instance types and use `HiddenSageMakerImageVersionAliases` to
hide SageMaker images.

Note that when you use `HiddenSageMakerImageVersionAliases`:

- The API only accepts minor `VersionAliases` (for example,
  `1.9`), rather than patch versions (For example,
  `1.9.1`).
- You may enter unpublished versions through the CLI or SDK. However,
  these versions will not be displayed in the console and will be
  overwritten after the rules are edited through the console.
  In the following example, for Code Editor, based on Code-OSS, Visual Studio Code - Open Source and JupyterLab, the following are
  being hidden for user `userProfileName` in the domain
  `domainId`:

- The instance types `ml.r6id.24xlarge` and
  `ml.r6id.32xlarge`.
- The image `sagemaker_distribution` versions
  `1.9` and `1.8`.

```
aws sagemaker update-user-profile \
    --domain-id domainId \
    --user-profile-name userProfileName \
    --user-settings '{
        "StudioWebPortalSettings": {
            "HiddenInstanceTypes": [ "ml.r6id.24xlarge", "ml.r6id.32xlarge" ],
            "HiddenSageMakerImageVersionAliases": [
                {
                    "SageMakerImageName": "sagemaker_distribution",
                    "VersionAliases": [ "1.9", "1.8" ]
                }
            ]
        }
    }'
```

Note that not all instance types and images are available in all
AWS Regions.
