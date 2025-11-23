# Troubleshooting triggers and AWS CodeCommit

The following information might help you troubleshoot issues with triggers in
AWS CodeCommit.

###### Topics

- [Trigger error: A repository trigger does not run when
  expected](#troubleshooting-ti1 "#troubleshooting-ti1")

## Trigger error: A repository trigger does not run when

expected

**Problem:** One or more triggers configured for a repository
does not appear to run or does not run as expected.

**Possible fixes:** If the target of the trigger is an
AWS Lambda function, make sure you have configured the function's resource policy for
access by CodeCommit.

Alternatively, edit the trigger and make sure the events for which you want to trigger
actions have been selected and that the branches for the trigger include the branch where you
want to see responses to actions. Try changing the settings for the trigger to **All
repository events** and **All branches** and then testing the
trigger. For more information, see [Edit triggers for a repository](how-to-notify-edit.md "how-to-notify-edit.md").
