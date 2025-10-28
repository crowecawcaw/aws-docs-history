# AWS Region availability for readiness check

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC),
see [Amazon Application Recovery Controller (ARC)
endpoints and quotas](../../../general/latest/gr/r53arc.md "../../../general/latest/gr/r53arc.md") in the _Amazon Web Services General Reference_.

###### Note

Readiness check in Amazon Application Recovery Controller (ARC) is a global feature. However, readiness check resources are in
the US West (Oregon) Region, so you must specify the US West (Oregon)
Region (specify the parameter `--region us-west-2`) in Regional ARC AWS CLI commands, for
example, when you create resources such as resource sets and readiness checks.
