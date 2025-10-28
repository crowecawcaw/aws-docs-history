# Plan, configure and launch Amazon EMR clusters

This section explains configuration options and instructions for planning, configuring,
and launching clusters using Amazon EMR. Before you launch a cluster, you make choices about your
system based on the data that you're processing and your requirements for cost, speed,
capacity, availability, security, and manageability. Your choices include:

- What region to run a cluster in, where and how to store data, and how to output results. See [Configure Amazon EMR cluster location and data
  storage](emr-cluster-location-data-storage.md "emr-cluster-location-data-storage.md").
- Whether you are running Amazon EMR clusters on Outposts or Local Zones. See [EMR clusters on AWS Outposts](emr-plan-outposts.md "emr-plan-outposts.md") or [EMR clusters on AWS Local Zones](emr-plan-localzones.md "emr-plan-localzones.md").
- Whether a cluster is long-running or transient, and what software it runs. See [Configuring an Amazon EMR cluster to continue or
  terminate after step execution](emr-plan-longrunning-transient.md "emr-plan-longrunning-transient.md") and [Configure applications when you launch your Amazon EMR cluster](emr-plan-software.md "emr-plan-software.md").
- Whether a cluster has a single primary node or three primary nodes. See [Plan and configure primary nodes in your Amazon EMR cluster](emr-plan-ha.md "emr-plan-ha.md").
- The hardware and networking options that optimize cost, performance, and availability for your application. See [Configure Amazon EMR cluster hardware and networking](emr-plan-instances.md "emr-plan-instances.md").
- How to set up clusters so you can manage them more easily, and monitor activity, performance, and health. See [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md") and [Tag and categorize Amazon EMR cluster resources](emr-plan-tags.md "emr-plan-tags.md").
- How to authenticate and authorize access to cluster resources, and how to encrypt data. See [Security in Amazon EMR](emr-security.md "emr-security.md").
- How to integrate with other software and services. See [Drivers and third-party application integration on Amazon EMR](emr-plan-third-party.md "emr-plan-third-party.md").
