# Identifying network

resources

This section is intended for the network engineer who is responsible for connecting the
MediaLive Anywhere nodes to your organization's network. The network engineer performs these task in
consultation with the video engineer who designs the MediaLive Anywhere channels.

Follow these steps for each cluster that the video engineer has identified.

###### Topics

- [Identify networks](#emla-identify-networks "#emla-identify-networks")
- [Reserve CIDRs](#emla-reserve-cidrs "#emla-reserve-cidrs")
- [Identify routes](#emla-identify-routes "#emla-identify-routes")
- [Identify default route](#emla-identify-default-route "#emla-identify-default-route")
- [Summary of data](#emla-deploy-requirements-summary "#emla-deploy-requirements-summary")

## Identify networks

Identify at least one network for each cluster. The number of networks you require
depends on the rules that your network follows for traffic. A typical way to handle MediaLive Anywhere
traffic is the following:

- One network for MediaLive Anywhere management.
- One network for all push inputs into the nodes.
- One network for all outputs from the nodes.

You don't need to identify separate networks for each cluster. The same type of traffic
(for example, input traffic) in all the clusters can go over the same network.

## Reserve CIDRs

Your video engineer must provide you with information so that you can calculate the
number of IP addresses to reserve for the nodes in the cluster:

- The total number of push inputs in all the channels in the cluster. MediaLive Anywhere assigns
  IP addresses to each push input.
- The total number of outputs in all the output groups in all the channels. Note that
  you need the number of outputs, which might be more than the number of output groups.
  MediaLive Anywhere assigns source IP addresses for these outputs.

In each network, reserve one or more CIDR blocks for these IP addresses. If your network
is set up so that push inputs and outputs are on the same network, note that the two types
of traffic will share the same pool.

## Identify routes

MediaLive Anywhere needs to be configured with information about all routes that are first-hop out
of a node interface and last-hop into a node interface.

Provide the video engineer with these routes. Provide the routes as a CIDR block and a
Gateway (if applicable).

## Identify default route

Identify one of the routes as the default route for traffic to and from the node. MediaLive Anywhere
uses this default when the destination for the traffic isn't covered by the route table for
any of the networks.

## Summary of data

Here is a summary of the information that you should have collected for each cluster.
Provide this information to the user who will configure MediaLive Anywhere.

| Data                                                                                                                                                                                                                                                                  | Where to set up this data in MediaLive Anywhere |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Number of network for this cluster, and purpose of each network                                                                                                                                                                                                       | When creating the network                       |
| In each network, list of CIDR blocks to reserve for MediaLive Anywhere                                                                                                                                                                                                | When creating the network                       |
| Routes for each network                                                                                                                                                                                                                                               | When creating the network                       |
| The following set of information for each network interface on the<br>node:<br>• A type of encoding traffic on the network<br>• The ID of the network that handles that traffic<br>• A logical interface name to assign to the network interfaces on all the<br>nodes | When creating the node                          |
| The default route for all nodes on the cluster                                                                                                                                                                                                                        | When creating the cluster                       |
| Initial role of each node in the cluster (active or backup)                                                                                                                                                                                                           | When creating the node                          |
