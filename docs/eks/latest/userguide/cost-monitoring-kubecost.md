**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Install Kubecost

Amazon EKS supports Kubecost, which you can use to monitor your costs broken down by Kubernetes resources including Pods, nodes, namespaces, and labels. This topic covers installing Kubecost, and accessing the Kubecost dashboard.

Amazon EKS provides an AWS optimized bundle of Kubecost for cluster cost visibility. You can use your existing AWS support agreements to obtain support. For more information about the available versions of Kubecost, see [Learn more about Kubecost](cost-monitoring-kubecost-bundles.md "cost-monitoring-kubecost-bundles.md").

###### Note

Kubecost v3 introduces major architectural improvements including dramatically faster performance and enhanced automation capabilities. [Learn more about Kubecost v3.](cost-monitoring-kubecost-bundles.md#kubecost-v3 "cost-monitoring-kubecost-bundles.md#kubecost-v3")

Kubecost v2 introduces several major new features. [Learn more about Kubecost v2.](cost-monitoring-kubecost-bundles.md#kubecost-v2 "cost-monitoring-kubecost-bundles.md#kubecost-v2")

For more information about Kubecost, see the [Kubecost](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x "https://www.ibm.com/docs/en/kubecost/self-hosted/3.x") documentation and [Frequently asked questions](cost-monitoring-kubecost-bundles.md#cost-monitoring-faq "cost-monitoring-kubecost-bundles.md#cost-monitoring-faq").

## Install Amazon EKS optimized Kubecost bundle

You can use one of the following procedures to install the _Amazon EKS optimized Kubecost bundle_:

- Before start, it is recommended to review [Kubecost - Architecture Overview](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration "https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration") to understand how Kubecost works on Amazon EKS.
- If you are new to Amazon EKS, we recommend that you use the Amazon EKS add-on for the installation because it simplifies the _Amazon EKS optimized Kubecost bundle_ installation. For more information, see [Deploying Kubecost on an Amazon EKS cluster using Amazon EKS add-on](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration#ariaid-title3 "https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration#ariaid-title3").
- To customize the installation, you might configure your _Amazon EKS optimized Kubecost bundle_ with Helm. For more information, see [Deploying Kubecost on an Amazon EKS cluster using Helm](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration#ariaid-title8 "https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installations-amazon-eks-integration#ariaid-title8") in the _Kubecost documentation_.

###### Important

For Kubecost v3, the Helm chart location has changed to `public.ecr.aws/kubecost/kubecost`. If you are upgrading from v2, update your Helm repository references accordingly.

###### Note

For multi-cluster deployments with Kubecost v3, you need S3-compatible object storage (AWS S3 for EKS customers) for metrics storage. This replaces the Prometheus-compatible storage used in v2. For more information, see [Multi-Cluster Installation](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installation-multi-cluster "https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installation-multi-cluster") in the Kubecost documentation.

## Access Kubecost dashboard

Once the _Amazon EKS optimized Kubecost bundle_ setup done, you should have access to Kubecost dashboard. For more information, see [Access Kubecost Dashboard](cost-monitoring-kubecost-dashboard.md "cost-monitoring-kubecost-dashboard.md").
