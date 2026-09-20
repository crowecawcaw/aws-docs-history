

# Elastic Beanstalk cluster environments
<a name="concepts-cluster"></a>

With a Beanstalk Cluster environment, Elastic Beanstalk runs your application as containers on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that it creates and operates. You provide a container image, or source code that Elastic Beanstalk builds into an image. Elastic Beanstalk provisions the cluster, deploys your application, applies rolling updates, scales the number of running replicas, and reports environment health. You use the same Elastic Beanstalk application, application version, environment, and configuration option concepts as a Beanstalk Standard environment.

The following diagram depicts two Beanstalk Cluster environments sharing an Amazon EKS cluster.

![Two Beanstalk Cluster environments for one Elastic Beanstalk application share a service-operated Amazon EKS cluster because they are in the same AWS account and use the same VPC subnet set. Each environment has an optional Application Load Balancer and isolated application replicas. Amazon EKS Auto Mode supplies shared node capacity.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-overview-cluster.png)


Consider a Beanstalk Cluster environment when you want the benefits of container orchestration such as faster deployments, faster autoscaling, improved resource utilization when running multiple environments, and managed OpenTelemetry integration.

For more information on Beanstalk Cluster infrastructure, and the IAM roles that a Beanstalk Cluster environment uses, see [Beanstalk Cluster](beanstalk-cluster.md).