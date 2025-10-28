# Release: App Runner increases the maximum instance startup time to five minutes on December 07, 2023

AWS App Runner now supports maximum five minutes of instance startup time.

**Release date:** December 07, 2023

## Changes

The maximum time available for your AWS App Runner instance to complete its startup tasks has increased from one to five minutes.
This update provides your applications with an additional time of virtual CPU (vCPU) allocation to complete the startup.

With this increase, you can now use App Runner to host applications that require more startup time to complete initialization.
For example, you can now run services with lower compute configuration whose startup tasks complete more slowly.

For more information, see [Code development guidelines](../dg/develop.md#develop.tips "../dg/develop.md#develop.tips") in the
_AWS App Runner Developer Guide_.
