

# Optimal instance type configuration to receive automatic instance family updates
<a name="optimal-default-instance-troubleshooting"></a>

AWS Batch supported a single option in **instanceTypes** for `optimal` to match the demand of your job queues. We've introduced two new instance type options: `default_x86_64` and `default_arm64`. We will use `default_x86_64` if you make no instance type selection. These new options will automatically select cost-effective instance types across different families and generations based on your job queue requirements, allowing you to get your workloads running quickly.

The `optimal` option now selects instance types from modern m, c, and r instance families based on regional availability. AWS Batch periodically updates the pool with newer generations within these families. If you are using `optimal`, no action is needed on your part.

However, please be aware that only `ENABLED` and `VALID` Compute Environments (CEs) will be updated with new instance types. If you have any `DISABLED` or `INVALID` CEs, they will receive updates once they are re-enabled and set to a `VALID` state.