# Storage for login nodes

All shared storage configured on the cluster using ParallelCluster including managed storage will be mounted on all the login nodes.

**Retrieve login nodes information**

To retrieve the address of the single connection provisioned to access the login nodes, the cluster administrator can run the [describe-cluster](pcluster.md "pcluster.md") command. The command will also provide more information about the status of
the login nodes.

Login nodes are a new node type supported by ParallelCluster that can be specified with the [describe-cluster-instances](pcluster.md "pcluster.md") command when querying the status of a specific node type.

The availability of a single connection address to the Login nodes pool doesn’t prevent direct access to a specific login node. However, it is not recommended to use the direct connection to
avoid warnings from the ssh client. The ssh client stores host identifiers locally for each target address. Since the host identifier is specific per pool, use of different IPs and/or the single
connection address may have the same host identifier associated with different target addresses: this may cause warning from the ssh client since the same host identifier is associated multiple
targets.
