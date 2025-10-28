# Training plans creation

To reserve compute capacity using the SageMaker training plans capability, follow these
steps:

1. **Identify your target resource:** Begin by determining
   whether you need capacity for SageMaker training jobs or SageMaker HyperPod clusters.
2. **Specify your capacity requirements :** Define your
   capacity needs in detail. This includes selecting the appropriate instance type for your
   workload, determining the number of instances required, and specifying the duration of use.
   For information about the supported instance types in a given AWS Region, duration, and
   quantity options, see [Supported instance types,
   AWS Regions, and pricing](reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions "reserve-capacity-with-training-plans.md#training-plans-supported-instances-and-regions").
3. **Search for available training plan offerings:** Once
   you specify your requirements, use SageMaker training plans' search functionality to find available
   training plan offerings across one or more segments. Each offering includes details such as
   start time, specific availability zone for Reserved Capacity, and plan price. Review
   these offerings, considering factors like cost-effectiveness, geographical preferences, and
   alignment with your specified needs.

If no suitable plan is available, adjust your search criteria and look for a new set of
offerings. 4. **Create a training plan based on a suitable offering:**
After identifying a suitable offering, proceed to create your training plan. This process
involves selecting your chosen offering and initiating the reservation.

    * The training plan reservation creates an invoice.
    * The payment for the total amount is collected as part of the fulfillment process.
     Once the payment is completed, the plan is ready for scheduling your SageMaker training jobs
     or creating HyperPod clusters.

To learn about how to use training plans for your SageMaker training jobs , see [Training plans
utilization for SageMaker training jobs](training-plan-utilization-for-training-jobs.md "training-plan-utilization-for-training-jobs.md").

To learn about how to use training plans for your HyperPod clusters,
see [Training plans
utilization for Amazon SageMaker HyperPod clusters](training-plan-utilization-for-hyperpod.md "training-plan-utilization-for-hyperpod.md").
You can create a training plan using either the SageMaker AI console or programmatic methods. The
SageMaker AI console offers a visual, graphical interface with a comprehensive view of your options,
while programmatic creation can be done using the AWS CLI or SageMaker SDKs to interact directly with
the training plans API.

For step-by-step console instructions and detailed API references, refer to the respective
sections in this documentation.

###### Topics

- [SageMaker training plans creation using the
  SageMaker AI console](training-plan-creation-using-console.md "training-plan-creation-using-console.md")
- [SageMaker training plans creation using the
  SageMaker API, or AWS CLI](training-plan-creation-using-api-cli-sdk.md "training-plan-creation-using-api-cli-sdk.md")
