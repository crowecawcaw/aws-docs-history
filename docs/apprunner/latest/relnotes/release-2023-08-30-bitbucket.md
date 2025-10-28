# Release: App Runner adds support for Bitbucket source code repository on August 30, 2023

AWS App Runner now supports building and deploying services from Bitbucket repositories.

**Release date:** August 30, 2023

## Changes

AWS App Runner now supports the capability to deploy your source code from [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/") repositories.
Bitbucket is a Git-based source code repository hosting service. App Runner now supports two source code repository providers: GitHub and Bitbucket.

App Runner takes care of starting, running, scaling, and load balancing your service. You can use the CI/CD capability of App Runner to track changes
to your source code in your Bitbucket repo. When App Runner discovers a change, it automatically builds and deploys the new version to your App Runner
service.

For more information, see [Source code repository providers](../dg/service-source-code.md#service-source-code.providers "../dg/service-source-code.md#service-source-code.providers") in
the _AWS App Runner Developer Guide_.
