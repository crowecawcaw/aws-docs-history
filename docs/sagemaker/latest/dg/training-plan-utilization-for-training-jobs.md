# Training plans

utilization for SageMaker training jobs

You can use a SageMaker training plans for your training jobs by specifying the plan of your choice
when creating a training job.

###### Note

The training plan must be in the `Scheduled` or `Active` status to
be used by a training job.

If the required capacity is not immediately available for a training job, the job waits
until it becomes available, or until the `StoppingCondition` is met, or the job has
been `Pending` for capacity for 2 days, whichever comes first. If the stopping
condition is met, the job is stopped. If a job has been pending for 2 days, it is terminated
with an `InsufficientCapacityError`.

###### Important

**Reserved Capacity termination process:** You have full
access to all reserved instances until 30 minutes before the Reserved Capacity end time.
When there are 30 minutes remaining in your Reserved Capacity, SageMaker training plans begin the
process of terminating any running instances within that Reserved Capacity.

To ensure you don't lose progress due to these terminations, we recommend checkpointing
your training jobs.

## Checkpoint your training job

When using SageMaker training plans for your SageMaker training jobs, ensure to implement checkpointing
in your training script. This allows you to save your training progress before a
Reserved Capacity expires. Checkpointing is especially important when working with reserved
capacities, as it enables you to resume training from the last saved point if your job is
interrupted between two reserved capacities or when your training plan reaches its end
date.

To achieve this, you can use the
`SAGEMAKER_CURRENT_CAPACITY_BLOCK_EXPIRATION_TIMESTAMP` environment variable.
This variable helps determine when to initiate the checkpointing process. By incorporating
this logic into your training script, you ensure that your model's progress is saved at
appropriate intervals.

Here's an example of how you can implement this checkpointing logic in your Python
training script:

```
import os
import time
from datetime import datetime, timedelta

def is_close_to_expiration(threshold_minutes=30):
    # Retrieve the expiration timestamp from the environment variable
    expiration_time_str = os.environ.get('SAGEMAKER_CURRENT_CAPACITY_BLOCK_EXPIRATION_TIMESTAMP', '0')

    # If the timestamp is not set (default '0'), return False
    if expiration_time_str == '0':
        return False

    # Convert the timestamp string to a datetime object
    expiration_time = datetime.fromtimestamp(int(expiration_time_str))

    # Calculate the time difference between now and the expiration time
    time_difference = expiration_time - datetime.now()

    # Return True if we're within the threshold time of expiration
    return time_difference < timedelta(minutes=threshold_minutes)

def start_checkpointing():
    # Placeholder function for checkpointing logic
    print("Starting checkpointing process...")
    # TODO: Implement actual checkpointing logic here
    # For example:
    # - Save model state
    # - Save optimizer state
    # - Save current epoch and iteration numbers
    # - Save any other relevant training state

# Main training loop
num_epochs = 100
final_checkpointing_done = False
for epoch in range(num_epochs):
    # TODO: Replace this with your actual training code
    # For example:
    # - Load a batch of data
    # - Forward pass
    # - Calculate loss
    # - Backward pass
    # - Update model parameters

    # Check if we're close to capacity expiration and haven't done final checkpointing
    if not final_checkpointing_done and is_close_to_expiration():
        start_checkpointing()
        final_checkpointing_done = True

    # Simulate some training time (remove this in actual implementation)
    time.sleep(1)
print("Training completed.")
```

###### Note

- Training job provisioning follows a First-In-First-Out (FIFO) order, but a smaller
  cluster job created later might be assigned capacity before a larger cluster job created
  earlier, if the larger job cannot be fulfilled.
- SageMaker training managed warm-pool is compatible with SageMaker training plans. For cluster
  re-use, you must provide identical `TrainingPlanArn` values in subsequent
  `CreateTrainingJob` requests to reuse the same cluster.

###### Topics

- [Create a training job
  using the SageMaker AI console](use-training-plan-for-training-jobs-using-console.md "use-training-plan-for-training-jobs-using-console.md")
- [Create a training job
  using the API, AWS CLI, SageMaker SDK](use-training-plan-for-training-jobs-using-api-cli-sdk.md "use-training-plan-for-training-jobs-using-api-cli-sdk.md")
