

# Beanstalk Cluster architecture
<a name="beanstalk-cluster-concepts"></a>

Beanstalk Cluster uses the same Elastic Beanstalk application, application version, environment, and configuration option concepts as Beanstalk Standard. Beanstalk Standard is the EC2-based environment type. Beanstalk Cluster uses a different compute layer and configuration surface. This topic describes the differences by aspect and identifies the applicable environment type.

## Compute model
<a name="beanstalk-cluster-compute"></a>

In Beanstalk Standard, Elastic Beanstalk launches Amazon Elastic Compute Cloud (Amazon EC2) instances in an Auto Scaling group dedicated to the environment. The application runs directly on those instances. In a Beanstalk Cluster environment, Elastic Beanstalk instead runs the application as a container image on an Amazon EKS cluster that can be shared by your Beanstalk Cluster environments. Elastic Beanstalk creates and operates the cluster. Elastic Beanstalk schedules the application onto the cluster. Elastic Beanstalk isolates each environment on the cluster and reconciles the number of application replicas to match the configured values. You do not create a cluster, choose which cluster an environment runs on, or select its Kubernetes version.

Several of your environments can run on the same Amazon EKS cluster. Elastic Beanstalk places an environment on the cluster that serves the configured VPC subnets. It creates a cluster the first time those subnets are used; see [Environment grouping](#beanstalk-cluster-clusters-sharing). Amazon EKS Auto Mode provides node capacity. It adds and removes nodes to fit the containers that are scheduled. Because the cluster can be shared and node capacity is managed by Amazon EKS, instance counts are not configured through the `aws:autoscaling:asg` namespace. Instead, the number of application replicas is set with the `min-replica` and `max-replica` options in the `aws:elasticbeanstalk:eks:environment:autoscaling` namespace. For the replica bounds and the triggers that change the replica count, see [Scaling Beanstalk Cluster environments](configuring-cluster-scaling.md).

Elastic Beanstalk resolves the environment's configuration from the option settings that you supply, and applies the resolved configuration when it creates or updates the environment. When the same configuration option is supplied more than once, the last occurrence wins. To change the configuration, update the option settings.

## Differences from Beanstalk Standard
<a name="beanstalk-cluster-differences"></a>

The following table summarizes the customer-facing differences between Beanstalk Standard and a Beanstalk Cluster environment. Each row links to the topic that covers the Elastic Beanstalk concept in depth.


| Aspect | Beanstalk Standard | Beanstalk Cluster environment | 
| --- | --- | --- | 
| Compute | Dedicated Amazon EC2 instances in an Auto Scaling group configured through the aws:autoscaling:\* namespaces. | Containers scheduled onto an Amazon EKS cluster that can be shared by your Beanstalk Cluster environments. Elastic Beanstalk isolates each environment on the cluster. Nodes are provided by Amazon EKS Auto Mode. | 
| Scaling | Amazon EC2 instances added and removed by an Auto Scaling group, with triggers and scheduled actions configured through the aws:autoscaling:\* namespaces. See [Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.as.md). | Application replicas added and removed within the min-replica and max-replica bounds, on CPU, memory, a schedule, or a metric that your own endpoint reports. See [Scaling Beanstalk Cluster environments](configuring-cluster-scaling.md). | 
| Deployment artifact | A source bundle that Elastic Beanstalk runs on a platform (solution stack) AMI. See [Elastic Beanstalk supported platforms](concepts.platforms.md). | A container image in Amazon Elastic Container Registry (Amazon ECR). The image is provided directly, or source is provided for Elastic Beanstalk to build into an image. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md). | 
| Platform concept | A managed solution stack (operating system, web server, and language runtime on an AMI). See [Elastic Beanstalk supported platforms](concepts.platforms.md). | No solution stack or AMI. The runtime is defined by the container image and the version of the cluster Elastic Beanstalk creates. | 
| Deployment policy | All-at-once, rolling, or immutable deployments configured through the aws:elasticbeanstalk:command namespace. | A rolling update (the default) or all at once, configured with the strategy option in the aws:elasticbeanstalk:eks:environment:deployment namespace. The option value for all at once is Recreate. | 
| Configuration namespaces | Classic namespaces such as aws:autoscaling:\* and aws:elasticbeanstalk:environment. See [Configuration options](command-options.md). | The aws:elasticbeanstalk:eks:\* namespaces. None of the classic compute namespaces apply. | 
| Health | Reported from the host manager and load balancer on each instance. | Per-instance health is not reported. With an Application Load Balancer, health includes the load balancer metrics that Elastic Beanstalk evaluates. With load-balancer-type=None, that request-rate, error-rate, and latency evaluation does not apply. See [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md). | 

## Customer-provided and service-managed resources
<a name="beanstalk-cluster-resources"></a>

Elastic Beanstalk creates and operates the Amazon EKS cluster that runs a Beanstalk Cluster environment. The cluster and node AWS Identity and Access Management (IAM) roles required by Amazon EKS are customer-provided. We recommend that you use the role names and AWS managed policies described in [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md), because Elastic Beanstalk requires every environment on a cluster to supply the same roles. An application role can also be provided for the running application through Amazon EKS Pod Identity. The application role is selected in the Elastic Beanstalk console during environment creation. For the complete IAM responsibility model and application-role procedure, see [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).

VPC subnets for the environment are optional. When subnets are omitted, Elastic Beanstalk uses the public subnets of the default VPC. The subnet set determines which cluster runs the environment. For cluster assignment and the infrastructure that Elastic Beanstalk operates, see [Environment grouping](#beanstalk-cluster-clusters-sharing).

Elastic Beanstalk operates the application on the service-created cluster. It deploys the container image and applies rolling updates through the `aws:elasticbeanstalk:eks:environment:deployment` namespace. It reconciles the running number of application replicas to the `min-replica` and `max-replica` bounds in the configuration. It reports environment-level health through the health statuses described in [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md). Elastic Beanstalk tracks each cluster it assigns environments to as service-managed.

**Important**  
Elastic Beanstalk assigns environments only to clusters that match the expected service-managed configuration. If the infrastructure no longer matches that configuration, Elastic Beanstalk stops selecting the cluster for new environments. Environment changes are made through Elastic Beanstalk operations and configuration.

## Application requirements and limitations
<a name="beanstalk-cluster-when-to-use"></a>

A Beanstalk Cluster environment requires an application that can run as a container image and as one or more identical, interchangeable replicas. A load balancer is optional. When a load balancer is configured, it distributes requests across application replicas. A stateless web service or API whose replicas hold no local state that must survive a restart meets this requirement. The request port, CPU and memory requests, number of application replicas, and deployment behavior are configured through the `aws:elasticbeanstalk:eks:*` options. Elastic Beanstalk provides the cluster capacity through Amazon EKS Auto Mode.

Confirm the following application requirements and limitations before creating a Beanstalk Cluster environment:
+ Local storage is not persistent. Each copy of the application has ephemeral storage that is lost when the copy restarts. An application that writes uploads, caches, or working files to the local disk and requires them to survive a restart is incompatible without external persistent storage.
+ Requests are distributed across the application replicas.
+ Elastic Beanstalk builds a container image from source for supported languages. You can also provide a Dockerfile or a prebuilt image. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

## Configuration example
<a name="beanstalk-cluster-example"></a>

The following AWS CLI request sets the request port, memory request, number of running replicas, and deployment behavior for a Beanstalk Cluster environment. The settings use the `aws:elasticbeanstalk:eks:*` namespaces.

```
$ aws elasticbeanstalk update-environment \
    --environment-name my-cluster-env \
    --option-settings \
        Namespace=aws:elasticbeanstalk:eks:environment,OptionName=service-port,Value=8080 \
        Namespace=aws:elasticbeanstalk:eks:environment,OptionName=memory,Value=1Gi \
        Namespace=aws:elasticbeanstalk:eks:environment,OptionName=load-balancer-type,Value=ALB \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling,OptionName=min-replica,Value=3 \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling,OptionName=max-replica,Value=3 \
        Namespace=aws:elasticbeanstalk:eks:environment:deployment,OptionName=strategy,Value=RollingUpdate \
        Namespace=aws:elasticbeanstalk:eks:environment:deployment:strategy:rolling,OptionName=max-surge,Value=25% \
        Namespace=aws:elasticbeanstalk:eks:environment:deployment:strategy:rolling,OptionName=max-unavailable,Value=0
```

The `strategy` option accepts `RollingUpdate` or `Recreate`, which the console shows as a rolling update and as all at once. With `RollingUpdate`, `max-surge` bounds how many extra replicas Elastic Beanstalk starts during a deployment. The `max-unavailable` option bounds how many existing replicas it takes down at a time. Each option accepts a count or a percentage. The `memory` value uses Kubernetes quantity notation, such as `1Gi` or `512Mi`. For the full set of options, see [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

## Environment grouping
<a name="beanstalk-cluster-clusters-sharing"></a>

Elastic Beanstalk groups your Beanstalk Cluster environments onto clusters by the VPC subnets they use:
+ Environments in the same AWS account that use the same set of subnets run on the *same* cluster.
+ An environment that uses a different set of subnets runs on a *different* cluster.

The first environment you create with a given set of subnets causes Elastic Beanstalk to create a cluster for it, which takes about ten minutes. Elastic Beanstalk reports this in the environment's events:

```
INFO  Creating CloudFormation stack for cluster infrastructure. This is a one-time operation and generally takes about 10 minutes. stack='beanstalk-cluster-{{uuid}}'
INFO  Starting cluster assignment. environment='my-cluster-env'
INFO  Successfully completed cluster assignment. environment='my-cluster-env' clusterArn='arn:aws:eks:us-east-1:{{111122223333}}:cluster/beanstalk-cluster-{{uuid}}'
```

Elastic Beanstalk places later environments that use the same subnets on that existing cluster. Their events report the assignment without the stack-creation message. Elastic Beanstalk names both the cluster and the AWS CloudFormation stack that creates it `beanstalk-cluster-{{uuid}}`.

The order in which Elastic Beanstalk considers subnets does not matter; the same subnets in a different order are the same set. Only the subnet set selects the cluster. When a cluster is already registered for the subnet set, the cluster and node role settings that you provide must match the roles registered for that cluster. Elastic Beanstalk rejects conflicting role settings; different role ARNs do not select a different cluster. You supply the observability role as well, and Elastic Beanstalk validates it against the cluster in the same way. The optional application role belongs to the environment and can differ between environments. Configure it with the environment-creation procedure in [Configure an application role](beanstalk-cluster-permissions.md#beanstalk-cluster-permissions-application-role).

Elastic Beanstalk does not limit how many environments share a cluster. Amazon EKS Auto Mode adds nodes to fit the containers scheduled on the cluster. Cluster sharing does not add an environment-specific scaling limit. Each environment remains subject to its configured replica or autoscaling limits, applicable service quotas, and available capacity. To run an environment on a separate cluster, create it with a different set of subnets.

**Important**  
You cannot change the subnets or the cluster, node, and observability roles of an existing Beanstalk Cluster environment. Elastic Beanstalk rejects such an update rather than moving your environment to a different cluster, and reports: `Changes to EKS cluster configuration (subnets and IAM roles) are not currently supported for an existing environment. Please revert these option settings to continue.` To move an application to different subnets or roles, create a new environment with the settings that you want, and then swap the two environment CNAMEs. See [Blue/Green deployments with Elastic Beanstalk](using-features.CNAMESwap.md). Decide which subnets and cluster roles an environment uses when you create it. See [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md).

## Isolation between environments that share compute
<a name="beanstalk-cluster-isolation-pointer"></a>

Subnets are the primary boundary between environments. Because the subnet set selects the cluster, giving a group of environments its own subnets gives that group its own cluster, its own nodes, and its own network. Within a single cluster, Elastic Beanstalk isolates network traffic between Beanstalk Cluster environments by default, and options in the `aws:elasticbeanstalk:eks:environment` namespace let you permit specific environments to communicate or place an environment on dedicated nodes.

For the boundary each choice gives you, the options that widen it, and what a shared cluster does not separate, see [Multi-tenancy for Beanstalk Cluster environments](beanstalk-cluster-multi-tenancy.md).

## Managed infrastructure configuration
<a name="beanstalk-cluster-clusters-config"></a>

Elastic Beanstalk creates each cluster with a fixed configuration that you do not choose:


| Setting | What Elastic Beanstalk configures | 
| --- | --- | 
| Kubernetes version | Elastic Beanstalk selects the version at cluster creation. Elastic Beanstalk creates a new cluster with the most recent Kubernetes version that it supports. An environment on an existing cluster runs the version that cluster already has. That version remains fixed for the life of the cluster. | 
| Node capacity | Amazon EKS Auto Mode, which adds and removes nodes to fit the containers scheduled on the cluster. Node-capacity configuration is service-managed. | 
| Cluster infrastructure access | Service-managed. Configure the environment through the Elastic Beanstalk API, the AWS CLI, or the Elastic Beanstalk console. | 
| Cluster add-ons | Elastic Beanstalk installs and pins the add-ons your environment relies on. When Elastic Beanstalk introduces a new pinned add-on version, it applies the update to your cluster during a subsequent environment create or update. You do not plan or apply the update yourself. | 

Because Elastic Beanstalk sets these itself, you configure your *application* through the `aws:elasticbeanstalk:eks:*` options rather than configuring the cluster. See [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

## Cluster configuration drift
<a name="beanstalk-cluster-clusters-drift"></a>

Elastic Beanstalk operates a cluster it created only while that cluster matches the expected service-managed configuration. If the infrastructure no longer matches that configuration, Elastic Beanstalk detects configuration drift, pauses cluster maintenance, and reports an environment event:

```
ERROR  Cluster drift detected for environment 'my-cluster-env'. {{what changed}}. Service will skip cluster maintenance for this environment.
```

While a cluster is drifted:
+ Elastic Beanstalk does not place new environments on it.
+ Elastic Beanstalk no longer maintains it, including service-managed add-on version updates.
+ Updates to the environments already running on it fail.

Drift is recoverable. To recover, revert the change that caused it, so that the cluster matches the configuration that Elastic Beanstalk expects again. The drift event names what changed, which tells you what to revert. Elastic Beanstalk re-evaluates the cluster on the next environment operation, and resumes managing it when the configuration matches. Retry the operation that failed.

If you can't restore the expected configuration, contact AWS Support.

To avoid drift, make environment changes through Elastic Beanstalk operations and configuration options rather than by changing the cluster directly. See [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

## Cluster deletion
<a name="beanstalk-cluster-clusters-lifecycle"></a>

Elastic Beanstalk schedules cluster deletion three hours after you terminate its last environment. If you create another environment with the same subnets during this interval, Elastic Beanstalk cancels the pending cleanup and reuses the existing cluster.

**To verify service-managed infrastructure deletion**

1. Before terminating the last environment, record the cluster ARN through Elastic Beanstalk. For service-created Cluster infrastructure, the CloudFormation template sets the cluster name to the stack name. The name after the final slash of the cluster ARN therefore identifies the stack for the read-only deletion verification in this procedure:

   ```
   $ aws elasticbeanstalk describe-environment-resources \
       --environment-name my-cluster-env \
       --query 'EnvironmentResources.Cluster.Name'
   ```

   The command returns the cluster ARN. The stack name is the portion of the ARN after its final slash.
**Important**  
The derived stack name is only for the read-only CloudFormation waiter and describe operations shown below. Do not pass it to `delete-stack`, `update-stack`, or any other operation that changes service-managed infrastructure.

   Record the cluster ARN and the derived stack name; you use them for the read-only verification steps that follow.

1. Terminate the environment and verify that it reaches `Terminated` by following the steps in [Terminate an Elastic Beanstalk environment](using-features.terminating.md). Cluster cleanup starts separately after the three-hour reuse interval; environment termination does not wait for cluster deletion.

1. After three hours, use an IAM principal with permission to describe the service-created stack. The CloudFormation waiter uses read-only stack descriptions every 30 seconds for up to 60 minutes and succeeds when the stack no longer exists:

   ```
   $ aws cloudformation wait stack-delete-complete \
       --stack-name {{cluster-stack-name}}
   ```

   The waiter succeeds when the stack no longer exists. If it fails, the stack still exists after the deadline; use `aws cloudformation describe-stacks` and `aws cloudformation describe-stack-events` to inspect the stack status and any `DELETE_FAILED` events.

1. If the waiter reports that the stack still exists after the deadline, determine whether another environment reused the cluster. List the active Beanstalk Cluster environments in the account and Region:

   ```
   $ aws elasticbeanstalk describe-environments \
       --query "Environments[?Tier.Name=='Cluster' && Tier.Type=='EKS'].EnvironmentName"
   ```

   For each listed environment, read its cluster ARN:

   ```
   $ aws elasticbeanstalk describe-environment-resources \
       --environment-name {{environment-name}} \
       --query 'EnvironmentResources.Cluster.Name'
   ```

   An environment whose cluster ARN matches the recorded cluster ARN means that deletion was canceled for reuse. If no environment matches, use the stack status and `DELETE_FAILED` events to diagnose retained resources. Do not manually delete or modify a service-managed stack. Contact AWS Support if the stack remains after the deadline without an active environment or an actionable CloudFormation failure.