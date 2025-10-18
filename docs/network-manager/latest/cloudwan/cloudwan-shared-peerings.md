# Shared peerings in AWS Cloud WAN

Shared peering allows you to establish peering connections between your Cloud WAN core
 network and transit gateways in the same AWS Region. You can dynamically exchange routing
 and reachability information between your core network edge and transit gateway over these
 peering connections, and interconnect your existing transit gateway-based network with your
 Cloud WAN network. You can create a new transity gateway policy table for this new shared
 peering or you can choose an existing transit gatewa policy table to use. 

When a core network owner shares their core network with your account, you are then able
 to create new peerings for the shared core network, delete existing peerings, or manage the
 tags associated with a peering. When you create a shared peering you can choose the core
 network that you want to associate the peering with, the edge location, and any transit
 gateways you want to share in this peering. In addition, you can also choose whether to
 create a new policy table for the shared peering or to use an existing policy table. If you
 choose an existing table, you'll be prompted to supply the transit gateway policy table to
 use. 

###### Topics

* [Create a shared peering](cloudwan-peerings-share-create.md "cloudwan-peerings-share-create.md")
* [Delete a shared peering](cloudwan-peerings-share-delete.md "cloudwan-peerings-share-delete.md")
* [Edit tags for a shared peering](cloudwan-peerings-share-tags.md "cloudwan-peerings-share-tags.md")
