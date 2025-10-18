AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with user settings in the AWS Cloud9 IDE

*User settings* are settings that apply across each AWS Cloud9 development environment that's
 associated with your AWS Identity and Access Management (IAM user). They include the following settings:


* General user interface settings such as enabling animations and marking changed
 tabs
* File system navigation settings
* File find and search settings
* Color schemes for terminal sessions and output
* Additional code editor settings, such as font sizes, code folding, full line selection,
 scrolling animations, and font sizes
As you change your user settings, AWS Cloud9 pushes those changes to the cloud and associates
 them with your IAM user. AWS Cloud9 also continually scans the cloud for changes to user settings
 that are associated with your IAM user, and applies those settings to your current environment. You
 can use this to experience the same look and feel no matter what AWS Cloud9 environment you're
 working in.

###### Note

To store and retrieve your IDE settings, AWS Cloud9 uses the internal APIs
 `GetUserSettings` and `UpdateUserSettings`.

You can share your user settings with other users, as follows:


* [View or change your user settings](#settings-user-view "#settings-user-view")
* [Share your user settings with another user](#settings-user-share "#settings-user-share")
* [Customize your user
 settings](settings-user-change.md "settings-user-change.md")

## View or change your user settings



1. On the menu bar, choose **AWS Cloud9**,
 **Preferences**.
2. To view your user settings across each of your environments, on the
 **Preferences** tab, in the side navigation pane, choose **User
 Settings**.
3. In the **User Settings** pane, change your user settings across each
 of your environments.
4. To apply your changes to any other of your environments, simply open that environment. If
 that environment is already open, refresh the web browser tab for that environment.

For more information about how you can make changes in your user settings, see [Customize your user settings](settings-user-change.md "settings-user-change.md").


## Share your user settings with another user



1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose
 **AWS Cloud9, Open Your User Settings**.
2. In the source environment, copy the contents of the **user.settings** tab
 that's displayed.
3. In the target environment, overwrite the contents of the **user.settings**
 tab with the copied contents from the source environment.
4. In the target environment, save the **user.settings** tab.
