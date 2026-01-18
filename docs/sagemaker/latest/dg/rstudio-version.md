# RStudio Versioning

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

This guide provides information about the `2025.05.1+513.pro3` version update
for RStudio on SageMaker AI. Starting October 31, 2025, new domains with RStudio support are
created with Posit Workbench version `2025.05.1+513.pro3`. This
applies to the `RStudioServerPro` applications and default
`RSessionGateway` applications.

The following sections provide information about the `2025.05.1+513.pro3`
release.

## Latest version updates

The latest RStudio version is `2025.05.1+513.pro3`.

- R versions supported:
  - 4.5.1
  - 4.4.3
  - 4.4.0
  - 4.3.3
  - 4.2.3
  - 4.2.1
  - 4.1.3
  - 4.0.2

For more information about the changes in this release, see [https://docs.posit.co/ide/news/](https://docs.posit.co/ide/news/ "https://docs.posit.co/ide/news/").

###### Note

To ensure compatibility, we recommend using RSessions with a prefix that matches
the current Posit Workbench version.

If you see the following warning, there is a version mismatch between the
`RSession` and the Posit Workbench version used in
RStudio on SageMaker AI. To resolve this issue, update the RStudio
version for the domain. For information about updating the RStudio version, see
[Upgrade to the new version](rstudio-version-upgrade.md "rstudio-version-upgrade.md").

```
Session version 2024.04.2+764.pro1 does not match server version 2025.05.1+513.pro3 - this is an unsupported configuration, and you may experience unexpected issues as a result.
```

## Versioning

There are currently two versions of Posit Workbench supported by SageMaker AI.

- Latest version: `2025.05.1+513.pro3`

Deprecation Date: December 5, 2026

- Previous version: `2024.04.2+764.pro1`

Deprecation Date: April 30, 2026

###### Note

While you can continue creating new domains with the older version `2024.04.2+764.pro1` until 04/30/2026
by explicitly pinning the version when you create the domain using CLI, we strongly recommend customers to begin using the
`2025.05` version in all domains. POSIT has ceased providing vulnerability fixes for `2024.04.2+764.pro1`.

Versions `2023.03.2-547.pro5` and `2022.02.2-485.pro2` are deprecated and are no longer supported.
We recommend updating to the latest version.

The default Posit Workbench version that SageMaker AI selects depends on the
creation date of the domain.

- For domains created after October 31, 2025, version
  `2025.05.1+513.pro3` is the default selected version.
- For domains created after September 04, 2024 and before October 31, 2025,
  version `2024.04.2+764.pro1` is the default selected version. You can
  update your domains to the latest version (`2025.05.1+513.pro3`) by
  setting it as the default version for the domain. For more information, see
  [Upgrade to the new version](rstudio-version-upgrade.md "rstudio-version-upgrade.md").

###### Note

The default `RSessionGateway` application version matches the current version of
the `RStudioServerPro` application.

The following table lists the image ARNs for both versions for each AWS Region.
These ARNs are passed as part of an `update-domain` command to set the
desired version.

| Region         | `2024.04.2+764.pro1` Image ARN                                                | `2025.05.1+513.pro3` Image ARN                                                              |
| -------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| us-east-1      | arn:aws:sagemaker:us-east-1:081325390199:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:us-east-1:081325390199:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| us-east-2      | arn:aws:sagemaker:us-east-2:429704687514:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:us-east-2:429704687514:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| us-west-1      | arn:aws:sagemaker:us-west-1:742091327244:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:us-west-1:742091327244:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| us-west-2      | arn:aws:sagemaker:us-west-2:236514542706:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:us-west-2:236514542706:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| af-south-1     | arn:aws:sagemaker:af-south-1:559312083959:image/rstudio-workbench-2024.04     | arn:aws:sagemaker:af-south-1:559312083959:image/rstudio-workbench-2025.05-sagemaker-1.0     |
| ap-east-1      | arn:aws:sagemaker:ap-east-1:493642496378:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:ap-east-1:493642496378:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| ap-south-1     | arn:aws:sagemaker:ap-south-1:394103062818:image/rstudio-workbench-2024.04     | arn:aws:sagemaker:ap-south-1:394103062818:image/rstudio-workbench-2025.05-sagemaker-1.0     |
| ap-northeast-2 | arn:aws:sagemaker:ap-northeast-2:806072073708:image/rstudio-workbench-2024.04 | arn:aws:sagemaker:ap-northeast-2:806072073708:image/rstudio-workbench-2025.05-sagemaker-1.0 |
| ap-southeast-1 | arn:aws:sagemaker:ap-southeast-1:492261229750:image/rstudio-workbench-2024.04 | arn:aws:sagemaker:ap-southeast-1:492261229750:image/rstudio-workbench-2025.05-sagemaker-1.0 |
| ap-southeast-2 | arn:aws:sagemaker:ap-southeast-2:452832661640:image/rstudio-workbench-2024.04 | arn:aws:sagemaker:ap-southeast-2:452832661640:image/rstudio-workbench-2025.05-sagemaker-1.0 |
| ap-northeast-1 | arn:aws:sagemaker:ap-northeast-1:102112518831:image/rstudio-workbench-2024.04 | arn:aws:sagemaker:ap-northeast-1:102112518831:image/rstudio-workbench-2025.05-sagemaker-1.0 |
| ca-central-1   | arn:aws:sagemaker:ca-central-1:310906938811:image/rstudio-workbench-2024.04   | arn:aws:sagemaker:ca-central-1:310906938811:image/rstudio-workbench-2025.05-sagemaker-1.0   |
| eu-central-1   | arn:aws:sagemaker:eu-central-1:936697816551:image/rstudio-workbench-2024.04   | arn:aws:sagemaker:eu-central-1:936697816551:image/rstudio-workbench-2025.05-sagemaker-1.0   |
| eu-west-1      | arn:aws:sagemaker:eu-west-1:470317259841:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:eu-west-1:470317259841:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| eu-west-2      | arn:aws:sagemaker:eu-west-2:712779665605:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:eu-west-2:712779665605:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| eu-west-3      | arn:aws:sagemaker:eu-west-3:615547856133:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:eu-west-3:615547856133:image/rstudio-workbench-2025.05-sagemaker-1.0      |
| eu-north-1     | arn:aws:sagemaker:eu-north-1:243637512696:image/rstudio-workbench-2024.04     | arn:aws:sagemaker:eu-north-1:243637512696:image/rstudio-workbench-2025.05-sagemaker-1.0     |
| eu-south-1     | arn:aws:sagemaker:eu-south-1:592751261982:image/rstudio-workbench-2024.04     | arn:aws:sagemaker:eu-south-1:592751261982:image/rstudio-workbench-2025.05-sagemaker-1.0     |
| sa-east-1      | arn:aws:sagemaker:sa-east-1:782484402741:image/rstudio-workbench-2024.04      | arn:aws:sagemaker:sa-east-1:782484402741:image/rstudio-workbench-2025.05-sagemaker-1.0      |

### Changes to BYOI Images

If you use a BYOI image with RStudio and update your `RStudioServerPro`
version to `2025.05.1+513.pro3`, you must upgrade your custom images to use
the `2025.05.1+513.pro3` release and redeploy your existing RSessions. If
you attempt to load a non-compatible image in an RSession of a domain using
the `2025.05.1+513.pro3` version, the RSession fails because it cannot
parse parameters that it receives. To prevent failure, update all of the deployed custom
images in your existing `RStudioServerPro` application.

The `RSW_VERSION` in the Dockerfile must be consistent with
the Posit Workbench version used in RStudio on SageMaker AI. You can validate the
current version in Posit Workbench. To do so, use the version name that's
located in the lower left corner of the Posit Workbench launcher
page.

```
ARG RSW_VERSION=2025.05.1+513.pro3
ENV RSTUDIO_FORCE_NON_ZERO_EXIT_CODE="1"
ARG RSW_NAME=rstudio-workbench
ARG OS_CODE_NAME=jammy
ARG RSW_DOWNLOAD_URL=https://s3.amazonaws.com/rstudio-ide-build/server/${OS_CODE_NAME}/amd64
RUN RSW_VERSION_URL=`echo -n "${RSW_VERSION}" | sed 's/+/-/g'` \
    && curl -o rstudio-workbench.deb ${RSW_DOWNLOAD_URL}/${RSW_NAME}-${RSW_VERSION_URL}-amd64.deb \
    && gdebi -n ./rstudio-workbench.deb
```
