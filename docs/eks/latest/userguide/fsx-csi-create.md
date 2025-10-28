**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy the FSx for Lustre driver

This topic shows you how to deploy the [FSx for Lustre CSI driver](fsx-csi.md "fsx-csi.md") to your Amazon EKS cluster and verify that it works. We recommend using the latest version of the driver. For available versions, see [CSI Specification Compatibility Matrix](https://github.com/kubernetes-sigs/aws-fsx-csi-driver/blob/master/docs/README.md#csi-specification-compatibility-matrix "https://github.com/kubernetes-sigs/aws-fsx-csi-driver/blob/master/docs/README.md#csi-specification-compatibility-matrix") on GitHub.

###### Note

The driver isn’t supported on Fargate or Amazon EKS Hybrid Nodes.

For detailed descriptions of the available parameters and complete examples that demonstrate the driver’s features, see the [FSx for Lustre Container Storage Interface (CSI) driver](https://github.com/kubernetes-sigs/aws-fsx-csi-driver "https://github.com/kubernetes-sigs/aws-fsx-csi-driver") project on GitHub.

## Prerequisites

- An existing cluster.
- The Amazon FSx CSI Driver EKS add-on requires the EKS Pod Identity agent for authentication. Without this component, the add-on will fail with the error `Amazon EKS Pod Identity agent is not installed in the cluster`, preventing volume operations. Install the Pod Identity agent before or after deploying the FSx CSI Driver add-on. For more information, see [Set up the Amazon EKS Pod Identity Agent](pod-id-agent-setup.md "pod-id-agent-setup.md").
- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the _AWS CloudShell User Guide_.
- Version `0.215.0` or later of the `eksctl` command line tool installed on your device or AWS CloudShell. To install or update `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").

## Step 1: Create an IAM role

The Amazon FSx CSI plugin requires IAM permissions to make calls to AWS APIs on your behalf.

###### Note

Pods will have access to the permissions that are assigned to the IAM role unless you block access to IMDS. For more information, see [Secure Amazon EKS clusters with best practices](security-best-practices.md "security-best-practices.md").

The following procedure shows you how to create an IAM role and attach the AWS managed policy to it.

1. Create an IAM role and attach the AWS managed policy with the following command. Replace `my-cluster` with the name of the cluster you want to use. The command deploys an AWS CloudFormation stack that creates an IAM role and attaches the IAM policy to it.

```
eksctl create iamserviceaccount \
    --name fsx-csi-controller-sa \
    --namespace kube-system \
    --cluster my-cluster \
    --role-name AmazonEKS_FSx_CSI_DriverRole \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonFSxFullAccess \
    --approve
```

You’ll see several lines of output as the service account is created. The last lines of output are similar to the following.

```
[ℹ]  1 task: {
    2 sequential sub-tasks: {
        create IAM role for serviceaccount "kube-system/fsx-csi-controller-sa",
        create serviceaccount "kube-system/fsx-csi-controller-sa",
    } }
[ℹ]  building iamserviceaccount stack "eksctl-my-cluster-addon-iamserviceaccount-kube-system-fsx-csi-controller-sa"
[ℹ]  deploying stack "eksctl-my-cluster-addon-iamserviceaccount-kube-system-fsx-csi-controller-sa"
[ℹ]  waiting for CloudFormation stack "eksctl-my-cluster-addon-iamserviceaccount-kube-system-fsx-csi-controller-sa"
[ℹ]  created serviceaccount "kube-system/fsx-csi-controller-sa"
```

Note the name of the AWS CloudFormation stack that was deployed. In the previous example output, the stack is named `eksctl-my-cluster-addon-iamserviceaccount-kube-system-fsx-csi-controller-sa`.

Now that you have created the Amazon FSx CSI driver IAM role, you can continue to the next section. When you deploy the add-on with this IAM role, it creates and is configured to use a service account that’s named `fsx-csi-controller-sa`. The service account is bound to a Kubernetes `clusterrole` that’s assigned the required Kubernetes permissions.

## Step 2: Install the Amazon FSx CSI driver

We recommend that you install the Amazon FSx CSI driver through the Amazon EKS add-on to improve security and reduce the amount of work. To add an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md").

###### Important

Pre-existing Amazon FSx CSI driver installations in the cluster can cause add-on installation failures. When you attempt to install the Amazon EKS add-on version while a non-EKS FSx CSI Driver exists, the installation will fail due to resource conflicts. Use the `OVERWRITE` flag during installation to resolve this issue.

```
aws eks create-addon --addon-name aws-fsx-csi-driver --cluster-name my-cluster --resolve-conflicts OVERWRITE
```

Alternatively, if you want a self-managed installation of the Amazon FSx CSI driver, see [Installation](https://github.com/kubernetes-sigs/aws-fsx-csi-driver/blob/master/docs/install.md "https://github.com/kubernetes-sigs/aws-fsx-csi-driver/blob/master/docs/install.md") on GitHub.

## Step 3: Deploy a storage class, persistent volume claim, and sample app

This procedure uses the [FSx for Lustre Container Storage Interface (CSI) driver](https://github.com/kubernetes-sigs/aws-fsx-csi-driver "https://github.com/kubernetes-sigs/aws-fsx-csi-driver") GitHub repository to consume a dynamically-provisioned FSx for Lustre volume.

1. Note the security group for your cluster. You can see it in the AWS Management Console under the **Networking** section or by using the following AWS CLI command. Replace `my-cluster` with the name of the cluster you want to use.

```
aws eks describe-cluster --name my-cluster --query cluster.resourcesVpcConfig.clusterSecurityGroupId
```

2. Create a security group for your Amazon FSx file system according to the criteria shown in [Amazon VPC Security Groups](../../../fsx/latest/LustreGuide/limit-access-security-groups.md#fsx-vpc-security-groups "../../../fsx/latest/LustreGuide/limit-access-security-groups.md#fsx-vpc-security-groups") in the Amazon FSx for Lustre User Guide. For the **VPC**, select the VPC of your cluster as shown under the **Networking** section. For "the security groups associated with your Lustre clients", use your cluster security group. You can leave the outbound rules alone to allow **All traffic**.
3. Download the storage class manifest with the following command.

```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-fsx-csi-driver/master/examples/kubernetes/dynamic_provisioning/specs/storageclass.yaml
```

4. Edit the parameters section of the `storageclass.yaml` file. Replace every example value with your own values.

```
parameters:
  subnetId: subnet-0eabfaa81fb22bcaf
  securityGroupIds: sg-068000ccf82dfba88
  deploymentType: PERSISTENT_1
  automaticBackupRetentionDays: "1"
  dailyAutomaticBackupStartTime: "00:00"
  copyTagsToBackups: "true"
  perUnitStorageThroughput: "200"
  dataCompressionType: "NONE"
  weeklyMaintenanceStartTime: "7:09:00"
  fileSystemTypeVersion: "2.12"
```

    * **`subnetId`** – The subnet ID that the Amazon FSx for Lustre file system should be created in. Amazon FSx for Lustre isn’t supported in all Availability Zones. Open the Amazon FSx for Lustre console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/") to confirm that the subnet that you want to use is in a supported Availability Zone. The subnet can include your nodes, or can be a different subnet or VPC:




    	+ You can check for the node subnets in the AWS Management Console by selecting the node group under the **Compute** section.
    	+ If the subnet that you specify isn’t the same subnet that you have nodes in, then your VPCs must be [connected](../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.md"), and you must ensure that you have the necessary ports open in your security groups.
    * **`securityGroupIds`** – The ID of the security group you created for the file system.
    * **`deploymentType` (optional)** – The file system deployment type. Valid values are `SCRATCH_1`, `SCRATCH_2`, `PERSISTENT_1`, and `PERSISTENT_2`. For more information about deployment types, see [Create your Amazon FSx for Lustre file system](../../../fsx/latest/LustreGuide/getting-started-step1.md "../../../fsx/latest/LustreGuide/getting-started-step1.md").
    * **other parameters (optional)** – For information about the other parameters, see [Edit StorageClass](https://github.com/kubernetes-sigs/aws-fsx-csi-driver/tree/master/examples/kubernetes/dynamic_provisioning#edit-storageclass "https://github.com/kubernetes-sigs/aws-fsx-csi-driver/tree/master/examples/kubernetes/dynamic_provisioning#edit-storageclass") on GitHub.

5. Create the storage class manifest.

```
kubectl apply -f storageclass.yaml
```

An example output is as follows.

```
storageclass.storage.k8s.io/fsx-sc created
```

6. Download the persistent volume claim manifest.

```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-fsx-csi-driver/master/examples/kubernetes/dynamic_provisioning/specs/claim.yaml
```

7. (Optional) Edit the `claim.yaml` file. Change `1200Gi` to one of the following increment values, based on your storage requirements and the `deploymentType` that you selected in a previous step.

```
storage: 1200Gi
```

    * `SCRATCH_2` and `PERSISTENT` – `1.2 TiB`, `2.4 TiB`, or increments of 2.4 TiB over 2.4 TiB.
    * `SCRATCH_1` – `1.2 TiB`, `2.4 TiB`, `3.6 TiB`, or increments of 3.6 TiB over 3.6 TiB.

8. Create the persistent volume claim.

```
kubectl apply -f claim.yaml
```

An example output is as follows.

```
persistentvolumeclaim/fsx-claim created
```

9. Confirm that the file system is provisioned.

```
kubectl describe pvc
```

An example output is as follows.

```
Name:          fsx-claim
Namespace:     default
StorageClass:  fsx-sc
Status:        Bound
[...]
```

###### Note

The `Status` may show as `Pending` for 5-10 minutes, before changing to `Bound`. Don’t continue with the next step until the `Status` is `Bound`. If the `Status` shows `Pending` for more than 10 minutes, use warning messages in the `Events` as reference for addressing any problems. 10. Deploy the sample application.

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-fsx-csi-driver/master/examples/kubernetes/dynamic_provisioning/specs/pod.yaml
```

11. Verify that the sample application is running.

```
kubectl get pods
```

An example output is as follows.

```
NAME      READY   STATUS              RESTARTS   AGE
fsx-app   1/1     Running             0          8s
```

12. Verify that the file system is mounted correctly by the application.

```
kubectl exec -ti fsx-app -- df -h
```

An example output is as follows.

```
Filesystem                   Size  Used Avail Use% Mounted on
overlay                       80G  4.0G   77G   5% /
tmpfs                         64M     0   64M   0% /dev
tmpfs                        3.8G     0  3.8G   0% /sys/fs/cgroup
192.0.2.0@tcp:/abcdef01      1.1T  7.8M  1.1T   1% /data
/dev/nvme0n1p1                80G  4.0G   77G   5% /etc/hosts
shm                           64M     0   64M   0% /dev/shm
tmpfs                        6.9G   12K  6.9G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs                        3.8G     0  3.8G   0% /proc/acpi
tmpfs                        3.8G     0  3.8G   0% /sys/firmware
```

13. Verify that data was written to the FSx for Lustre file system by the sample app.

```
kubectl exec -it fsx-app -- ls /data
```

An example output is as follows.

```
out.txt
```

This example output shows that the sample app successfully wrote the `out.txt` file to the file system.

###### Note

Before deleting the cluster, make sure to delete the FSx for Lustre file system. For more information, see [Clean up resources](../../../fsx/latest/LustreGuide/getting-started-step4.md "../../../fsx/latest/LustreGuide/getting-started-step4.md") in the _FSx for Lustre User Guide_.

## Performance tuning for FSx for Lustre

When using FSx for Lustre with Amazon EKS, you can optimize performance by applying Lustre tunings during node initialization. The recommended approach is to use launch template user data to ensure consistent configuration across all nodes.

These tunings include:

- Network and RPC optimizations
- Lustre module management
- LRU (Lock Resource Unit) tunings
- Client cache control settings
- RPC controls for OST and MDC

For detailed instructions on implementing these performance tunings:

- For optimizing performance for standard nodes (non-EFA), see [Optimize Amazon FSx for Lustre performance on nodes (non-EFA)](fsx-csi-tuning-non-efa.md "fsx-csi-tuning-non-efa.md") for a complete script that can be added to your launch template user data.
- For optimizing performance for EFA-enabled nodes, see [Optimize Amazon FSx for Lustre performance on nodes (EFA)](fsx-csi-tuning-efa.md "fsx-csi-tuning-efa.md").
