

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for redirecting HTTP requests to HTTPS endpoints on February 22, 2023
<a name="release-2023-02-22-http-https-support"></a>

**Release date:** February 22, 2023

## Changes
<a name="release-2023-02-22-http-https-support.changes"></a>

App Runner now supports automatic redirection of incoming HTTP web requests to their corresponding HTTPS App Runner endpoints. Previously, only incoming HTTPS web requests were supported. All incoming HTTP web requests to your App Runner service failed with a timeout status response. With this release, you receive the flexibility to use both HTTP and HTTPS endpoints to access the applications on your App Runner service. 

For more information, see [Developing application code for App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/develop.html) in the *AWS App Runner Developer Guide*.