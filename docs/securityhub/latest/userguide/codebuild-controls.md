# Security Hub controls for CodeBuild

These Security Hub controls evaluate the AWS CodeBuild service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials

**Related requirements:** NIST.800-53.r5 SA-3, PCI DSS v3.2.1/8.2.1, PCI DSS v4.0.1/8.3.2

**Category:** Protect > Secure development

**Severity:** Critical

**Resource type:**
`AWS::CodeBuild::Project`

**AWS Config rule:**
[`codebuild-project-source-repo-url-check`](../../../config/latest/developerguide/codebuild-project-source-repo-url-check.md "../../../config/latest/developerguide/codebuild-project-source-repo-url-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS CodeBuild project Bitbucket source repository URL contains
personal access tokens or a user name and password. The control fails if the Bitbucket source repository URL
contains personal access tokens or a user name and password.

###### Note

This control evaluates both the primary source and secondary sources of a CodeBuild build project. For more information
about project sources, see [Multiple input sources and output artifacts sample](../../../codebuild/latest/userguide/sample-multi-in-out.md "../../../codebuild/latest/userguide/sample-multi-in-out.md")
in the _AWS CodeBuild User Guide_.

Sign-in credentials shouldn't be stored or transmitted in clear text or appear in
the source repository URL. Instead of personal access tokens or sign-in credentials, you should access your source
provider in CodeBuild, and change your source repository URL to contain only the path to the Bitbucket repository
location. Using personal access tokens or sign-in credentials could result in unintended data exposure or
unauthorized access.

### Remediation

You can update your CodeBuild project to use OAuth.

###### To remove basic authentication / (GitHub) Personal Access Token from CodeBuild project

source

1. Open the CodeBuild console at
   [https://console.aws.amazon.com/codebuild/](https://console.aws.amazon.com/codebuild/ "https://console.aws.amazon.com/codebuild/").
2. Choose the build project that contains personal access tokens or a user name and
   password.
3. From **Edit**, choose **Source**.
4. Choose **Disconnect from GitHub / Bitbucket**.
5. Choose **Connect using OAuth**, then choose **Connect to GitHub
   / Bitbucket**.
6. When prompted, choose **authorize as appropriate**.
7. Reconfigure your repository URL and additional configuration settings, as needed.
8. Choose **Update source**.

For more information, refer to [CodeBuild use case-based
samples](../../../codebuild/latest/userguide/use-case-based-samples.md "../../../codebuild/latest/userguide/use-case-based-samples.md") in the _AWS CodeBuild User Guide_.

## [CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials

**Related requirements:** NIST.800-53.r5 IA-5(7), NIST.800-53.r5 SA-3, PCI DSS v3.2.1/8.2.1, PCI DSS v4.0.1/8.3.2

**Category:** Protect > Secure development

**Severity:** Critical

**Resource type:**
`AWS::CodeBuild::Project`

**AWS Config rule:**
[`codebuild-project-envvar-awscred-check`](../../../config/latest/developerguide/codebuild-project-envvar-awscred-check.md "../../../config/latest/developerguide/codebuild-project-envvar-awscred-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the project contains the environment variables
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

Authentication credentials `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` should never be stored in clear text, as this could lead to
unintended data exposure and unauthorized access.

### Remediation

To remove environment variables from a CodeBuild project, see [Change a build project's settings in AWS CodeBuild](../../../codebuild/latest/userguide/change-project.md "../../../codebuild/latest/userguide/change-project.md") in the _AWS CodeBuild User Guide_.
Ensure nothing is selected for **Environment variables**.

You can store environment variables with sensitive values in the AWS Systems Manager Parameter Store or AWS Secrets Manager and then retrieve them from
your build spec. For instructions, see the box labeled **Important** in the [Environment section](../../../codebuild/latest/userguide/change-project-console.md#change-project-console-environment "../../../codebuild/latest/userguide/change-project-console.md#change-project-console-environment") in the _AWS CodeBuild User Guide_.

## [CodeBuild.3] CodeBuild S3 logs should be encrypted

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SI-7(6), PCI DSS v4.0.1/10.3.2

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Low

**Resource type:**
`AWS::CodeBuild::Project`

**AWS Config rule:**
[`codebuild-project-s3-logs-encrypted`](../../../config/latest/developerguide/codebuild-project-s3-logs-encrypted.md "../../../config/latest/developerguide/codebuild-project-s3-logs-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon S3 logs for an AWS CodeBuild project are encrypted. The control fails if encryption is deactivated
for S3 logs for a CodeBuild project.

Encryption of data at rest is a recommended best practice to add a layer of access management around your data.
Encrypting the logs at rest reduces the risk that a user not authenticated by AWS will access the data stored on disk.
It adds another set of access controls to limit the ability of unauthorized users to access the data.

### Remediation

To change the encryption settings for CodeBuild project S3 logs, see [Change a build project's settings in AWS CodeBuild](../../../codebuild/latest/userguide/change-project.md "../../../codebuild/latest/userguide/change-project.md") in the _AWS CodeBuild User Guide_.

## [CodeBuild.4] CodeBuild project environments should have a logging AWS Configuration

**Related requirements:** NIST.800-53.r5 AC-2(12), NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-9(7), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4, NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::CodeBuild::Project`

**AWS Config rule:**
[`codebuild-project-logging-enabled`](../../../config/latest/developerguide/codebuild-project-logging-enabled.md "../../../config/latest/developerguide/codebuild-project-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a CodeBuild project environment has at least one log option, either to S3 or CloudWatch logs enabled. This control fails if a CodeBuild project environment does not have at least one log option enabled.

From a security perspective, logging is an important feature to enable for future forensics efforts in the case of any security incidents. Correlating anomalies in CodeBuild projects with threat detections can increase confidence in the accuracy of those threat detections.

### Remediation

For more information on how to configure CodeBuild project log settings, see [Create a build project (console)](../../../codebuild/latest/userguide/create-project-console.md#create-project-console-logs "../../../codebuild/latest/userguide/create-project-console.md#create-project-console-logs") in the CodeBuild User Guide.

## [CodeBuild.5] CodeBuild project environments should not have privileged mode enabled

###### Important

Security Hub retired this control in April 2024.
For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md "controls-change-log.md").

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2)

**Category:** Protect > Secure Access Management

**Severity:** High

**Resource type:**
`AWS::CodeBuild::Project`

**AWS Config rule:**
[`codebuild-project-environment-privileged-check`](../../../config/latest/developerguide/codebuild-project-environment-privileged-check.md "../../../config/latest/developerguide/codebuild-project-environment-privileged-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS CodeBuild project environment has privileged mode enabled or disabled. The control fails if
an CodeBuild project environment has privileged mode enabled.

By default, Docker containers do not allow access to any devices. Privileged mode grants a build project's Docker
container access to all devices. Setting `privilegedMode` with value `true` permits the Docker daemon to run
inside a Docker container. The Docker daemon listens for Docker API requests and manages Docker objects such as images, containers,
networks, and volumes. This parameter should only be set to true if the build project is used to build Docker images. Otherwise,
this setting should be disabled to prevent unintended access to Docker APIs as well as the container's underlying hardware.
Setting `privilegedMode` to `false` helps protect critical resources from tampering and deletion.

### Remediation

To configure CodeBuild project environment settings, see [Create a build project (console)](../../../codebuild/latest/userguide/create-project-console.md#create-project-console-environment "../../../codebuild/latest/userguide/create-project-console.md#create-project-console-environment") in the _CodeBuild User Guide_. In the
**Environment** section, don't select the **Privileged** setting.

## [CodeBuild.7] CodeBuild report group exports should be encrypted at rest

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::CodeBuild::ReportGroup`

**AWS Config rule:**
[`codebuild-report-group-encrypted-at-rest`](../../../config/latest/developerguide/codebuild-report-group-encrypted-at-rest.md "../../../config/latest/developerguide/codebuild-report-group-encrypted-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the test results of an AWS CodeBuild report group that are exported to an Amazon Simple Storage Service (Amazon S3)
bucket are encrypted at rest. The control fails if the report group export isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To encrypt the report group export to S3, see [Update a report group](../../../codebuild/latest/userguide/report-group-export-settings.md "../../../codebuild/latest/userguide/report-group-export-settings.md") in
the _AWS CodeBuild User Guide_.
