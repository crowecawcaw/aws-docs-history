AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime artifacts

AWS Blu Age Runtime artifacts are the components for deploying and running modernized applications. This
document outlines the different types of artifacts available, their storage locations, and
how to access them.

## AWS Blu Age Runtime (non-managed) artifacts

### Artifacts access and

storage

The AWS Blu Age Runtime artifacts for non-managed deployments are stored in region-specific S3
buckets. Each version has its own dedicated folder, allowing for easy version
management and access.

There are two types of buckets:

**Release buckets**

Release buckets contain directories for the most recently deployed versions and
follow the naming convention:
`aws-bluage-runtime-artifacts-<accountId>-<region>`.

**Pre-release buckets**

Pre-release buckets contain directories for alpha versions corresponding to the
latest short-lived incremental pre-releases and follow the naming convention: `convention: aws-bluage-runtime-artifacts-dev-<accountId>-<region>`.

Access to the Production and to the Pre-release buckets are granted independently.
For more information on how to request access, and more details about the S3 bucket
organization, see [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .

### Artifacts contents

In both Release and Pre-release buckets, you'll find:

**aws-bluage-runtime-x.y.z.tar.gz**

This archive, where x.y.z represents the version number (`major.minor.patch` as
per semantic versioning, see [AWS Blu Age versioning](ba-versioning.md "ba-versioning.md")), and contains the core
AWS Blu Age Runtime components essential for executing AWS Blu Age applications, including:

- **Gapwalk**: A crucial component of the
  AWS Blu Age Runtime, designed to bridge the gap between legacy applications
  and modern cloud-native environments. It serves as a compatibility layer
  that allows applications modernized by AWS Blu Age to run effectively on
  contemporary platforms.
- **bluage.bin**: The core binary file of
  the AWS Blu Age Runtime. This file is critical for the operation of the
  runtime.
- All necessary libraries and supporting files for the AWS Blu Age Runtime
  operation.

**aws-bluage-webapps-x.y.z.tar.gz**

This archive, where x.y.z follows the same versioning scheme as above, includes
web applications and libraries necessary for managing and controlling AWS Blu Age
deployments:

- **BAC** (Blusam console) WAR file, which is
  used for monitoring the Blusam database.
- **JAC** (JICS console) WAR file, used for
  monitoring the JICS database.
- Necessary supporting libraries.

### Additional files

- Checksum files that let you verify integrity for both Blu Age archives
  following the naming convention:
  - For Runtime:
    `aws-bluage-runtime-x.y.z.tar.gz.checksumSHA256`
  - For Webapps:
    `aws-bluage-webapps-x.y.z.tar.gz.checksumSHA256`

- CVE report files (For the release versions only) list the present CVEs on
  this version and follow the naming convention:
  - For Runtime:
    `Bluage-Runtime-x.y.z-CVEs.txt`
  - For Webapps:
    `Bluage-Webapps-x.y.z-CVEs.txt`

For details on how security vulnerabilities are addressed, see [AWS Mainframe Modernization Refactor with AWS Blu Age release
overview](lifecycle-m2.md#lifecycle-ba-overview "lifecycle-m2.md#lifecycle-ba-overview").

###### Note

While we strive to release our products without CVEs, new CVEs may appear
later on. The CVE report file is updated regularly to reflect the latest
status.

## Developer AWS Blu Age Runtime artifacts

### Artifacts access and

storage

The AWS Blu Age Developer Runtime artifacts are stored in dedicated S3 buckets.
This runtime includes both Release and Alpha pre-release versions. Access to these
artifacts is managed through AWS Blu Age toolbox requests. Once your request is
processed and approved, you'll be granted access to the appropriate bucket from the
AWS account specified in your request.

**Developer Runtime bucket**

The main bucket for the Developer Runtime is:
`s3://toolbox-dev-runtime`

For more detailed information on requesting access and understanding the bucket
structure, see [Dev and Special AWS Blu Age Runtimes](https://bluinsights.aws/docs/dev-special-bluage-runtime "https://bluinsights.aws/docs/dev-special-bluage-runtime") documentation.

### Artifact

contents

Developer runtime artifacts typically include:

**gapwalk-x.y.z-dev.tar.gz**

This archive contains the development version of the Gapwalk component, which is a
crucial part of the AWS Blu Age Runtime. It's designed to bridge legacy applications
with modern cloud-native environments.

**gapwalk-runtime-x.y.z-javadoc.zip**

This zip file contains the JavaDoc documentation for the Gapwalk runtime. JavaDoc
provides detailed API documentation, which is especially useful for developers working
on integrating or extending the Gapwalk runtime.

**gapwalk-webapps-x.y.z-javadoc.zip**

Similar to the runtime JavaDoc, this zip file contains the JavaDoc documentation
specifically for the Gapwalk web applications. This documentation is crucial for
developers working with or customizing the web-based components of the Gapwalk
system.
