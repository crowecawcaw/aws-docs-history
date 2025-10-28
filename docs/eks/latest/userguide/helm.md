**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy applications with Helm on Amazon EKS

The Helm package manager for Kubernetes helps you install and manage applications on your Kubernetes cluster. For more information, see the [Helm documentation](https://docs.helm.sh/ "https://docs.helm.sh/"). This topic helps you install and run the Helm binaries so that you can install and manage charts using the Helm CLI on your local system.

###### Important

Before you can install Helm charts on your Amazon EKS cluster, you must configure `kubectl` to work for Amazon EKS. If you have not already done this, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md") before proceeding. If the following command succeeds for your cluster, you’re properly configured.

```
kubectl get svc
```

1. Run the appropriate command for your client operating system.
   - If you’re using macOS with [Homebrew](https://brew.sh/ "https://brew.sh/"), install the binaries with the following command.

   ```
   brew install helm
   ```

   - For more installation options, see [Installing Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/") in the Helm Docs.

   ###### Note

   If you get a message that `openssl` must first be installed, you can install it with the following command.

```
sudo yum install openssl
```

1. To pick up the new binary in your `PATH`, Close your current terminal window and open a new one.
2. See the version of Helm that you installed.

```
helm version --template='{{ .Version }}{{ "\n" }}'
```

An example output is as follows.

```
v3.17.2
```

3. Make sure the version installed is compatible with your cluster version. Check [Supported Version Skew](https://helm.sh/docs/topics/version_skew/#supported-version-skew "https://helm.sh/docs/topics/version_skew/#supported-version-skew") to learn more. For example, if you are running with `3.17.x`, supported Kubernetes version should not out of the range of `1.29.x` ~ `1.32.x`.
4. At this point, you can run any Helm commands (such as `helm install `chart-name``) to install, modify, delete, or query Helm charts in your cluster. If you’re new to Helm and don’t have a specific chart to install, you can:
   - Experiment by installing an example chart. See [Install an example chart](https://helm.sh/docs/intro/quickstart#install-an-example-chart "https://helm.sh/docs/intro/quickstart#install-an-example-chart") in the Helm [Quickstart guide](https://helm.sh/docs/intro/quickstart/ "https://helm.sh/docs/intro/quickstart/").
   - Create an example chart and push it to Amazon ECR. For more information, see [Pushing a Helm chart](../../../AmazonECR/latest/userguide/push-oci-artifact.md "../../../AmazonECR/latest/userguide/push-oci-artifact.md") in the _Amazon Elastic Container Registry User Guide_.
   - Install an Amazon EKS chart from the [eks-charts](https://github.com/aws/eks-charts#eks-charts "https://github.com/aws/eks-charts#eks-charts")GitHub repo or from [ArtifactHub](https://artifacthub.io/packages/search?page=1&repo=aws "https://artifacthub.io/packages/search?page=1&repo=aws").
