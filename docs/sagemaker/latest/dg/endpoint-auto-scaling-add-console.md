# Configure model auto scaling with

the console

###### To configure auto scaling for a model (console)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the navigation pane, choose **Inference**, and then choose
   **Endpoints**.
3. Choose your endpoint, and then for **Endpoint runtime
   settings**, choose the variant.
4. Choose **Configure auto scaling**.
5. On the **Configure variant automatic scaling** page, for
   **Variant automatic scaling**, do the following:
   1. For **Minimum instance count**, type the minimum
      number of instances that you want the scaling policy to maintain. At
      least 1 instance is required.
   2. For **Maximum instance count**, type the maximum
      number of instances that you want the scaling policy to maintain.

6. For **Built-in scaling policy**, do the following:
   1. For the **Target metric**,
      `SageMakerVariantInvocationsPerInstance` is automatically
      selected for the metric and cannot be changed.
   2. For the **Target value**, type the average number of
      invocations per instance per minute for the model. To determine this
      value, follow the guidelines in [Load testing](endpoint-scaling-loadtest.md "endpoint-scaling-loadtest.md").
   3. (Optional) For **Scale-in cool down (seconds)** and
      **Scale-out cool down (seconds)**, enter the amount
      of time, in seconds, for each cool down period.
   4. (Optional) Select **Disable scale in** if you don’t
      want auto scaling to terminate instances when traffic decreases.

7. Choose **Save**.
   This procedure registers a model as a scalable target with Application Auto Scaling. When you register
   a model, Application Auto Scaling performs validation checks to ensure the following:

- The model exists
- The permissions are sufficient
- You aren't registering a variant with an instance that is a burstable
  performance instance such as T2

###### Note

SageMaker AI doesn't support auto scaling for burstable instances such as T2,
because they already allow for increased capacity under increased workloads.
For information about burstable performance instances, see [Amazon EC2 instance
types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
