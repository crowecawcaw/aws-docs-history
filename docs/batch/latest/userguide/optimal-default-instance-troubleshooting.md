# Optimal instance type configuration to

receive automatic instance family updates

###### Note

Starting on 11/01/2025 the behavior of `optimal` is going to be changed to
match `default_x86_64`. During the change your instance families could be
updated to a newer generation. You do not need to perform any actions for the upgrade to
happen.

AWS Batch supported a single option in **instanceTypes** for `optimal` to match
the demand of your job queues. We've introduced two new instance type options:
`default_x86_64` and `default_arm64`. We will use `default_x86_64` if
you make no instance type selection. These new options will automatically select
cost-effective instance types across different families and generations based on your job
queue requirements, allowing you to get your workloads running quickly.

As sufficient capacity of new instance types become available in an AWS Region, the
corresponding default pool will be automatically updated with the new instance type. The
existing `optimal` option will continue to be supported and is not being
deprecated, as it will be supported by the underlying default pools to provide updated
instances going forward. If you are using '`optimal`, no action is needed on your
part.

However, please be aware that only `ENABLED` and `VALID` Compute Environments (CEs) will be
automatically updated with new instance types. If you have any `DISABLED` or `INVALID` CEs, they
will receive updates once they are re-enabled and set to a `VALID` state.
