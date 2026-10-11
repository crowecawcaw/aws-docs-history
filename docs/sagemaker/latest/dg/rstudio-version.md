

# RStudio Versioning
<a name="rstudio-version"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

This guide provides information about the `2026.08.2+200.pro1` version update for RStudio on SageMaker AI. Starting September 30, 2026, new domains with RStudio support are created with Posit Workbench version `2026.08.2+200.pro1`. This applies to the `RStudioServerPro` applications and default `RSessionGateway` applications.

The following sections provide information about the `2026.08.2+200.pro1` release.

**Note**  
Confirm R version support prior to upgrading. Versions outside the supported list can be used by creating a custom image. For more information, see [Changes to BYOI Images](#rstudio-version-byoi).

## Latest version updates
<a name="rstudio-version-latest"></a>

The latest RStudio version is `2026.08.2+200.pro1`. 
+ R versions supported:
  + 4.6.1

For more information about the changes in this release, see [https://docs.posit.co/ide/news/](https://docs.posit.co/ide/news/). 

**Note**  
To ensure compatibility, we recommend using RSessions with a prefix that matches the current Posit Workbench version.  
If you use a custom (BYOI) image and see the following warning, there is a version mismatch between the `RSession` in your custom image and the Posit Workbench version used in RStudio on SageMaker AI. To resolve this issue, update your custom image so that its `RSW_VERSION` matches the current Posit Workbench version. For more information, see [Changes to BYOI Images](#rstudio-version-byoi).  

```
Session version 2025.05.1+513.pro3 does not match server version 2026.08.2+200.pro1 - this is an unsupported configuration, and you may experience unexpected issues as a result.
```

## Versioning
<a name="rstudio-version-new"></a>

There are currently two versions of Posit Workbench supported by SageMaker AI. 
+ Latest version: `2026.08.2+200.pro1`

  Deprecation Date: January 31, 2028
+ Previous version: `2025.05.1+513.pro3`

  Deprecation Date: December 5, 2026

**Note**  
You can continue creating new domains with the older version `2025.05.1+513.pro3` until December 5, 2026 by explicitly pinning the version when you create the domain through the AWS CLI. We recommend that you begin using the `2026.08.2+200.pro1` version in all domains as soon as possible.  
Versions `2024.04.2+764.pro1`, `2023.03.2-547.pro5`, and `2022.02.2-485.pro2` are deprecated and are no longer supported. We recommend updating to the latest version.

The default Posit Workbench version that SageMaker AI selects depends on the creation date of the domain. 
+ For domains created after September 30, 2026, version `2026.08.2+200.pro1` is the default selected version. 
+ For domains created after October 31, 2025 and before September 30, 2026, version `2025.05.1+513.pro3` is the default selected version. You can update your domains to the latest version (`2026.08.2+200.pro1`) by setting it as the default version for the domain. For more information, see [Upgrade to the new version](rstudio-version-upgrade.md).

**Note**  
The default `RSessionGateway` application version matches the current version of the `RStudioServerPro` application.

The following table lists the image ARNs for both versions for each AWS Region. These ARNs are passed as part of an `update-domain` command to set the desired version.


|  Region | 2025 Image ARN | 2026 Image ARN | 
| --- | --- | --- | 
| us-east-1 |  arn:aws:sagemaker:us-east-1:081325390199:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:us-east-1:081325390199:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| us-east-2 |  arn:aws:sagemaker:us-east-2:429704687514:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:us-east-2:429704687514:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| us-west-1 |  arn:aws:sagemaker:us-west-1:742091327244:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:us-west-1:742091327244:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| us-west-2 |  arn:aws:sagemaker:us-west-2:236514542706:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:us-west-2:236514542706:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| af-south-1 |  arn:aws:sagemaker:af-south-1:559312083959:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:af-south-1:559312083959:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-east-1 |  arn:aws:sagemaker:ap-east-1:493642496378:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-east-1:493642496378:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-south-1 |  arn:aws:sagemaker:ap-south-1:394103062818:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-south-1:394103062818:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-northeast-2 |  arn:aws:sagemaker:ap-northeast-2:806072073708:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-northeast-2:806072073708:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-southeast-1 |  arn:aws:sagemaker:ap-southeast-1:492261229750:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-southeast-1:492261229750:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-southeast-2 |  arn:aws:sagemaker:ap-southeast-2:452832661640:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-southeast-2:452832661640:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ap-northeast-1 |  arn:aws:sagemaker:ap-northeast-1:102112518831:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ap-northeast-1:102112518831:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| ca-central-1 |  arn:aws:sagemaker:ca-central-1:310906938811:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:ca-central-1:310906938811:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-central-1 |  arn:aws:sagemaker:eu-central-1:936697816551:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-central-1:936697816551:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-west-1 |  arn:aws:sagemaker:eu-west-1:470317259841:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-west-1:470317259841:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-west-2 |  arn:aws:sagemaker:eu-west-2:712779665605:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-west-2:712779665605:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-west-3 |  arn:aws:sagemaker:eu-west-3:615547856133:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-west-3:615547856133:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-north-1 |  arn:aws:sagemaker:eu-north-1:243637512696:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-north-1:243637512696:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| eu-south-1 |  arn:aws:sagemaker:eu-south-1:592751261982:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:eu-south-1:592751261982:image/rstudio-workbench-2026.08-sagemaker-1.0  | 
| sa-east-1 |  arn:aws:sagemaker:sa-east-1:782484402741:image/rstudio-workbench-2025.05-sagemaker-1.1  |  arn:aws:sagemaker:sa-east-1:782484402741:image/rstudio-workbench-2026.08-sagemaker-1.0  | 

### Changes to BYOI Images
<a name="rstudio-version-byoi"></a>

If you use a custom (BYOI) image with RStudio and update your `RStudioServerPro` version to `2026.08.2+200.pro1`, you must upgrade your custom images to use the `2026.08.2+200.pro1` release. You must also redeploy your existing RSessions. If you attempt to load a non-compatible image in an RSession of a domain using the `2026.08.2+200.pro1` version, the RSession fails because it cannot parse parameters that it receives. To prevent failure, update all of the deployed custom images in your existing `RStudioServerPro` application. 

You can also use a custom (BYOI) image to run R versions that are outside the supported list for the current Posit Workbench version. Build the custom image with the R version you require, and register it with your domain.

The `RSW_VERSION` in the Dockerfile must be consistent with the Posit Workbench version used in RStudio on SageMaker AI. You can validate the current version in Posit Workbench. To do so, use the version name that's located in the lower left corner of the Posit Workbench launcher page.

```
ARG RSW_VERSION=2026.08.2+200.pro1
ENV RSTUDIO_FORCE_NON_ZERO_EXIT_CODE="1"
ARG RSW_NAME=rstudio-workbench
ARG OS_CODE_NAME=jammy
ARG RSW_DOWNLOAD_URL=https://s3.amazonaws.com/rstudio-ide-build/server/${OS_CODE_NAME}/amd64
RUN RSW_VERSION_URL=`echo -n "${RSW_VERSION}" | sed 's/+/-/g'` \
    && curl -o rstudio-workbench.deb ${RSW_DOWNLOAD_URL}/${RSW_NAME}-${RSW_VERSION_URL}-amd64.deb \
    && gdebi -n ./rstudio-workbench.deb
```