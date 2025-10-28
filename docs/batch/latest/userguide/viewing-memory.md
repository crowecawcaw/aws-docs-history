# Tutorial: View compute resource memory

You can view how much memory a compute resource registers with in the Amazon ECS console or with the [DescribeContainerInstances](../../../AmazonECS/latest/APIReference/API_DescribeContainerInstances.md "../../../AmazonECS/latest/APIReference/API_DescribeContainerInstances.md") API operation. If you're
trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular
instance type, you can observe the memory available for that compute resource and then assign your jobs that much
memory.

###### To view compute resource memory

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Choose **Clusters**, and then choose the cluster that hosts your compute resources to view.

The cluster name for your compute environment begins with
your compute environment name. 3. Choose **Infrastructure**. 4. Under **Container instances**, choose the container instance. 5. The **Resources and networking** section shows the registered and available memory for the compute
resource.

The **Total capacity** memory value is what the compute resource registered with Amazon ECS when it
was first launched, and the **Available** memory value is what hasn't already been allocated to
jobs.
