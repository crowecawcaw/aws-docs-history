# Prescriptive guidance to integrate DAX with DynamoDB applications

[DynamoDB Accelerator](DAX.md "DAX.md") (DAX), is a DynamoDB-compatible caching service that provides fast in-memory performance for demanding applications, such as read-heavy applications. Using DAX, you can achieve response times in microseconds for accessing frequently requested data. This DynamoDB Accelerator prescriptive guide provides comprehensive insights and best practices for integrating DAX with your DynamoDB applications.

This guide provides foundational knowledge for those who are new to DAX or want to optimize their existing configurations. This guide covers various topics, for example, when to use DAX and creating a [DAX cluster](DAX.concepts.md#DAX.concepts.clusters "DAX.concepts.md#DAX.concepts.clusters"). It also includes practical examples and detailed explanations to help you effectively implement DAX in your projects. Finally, this guide offers advanced strategies that you need to implement to maximize DAX caching capabilities for ensuring fast and scalable applications.

###### Topics

- [Evaluating the suitability of DAX for your use cases](evaluate-dax-suitability.md "evaluate-dax-suitability.md")
- [Configuring your DAX client](dax-config-dax-client.md "dax-config-dax-client.md")
- [Configuring your DAX cluster](dax-config-considerations.md "dax-config-considerations.md")
- [Sizing your DAX cluster](dax-cluster-sizing.md "dax-cluster-sizing.md")
- [Deploying a cluster](dax-deploy-cluster.md "dax-deploy-cluster.md")
- [Managing cluster operations](dax-cluster-operations.md "dax-cluster-operations.md")
- [Monitoring DAX](pres-guide-monitor-dax.md "pres-guide-monitor-dax.md")
