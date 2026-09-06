

# Create the clusters
<a name="emla-setup-cl-create"></a>

Create the clusters after you have created the networks. 

1. In the navigation bar, choose MediaLive Anywhere, then choose **Cluster**. On the **Cluster** page, choose **Create cluster**. 

1. Complete the fields:
   + **Name**: We recommend that you assign a name that hints at the types of nodes in the cluster.
   + **Instance role ARN**: You must choose an instance role for MediaLive. Obtain the ARN from the AWS administrative user for your organization. For information about this instance role, see [Creating the instance role](emla-deploy-instance-role.md). 
   + **Interface mappings**: See [Designing mappings for node interfaces](emla-design-mappings.md).
   + **Default route**: Select the logical interface name (from the **Interface mappings**) that is the default that the network engineer identified in [Identifying network resources](emla-deploy-identify-network-requirements.md).

1. Choose Create. MediaLive Anywhere creates the cluster and adds it to the list of clusters. 