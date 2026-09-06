

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Grant AWS services write access to Kubernetes APIs
<a name="mutate-kubernetes-resources"></a>

## Required permissions
<a name="mutate-kubernetes-resources-permissions"></a>

To enable AWS services to perform write operations on Kubernetes resources in your Amazon EKS cluster, you must grant both the `eks:AccessKubernetesApi` and `eks:MutateViaKubernetesApi` IAM permissions.

For example, Amazon SageMaker HyperPod uses these permissions to enable model deployment from SageMaker AI Studio. For more information, see [Set up optional JavaScript SDK permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html#sagemaker-hyperpod-model-deployment-setup-optional-js) in the Amazon SageMaker AI Developer Guide.

**Important**  
Write operations such as create, update, and delete require both permissions—if either permission is missing, write operations will fail.

## CloudTrail visibility
<a name="cloudtrail-visibility"></a>

While performing write operations on Kubernetes resources, you will see specific operation names in your CloudTrail logs:
+  `createKubernetesObject` - When creating new resources
+  `updateKubernetesObject` - When modifying existing resources
+  `deleteKubernetesObject` - When removing resources

These CloudTrail events provide detailed audit trails of all modifications made to your Kubernetes resources.

**Note**  
These operation names appear in CloudTrail logs for auditing purposes only. They are not IAM actions and cannot be used in IAM policy statements. To control write access to Kubernetes resources through IAM policies, use the `eks:MutateViaKubernetesApi` permission as shown in the [Required permissions](#mutate-kubernetes-resources-permissions) section.