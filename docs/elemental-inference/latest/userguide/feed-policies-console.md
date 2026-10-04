

# Managing a policy using the console
<a name="feed-policies-console"></a>

You can attach, update, and remove a feed's resource policy on the **Permissions** tab of the feed details page. When no policy is set, the **Resource policy** section shows the message **No resource policy configured.** Until you add a policy, only your AWS account can read the feed's metadata.

1. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/), and choose **Feeds**. Then select the feed.

1. Choose the **Permissions** tab. If the feed has a policy, the **Resource policy** section shows it in an inline JSON editor. If the feed doesn't have a policy, choose **Add resource policy** to open the editor.

1. To build a policy, edit the JSON directly, or choose **Add new statement** to insert a statement. You can add an example statement that grants the MediaTailor service read access to the feed's metadata. For an example policy, see [Example policy for MediaTailor access](feed-policies-example.md).

1. To attach the policy, choose **Save**. To discard your changes, choose **Cancel**.

1. To remove the policy, choose **Delete policy**, and then confirm. Deleting the policy revokes any cross-account or service access that it granted.

**Note**  
You can also set a resource policy when you create a feed. On the create-feed page, the **Resource policy** section provides **Add resource policy** and **Remove resource policy**.