# Disable Home Folders

You can disable home folders for a stack without losing user content already
stored in home folders. Disabling home folders for a stack has the following
effects:

- Users who are connected to active streaming sessions for the stack
  receive an error message. They are informed that they can no longer
  store content in their home folder.
- Home folders do not appear for any new sessions that use the stack
  with home folders disabled.
- Disabling home folders for one stack does not disable it for other
  stacks.
- Even if home folders are disabled for all stacks, AppStream 2.0 does not
  delete the user content.
  To restore access to home folders for the stack, enable home folders again by
  following the steps described earlier in this topic.

###### To disable home folders while creating a stack

- Follow the steps in [Create a Stack in Amazon AppStream 2.0](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md") and make sure that the
  **Enable Home Folders** option is cleared.

###### To disable home folders for an existing stack

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack.
3. Below the stacks list, choose **Storage** and clear
   **Enable Home Folders**.
4. In the **Disable Home Folders** dialog box, type
   `CONFIRM` (case-sensitive) to confirm your choice, then
   choose **Disable**.
