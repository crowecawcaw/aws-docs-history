# Channel stuck in CREATING state

- **Symptom:** The Channel remains in `CREATING` for an extended period and does not transition to `ACTIVE` or `FAILED`.
- **Causes:** Provisioning is still in progress, or a transient service-side delay. Configuration errors — such as missing service-role permissions, a destination or DLQ bucket that doesn't exist, or (for plain JSON) a schema that can't be resolved from GSR — cause the Channel to transition to `FAILED` rather than remain in `CREATING`. For `JSON_SCHEMA_GSR`, an unresolvable schema is detected during delivery, not at creation.
- **Resolution:** Allow provisioning to finish. Run `DescribeChannel` to check the state — if it is `FAILED`, read the failure detail (and Amazon CloudWatch Logs, if enabled) to identify the configuration problem, then delete and recreate the Channel. If the Channel stays in `CREATING` well beyond the expected time, contact AWS Support.
