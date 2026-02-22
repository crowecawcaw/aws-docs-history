# Listeners for standard accelerators in AWS Global Accelerator

With AWS Global Accelerator, you add listeners that process inbound connections from clients based on the
ports and protocols that you specify. Listeners support TCP and UDP protocols.

You define a standard listener when you create your standard accelerator, and
you can add more listeners at any time. You associate each listener with one or more endpoint
groups, and you associate each endpoint group with one AWS Region.

Optionally, you can configure _client affinity_ for a listener. With client
affinity, Global Accelerator directs all requests from a user at a specific source (client) IP address to the same
endpoint resource. Choosing this option maintains client affinity for your users.

###### Contents

- [Add a standard listener](about-listeners.md "about-listeners.md")
- [Edit a standard listener](about-listeners.md "about-listeners.md")
- [Remove a standard listener](about-listeners.md "about-listeners.md")
- [How client affinity works in Global Accelerator](about-listeners-client-affinity.md "about-listeners-client-affinity.md")
