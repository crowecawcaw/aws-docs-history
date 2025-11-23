# Delete an Direct Connect virtual interface BGP peer

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can
delete one of the BGP peering sessions (but not both). You can delete a virtual interface BGP peer using either the Direct Connect console or using the command line or API.

###### To delete a BGP peer

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual
   Interfaces**.
3. Select the virtual interface and then choose **View
   details**.
4. Under **Peerings,** select the peering that you want to
   delete and then choose **Delete**.
5. In the **Remove peering from virtual interface** dialog
   box, choose **Delete**.

###### To delete a BGP peer using the command line or API

- [delete-bgp-peer](../../../cli/latest/reference/directconnect/delete-bgp-peer.md "../../../cli/latest/reference/directconnect/delete-bgp-peer.md") (AWS CLI)
- [DeleteBGPPeer](../APIReference/API_DeleteBGPPeer.md "../APIReference/API_DeleteBGPPeer.md")
  (Direct Connect API)
