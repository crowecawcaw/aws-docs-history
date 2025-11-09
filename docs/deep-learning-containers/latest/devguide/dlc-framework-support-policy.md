# Framework Support Policy Table

For more details see the [Framework Support Policy](support-policy.md "support-policy.md").

## Supported Framework Versions

The containers are available in the following regions:

| Framework  | Current version | CUDA version                                          | GitHub GA  | End of patch |
| ---------- | --------------- | ----------------------------------------------------- | ---------- | ------------ |
| PyTorch    | 2.8             | 12.9                                                  | 2025-08-06 | 2026-08-06   |
| PyTorch    | 2.7             | 12.8                                                  | 2025-04-23 | 2026-04-23   |
| PyTorch    | 2.6             | • 12.6 for Training DLCs<br>• 12.4 for Inference DLCs | 2025-01-29 | 2026-01-29   |
| TensorFlow | 2.19            | • 12.5 for Training DLCs<br>• 12.2 for Inference DLCs | 2025-03-11 | 2026-03-11   |

## Unsupported Framework Versions

Versions listed in this table will appear for 2 years past their support date.

| Framework  | Current version | CUDA version                                                      | GitHub GA  | End of patch |
| ---------- | --------------- | ----------------------------------------------------------------- | ---------- | ------------ |
| PyTorch    | 2.5             | 12.4                                                              | 2024-10-29 | 2025-10-29   |
| PyTorch    | 2.4             | 12.4                                                              | 2024-07-24 | 2025-07-24   |
| PyTorch    | 2.3             | 12.1                                                              | 2024-04-24 | 2025-04-24   |
| PyTorch    | 2.2             | • 12.1 for Training DLCs<br>• 11.8 for Inference DLCs             | 2024-01-30 | 2025-01-30   |
| PyTorch    | 2.1             | • 12.1 for Training DLCs<br>• 11.8 for Inference DLCs             | 2023-10-04 | 2024-10-04   |
| PyTorch    | 2.0             | • 12.1 for Training DLC<br>• 11.8 for Training and Inference DLCs | 2023-03-15 | 2024-03-15   |
| PyTorch    | 1.13            | 11.7                                                              | 2022-10-28 | 2024-10-28   |
| PyTorch    | 1.12            | • 11.3 for SageMaker DLC<br>• 11.6 for EC2/ECS/EKS DLC            | 2022-07-01 | 2023-07-01   |
| PyTorch    | 1.11            | • 11.3 for SageMaker DLC<br>• 11.5 for EC2/ECS/EKS DLC            | 2022-03-10 | 2023-03-10   |
| TensorFlow | 2.18            | • 12.5 for Training DLCs<br>• 12.2 for Inference DLCs             | 2024-10-24 | 2025-10-24   |
| TensorFlow | 2.16            | • 12.3 for Training DLCs<br>• 12.2 for Inference DLCs             | 2024-03-07 | 2025-03-07   |
| TensorFlow | 2.14            | 11.8                                                              | 2023-09-26 | 2024-09-26   |
| TensorFlow | 2.13            | 11.8                                                              | 2023-07-19 | 2024-07-19   |
| TensorFlow | 2.12            | 11.8                                                              | 2023-03-23 | 2024-03-23   |
| TensorFlow | 2.11            | 11.2                                                              | 2022-11-18 | 2023-11-18   |
| TensorFlow | 2.10            | 11.2                                                              | 2022-09-06 | 2023-09-06   |
| TensorFlow | 2.9             | 11.2                                                              | 2022-05-17 | 2023-05-17   |
| TensorFlow | 2.8             | 11.2                                                              | 2022-02-02 | 2023-02-02   |
| TensorFlow | 2.7             | 11.2                                                              | 2021-11-04 | 2022-11-04   |

## Updates

- 2024-08-14 Updated the version format from major.minor.patch to major.minor to reduce confusion.
- 2023-10-30 Extend support for PT 1.13 by one year, as it is the last 1.x version released by PyTorch.
- 2023-10-01 End of support for MXNet and Elastic Inference

### Unsupported Frameworks

From 1st Oct 2023, MXNet, Elastic Inference frameworks are not supported because of lack of upstream support on those frameworks. Please use one of our supported frameworks as per section &ldquo;Supported Framework Versions&rdquo; in this document.
