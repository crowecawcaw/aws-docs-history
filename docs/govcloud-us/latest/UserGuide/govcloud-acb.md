# AWS CodeBuild in AWS GovCloud (US)

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue. You can get started quickly by using prepackaged build environments, or you can create custom build environments that use your own build tools. With CodeBuild, you are charged by the minute for the compute resources you use.

## How AWS CodeBuild differs for AWS GovCloud (US)

- The ARM environment types are not available in the AWS GovCloud (US) Regions.
- The Linux GPU environment types are not available in the AWS GovCloud (US) Regions.
- The `2xlarge` compute type is not available in the AWS GovCloud (US) Regions.
- The ability to pause a running build and then use AWS Systems Manager Session Manager to connect to the build container is not available in the AWS GovCloud (US) Regions.
- The public builds feature of CodeBuild is not available in the AWS GovCloud (US) Regions.
- Windows managed and custom images are not available in the AWS GovCloud (US) Regions.
- Batch Configuration is not available in the AWS GovCloud (US) Regions.
- Compute Fleets are not available in AWS GovCloud (US) Regions.

## Documentation for AWS CodeBuild

[AWS CodeBuild documentation](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
