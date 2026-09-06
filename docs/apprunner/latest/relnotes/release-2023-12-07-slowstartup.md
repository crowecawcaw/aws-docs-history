

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner increases the maximum instance startup time to five minutes on December 07, 2023
<a name="release-2023-12-07-slowstartup"></a>

AWS App Runner now supports maximum five minutes of instance startup time.

**Release date:** December 07, 2023

## Changes
<a name="release-2023-12-07-slowstartup.changes"></a>

The maximum time available for your AWS App Runner instance to complete its startup tasks has increased from one to five minutes. This update provides your applications with an additional time of virtual CPU (vCPU) allocation to complete the startup.

With this increase, you can now use App Runner to host applications that require more startup time to complete initialization. For example, you can now run services with lower compute configuration whose startup tasks complete more slowly.

For more information, see [Code development guidelines](https://docs.aws.amazon.com/apprunner/latest/dg/develop.html#develop.tips) in the *AWS App Runner Developer Guide*.