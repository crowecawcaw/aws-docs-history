**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Learn about Amazon EKS Auto Mode Managed instances

This topic explains how Amazon EKS Auto Mode manages Amazon EC2 instances in your EKS cluster. When you enable EKS Auto Mode, your cluster’s compute resources are automatically provisioned and managed by EKS, changing how you interact with the EC2 instances that serve as nodes in your cluster.

Understanding how Amazon EKS Auto Mode manages instances is essential for planning your workload deployment strategy and operational procedures. Unlike traditional EC2 instances or managed node groups, these instances follow a different lifecycle model where EKS assumes responsibility for many operational aspects, while restricting certain types of access and customization.

Amazon EKS Auto Mode automates routine tasks for creating new EC2 Instances, and attaches them as nodes to your EKS cluster. EKS Auto Mode detects when a workload can’t fit onto existing nodes, and creates a new EC2 Instance.

Amazon EKS Auto Mode is responsible for creating, deleting, and patching EC2 Instances. You are responsible for the containers and pods deployed on the instance.

EC2 Instances created by EKS Auto Mode are different from other EC2 Instances, they are managed instances. These managed instances are owned by EKS and are more restricted. You can’t directly access or install software on instances managed by EKS Auto Mode.

AWS suggests running either EKS Auto Mode or self-managed Karpenter. You can install both during a migration or in an advanced configuration. If you have both installed, configure your node pools so that workloads are associated with either Karpenter or EKS Auto Mode.

For more information, see [Amazon EC2 managed instances](../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md "../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md") in the Amazon EC2 user guide.

## Comparison table

| Standard EC2 Instance                                                  | EKS Auto Mode managed instance                                                                                                                      |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| You are responsible for patching and updating the instance.            | AWS automatically patches and updates the instance.                                                                                                 |
| EKS is not responsible for the software on the instance.               | EKS is responsible for certain software on the instance, such as `kubelet`, the container runtime, and the operating system.                        |
| You can delete the EC2 Instance using the EC2 API.                     | EKS determines the number of instances deployed in your account. If you delete a workload, EKS will reduce the number of instances in your account. |
| You can use SSH to access the EC2 Instance.                            | You can deploy pods and containers to the managed instance.                                                                                         |
| You determine the operating system and image (AMI).                    | AWS determines the operating system and image.                                                                                                      |
| You can deploy workloads that rely on Windows or Ubuntu functionality. | You can deploy containers based on Linux, but without specific OS dependencies.                                                                     |
| You determine what instance type and family to launch.                 | AWS determines what instance type and family to launch. You can use a Node Pool to limit the instance types EKS Auto Mode selects from.             |

The following functionality works for both Managed instances and Standard EC2 instances:

- You can use instance storage as ephemeral storage for workloads.

### AMI Support

With EKS Auto Mode, AWS determines the image (AMI) used for your compute nodes. AWS monitors the rollout of new EKS Auto Mode AMI versions. If you experience workload issues related to an AMI version, create a support case. For more information, see [Creating support cases and case management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") in the AWS Support User Guide.

Generally, EKS releases a new AMI each week containing CVE and security fixes.

## Managed resource visibility

###### Note

Beginning April 22, 2026, new Amazon EC2 managed instances and associated resources (for example, EC2 launch templates, EBS volumes, and network interfaces (ENIs)) created by EKS Auto Mode are hidden from EC2 console views and `describe` API list operations by default. Managed resources that already existed in your account before that date remain visible. You can change this behavior using managed resource visibility settings.

Amazon EC2 provides managed resource visibility settings that control whether managed resources appear in your EC2 console views and API list operations such as `DescribeInstances`.

When managed resources are hidden, EKS Auto Mode managed instances and their associated resources (EBS volumes, launch templates, and network interfaces) do not appear in the EC2 console or `describe` API responses. This can simplify governance dashboards, reduce noise in observability tools, and prevent false positives in cloud security posture management (CSPM) scanners that flag managed resources as customer misconfigurations.

Visibility settings apply account-wide to all IAM principals. You cannot selectively show or hide managed resources by resource type or by the service that created them. Hidden resources remain fully operational and billable.

You can change visibility settings at any time through the Amazon EC2 console or the AWS CLI. For more information, see [Managed resource visibility settings](../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md#managed-resource-visibility-settings "../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md#managed-resource-visibility-settings") in the _Amazon EC2 User Guide_.

###### Note

Even when managed resources are hidden from EC2 console views and list APIs, you can still view EKS Auto Mode instances through:

- The Amazon EKS console, under your cluster’s **Compute** tab.
- Kubernetes APIs (for example, `kubectl get nodes`).
- Direct EC2 API queries by instance ID (for example, `describe-instances --instance-ids i-0123456789abcdef0`).
- The `DescribeInstances` API with the `include-managed-resources` parameter.
- The EC2 console, after changing the managed resource visibility setting.

## EKS Auto Mode supported instance reference

EKS Auto Mode only creates instances of supported types, and that meet a minimum size requirement.

EKS Auto Mode supports the following instance types:

| Family                              | Instance Types                                                                                                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute Optimized (C)               | c9g, c8a, c8g, c8gb, c8gd, c8gn, c8i, c8i-flex, c8id, c7a, c7g, c7gd, c7gn, c7i, c7i-flex, c6a, c6g, c6gd, c6gn, c6i, c6id, c6in, c5, c5a, c5ad, c5d, c5n, c4                |
| General Purpose (M)                 | m9gd, m8a, m8azn, m8g, m8gb, m8gd, m8gn, m8i, m8i-flex, m8id, m7a, m7g, m7gd, m7i, m7i-flex, m6a, m6g, m6gd, m6i, m6id, m6idn, m6in, m5, m5a, m5ad, m5d, m5dn, m5n, m5zn, m4 |
| Memory Optimized (R)                | r8a, r8g, r8gb, r8gd, r8gn, r8i, r8i-flex, r8id, r7a, r7g, r7gd, r7i, r7iz, r6a, r6g, r6gd, r6i, r6id, r6idn, r6in, r5, r5a, r5ad, r5b, r5d, r5dn, r5n, r4                   |
| Burstable (T)                       | t4g, t3, t3a, t2                                                                                                                                                             |
| High Memory (Z/X)                   | z1d, x8aedz, x8g, x8i, x2gd                                                                                                                                                  |
| Storage Optimized (I/D)             | i8g, i8ge, i7i, i7ie, i4g, is4gen, im4gn, i4i, i3, i3en, d3, d3en                                                                                                            |
| Accelerated Computing (Trn/P/Inf/G) | trn2, trn1, trn1n, p6-b200, p6-b300, p5, p5e, p5en, p4d, p4de, p3, p3dn, inf2, inf1, g7e, g6, gr6, g6e, g5, g5g, g4ad, g4dn                                                  |
| High Performance Computing (X2/HPC) | x2idn, x2iedn, x2iezn, hpc8a                                                                                                                                                 |

Additionally, EKS Auto Mode will only create EC2 instances that meet the following requirements:

- More than 1 CPU
- Instance size is not nano, micro or small

For more information, see [Amazon EC2 instance type naming conventions](../../../ec2/latest/instancetypes/instance-type-names.md "../../../ec2/latest/instancetypes/instance-type-names.md").

## Instance Metadata Service

- EKS Auto Mode enforces IMDSv2 with a hop limit of 1 by default, adhering to AWS security best practices.
- This default configuration cannot be modified in Auto Mode.
- For add-ons that typically require IMDS access, supply parameters (such as AWS region) during installation to avoid IMDS lookups. For more information, see [Determine fields you can customize for Amazon EKS add-ons](kubernetes-field-management.md "kubernetes-field-management.md").
- If a Pod absolutely requires IMDS access when running in Auto Mode, the Pod must be configured to run with `hostNetwork: true`. This allows the Pod to access the instance metadata service directly.
- Consider the security implications when granting Pods access to instance metadata.

For more information about the Amazon EC2 Instance Metadata Service (IMDS), see [Configure the Instance Metadata Service options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md") in the _Amazon EC2 User Guide_.

## Considerations

- If the configured ephemeral storage in the NodeClass is smaller than the NVMe local storage for the instance, EKS Auto Mode eliminates the need for manual configuration by automatically taking the following actions:

  - Uses a smaller (20 GiB) Amazon EBS data volume to reduce costs.
  - Formats and configures the NVMe local storage for ephemeral data use. This includes setting up a RAID 0 array if there are multiple NVMe drives.

- When `ephemeralStorage.size` equals or exceeds the local NVMe capacity, the following actions occur:

  - Auto Mode skips the small EBS volume.
  - The NVMe drive(s) are exposed directly for your workload.

- Amazon EKS Auto Mode does not support the following AWS Fault Injection Service actions:

  - `ec2:RebootInstances`
  - `ec2:SendSpotInstanceInterruptions`
  - `ec2:StartInstances`
  - `ec2:StopInstances`
  - `ec2:TerminateInstances`
  - `ec2:PauseVolumeIO`

- Amazon EKS Auto Mode supports AWS Fault Injection Service EKS Pod actions. For more information, see [Managing Fault Injection Service experiments](../../../resilience-hub/latest/userguide/testing.md "../../../resilience-hub/latest/userguide/testing.md") and [Use the AWS FIS aws:eks:pod actions](../../../fis/latest/userguide/eks-pod-actions.md#configure-service-account "../../../fis/latest/userguide/eks-pod-actions.md#configure-service-account") in the AWS Resilience Hub User Guide.
- You do not need to install the `Neuron Device Plugin` on EKS Auto Mode nodes.

If you have other types of nodes in your cluster, you need to configure the Neuron Device plugin to not run on Auto Mode nodes. For more information, see [Control if a workload is deployed on EKS Auto Mode nodes](associate-workload.md "associate-workload.md").
