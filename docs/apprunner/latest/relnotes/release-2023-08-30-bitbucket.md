

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for Bitbucket source code repository on August 30, 2023
<a name="release-2023-08-30-bitbucket"></a>

AWS App Runner now supports building and deploying services from Bitbucket repositories.

**Release date:** August 30, 2023

## Changes
<a name="release-2023-08-30-bitbucket.changes"></a>

AWS App Runner now supports the capability to deploy your source code from [Bitbucket](https://bitbucket.org/) repositories. Bitbucket is a Git-based source code repository hosting service. App Runner now supports two source code repository providers: GitHub and Bitbucket.

App Runner takes care of starting, running, scaling, and load balancing your service. You can use the CI/CD capability of App Runner to track changes to your source code in your Bitbucket repo. When App Runner discovers a change, it automatically builds and deploys the new version to your App Runner service.

For more information, see [Source code repository providers](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.providers) in the *AWS App Runner Developer Guide*. 