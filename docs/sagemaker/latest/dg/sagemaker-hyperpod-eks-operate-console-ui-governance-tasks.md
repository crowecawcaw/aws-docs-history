

# Tasks
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-tasks"></a>

The following provides information on Amazon SageMaker HyperPod EKS cluster tasks. Tasks are operations or jobs that are sent to the cluster. These can be machine learning operations, like training, running experiments, or inference. The viewable task details list include status, run time, and how much compute is being used per task. 

In the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/), under **HyperPod Clusters**, you can navigate to the HyperPod console and view your list of HyperPod clusters in your Region. Choose your cluster and navigate to the **Tasks** tab.

For the **Tasks** tab to be viewable from anyone besides the administrator, the administrator needs to [add an access entry to the EKS cluster for the IAM role](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html). 

**Note**  
To view your HyperPod EKS cluster tasks in the dashboard:  
Configure Kubernetes Role-Based Access Control (RBAC) for data scientist users in the designated HyperPod namespace to authorize task execution on Amazon EKS-orchestrated clusters. Namespaces follow the format `hyperpod-ns-{{team-name}}`. To establish RBAC permissions, refer to the [team role creation instructions](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role).
Ensure that your job is submitted with the appropriate namespace and priority class labels. For a comprehensive example, see [Submit a job to SageMaker AI-managed queue and namespace](sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md#hp-eks-cli-start-job).

For EKS clusters, kubeflow (PyTorch, MPI, TensorFlow) tasks are shown. By default, PyTorch tasks are shown. You can filter for PyTorch, MPI, TensorFlow tasks by choosing the dropdown menu or using the search field. The information that is shown for each task includes the task name, status, namespace, priority class, and creation time. 