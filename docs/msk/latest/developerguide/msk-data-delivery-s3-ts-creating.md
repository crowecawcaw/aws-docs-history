

# Channel stuck in CREATING state
<a name="msk-data-delivery-s3-ts-creating"></a>
+ **Symptom:** The Channel remains in `CREATING` for an extended period and does not transition to `ACTIVE` or `FAILED`.
+ **Causes:** Provisioning is still in progress, or a transient service-side delay. Configuration errors cause the Channel to transition to `FAILED` rather than remain in `CREATING`. Examples include missing service-role permissions and a destination or DLQ bucket that doesn't exist.
+ **Resolution:** Allow provisioning to finish. Run `DescribeChannel` to check the state — if it is `FAILED`, read the failure detail (and Amazon CloudWatch Logs, if enabled) to identify the configuration problem, then delete and recreate the Channel. If the Channel stays in `CREATING` well beyond the expected time, contact AWS Support.