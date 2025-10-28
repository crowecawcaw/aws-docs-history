**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Minimize latency with Amazon File Cache

Amazon File Cache is a fully managed, high-speed cache on AWS that’s used to process file data, regardless of where the data is stored. Amazon File Cache automatically loads data into the cache when it’s accessed for the first time and releases data when it’s not used. For more information, see the [Amazon File Cache User Guide](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md").

The Amazon File Cache Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the life cycle of Amazon file caches. Note that the Amazon File Cache CSI driver is not compatible with Amazon EKS Hybrid Nodes. To deploy the Amazon File Cache CSI driver to your Amazon EKS cluster, see [aws-file-cache-csi-driver](https://github.com/kubernetes-sigs/aws-file-cache-csi-driver "https://github.com/kubernetes-sigs/aws-file-cache-csi-driver") on GitHub.
