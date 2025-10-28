# Resilience in ROSA

## AWS global infrastructure resilience

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking.
With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption.
Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

ROSA provides customers with the option to run the Kubernetes control plane and data plane in a single AWS Availability Zone, or across multiple Availability Zones.
While Single-AZ clusters can be useful for experimentation, customers are encouraged to run their workloads in more than one Availability Zone.
This ensures that applications can withstand even a complete Availability Zone failure - a very rare event in itself.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](http://aws.amazon.com/about-aws/global-infrastructure/ "http://aws.amazon.com/about-aws/global-infrastructure/").

## ROSA cluster resilience

The ROSA control plane consists of at least three OpenShift control plane nodes.
Each control plane node is made up of an API server instance, an `etcd` instance, and controllers.
In the event of a control plane node failure, all API requests are automatically routed to the other available nodes to ensure cluster availability.

The ROSA data plane consists of at least two OpenShift infrastructure nodes and two OpenShift worker nodes.
Infrastructure nodes run pods that support OpenShift cluster infrastructure components such as the default router, the built-in OpenShift registry, and the components for cluster metrics and monitoring.
OpenShift worker nodes run end-user application pods.

Red Hat site reliability engineers (SREs) fully manage the control plane and infrastructure nodes.
Red Hat SREs proactively monitor the ROSA cluster, and are responsible for replacing any failed control plane nodes and infrastructure nodes.
For more information, see [Overview of responsibilities for ROSA](rosa-responsibilities.md "rosa-responsibilities.md").

###### Important

Because ROSA is a managed service, Red Hat is responsible for managing the underlying AWS infrastructure that ROSA uses.
Customers should not attempt to manually shut down the Amazon EC2 instances that ROSA uses from the AWS console or AWS CLI.
This action can lead to customer data loss.

If a worker node fails on the data plane, the control plane relocates unscheduled pods to the functioning worker node(s) until the failed node is recovered or replaced.
Failed worker nodes can be replaced manually or automatically by enabling automatic scaling of machines in a cluster.
For more information, see [Cluster autoscaling](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/cluster_administration/rosa-cluster-autoscaling "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/cluster_administration/rosa-cluster-autoscaling") in the Red Hat documentation.

## Customer-deployed application resilience

Although ROSA provides many protections to ensure high availability of the service, customers are responsible for building their deployed applications for high availability to protect workloads against downtime.
For more information, see [About availability for ROSA](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#about-availability-for-rosa "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#about-availability-for-rosa") in the Red Hat documentation.
