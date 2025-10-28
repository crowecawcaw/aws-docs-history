# Deleting

a SageMaker HyperPod cluster

Use the following instructions to delete SageMaker HyperPod clusters orchestrated by
Amazon EKS in the SageMaker AI console.

1. Under **Clusters** in the main pane of the SageMaker HyperPod
   console, choose the cluster you want to delete.
2. Select your cluster, and choose **Delete**.
3. In the pop-up window for cluster deletion, review the cluster information
   carefully to confirm that you chose the right cluster to delete.
4. After you reviewed the cluster information, choose **Yes, delete
   cluster**.
5. In the text field to confirm this deletion, type
   `delete`.
6. Choose **Delete** on the lower right corner of the pop-up
   window to finish sending the cluster deletion request.

###### Note

When cluster deletion fails due to attached SageMaker HyperPod task governance
policies, you will need to [Delete policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md").
