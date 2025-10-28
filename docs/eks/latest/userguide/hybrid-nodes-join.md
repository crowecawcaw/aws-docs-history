**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Connect hybrid nodes

###### Note

The following steps apply to hybrid nodes running compatible operating systems except Bottlerocket. For steps to connect a hybrid node that runs Bottlerocket, see [Connect hybrid nodes with Bottlerocket](hybrid-nodes-bottlerocket.md "hybrid-nodes-bottlerocket.md").

This topic describes how to connect hybrid nodes to an Amazon EKS cluster. After your hybrid nodes join the cluster, they will appear with status Not Ready in the Amazon EKS console and in Kubernetes-compatible tooling such as kubectl. After completing the steps on this page, proceed to [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") to make your hybrid nodes ready to run applications.

## Prerequisites

Before connecting hybrid nodes to your Amazon EKS cluster, make sure you have completed the prerequisite steps.

- You have network connectivity from your on-premises environment to the AWS Region hosting your Amazon EKS cluster. See [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md") for more information.
- You have a compatible operating system for hybrid nodes installed on your on-premises hosts. See [Prepare operating system for hybrid nodes](hybrid-nodes-os.md "hybrid-nodes-os.md") for more information.
- You have created your Hybrid Nodes IAM role and set up your on-premises credential provider (AWS Systems Manager hybrid activations or AWS IAM Roles Anywhere). See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md") for more information.
- You have created your hybrid nodes-enabled Amazon EKS cluster. See [Create an Amazon EKS cluster with hybrid nodes](hybrid-nodes-cluster-create.md "hybrid-nodes-cluster-create.md") for more information.
- You have associated your Hybrid Nodes IAM role with Kubernetes Role-Based Access Control (RBAC) permissions. See [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md "hybrid-nodes-cluster-prep.md") for more information.

## Step 1: Install the hybrid nodes CLI (`nodeadm`) on each on-premises host

If you are including the Amazon EKS Hybrid Nodes CLI (`nodeadm`) in your pre-built operating system images, you can skip this step. For more information on the hybrid nodes version of `nodeadm`, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

The hybrid nodes version of `nodeadm` is hosted in Amazon S3 fronted by Amazon CloudFront. To install `nodeadm` on each on-premises host, you can run the following command from your on-premises hosts.

**For x86_64 hosts:**

```
curl -OL 'https://hybrid-assets.eks.amazonaws.com/releases/latest/bin/linux/amd64/nodeadm'
```

**For ARM hosts**

```
curl -OL 'https://hybrid-assets.eks.amazonaws.com/releases/latest/bin/linux/arm64/nodeadm'
```

Add executable file permission to the downloaded binary on each host.

```
chmod +x nodeadm
```

## Step 2: Install the hybrid nodes dependencies with `nodeadm`

If you are installing the hybrid nodes dependencies in pre-built operating system images, you can skip this step. The `nodeadm install` command can be used to install all dependencies required for hybrid nodes. The hybrid nodes dependencies include containerd, kubelet, kubectl, and AWS SSM or AWS IAM Roles Anywhere components. See [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md") for more information on the components and file locations installed by `nodeadm install`. See [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md") for hybrid nodes for more information on the domains that must be allowed in your on-premises firewall for the `nodeadm install` process.

Run the command below to install the hybrid nodes dependencies on your on-premises host. The command below must be run with a user that has sudo/root access on your host.

###### Important

The hybrid nodes CLI (`nodeadm`) must be run with a user that has sudo/root access on your host.

- Replace `K8S_VERSION` with the Kubernetes minor version of your Amazon EKS cluster, for example `1.31`. See [Amazon EKS supported versions](kubernetes-versions.md "kubernetes-versions.md") for a list of the supported Kubernetes versions.
- Replace `CREDS_PROVIDER` with the on-premises credential provider you are using. Valid values are `ssm` for AWS SSM and `iam-ra` for AWS IAM Roles Anywhere.

```
nodeadm install `K8S_VERSION` --credential-provider `CREDS_PROVIDER`

```

## Step 3: Connect hybrid nodes to your cluster

Before connecting your hybrid nodes to your cluster, make sure you have allowed the required access in your on-premises firewall and in the security group for your cluster for the Amazon EKS control plane to/from hybrid node communication. Most issues at this step are related to the firewall configuration, security group configuration, or Hybrid Nodes IAM role configuration.

###### Important

The hybrid nodes CLI (`nodeadm`) must be run with a user that has sudo/root access on your host.

1. Create a `nodeConfig.yaml` file on each host with the values for your deployment. For a full description of the available configuration settings, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md"). If your Hybrid Nodes IAM role does not have permission for the `eks:DescribeCluster` action, you must pass your Kubernetes API endpoint, cluster CA bundle, and Kubernetes service IPv4 CIDR in the cluster section of your `nodeConfig.yaml`.
   1. Use the `nodeConfig.yaml` example below if you are using AWS SSM hybrid activations for your on-premises credentials provider.
      1. Replace `CLUSTER_NAME` with the name of your cluster.
      2. Replace `AWS_REGION` with the AWS Region hosting your cluster. For example, `us-west-2`.
      3. Replace `ACTIVATION_CODE` with the activation code you received when creating your AWS SSM hybrid activation. See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md") for more information.
      4. Replace `ACTIVATION_ID` with the activation ID you received when creating your AWS SSM hybrid activation. You can retrieve this information from the AWS Systems Manager console or from the AWS CLI `aws ssm describe-activations` command.

      ```
      apiVersion: node.eks.aws/v1alpha1
      kind: NodeConfig
      spec:
        cluster:
          name: CLUSTER_NAME
          region: AWS_REGION
        hybrid:
          ssm:
            activationCode: ACTIVATION_CODE
            activationId: ACTIVATION_ID
      ```

   2. Use the `nodeConfig.yaml` example below if you are using AWS IAM Roles Anywhere for your on-premises credentials provider.
      1. Replace `CLUSTER_NAME` with the name of your cluster.
      2. Replace `AWS_REGION` with the AWS Region hosting your cluster. For example, `us-west-2`.
      3. Replace `NODE_NAME` with the name of your node. The node name must match the CN of the certificate on the host if you configured the trust policy of your Hybrid Nodes IAM role with the `"sts:RoleSessionName": "${aws:PrincipalTag/x509Subject/CN}"` resource condition. The `nodeName` you use must not be longer than 64 characters.
      4. Replace `TRUST_ANCHOR_ARN` with the ARN of the trust anchor you configured in the steps for Prepare credentials for hybrid nodes.
      5. Replace `PROFILE_ARN` with the ARN of the trust anchor you configured in the steps for [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md").
      6. Replace `ROLE_ARN` with the ARN of your Hybrid Nodes IAM role.
      7. Replace `CERTIFICATE_PATH` with the path in disk to your node certificate. If you don’t specify it, the default is `/etc/iam/pki/server.pem`.
      8. Replace `KEY_PATH` with the path in disk to your certificate private key. If you don’t specify it, the default is `/etc/iam/pki/server.key`.

      ```
      apiVersion: node.eks.aws/v1alpha1
      kind: NodeConfig
      spec:
        cluster:
          name: CLUSTER_NAME
          region: AWS_REGION
        hybrid:
          iamRolesAnywhere:
            nodeName: NODE_NAME
            trustAnchorArn: TRUST_ANCHOR_ARN
            profileArn: PROFILE_ARN
            roleArn: ROLE_ARN
            certificatePath: CERTIFICATE_PATH
            privateKeyPath: KEY_PATH
      ```

2. Run the `nodeadm init` command with your `nodeConfig.yaml` to connect your hybrid nodes to your Amazon EKS cluster.

```
nodeadm init -c file://nodeConfig.yaml
```

If the above command completes successfully, your hybrid node has joined your Amazon EKS cluster. You can verify this in the Amazon EKS console by navigating to the Compute tab for your cluster ([ensure IAM principal has permissions to view](view-kubernetes-resources.md#view-kubernetes-resources-permissions "view-kubernetes-resources.md#view-kubernetes-resources-permissions")) or with `kubectl get nodes`.

###### Important

Your nodes will have status `Not Ready`, which is expected and is due to the lack of a CNI running on your hybrid nodes. If your nodes did not join the cluster, see [Troubleshooting hybrid nodes](hybrid-nodes-troubleshooting.md "hybrid-nodes-troubleshooting.md").

## Step 4: Configure a CNI for hybrid nodes

To make your hybrid nodes ready to run applications, continue with the steps on [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").
