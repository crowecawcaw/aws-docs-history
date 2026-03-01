# Disable Google Drive for Your WorkSpaces Applications Users

You can disable Google Drive for a stack without losing user content that is
already stored on Google Drive. Disabling Google Drive for a stack has the following
effects:

- Users who are connected to active streaming sessions for the stack receive
  an error message. They are informed that they do not have permissions to
  access their Google Drive.
- Any new sessions that use the stack with Google Drive disabled do not
  display Google Drive.
- Only the specific stack for which Google Drive is disabled is
  affected.
- Even if Google Drive is disabled for all stacks, WorkSpaces Applications does not delete
  the user content stored in their Google Drive.
  Follow these steps to disable Google Drive for an existing stack.

###### To disable Google Drive for an existing stack

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to disable Google Drive.
3. Below the stacks list, choose **Storage**, and clear the
   **Enable Google Drive for Google Workspace**
   option.
4. In the **Disable Google Drive for Google Workspace**
   dialog box, type `CONFIRM` (case-sensitive) to confirm your
   choice, then choose **Disable**.

When users of the stack start their next WorkSpaces Applications streaming session, they
can no longer access their Google Drive folder from within that session and
future sessions.
