# View or edit an AWS Cloud WAN Connect
 attachment

You can view information about a Connect attachment. For an existing attachment you can
 create a GRE or Tunnel-less Connect peer, as well as edit the key-value tags associated with
 the attachment. If you want to add a new Connect attachment, see [Connect attachments and Connect peers in AWS Cloud WAN](cloudwan-connect-attachment.md "cloudwan-connect-attachment.md").

###### To view and edit a Connect peer attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Select the check box for an attachment where the **Resource
 Type** is **Connect**.
6. Details about the attachment are displayed, as well as any Connect peers and tags
 that are associated with the attachment. Here you can also add a new Connect peer,
 as well as add, edit, or remove tags.




	* To add a new GRE or Tunnel-less Connect peer attachment, choose the
	 **Connect peers** tab and follow the steps here: [Create an AWS Cloud WAN Connect peer for a core
	 network](cloudwan-connect-peer-attachment.md "cloudwan-connect-peer-attachment.md").
	* To add or edit attachment Tags, choose the **Tags** tab.
	 The current list of tags associated with this attachment are displayed.
	 Choose **Edit tags** to modify or delete current tags, and
	 to add new tags. If you made any changes, choose **Edit
	 attachment** to save the changes. The
	 **Attachments** page displays along with a confirmation
	 that the attachment was modified successfully.

## View a Connect or Connect peer attachment using
 the command line or API


Use the command line or API to view a Connect or Connect peer attachment.



###### To view a Connect or Connect peer attachment using the command line or
 API


* For a Connect attachment, see [get-connect-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-attachment.html "https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-attachment.html").
* For a Connect peer attachment, see [get-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-peer.html "https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-peer.html").
