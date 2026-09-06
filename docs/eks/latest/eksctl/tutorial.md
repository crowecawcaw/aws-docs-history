

# Tutorial
<a name="tutorial"></a>

This topic walks you through installing and configuring eksctl, then using it to create an Amazon EKS cluster.

## Step 1: Install eksctl
<a name="_step_1_install_eksctl"></a>

Complete the following steps to download and install the latest version of eksctl on your Linux or macOS device:

 **To install eksctl with Homebrew** 

1. (Prerequisite) Install [Homebrew](https://brew.sh/).

1. Add the AWS tap:

   ```
   brew tap aws/tap
   ```

1. Install eksctl

   ```
   brew install aws/tap/eksctl
   ```

Before using eksctl, complete these configuration steps:

1. Install prerequisites:
   +  [Install AWS CLI version](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) 2.x or later.
   + Install [kubectl](https://formulae.brew.sh/formula/kubernetes-cli) using Homebrew:

     ```
     brew install kubernetes-cli
     ```

1.  [Configure AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in your environment:

   ```
   aws configure
   ```

1. Verify AWS CLI configuration:

   ```
   aws sts get-caller-identity
   ```

## Step 2: Create cluster config file
<a name="_step_2_create_cluster_config_file"></a>

Create a cluster configuration file using these steps:

1. Create a new file named `cluster.yaml`:

   ```
   touch cluster.yaml
   ```

1. Add the following basic cluster configuration:

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

1. Customize the configuration:
   + Update the `region` to match your desired AWS region.
   + Modify the `instanceType` based on your workload requirements.
   + Adjust the `desiredCapacity`, `minSize`, and `maxSize` according to your needs.

1. Validate the configuration file:

   ```
   eksctl create cluster -f cluster.yaml --dry-run
   ```

## Step 3: Create cluster
<a name="_step_3_create_cluster"></a>

Follow these steps to create your EKS cluster:

1. Create the cluster using the configuration file:

   ```
   eksctl create cluster -f cluster.yaml
   ```

1. Wait for cluster creation (this typically takes 15-20 minutes).

1. Verify cluster creation:

   ```
   eksctl get cluster
   ```

1. Configure kubectl to use your new cluster:

   ```
   aws eks update-kubeconfig --name basic-cluster --region us-west-2
   ```

1. Verify cluster connectivity:

   ```
   kubectl get nodes
   ```

Your cluster is now ready to use.

### Optional: Delete Cluster
<a name="_optional_delete_cluster"></a>

Remember to delete the cluster when you’re done to avoid unnecessary charges:

```
eksctl delete cluster -f cluster.yaml
```

**Note**  
Cluster creation can incur AWS charges. Make sure to review the [Amazon EKS pricing](https://aws.amazon.com/eks/pricing/) before creating a cluster.

## Next Steps
<a name="_next_steps"></a>
+ Configure Kubectl to connect to the cluster
+ Deploy a sample app