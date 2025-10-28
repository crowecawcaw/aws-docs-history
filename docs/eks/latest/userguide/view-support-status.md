**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View current cluster support period

The **cluster support period** section of the AWS console indicates if your cluster is _currently_ on standard or extended support. If your cluster support period is **Extended support**, you are being charged for EKS extended support.

For more information about standard and extended support, see [Understand the Kubernetes version lifecycle on EKS](kubernetes-versions.md "kubernetes-versions.md").

1. Navigate to the **Clusters** page in the EKS section of the AWS Console. Confirm the console is set to the same AWS region as the cluster you want to review.
2. Review the **Support Period** column. If the value is **Standard support until…​**, you are not currently being charged for extended support. You are within the standard support period. If the value is **Extended support…​** this cluster is currently being charged for extended support.

###### Note

The **Support Period** cannot be retrieved with the AWS API or CLI.
