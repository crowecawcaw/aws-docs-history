

# Beanstalk Cluster
<a name="beanstalk-cluster"></a>

Run an application on Elastic Beanstalk without provisioning or operating the compute underneath it. You provide a container image or source code; Elastic Beanstalk creates and operates the environment that runs it.

Beanstalk Cluster is an Elastic Beanstalk environment type with service-operated compute. Applications can be supplied as container images or as source code that Elastic Beanstalk builds into images. Elastic Beanstalk creates the environment, deploys the application, applies rolling updates, scales the number of application replicas, and reports environment health. Server provisioning, patching, scaling, and compute-platform management are handled by Elastic Beanstalk.

With Beanstalk Cluster, you use the same Elastic Beanstalk application, application version, environment, and configuration option concepts as Beanstalk Standard. Beanstalk Standard runs your application on EC2 instances that you configure through the `aws:autoscaling:*` and `aws:elasticbeanstalk:environment` configuration namespaces. In Beanstalk Cluster, the application runs as containers on an Amazon EKS cluster that Elastic Beanstalk creates and operates. Configure their behavior through the top-level `aws:elasticbeanstalk:eks` namespace and its child namespaces. For the differences from Beanstalk Standard, see [Beanstalk Cluster architecture](beanstalk-cluster-concepts.md).

**Topics**
+ [Next steps](#beanstalk-cluster-next-steps)
+ [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md)
+ [Beanstalk Cluster architecture](beanstalk-cluster-concepts.md)
+ [Multi-tenancy for Beanstalk Cluster environments](beanstalk-cluster-multi-tenancy.md)
+ [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md)
+ [Scaling Beanstalk Cluster environments](configuring-cluster-scaling.md)
+ [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md)
+ [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md)
+ [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md)

**Important**  
A Beanstalk Cluster environment requires you to provide a cluster IAM role that Amazon EKS assumes and a node IAM role that the cluster's Amazon EC2 nodes assume. Elastic Beanstalk creates the Amazon EKS cluster with those roles, assigns your environment to it, and manages the application running in it. Environments in the same account that use the same subnets share one cluster. For the resources you provide and how clusters are shared, see [Beanstalk Cluster architecture](beanstalk-cluster-concepts.md).

## Next steps
<a name="beanstalk-cluster-next-steps"></a>

To create an application and environment, follow [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md). To review the compute and deployment model, including how environments are grouped onto shared clusters, see [Beanstalk Cluster architecture](beanstalk-cluster-concepts.md). To choose an isolation boundary between environments and control which of them can communicate, see [Multi-tenancy for Beanstalk Cluster environments](beanstalk-cluster-multi-tenancy.md). To package an application as a container image, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).