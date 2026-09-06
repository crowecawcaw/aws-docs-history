

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Viewing health check association status in Shield Advanced
<a name="health-check-association-status"></a>

You can see the status of the health check that's associated with a protection on the AWS WAF & Shield console **Protected resources** page and on the details page of each resource. 
+ **Healthy** – The health check is available and is reporting healthy.
+ **Unhealthy** – The health check is available and is reporting unhealthy.
+ **Unavailable** – The health check is not available for use by Shield Advanced. 

**To resolve an **Unavailable** health check**

Create and use a new health check. Don't try to associate a health check again after it has had a status of unavailable in Shield Advanced. 

For detailed guidance on following these steps, see the preceding topics. 

1. In Shield Advanced, disassociate the health check from the resource. 

1. In Route 53, create a new health check for the resource and note its ID. For information, see [Creating and Updating Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating.html) in the Amazon Route 53 Developer Guide.

1. In Shield Advanced, associate the new health check with the resource. 