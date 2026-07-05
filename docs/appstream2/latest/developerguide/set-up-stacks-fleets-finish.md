# Clean Up Resources in Amazon WorkSpaces Applications

You can stop your running fleet and delete your active stack to free up resources and
to avoid unintended charges to your account. We recommend stopping any unused, running
fleets.

Note that you cannot delete a stack with an associated fleet.

###### Important

To delete a fleet that has an associated auto scaling policy, the IAM role used to
perform the deletion must include the
`application-autoscaling:DeregisterScalableTarget` permission. Without
this permission, the fleet deletion will not fail, however, the service cannot
deregister the auto scaling target associated with the fleet and it will remain as an
orphan resource. Ensure this permission is included in the user's IAM policy before
attempting to delete a fleet with active scaling policies.

###### To clean up your resources

1. In the navigation pane, choose **Stacks**.
2. Select the stack and choose **Actions**,
   **Disassociate Fleet**. In the confirmation dialog box,
   choose **Disassociate.**
3. In the navigation pane, choose **Fleets**.
4. Select the fleet that you want to stop, choose **Actions**,
   and then choose **Stop**. It takes about 5 minutes to stop a
   fleet.
5. When the status of the fleet is **Stopped**, choose
   **Actions**, **Delete**.
6. In the navigation pane, choose **Stacks**.
7. Select the stack and choose **Actions**,
   **Delete**.
