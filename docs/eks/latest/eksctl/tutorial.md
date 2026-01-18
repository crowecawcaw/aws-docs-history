# Tutorial

This topic walks you through installing and configuring eksctl, then using it to create an Amazon EKS cluster.

## Step 1: Install eksctl

Complete the following steps to download and install the latest version of eksctl on your Linux or macOS device:

**To install eksctl with Homebrew**

1. (Prerequisite) Install [Homebrew](https://brew.sh/ "https://brew.sh/").
2. Add the AWS tap:

```
 brew tap aws/tap
```

3. Install eksctl

```
 brew install aws/tap/eksctl
```

Before using eksctl, complete these configuration steps:

1. Install prerequisites:
   - [Install AWS CLI version](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") 2.x or later.
   - Install [kubectl](https://formulae.brew.sh/formula/kubernetes-cli "https://formulae.brew.sh/formula/kubernetes-cli") using Homebrew:

   ```
    brew install kubernetes-cli
   ```

2. [Configure AWS credentials](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in your environment:

```
 aws configure
```

3. Verify AWS CLI configuration:

```
 aws sts get-caller-identity
```

## Step 2: Create cluster config file

Create a cluster configuration file using these steps:

1. Create a new file named `cluster.yaml`:

```
 touch cluster.yaml
```

2. Add the following basic cluster configuration:

```
 apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
   name: basic-cluster
   region: us-west-2

nodeGroups:
   - name: ng-1
      instanceType: m5.large
      desiredCapacity: 2
      minSize: 1
      maxSize: 3
      ssh:
      allow: false
```

3. Customize the configuration:
   - Update the `region` to match your desired AWS region.
   - Modify the `instanceType` based on your workload requirements.
   - Adjust the `desiredCapacity`, `minSize`, and `maxSize` according to your needs.

4. Validate the configuration file:

```
 eksctl create cluster -f cluster.yaml --dry-run
```

## Step 3: Create cluster

Follow these steps to create your EKS cluster:

1. Create the cluster using the configuration file:

```
 eksctl create cluster -f cluster.yaml
```

2. Wait for cluster creation (this typically takes 15-20 minutes).
3. Verify cluster creation:

```
 eksctl get cluster
```

4. Configure kubectl to use your new cluster:

```
 aws eks update-kubeconfig --name basic-cluster --region us-west-2
```

5. Verify cluster connectivity:

```
 kubectl get nodes
```

Your cluster is now ready to use.

### Optional: Delete Cluster

Remember to delete the cluster when you’re done to avoid unnecessary charges:

```
 eksctl delete cluster -f cluster.yaml
```

###### Note

Cluster creation can incur AWS charges. Make sure to review the [Amazon EKS pricing](https://aws.amazon.com/eks/pricing/ "https://aws.amazon.com/eks/pricing/") before creating a cluster.

## Next Steps

- Configure Kubectl to connect to the cluster
- Deploy a sample app
