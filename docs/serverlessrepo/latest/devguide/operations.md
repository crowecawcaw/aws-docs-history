# Operations

The AWS Serverless Application Repository REST API includes the following operations.

- [CreateApplication](applications.md#CreateApplication "applications.md#CreateApplication")

Creates an application, optionally including an AWS SAM file to create the first application version in the same call.

- [CreateApplicationVersion](applications-applicationid-versions-semanticversion.md#CreateApplicationVersion "applications-applicationid-versions-semanticversion.md#CreateApplicationVersion")

Creates an application version.

- [CreateCloudFormationChangeSet](applications-applicationid-changesets.md#CreateCloudFormationChangeSet "applications-applicationid-changesets.md#CreateCloudFormationChangeSet")

Creates an AWS CloudFormation change set for the given application.

- [CreateCloudFormationTemplate](applications-applicationid-templates.md#CreateCloudFormationTemplate "applications-applicationid-templates.md#CreateCloudFormationTemplate")

Creates an AWS CloudFormation template.

- [DeleteApplication](applications-applicationid.md#DeleteApplication "applications-applicationid.md#DeleteApplication")

Deletes the specified application.

- [GetApplication](applications-applicationid.md#GetApplication "applications-applicationid.md#GetApplication")

Gets the specified application.

- [GetApplicationPolicy](applications-applicationid-policy.md#GetApplicationPolicy "applications-applicationid-policy.md#GetApplicationPolicy")

Retrieves the policy for the application.

- [GetCloudFormationTemplate](applications-applicationid-templates-templateid.md#GetCloudFormationTemplate "applications-applicationid-templates-templateid.md#GetCloudFormationTemplate")

Gets the specified AWS CloudFormation template.

- [ListApplicationDependencies](applications-applicationid-dependencies.md#ListApplicationDependencies "applications-applicationid-dependencies.md#ListApplicationDependencies")

Retrieves the list of applications nested in the containing application.

- [ListApplications](applications.md#ListApplications "applications.md#ListApplications")

Lists applications owned by the requester.

- [ListApplicationVersions](applications-applicationid-versions.md#ListApplicationVersions "applications-applicationid-versions.md#ListApplicationVersions")

Lists versions for the specified application.

- [PutApplicationPolicy](applications-applicationid-policy.md#PutApplicationPolicy "applications-applicationid-policy.md#PutApplicationPolicy")

Sets the permission policy for an application. For the list of actions supported for this operation, see [Application Permissions](access-control-resource-based.md#application-permissions "access-control-resource-based.md#application-permissions") .

- [UnshareApplication](applications-applicationid-unshare.md#UnshareApplication "applications-applicationid-unshare.md#UnshareApplication")

Unshares an application from an AWS Organization.

This operation can be called only from the organization's management account.

- [UpdateApplication](applications-applicationid.md#UpdateApplication "applications-applicationid.md#UpdateApplication")

Updates the specified application.
