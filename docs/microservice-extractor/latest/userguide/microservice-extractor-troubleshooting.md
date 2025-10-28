AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Troubleshooting

AWS Microservice Extractor for .NET

The following remediation strategies can help you troubleshoot problems with
AWS Microservice Extractor for .NET.

###### Troubleshooting topics:

- [AWS profile errors](#troubleshooting-failure-profile-checker "#troubleshooting-failure-profile-checker")
- [Build failures](#troubleshooting-build "#troubleshooting-build")
- [Extraction errors](#troubleshooting-extraction "#troubleshooting-extraction")
- [Application artifact location](#troubleshooting-logs "#troubleshooting-logs")
- [Onboarding and visualization errors](#troubleshooting-onboarding "#troubleshooting-onboarding")
- [Creating groups](#troubleshooting-groups "#troubleshooting-groups")
- [Uninstalling application](#troubleshooting-uninstalling "#troubleshooting-uninstalling")
- [Metrics and logs collected by
  AWS Microservice Extractor for .NET](#troubleshooting-metrics-logs "#troubleshooting-metrics-logs")
- [Questions and feedback](#troubleshooting-questions "#troubleshooting-questions")

## AWS profile errors

###### Description

An error regarding the specified AWS profile is returned. For example:

```
The specified AWS profile is invalid or does not have permission to send metrics to AWS. Please refer to the Microservice Extractor User Guide for instructions on how to setup a valid AWS profile for use with Microservice Extractor.
```

**Solution**

- Verify that you your user has the required permissions. To view the required
  policies, see the [Microservice Extractor prerequisites](microservice-extractor-prerequisites.md "microservice-extractor-prerequisites.md").

To provide access, add permissions to your users, groups, or roles:

    + Users and groups in AWS IAM Identity Center:


    Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the *AWS IAM Identity Center User Guide*.
    + Users managed in IAM through an identity provider:


    Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
     in the *IAM User Guide*.
    + IAM users:




    	- Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
    	- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

- Add a named AWS profile with proper credentials, if required. For more
  information, see [Named
  profiles](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles") in the _AWS CLI User Guide_.

## Build failures

###### Description

The build fails when you attempt to build your repositories.

###### Solution

Verify the following:

- The application is supported by Microservice Extractor. See [Prerequisites for analysis and extraction of monolithic application](microservice-extractor-prerequisites.md#microservice-extractor-prerequisites-analysis-extraction "microservice-extractor-prerequisites.md#microservice-extractor-prerequisites-analysis-extraction")
  to view the application prerequisites.
- You have installed MSBuild, and Microservice Extractor is pointing to it on the
  **Settings** page.
- MSBuild is working properly. Check the MSBuild log on the
  **Application details** page. If there is no preview, or
  choosing the log returns an error, then MSBuild is likely failing. Verify that
  you can build the application manually to see if MSBuild is working
  properly.
- Microservice Extractor is using the same MSBuild version as your installed version of
  Visual Studio. If the versions don't match, you can update the MSBuild version
  used by Microservice Extractor from the **Settings** page.
- Relevant switches are added to the .csproj file so that the default msbuild
  operation can use them. By default, Microservice Extractor appends the
  `RestorePackagesConfig` and `restore` switches to
  restore NuGet packages during build.

## Extraction errors

###### Description

When you attempt to extract segments of your code as independent services, an
error is returned.

###### Solution

For the following error:

```
Command failed: failed to run build command on ...\MyApp.sln: failed to execute command: exec: "msbuild": executable file not found in %PATH%
```

- Verify that you have installed MSBuild and Microservice Extractor is pointing to it on
  the **Settings** page.
- Add MSBuild to the system path environment variable.

**Check logs**

- You can determine the cause of most extraction failures by viewing
  ``%USERPORFILE%`\AppData\Roaming\ServiceExtract\logs\Extraction\extract\*log`.
  Generally, the last line in this file contains a message with the cause of the
  error.
- If the error message in the log refers to a build failure, check
  ``%USERPORFILE%`\AppData\Roaming\ServiceExtract\logs\msbuild.log`for details. Note that the extraction builds both the new service and the
modified original application. The output of each of these builds is sent to`msbuild.log`.

## Application artifact location

To determine the application artifact file location, do the following:

1. Find the application ID in the **Summary** section of the
   **Application details** page.
2. The directory of the corresponding application is:
   `C:\Users\`<username>`\AppData\Roaming\ServiceExtract\version-1\cache\version-`<versionNumber>`\`<applicationId>``

## Onboarding and visualization errors

If you are encountering problems onboarding an application and viewing the
visualization, try the following solutions:

1. The metric policy may not be properly configured. Check the Electron main
   application log to check for the last succeeded state and high-level errors. If
   the metrics policy is not properly configured, the log file should display many
   error messages about metrics.
2. Check the directory of the corresponding application ID for the following
   intermediate artifact files: `edges.csv` and
   `vertices.csv` inside of the `data-extraction-output`
   folder.

## Creating groups

If you experience problems when creating groups, perform the following steps:

1. Check in the directory for the corresponding application ID for the following
   intermediate artifact file: `tags.csv` inside of the
   `tags-data` folder.
2. Verify that the groupings are correctly reflected in the file.
3. Choose **Reset view** to remove all of the groups, and try
   again.

## Uninstalling application

If you encounter issues when attempting to uninstall the application as a non-admin
user when using the **Apps and Features** interface in Windows, perform
the following steps:

1. Open **Control Panel**>**Uninstall a
   program**. Or, choose the **Windows**
   icon>**Run**> and enter `appwiz.cpl`.
2. Choose **AWS Microservice Extractor for .NET** from the list of installed
   applications, and select **Uninstall** to remove the
   application and its installation files.

## Metrics and logs collected by

AWS Microservice Extractor for .NET

AWS Microservice Extractor for .NET collects the following files from
`C:\Users\`<username>`\AppData\Roaming\ServiceExtract\logs`
on the server or desktop where the tool runs:

- `logs*.log`
- `logs\ProcessOrchestrator*.log`
- `logs\Extraction*.log`
- `logs\PortingAssistant*.log`

## Questions and feedback

If you have questions that are not addressed in the AWS Microservice Extractor for .NET technical
documentation, contact
`<aws-microservice-extractor-support@amazon.com>`.

You can also provide feedback by choosing **Feedback** in the upper
right-hand corner of this page.
