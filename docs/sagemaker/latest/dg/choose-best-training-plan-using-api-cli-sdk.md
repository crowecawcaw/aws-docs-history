# Reserve the best training

plan

After reviewing the available training plan offerings that best match your requirements,
you can reserve a specific plan by calling the [`CreateTrainingPlan`](../APIReference/API_CreateTrainingPlan.md "../APIReference/API_CreateTrainingPlan.md") API operation. When created, the plan initially
enters a `Pending` state and remains there until the reservation process is
complete. The response to the API call returns a training plan Amazon Resource Name (ARN).
Make a note of this ARN for tracking and monitoring purposes later on. The training plan
reservation is fulfilled asynchronously in the backend. The payment for the total amount is
automatically collected as part of the fulfillment process. Once the payment transaction is
completed and the requested reserved capacities are secured, the training plan is set to the
`Scheduled` state, and is ready for scheduling.

###### Important

- Training plans cannot be modified once purchased.
- Training plans cannot be shared across AWS accounts or within your AWS
  Organization.
  The following example uses the an AWS CLI command to request a specific training plan,
  passing the plan ID as a parameter.

```
aws sagemaker create-training-plan \
--training-plan-offering-id "`tpo-SHA-256-hash-value`" \
--training-plan-name "`name`" \
```

This JSON document is a sample response from the SageMaker training plans API. The response
contains the Amazon Resource Name (ARN) of the training plan that has been successfully
created.

###### Note

The training plan remains in a `Pending` status until the fulfillment
process is complete.

```
{
   "TrainingPlanArn":"arn:aws:sagemaker:us-east-1:123456789123:training-plan/large-models-fine-tuning"
}
```

The following sections define the mandatory and optional input request parameters for
the [`CreateTrainingPlan`](../APIReference/API_CreateTrainingPlan.md "../APIReference/API_CreateTrainingPlan.md") API operation.

## Required

parameters

When calling [`CreateTrainingPlan`](../APIReference/API_CreateTrainingPlan.md "../APIReference/API_CreateTrainingPlan.md") API to reserve a particular training plan,
you must provide the following values:

- `TrainingPlanOfferingId`: The ID of the plan you are choosing. You can
  retrieve the ID of a plan offering in the response of your
  `SearchTrainingPlanOfferings` API call. Its format should start with
  `pto-*`.
- `TrainingPlanName`: The name of the plan you are creating.
