# AWS Cloud WAN prefix list associations

You can use customer managed prefix lists in your Cloud WAN routing policy to simplify rules management. You need to associate your prefix list with the core network with the create-core-network-prefix-list-association API. The prefix list must be defined in the Cloud WAN home region (us-west-2). Although defined in Cloud WAN home region, the prefix-list based policy will apply globally to all the relevant core network edges (regions) in your core network.

Before you can create a prefix list association, you must first have created a prefix
list. For more information about creating prefix lists, see [Consolidate and manage network CIDR
blocks with managed prefix lists](../../../vpc/latest/userguide/managed-prefix-lists.md "../../../vpc/latest/userguide/managed-prefix-lists.md") in the _Amazon Virtual Private Cloud User
Guide_.

###### Note

Creating or deleting prefix list associations will move the state of your core network to updating. The status of the association is based on the core network state, once it is finished updating the association will either be fully available or deleted.
