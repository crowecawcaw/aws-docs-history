

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner improves performance for image-based deployments on December 01, 2023
<a name="release-2023-12-01-image-deploy-performance-improvement"></a>

AWS App Runner now includes enhancements to reduce the time taken for image-based service deployment.

**Release date:** December 01, 2023

## Changes
<a name="release-2023-12-01-image-deploy-performance-improvement.changes"></a>

AWS App Runner now includes service enhancements that reduce the duration for deploying application using container images. Our benchmarks show about 30-40% reduction in deployment time depending on the container image size.

The enhancements also improve App Runner behavior when it is unable to pull a container image from the container repository. Previously, when App Runner couldn’t pull an image, it retried for ten minutes before entering a failed state. Now if App Runner is unable pull the container image, it will fail the deployment immediately and send a message with the details of the failure. 

You are not required to make any changes to your existing App Runner services to reap the benefits of these enhancements.

For more information about image deployments, see [App Runner service based on a source image](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-image.html) in the *AWS App Runner Developer Guide*. 