# Global and core networks in AWS Cloud WAN

A core network owner can maintain all aspects of global and core networks, including
 viewing, deleting, and updating tags for both global and core networks. 

For example, you might need to delete a global network if you've reached the maximum
 number of global networks for your account. The default number of global networks per
 account is 5, but you can request an increase. If your global network has an associated core
 network, you'll first need to delete the core network and any of its network resources. Once deleted, a global network can't be retrieved. You'll need to create that global network again. See [General](cloudwan-quotas.md#cloudwan-quotas-general.html "cloudwan-quotas.md#cloudwan-quotas-general.html") on the AWS Cloud WAN Quotas page. 

Each global network can have only one core network associated with it. You can't request
 an increase for more than one core network. If you want to add a new core network to an
 existing global network without creating a new global network, you'll first need to delete
 the existing core network. Before deleting the core network, you must first delete all
 network resources from that core network. A deleted core network can't be retrieved. You'll
 need to recreate that core network again.

###### Topics

* [View global network information](cloudwan-global-view.md "cloudwan-global-view.md")
* [Delete a global network](cloudwan-global-network-delete.md "cloudwan-global-network-delete.md")
* [View core network information](cloudwan-core-network-view.md "cloudwan-core-network-view.md")
* [Delete a core network](cloudwan-core-network-delete.md "cloudwan-core-network-delete.md")
