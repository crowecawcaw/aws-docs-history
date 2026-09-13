

# Shared attachments in AWS Cloud WAN
<a name="cloudwan-shared-attachments"></a>

You can share attachments on any of your shared core networks. For more information on sharing core networks, see [Shared AWS Cloud WAN core network](cloudwan-share-network.md).

 When a core network owner shares their core network with your account, you are then able to create new VPC, transit gateway route table, or Direct Connect gateway attachments for the shared core network. You can also view the current attachments or delete an attachment from the shared core network.

**Note**  
A shared core network currently supports only VPC, transit gateway route table, and Direct Connect gateway attachments.

**Note**  
If `require-attachment-acceptance` is `false` for a segment, it's still possible for attachments to be added to or removed from a segment automatically when their tags change. If this behavior is not desired, set `require-attachment-acceptance` to `true`.

**Topics**
+ [Create a shared VPC attachment](cloudwan-vpc-share-create.md)
+ [Create a shared transit gateway route table attachment](cloudwan-tgw-share.md)
+ [Create a shared Direct Connect gateway attachment](cloudwan-dx-share.md)
+ [View shared attachments](cloudwan-shared-view.md)