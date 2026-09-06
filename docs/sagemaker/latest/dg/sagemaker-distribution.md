

# SageMaker Studio image support policy
<a name="sagemaker-distribution"></a>

**Important**  
Currently, all packages in SageMaker Distribution images are licensed for use with Amazon SageMaker AI and do not require additional commercial licenses. However, this might be subject to change in the future, and we recommend reviewing the licensing terms regularly for any updates.

Amazon SageMaker Distribution is a set of Docker images available on SageMaker Studio that include popular frameworks for machine learning, data science, and visualization.

The images include deep learning frameworks like PyTorch, TensorFlow and Keras; popular Python packages like numpy, scikit-learn and pandas; and IDEs like JupyterLab and Code Editor, based on Code-OSS, Visual Studio Code - Open Source. The distribution contains the latest versions of all these packages such that they are mutually compatible.

This page details the support policy and availability for SageMaker Distribution Images on SageMaker Studio.

## Versioning, release cadence, and support policy
<a name="sm-distribution-versioning"></a>

For details on versioning, release cadence, support policy, supported image versions, and unsupported image versions, see the [Amazon SageMaker Distribution support policy](https://github.com/aws/sagemaker-distribution/blob/main/support_policy.md) on GitHub.

### Frequently asked questions
<a name="sm-distribution-faqs"></a>

**What constitutes a major image version release?**

Major image versions are released every 6 months. A major image version release for Amazon SageMaker Distribution involves upgrading all core dependencies to the latest compatible versions and may include adding or removing packages. Python framework is only upgraded with new major version releases. For example, with major version 2 release, Python framework was upgraded from 3.10 to 3.11, PyTorch was upgraded from 2.0 to 2.3, TensorFlow was upgraded from 2.14 to 2.17, Autogluon was upgraded from 0.8 to 1.1, and 4 packages were added to the image.

**What constitutes a minor image version release?**

Minor image versions are released for all supported major versions monthly. A minor image version release for Amazon SageMaker Distribution involves upgrading all core dependencies except Python and CUDA to the latest compatible minor versions within the same major version and may include adding new packages. For example, with a minor version release, langchain might be upgraded from 0.1 to 0.2 and jupyter-ai from 2.18 to 2.20.

**What constitutes a patch image version release?**

Patch image versions are released as necessary to fix security vulnerabilities. A patch image version release for Amazon SageMaker Distribution involves updating all of its core dependencies to the latest compatible patch versions within the same minor version. SageMaker Distribution does not add or remove any packages during a patch version release. For example, with a patch version release, matplotlib might be upgraded from 3.9.1 to 3.9.2 and boto3 from 1.34.131 to 1.34.162.

**Where can I find the packages available in a specific image version?**

Each image version has a `release.md` file in the [GitHub repository's](https://github.com/aws/sagemaker-distribution) `build_artifacts` folder, showing all packages and package versions for CPU and GPU images. Separate changelog files for CPU and GPU versions detail package upgrades. Changelogs compare the new image version to the previous. For example, version 1.9.0 compares to the latest patch version of 1.8, version 1.9.1 compares to 1.9.0, and version 2.0.0 compares to the latest patch version of the latest minor version available at the time.

**How are images scanned for Common Vulnerabilities and Exposures (CVEs)?**

Amazon SageMaker AI leverages [Amazon Elastic Container Registry (Amazon ECR) enhanced scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html) to automatically detect vulnerabilities and fixes for SageMaker Distribution Images. AWS continuously runs ECR enhanced scanning for the latest patch version of all supported image versions. When vulnerabilities are detected and a fix is available, AWS releases an updated image version to remediate the issue.

**Can I still use older images after an image is no longer supported?**

Images are available on SageMaker Studio until the designated availability date. Older images remain available in ECR after they reach end of support and are removed from Studio. You can download older image versions from ECR and [create a custom SageMaker image](studio-byoi-create.md). However, we highly recommend upgrading to a supported image version that continuously receives security updates and bug fixes. Customers who build their own custom images are responsible for scanning and patching their images. For more information, see the [AWS Shared Responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

**Important**  
SageMaker Distribution v0.x.y is only used in Studio Classic. SageMaker Distribution v1.x.y is only used in JupyterLab.