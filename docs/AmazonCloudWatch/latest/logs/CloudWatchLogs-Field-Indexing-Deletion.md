# Effects of deleting a field index policy

If you delete a field index policy that has been in effect for a time, the
following happens:

- For up to 30 days after the policy is deleted, queries can still benefit
  from the indexed log events.
- If you delete a log-group level index policy, and there is already an
  account-level policy in place that would apply to that log group, the
  account-level policy will eventually apply to that log group.
