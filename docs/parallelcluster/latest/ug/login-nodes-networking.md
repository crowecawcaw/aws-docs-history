# Networking for login nodes

Login nodes are provisioned with a single connection address to the network load balancer configured for the pool of login nodes. The connectivity settings of the address are based on the type
of subnet specified in the Login nodes Pool configuration.

- If the subnet is private, the address will be private and, in order to grant access to the login nodes, the cluster administrator must provision a bastion host.
- If the subnet is public, the address will be public
  All connection requests are managed by the Network Load Balancer using round-robin routing.
