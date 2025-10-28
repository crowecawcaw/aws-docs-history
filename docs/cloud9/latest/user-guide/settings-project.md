AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with project settings in the

AWS Cloud9
IDE

_Project settings_, which apply only to the current AWS Cloud9 development environment, include the
following kinds of settings:

- Code editor settings, such as whether to use soft tabs and new file line
  ending
- File types to ignore
- The types of hints and warnings to display or suppress
- Code and formatting settings for programming languages such as
  JavaScript, PHP, Python, and
  Go
- The types of configurations to use when running and building code
  Although project settings apply to only a single environment, you can apply the project settings
  for one environment to any other environment.

- [View or change project settings](#settings-project-view "#settings-project-view")
- [Apply the current project settings for an
  environment to another environment](#settings-project-apply "#settings-project-apply")
- [Customize your project settings](settings-project-change.md "settings-project-change.md")

## View or change project settings

1. On the menu bar, choose **AWS Cloud9**,
   **Preferences**.
2. To view the project settings for the current environment, on the
   **Preferences** tab, in the side navigation pane, choose
   **Project Settings**.
3. To change the current project settings for the environment, change the settings that you
   want in the **Project Settings** pane.

For more information about how you can make changes in your project settings, see [Customize your project settings](settings-project-change.md "settings-project-change.md").

## Apply the current project settings for an environment to

another environment

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose
   **AWS Cloud9, Open Your Project Settings**.
2. In the source environment, copy the contents of the
   **project.settings** tab that's displayed.
3. In the target environment, overwrite the contents of the
   **project.settings** tab with the copied contents from the source
   environment.
4. In the target environment, save the **project.settings** tab.
