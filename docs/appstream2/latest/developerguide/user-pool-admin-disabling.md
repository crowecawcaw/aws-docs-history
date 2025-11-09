# Disabling Users in Amazon WorkSpaces Applications

You can disable one or more users in the user pool, one at a time. After they are
disabled, users can no longer log in to WorkSpaces Applications until they are re-enabled. This
action does not delete users. If users are connected when you disable them, their
sessions remain active until the session cookie expires (about one hour). Stack
assignments for the users are retained. If the users are re-enabled, their stack
assignments become active again.

###### To disable a user

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **User Pool** and
   select the user you want.
3. Choose **Actions**, **Disable
   user**.
4. Confirm that the correct user is specified, and choose **Disable
   User**.
