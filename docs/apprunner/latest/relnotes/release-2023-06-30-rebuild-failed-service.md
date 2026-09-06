

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support to update and rebuild failed services on June 30, 2023
<a name="release-2023-06-30-rebuild-failed-service"></a>

AWS App Runner now supports updating and rebuilding failed services.

**Release date:** June 30, 2023

## Changes
<a name="release-2023-06-30-rebuild-failed-service.changes"></a>

AWS App Runner now supports updating and rebuilding a failed App Runner service. Prior to this release, if your service creation failed for any reason you had to delete the service and create a new one. This led to longer wait times to get a successful service creation. 

With this release, you no longer need to delete the service. You can rebuild the failed service with or without any changes to the source code or configuration. 

 For more information, see [Rebuilding a failed App Runner service](https://docs.aws.amazon.com/apprunner/latest/dg/manage-rebuild.html) in the *AWS App Runner Developer Guide*. 