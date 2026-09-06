

# Dashboard
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-metrics"></a>

Amazon SageMaker HyperPod task governance provides a comprehensive dashboard view of your Amazon EKS cluster utilization metrics, including hardware, team, and task metrics. The following provides information on your HyperPod EKS cluster dashboard.

The dashboard provides a comprehensive view of cluster utilization metrics, including hardware, team, and task metrics. You will need to install the EKS add-on to view the dashboard. For more information, see [Dashboard setup](sagemaker-hyperpod-eks-operate-console-ui-governance-setup-dashboard.md).

In the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/), under **HyperPod Clusters**, you can navigate to the HyperPod console and view your list of HyperPod clusters in your Region. Choose your cluster and navigate to the **Dashboard** tab. The dashboard contains the following metrics. You can download the data for a section by choosing the corresponding **Export**.

**Utilization**

Provides health of the EKS cluster point-in-time and trend-based metrics for critical compute resources. By default, **All Instance Groups** are shown. Use the dropdown menu to filter your instance groups. The metrics included in this section are:
+ Number of total, running, and pending recovery instances. The number of pending recovery instances refer to the number of instances that need attention for recovery.
+ GPUs, GPU memory, vCPUs, and vCPUs memory.
+ GPU utilization, GPU memory utilization, vCPU utilization, and vCPU memory utilization.
+ An interactive graph of your GPU and vCPU utilization. 

**Teams**

Provides information into team-specific resource management. This includes:
+ Instance and GPU allocation.
+ GPU utilization rates.
+ Borrowed GPU statistics.
+ Task status (running or pending).
+ A bar chart view of GPU utilization versus compute allocation across teams.
+ Team detailed GPU and vCPU-related information. By default, the information displayed includes **All teams**. You can filter by team and instances by choosing the dropdown menus. In the interactive plot you can filter by time.

**Tasks**

**Note**  
To view your HyperPod EKS cluster tasks in the dashboard:  
Configure Kubernetes Role-Based Access Control (RBAC) for data scientist users in the designated HyperPod namespace to authorize task execution on Amazon EKS-orchestrated clusters. Namespaces follow the format `hyperpod-ns-{{team-name}}`. To establish RBAC permissions, refer to the [team role creation instructions](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role).
Ensure that your job is submitted with the appropriate namespace and priority class labels. For a comprehensive example, see [Submit a job to SageMaker AI-managed queue and namespace](sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md#hp-eks-cli-start-job).

Provides information on task-related metrics. This includes number of running, pending, and preempted tasks, and run and wait time statistics. By default, the information displayed includes **All teams**. You can filter by team by choosing the dropdown menu. In the interactive plot you can filter by time.