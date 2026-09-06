

# Delete a Direct Connect virtual interface BGP peer
<a name="delete-bgp-peer-vif"></a>

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can delete one of the BGP peering sessions (but not both). You can delete a virtual interface BGP peer using either the Direct Connect console or using the command line or API.

**To delete a BGP peer**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Under **Peerings,** select the peering that you want to delete and then choose **Delete**.

1. In the **Remove peering from virtual interface** dialog box, choose **Delete**.

**To delete a BGP peer using the command line or API**
+ [delete-bgp-peer](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-bgp-peer.html) (AWS CLI)
+ [DeleteBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteBGPPeer.html) (Direct Connect API)