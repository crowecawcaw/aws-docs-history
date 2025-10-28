**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable EKS Auto Mode on existing EKS clusters

You can enable EKS Auto Mode on existing EKS Clusters.

**AWS supports the following migrations:**

- Migrating from Karpenter to EKS Auto Mode nodes. For more information, see [Migrate from Karpenter to EKS Auto Mode using kubectl](auto-migrate-karpenter.md "auto-migrate-karpenter.md").
- Migrating from EKS Managed Node Groups to EKS Auto Mode nodes. For more information, see [Migrate from EKS Managed Node Groups to EKS Auto Mode](auto-migrate-mng.md "auto-migrate-mng.md").
- Migrating from EKS Fargate to EKS Auto Mode. For more information, see [Migrate from EKS Fargate to EKS Auto Mode](auto-migrate-fargate.md "auto-migrate-fargate.md").

**AWS does not support the following migrations:**

- Migrating volumes from the EBS CSI controller (using the Amazon EKS add-on) to EKS Auto Mode EBS CSI controller (managed by EKS Auto Mode). PVCs made with one can’t be mounted by the other, because they use two different Kubernetes volume provisioners.
  - The [`eks-auto-mode-ebs-migration-tool`](https://github.com/awslabs/eks-auto-mode-ebs-migration-tool "https://github.com/awslabs/eks-auto-mode-ebs-migration-tool") (AWS Labs project) enables migration between standard EBS CSI StorageClass (`ebs.csi.aws.com`) and EKS Auto EBS CSI StorageClass (`ebs.csi.eks.amazonaws.com`). Note that migration requires deleting and re-creating existing PersistentVolumeClaim/PersistentVolume resources, so validation in a non-production environment is essential before implementation.

- Migrating load balancers from the AWS Load Balancer Controller to EKS Auto Mode

You can install the AWS Load Balancer Controller on an Amazon EKS Auto Mode cluster. Use the `IngressClass` or `loadBalancerClass` options to associate Service and Ingress resources with either the Load Balancer Controller or EKS Auto Mode.

- Migrating EKS clusters with alternative CNIs or other unsupported networking configurations

## Migration reference

Use the following migration reference to configure Kubernetes resources to be owned by either self-managed controllers or EKS Auto Mode.

| Capability     | Resource             | Field               | Self Managed            | EKS Auto Mode               |
| -------------- | -------------------- | ------------------- | ----------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Block storage  | `StorageClass`       | `provisioner`       | `ebs.csi.aws.com`       | `ebs.csi.eks.amazonaws.com` |
| Load balancing | `Service`            | `loadBalancerClass` | `service.k8s.aws/nlb`   | `eks.amazonaws.com/nlb`     |
| Load balancing | `IngressClass`       | `controller`        | `ingress.k8s.aws/alb`   | `eks.amazonaws.com/alb`     |
| Load balancing | `IngressClassParams` | `apiversion`        | `elbv2.k8s.aws/v1beta1` | `eks.amazonaws.com/v1`      |
| Load balancing | `TargetGroupBinding` | `apiversion`        | `elbv2.k8s.aws/v1beta1` | `eks.amazonaws.com/v1`      |
| Compute        | `NodeClass`          | `apiVersion`        | `karpenter.sh/v1`       | `eks.amazonaws.com/v1`      | ## Migrating EBS volumes When migrating workloads to EKS Auto Mode, you need to handle EBS volume migration due to different CSI driver provisioners: <br>• EKS Auto Mode provisioner: `ebs.csi.eks.amazonaws.com` <br>• Open source EBS CSI provisioner: `ebs.csi.aws.com` Follow these steps to migrate your persistent volumes: 1. **Modify volume retention policy**: Change the existing platform version’s (PV’s) `persistentVolumeReclaimPolicy` to `Retain` to ensure the underlying EBS volume is not deleted. 2. **Remove PV from Kubernetes**: Delete the old PV resource while keeping the actual EBS volume intact. 3. **Create a new PV with static provisioning**: Create a new PV that references the same EBS volume but works with the target CSI driver. 4. **Bind to a new PVC**: Create a new PVC that specifically references your PV using the `volumeName` field. ### Considerations <br>• Ensure your applications are stopped before beginning this migration. <br>• Back up your data before starting the migration process. <br>• This process needs to be performed for each persistent volume. <br>• The workload must be updated to use the new PVC. ## Migrating load balancers You cannot directly transfer existing load balancers from the self-managed AWS load balancer controller to EKS Auto Mode. Instead, you must implement a blue-green deployment strategy. This involves maintaining your existing load balancer configuration while creating new load balancers under the managed controller. To minimize service disruption, we recommend a DNS-based traffic shifting approach. First, create new load balancers by using EKS Auto Mode while keeping your existing configuration operational. Then, use DNS routing (such as Route 53) to gradually shift traffic from the old load balancers to the new ones. Once traffic has been successfully migrated and you’ve verified the new configuration, you can decommission the old load balancers and self-managed controller. |
