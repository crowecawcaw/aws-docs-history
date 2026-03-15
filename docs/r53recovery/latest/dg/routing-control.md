# Creating a cluster in ARC

You must create a cluster to host routing controls and control panels in ARC.

A _cluster_ is a set of redundant Regional endpoints against which you can execute API calls to update or get the
state of one or more routing controls. A single cluster can host a number of routing controls.

###### Important

Be aware that you are charged by the hour for each cluster that you create. One cluster can
host a number of routing controls and control panels for recovery control management, typically enough for an application.

# To create a cluster

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Clusters**.
3. Choose **Create**, and then enter a name for your cluster.
4. Choose **Create cluster**.
