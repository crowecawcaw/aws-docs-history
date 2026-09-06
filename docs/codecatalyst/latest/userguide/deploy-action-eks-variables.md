

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# 'Deploy to Kubernetes cluster' variables
<a name="deploy-action-eks-variables"></a>

The **Deploy to Kubernetes cluster** action produces and sets the following variables at run time. These are known as *predefined variables*.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md).


| Key | Value | 
| --- | --- | 
| cluster | The Amazon.com Resource Name (ARN) of the of the Amazon EKS cluster that was deployed to during the workflow run.<br />Example: `arn:aws:eks:us-west-2:111122223333:cluster/codecatalyst-eks-cluster` | 
| deployment-platform | The name of the deployment platform.<br />Hardcoded to `AWS:EKS`. | 
| metadata | Reserved. JSON-formatted metadata related to the cluster deployed during the workflow run. | 
| namespace | The Kubernetes namespace into which the cluster was deployed.<br />Example: `default` | 
| resources | Reserved. JSON-formatted metadata related to the resources deployed during the workflow run. | 
| server | The name of the API server endpoint that you can use to communicate with your cluster using management tools such as `kubectl`.<br />For more information about the API service endpoint, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the **Amazon EKS User Guide**.<br />Example: `https://{{random-string}}.gr7.us-west-2.eks.amazonaws.com` | 