# Configuring registered installation details

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

After you create an Amazon Q Developer profile and register the app installation in GitHub, you can do the following from
the Amazon Q Developer console:

- Enable or disable the use of code reviews. Feature development and code transformation configuration cannot
  currently be modified.
- Find links to browser extensions that provide a way to add Amazon Q Developer feature labels in the GitHub issues.
- Add tags to search and filter your resources or track AWS costs.
- Delete a GitHub app installation registration.

## Editing features for Amazon Q Developer in GitHub

The features available for Amazon Q Developer in GitHub are enabled by default when you install the app in GitHub
and provide authorization to access your organization. You can choose to disable a feature if you no longer want to
use the feature in GitHub.

###### To enable or disable a feature for Amazon Q Developer in GitHub

1. Navigate to the [Amazon Q Developer
   console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github").
2. In the navigation pane, under **Amazon Q Developer in GitHub**, choose **Registered
   installations**.
3. Under the **Name** column, choose the registration name for the installation you
   want to enable or disable a feature.
4. Under **Features**, choose **Edit** to configure the feature
   availability.
5. In the modal, choose the toggle for the feature you want to enable or disable, and then choose
   **Save** to confirm the changes.

After enabling or disabling a feature in the [Amazon Q Developer
console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github"), the changes are reflected in GitHub. Attempting
to assign an issue to a Amazon Q Developer label after disabling the feature will lead to an error. Code reviews will no
longer take place in new pull requests if the feature is disabled.

## Installing browser extensions

You can install the Amazon Q Developer extension in one of the supported browsers. The extension enables you to quickly
assign feature development or code transformation tasks to Amazon Q Developer in GitHub issues without having to search through
label menus.

The Amazon Q Developer extension is available for the following browsers:

- [Google
  Chrome](https://chromewebstore.google.com/detail/amazon-q-github-issue-hel/oefafjbablenakmhacfllkmpaeabnnfi "https://chromewebstore.google.com/detail/amazon-q-github-issue-hel/oefafjbablenakmhacfllkmpaeabnnfi")
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/amazon-q-github-issue-helper "https://addons.mozilla.org/en-US/firefox/addon/amazon-q-github-issue-helper")
- [Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/amazon-q-github-issue-helper/poghackjbfhejeppjaegbnblangjbmmc "https://microsoftedge.microsoft.com/addons/detail/amazon-q-github-issue-helper/poghackjbfhejeppjaegbnblangjbmmc")

You can also view the supported browsers on the registration installation details page in the
[Amazon Q Developer
console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github").

## Deleting Amazon Q Developer GitHub app installation registration

You can delete a registration for one or more of your GitHub app installation through the Amazon Q Developer console. After
permanently deleting your registration, all data associated with the registration is also deleted. The action can't
be undone.

###### To delete your GitHub app installation

1.  Navigate to the [Amazon Q Developer
    console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github").
2.  In the navigation pane, under **Amazon Q Developer in GitHub**, choose **Registered
    installations**.
3.  Do one of the following:

        * Under the **Actions** column, choose **Delete registration** for
         the installation you want to delete.
        * Under the **Name** column, choose the registration name for the installation you
         want to delete, and the choose **Delete**.

    Under the **Actions** column, choose **Delete registration** for
    registered installation you want to delete.

4.  In the modal, review the details for deleting registration.
5.  In the text input field, enter `confirm`, and then choose **Delete**
    to confirm the changes.

Once you delete a GitHub app installation, you can choose to register a new installation.
