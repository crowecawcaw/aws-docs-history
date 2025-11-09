# Disable OneDrive for Your WorkSpaces Applications Users

You can disable OneDrive for a stack without losing user content that is already
stored on OneDrive. Disabling OneDrive for a stack has the following effects:

- Users who are connected to active streaming sessions for the stack receive
  an error message. They are informed that they do not have permissions to
  access their OneDrive.
- Any new sessions that use the stack with OneDrive disabled do not display
  OneDrive.
- Only the specific stack for which OneDrive is disabled is affected.
- Even if OneDrive is disabled for all stacks, WorkSpaces Applications does not delete the
  user content stored in their OneDrive.
  Follow these steps to disable OneDrive for an existing stack.

###### To disable OneDrive for an existing stack

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to disable OneDrive.
3. Below the stacks list, choose **Storage**, and clear
   **Enable OneDrive for Business** option.
4. In the **Disable OneDrive for Business** dialog box, type
   `CONFIRM` (case-sensitive) to confirm your choice, then
   choose **Disable**.

When users of the stack start their next WorkSpaces Applications streaming session, they
can no longer access their OneDrive folder from within that session and
future sessions.
