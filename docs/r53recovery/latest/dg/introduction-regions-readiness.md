

# AWS Region availability for readiness check
<a name="introduction-regions-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC), see [Amazon Application Recovery Controller (ARC) endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/r53arc.html) in the *Amazon Web Services General Reference*.

**Note**  
Readiness check in Amazon Application Recovery Controller (ARC) is a global feature. However, readiness check resources are in the US West (Oregon) Region, so you must specify the US West (Oregon) Region (specify the parameter `--region us-west-2`) in Regional ARC AWS CLI commands, for example, when you create resources such as resource sets and readiness checks.