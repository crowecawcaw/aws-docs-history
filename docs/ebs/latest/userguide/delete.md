# Delete Amazon Data Lifecycle Manager policies

Keep the following in mind when deleting Amazon Data Lifecycle Manager policies:

- If you delete a policy, the snapshots or AMIs created by that policy are not
  automatically deleted. If you no longer need the snapshots or AMIs, you must delete
  them manually.
- If you delete a policy that has a snapshot archiving-enabled policy, snapshots that are
  in the archive tier at the time of deleting the policy are no longer managed by Amazon Data Lifecycle Manager. You
  must manually delete the snapshot if they are no longer needed.
- If you delete a policy with an archive-enabled, age-based schedule, the snapshots created by
  the policy and that are scheduled to be archived are permanently deleted at the scheduled archive
  date and time, as indicated by the `aws:dlm:expirationtime` system tag.
  Use one of the following procedures to delete a lifecycle policy.

Console

###### To delete a lifecycle policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic Block Store**, **Lifecycle Manager**.
3. Select a lifecycle policy from the list.
4. Choose **Actions**, **Delete lifecycle policy**.
5. When prompted for confirmation, choose **Delete policy**.

Command line
Use the [delete-lifecycle-policy](../../../cli/latest/reference/dlm/delete-lifecycle-policy.md "../../../cli/latest/reference/dlm/delete-lifecycle-policy.md") command to delete a lifecycle policy and free up the
target tags specified in the policy for reuse.

###### Note

You can delete snapshots created only by Amazon Data Lifecycle Manager.

```
`aws dlm delete-lifecycle-policy --policy-id policy-`0123456789abcdef0``
```

The [Amazon Data Lifecycle Manager API Reference](../../../dlm/latest/APIReference.md "../../../dlm/latest/APIReference.md")
provides descriptions and syntax for each of the actions and data types for the Amazon Data Lifecycle Manager Query
API.

Alternatively, you can use one of the AWS SDKs to access the API in a way that's
tailored to the programming language or platform that you're using. For more information,
see [AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
