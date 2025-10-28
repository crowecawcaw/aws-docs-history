# Create a SageMaker HyperPod

cluster on training plans using the SageMaker AI console

To create an SageMaker HyperPod cluster using training plans from the SageMaker AI console UI, follow
these steps:

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Hyperpod**, and then
   **Create cluster**.
3. When configuring an instance group, you can select a plan that aligns with your
   compute capacity needs.

![SageMaker AI console interface showing a modal window for creating an instance group within an SageMaker HyperPod cluster. The form includes fields for instance group name, instance type, quantity, instance capacity (with options for on-demand and training plans), and a directory path for on-create lifecycle script.](images/training-plans/tp-create-hyperpod-cluster.png)
Review and create your cluster. Instance groups using a training plan scale up to the
specified target instance count when the training plan becomes `Active`, subject to
available capacity. Thirty minutes before each Reserved Capacity period ends, the instance
group begins scaling down to zero instances. This scaled-down state persists until the next
Reserved Capacity period begins or the plan ends. Throughout this process, an healthy
instance group maintains an `InService` status after its initial creation,
regardless of the current instance count.
