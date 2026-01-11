# Prebuilt SageMaker image support policy

All [pre-built SageMaker images](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"), including framework-specific containers, built-in
algorithm containers, algorithms and model packages listed in AWS Marketplace, and [AWS Deep Learning Containers](../../../deep-learning-containers/latest/devguide/what-is-dlc.md "../../../deep-learning-containers/latest/devguide/what-is-dlc.md") are regularly scanned for common vulnerabilities
listed by the [Common Vulnerabilities and Exposures (CVE)
Program](https://www.cve.org/ "https://www.cve.org/") and the [National Vulnerability
Database (NVD)](https://nvd.nist.gov/ "https://nvd.nist.gov/"). For more information about CVEs, see [CVE Frequently Asked Questions
(FAQs)](https://www.cve.org/ResourcesSupport/FAQs "https://www.cve.org/ResourcesSupport/FAQs"). Supported pre-built container images receive an updated minor version
release following any security patches.

All supported container images are routinely updated to address any critical CVEs. For
high severity scenarios, we recommend customers build and host a patched version of the
container in their own [Amazon Elastic Container Registry (Amazon ECR)](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md").

If you are running a container image version that is no longer supported, you may not have
the most updated drivers, libraries, and relevant packages. For a more up-to-date version,
we recommend that you upgrade to one of the supported frameworks available using the latest
image of your choice.

SageMaker AI doesn't release out-of-patch images for containers in new AWS Regions.

###### Note

As of August 2024, the `forecasting-deepar` container is no longer receiving
security patches or updates. While you can continue to use this container, you incur additional risk.
Containers are deprecated when the entire framework or algorithms is no longer supported, and
the underlying MXNet framework for the container has reached end-of-maintenance.

###### Topics

- [AWS Deep Learning Containers (DLC) support policy](#pre-built-containers-support-policy-dlc "#pre-built-containers-support-policy-dlc")
- [SageMaker AI ML Framework Container support policy](#pre-built-containers-support-policy-ml-framework "#pre-built-containers-support-policy-ml-framework")
- [SageMaker AI Built-in Algorithm Container support policy](#pre-built-containers-support-policy-built-in "#pre-built-containers-support-policy-built-in")
- [LLM Hosting Container support policy](#pre-built-containers-support-policy-llm-hosting "#pre-built-containers-support-policy-llm-hosting")
- [Unsupported containers and deprecation](#pre-built-containers-support-policy-deprecation "#pre-built-containers-support-policy-deprecation")

## AWS Deep Learning Containers (DLC) support policy

AWS Deep Learning Containers are a set of Docker images for training and serving deep
learning models. To view available images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md") in the Deep Learning Containers
GitHub repository.

DLCs hit their end of patch date 365 days after their GitHub release date. Patch
updates for DLCs are not “in-place” updates. You must delete the existing image on your
instance and pull the latest container image without terminating your instance. For more
information, see [Framework Support
Policy](../../../deep-learning-containers/latest/devguide/support-policy.md "../../../deep-learning-containers/latest/devguide/support-policy.md") in the _AWS Deep Learning Containers
Developer Guide_.

Reference the [AWS
Deep Learning Containers Framework Support Policy table](https://aws.amazon.com/releasenotes/dlc-support-policy/ "https://aws.amazon.com/releasenotes/dlc-support-policy/") to check which
frameworks and versions are actively supported for AWS DLCs. You can reference the
framework associated with a DLC in the support policy table for any images that are not
explicitly listed. For example, you can reference **PyTorch** in the
support policy table for DLC images such as `huggingface-pytorch-inference`
and `stabilityai-pytorch-inference`.

###### Note

If a DLC uses the HuggingFace [Transformers](https://huggingface.co/docs/transformers/en/index "https://huggingface.co/docs/transformers/en/index")
SDK, then only the image with the latest Transfromers version is supported. For more
information, see **HuggingFace** for the Region of
your choice in the [Docker Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md").

## SageMaker AI ML Framework Container support policy

The SageMaker AI ML Framework Containers are a set of Docker images for training and
serving machine learning workloads with environments optimized for common frameworks
such as XGBoost and Scikit Learn. To view available SageMaker AI ML Framework Containers,
see [Docker Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). Navigate to the AWS Region of your
choice, and browse images with the **(algorithm)** tag.
SageMaker AI ML Framework Containers also adhere to the [AWS Deep Learning Containers framework support policy](../../../deep-learning-containers/latest/devguide/support-policy.md "../../../deep-learning-containers/latest/devguide/support-policy.md").

To retrieve the latest image version for XGBoost 1.7-1 in framework mode, use the
following SageMaker Python SDK commands:

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost',region='us-east-1',version='3.0-5')
```

| Framework    | Current version | GitHub GA  | End of patch  |
| ------------ | --------------- | ---------- | ------------- |
| XGBoost      | 3.0-5           | 11/17/2025 | 11/17/2026    |
| XGBoost      | 1.7-1           | 03/06/2023 | 03/06/2025    |
| XGBoost      | 1.5-1           | 02/21/2022 | 02/21/2023    |
| XGBoost      | 1.3-1           | 05/21/2021 | 05/21/2022    |
| XGBoost      | 1.2-2           | 09/20/2020 | 09/20/2021    |
| XGBoost      | 1.2-1           | 07/19/2020 | 07/19/2021    |
| XGBoost      | 1.0-1           | >4 years   | Not supported |
| Scikit-Learn | 1.4-2           | 10/30/2025 | 10/30/2026    |
| Scikit-Learn | 1.2-1           | 03/06/2023 | 03/06/2025    |
| Scikit-Learn | 1.0-1           | 04/07/2022 | 04/07/2023    |
| Scikit-Learn | 0.23-1          | 3/6/2023   | 06/02/2021    |
| Scikit-Learn | 0.20-1          | >4 years   | Not supported |

## SageMaker AI Built-in Algorithm Container support policy

The SageMaker AI Built-in Algorithm Containers are a set of Docker images for training
and serving [SageMaker AI’s built-in machine learning algorithms](algos.md "algos.md"). To view available
SageMaker AI Built-in Algorithm Containers, see [Docker Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). Navigate to the AWS Region of your
choice, and browse images with the **(algorithm)** tag.

Patch updates for built-in container images are “in-place” updates. To stay up-to-date
with the latest security patches, we recommend checking out the latest built-in
algorithm image version using the `latest` image tag.

| Image container                                 | End of patch |
| ----------------------------------------------- | ------------ |
| `blazingtext:latest`                            | 05/15/2024   |
| `factorization-machines:latest`                 | 05/15/2024   |
| `forecasting-deepar:latest`                     | 08/26/2025   |
| `image-classification:latest`                   | 05/15/2024   |
| `instance-segmentation:latest`                  | 05/15/2024   |
| `ipembeddings:latest`                           | 05/15/2024   |
| `ipinsights:latest`                             | 05/15/2024   |
| `kmeans:latest`                                 | 05/15/2024   |
| `knn:latest`                                    | 05/15/2024   |
| `linear-learner:inference-cpu-1/training-cpu-1` | 05/15/2024   |
| `linear-learner:latest`                         | 05/15/2024   |
| `mxnet-algorithms:training-cpu/inference-cpu`   | 05/15/2024   |
| `ntm:latest`                                    | 05/15/2024   |
| `object-detection:latest`                       | 05/15/2024   |
| `object2vec:latest`                             | 05/15/2024   |
| `pca:latest`                                    | 05/15/2024   |
| `randomcutforest:latest`                        | 05/15/2024   |
| `semantic-segmentation:latest`                  | 05/15/2024   |
| `seq2seq:latest`                                | 05/15/2024   |

## LLM Hosting Container support policy

[LLM hosting
containers](https://github.com/awslabs/llm-hosting-container "https://github.com/awslabs/llm-hosting-container") such as the HuggingFace Text Generation Inference (TGI)
containers hit their end of patch date 30 days after their GitHub release date.

###### Important

We make an exception when there is a major version update. For example, if the
HuggingFace Text Generation Inference (TGI) toolkit updates to TGI 2.0, then we
continue to support the most recent version of TGI 1.4 for a period of three months
from the date of the GitHub release.

| Toolkit container | Current version | GitHub GA  | End of patch |
| ----------------- | --------------- | ---------- | ------------ |
| TGI               | tgi2.3.1        | 10/14/2024 | 11/14/2024   |
| TGI               | optimum0.0.25   | 10/04/2024 | 11/04/2024   |
| TGI               | tgi2.2.0        | 07/26/2024 | 08/30/2024   |
| TGI               | tgi2.0.0        | 05/15/2024 | 08/15/2024   |
| TGI               | tgi1.4.5        | 04/03/2024 | 07/03/2024   |
| TGI               | tgi1.4.2        | 02/22/2024 | 03/22/2024   |
| TGI               | tgi1.4.0        | 01/29/2024 | 02/29/2024   |
| TGI               | tgi1.3.3        | 12/19/2023 | 01/19/2024   |
| TGI               | tgi1.3.1        | 12/11/2023 | 01/11/2024   |
| TGI               | tgi1.2.0        | 12/04/2023 | 01/04/2024   |
| TGI               | optimum 0.0.24  | 08/23/2024 | 09/30/2024   |
| TGI               | optimum 0.0.23  | 07/26/2024 | 08/30/2024   |
| TGI               | optimum 0.0.21  | 05/10/2024 | 08/15/2024   |
| TGI               | optimum 0.0.19  | 02/19/2024 | 03/19/2024   |
| TGI               | optimum 0.0.18  | 02/01/2024 | 03/01/2024   |
| TGI               | optimum 0.0.17  | 01/24/2024 | 02/24/2024   |
| TGI               | optimum 0.0.16  | 01/18/2024 | 02/18/2024   |
| TEI               | tei1.4.0        | 08/01/2024 | 09/01/2024   |
| TEI               | tei1.2.3        | 04/26/2024 | 05/26/2024   |

## Unsupported containers and deprecation

When a container reaches end of patch or is deprecated, it no longer receives security
patching. Containers are deprecated when entire frameworks or algorithms are no longer
supported.

The following containers no longer receive support:

- As of August 2024, the `forecasting-deepar` container is no longer
  receiving security patches or updates due to the underlying MXNet framework for
  the container reaching end-of-maintenance.
- As of April 2024, [SageMaker AI Reinforcement Learning (RL) containers](https://github.com/aws/sagemaker-rl-container "https://github.com/aws/sagemaker-rl-container") are no longer
  supported. To build your own RL images, see [Building Your Image](https://github.com/aws/sagemaker-rl-container#building-your-image "https://github.com/aws/sagemaker-rl-container#building-your-image") in the SageMaker AI RL containers GitHub
  repository.
- As of September 2023, JumpStart Industry: Financial containers are no longer
  supported.
