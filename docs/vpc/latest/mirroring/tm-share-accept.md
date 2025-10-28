# Accept or delete a shared traffic mirror target

Before you can use a cross-account traffic mirror target, the traffic mirror target owner
shares the target with you by using the AWS Resource Access Manager. When you are in different AWS Organizations from the
owner, after the owner shares the traffic mirror target, you accept the share request. After
you accept the share request, you can use the traffic mirror target in a traffic mirror session.

The traffic mirror target is visible to shared accounts in their
`DescribeTrafficMirrorTarget` API calls. Only the traffic mirror target owner can
modify or delete the traffic mirror target.

Traffic mirror sessions that are created in a different account than the traffic mirror
target are visible in `DescribeTrafficMirrorSession` API calls that are made by the
traffic mirror target owner.

If you are in different AWS Organizations from the share owner, you must accept the resource share
before you can access the shared resources.

You can delete a resource share at any time. When you delete a resource share, all
principals that are associated with the resource share lose access to the shared resources.
Deleting a resource share does not delete the shared resources.

When you delete a shared traffic mirror target that is in use, the traffic mirror session
becomes inactive.

###### To accept or delete a shared traffic mirror target

1. Open the AWS Resource Access Manager console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/").
2. To accept a shared traffic mirror target, in the navigation pane, choose
   **Shared with me**, **Resource shares**.
3. Select the resource share.
4. Choose **Accept resource share**.
5. To view the shared traffic mirror target, open the **Traffic Mirror
   Targets** page in the Amazon VPC console.
6. To delete a shared traffic mirror target, on the navigation pane, choose **Shared by me**, **Resource
   shares**.
7. Select the resource share.

Be sure to select the correct resource share. You cannot recover a resource share
after you delete it. 8. Choose **Delete**. 9. When prompted for confirmation, enter `delete`, and then choose
**Delete**.
