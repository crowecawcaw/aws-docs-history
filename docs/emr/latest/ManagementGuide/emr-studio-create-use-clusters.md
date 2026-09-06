

# Attach a compute to an EMR Studio Workspace
<a name="emr-studio-create-use-clusters"></a>

Amazon EMR Studio runs notebook commands using a kernel on an EMR cluster. Before you can select a kernel, you should attach the Workspace to a cluster that uses Amazon EC2 instances, to an Amazon EMR on EKS cluster, or to an EMR Serverless application. EMR Studio lets you attach Workspaces to new or existing clusters, and gives you the flexibility to change clusters without closing the Workspace.

**Topics**
+ [Attach an Amazon EC2 cluster](#emr-studio-attach-cluster)
+ [Attach an Amazon EMR on EKS cluster](#emr-studio-use-eks-cluster)
+ [Attach an EMR Serverless application](#emr-studio-use-serverless-studio)
+ [Create a cluster](#emr-studio-create-cluster)
+ [Detach a compute](#emr-studio-detach-cluster)

## Attach an Amazon EC2 cluster to an EMR Studio Workspace
<a name="emr-studio-attach-cluster"></a>

You can attach an EMR cluster running on Amazon EC2 to a Workspace when you create the Workspace, or attach a cluster to an existing Workspace. If you want to create and attach a *new* cluster, see [Create and attach a new EMR cluster to an EMR Studio Workspace](#emr-studio-create-cluster).

**Note**  
A workspace in a Studio that has IAM Identity Center trusted identity propagation enabled can only attach to an EMR cluster with a security configuration that has Identity Center enabled.

------
#### [ On create ]

**Attach to an Amazon EMR compute cluster when you create a Workspace**

1. In the **Create a Workspace** dialog box, make sure you've already selected a subnet for the new Workspace. Expand the **Advanced configuration** section.

1. Choose **Attach Workspace to an EMR cluster**.

1. In the ** EMR cluster** dropdown list, select an existing EMR cluster to attach to the Workspace.

After you attach a cluster, finish creating the Workspace. When you open the new Workspace for the first time and choose the ** EMR clusters** panel, you should see your selected cluster attached.

------
#### [ On launch ]

**Attach to an Amazon EMR compute cluster when you launch the Workspace**

1. Navigate to the Workspaces list and select the row for the Workspace that you want to launch. Then, select **Launch Workspace** > **Launch with options**.

1. Choose an EMR cluster to attach to your Workspace.

After you attach a cluster, finish creating the Workspace. When you open the new Workspace for the first time and choose the **EMR clusters** panel, you should see your selected cluster attached.

------
#### [ In JupyterLab ]

**Attach a Workspace to an Amazon EMR compute cluster in JupyterLab**

1. Select your Workspace, then select **Launch Workspace** > **Quick launch**.

1. Inside JupyterLab, open the **Cluster**tab in the left sidebar.

1. Select the **EMR on EC2 cluster** dropdown, or select an Amazon EMR on EKS cluster.

1. Select **Attach** to attach the cluster to your Workspace.

After you attach the cluster, finish creating the Workspace. When you open the new Workspace for the first time and choose the ** EMR clusters** panel, you should see your selected cluster attached.

------
#### [ In the Workspace UI ]

**Attach a Workspace to an Amazon EMR compute cluster from the Workspace user interface**

1. In the Workspace that you want to attach to a cluster, choose the ** EMR clusters** icon from the left sidebar to open the **Cluster** panel.

1. Under **Cluster type**, expand the dropdown and select ** EMR cluster on EC2**.

1. Choose a cluster from the dropdown list. You might need to detach an existing cluster first to enable the cluster selection dropdown list.

1. Choose **Attach**. When the cluster is attached, you should see a success message appear.

------

## Attach an Amazon EMR on EKS cluster to an EMR Studio Workspace
<a name="emr-studio-use-eks-cluster"></a>

In addition to using Amazon EMR clusters running on Amazon EC2, you can attach a Workspace to an Amazon EMR on EKS cluster to run notebook code. For more information about Amazon EMR on EKS, see [What is Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html).

Before you can connect a Workspace to an Amazon EMR on EKS cluster, your Studio administrator must grant you access permissions.

**Note**  
You can't launch an Amazon EMR on EKS cluster in a EMR Studio that uses IAM Identity Center trusted identity propagation. 

------
#### [ On create ]

**To attach an Amazon EMR on EKS cluster when you create a Workspace**

1. In the **Create a Workspace** dialog box, expand the **Advanced configuration** section.

1. Choose **Attach Workspace to an Amazon EMR on EKS cluster**.

1. Under **Amazon EMR on EKS cluster**, choose a cluster from the dropdown list.

1. Under **Select an endpoint**, choose a managed endpoint to attach to the Workspace. A managed endpoint is a gateway that lets EMR Studio communicate with your chosen cluster.

1. Choose **Create a Workspace** to finish the Workspace creation process and attach the selected cluster.

After you attach a cluster, you can finish the Workspace creation process. When you open the new Workspace for the first time and choose the ** EMR clusters** panel, you should see that your selected cluster is attached.

------
#### [ In the Workspace UI ]

**To attach an Amazon EMR on EKS cluster from the Workspace user interface**

1. In the Workspace that you want to attach to a cluster, choose the ** EMR clusters** icon from the left sidebar to open the **Cluster** panel.

1. Expand the **Cluster type** dropdown and choose ** EMR clusters on EKS**.

1. Under ** EMR cluster on EKS**, choose a cluster from the dropdown list.

1. Under **Endpoint**, choose a managed endpoint to attach to the Workspace. A managed endpoint is a gateway that lets EMR Studio communicate with your chosen cluster.

1. Choose **Attach**. When the cluster is attached, you should see a success message appear.

------

## Attach an Amazon EMR Serverless application to an EMR Studio Workspace
<a name="emr-studio-use-serverless-studio"></a>

You can attach a Workspace to an EMR Serverless application to run interactive workloads. For more information, see [Using notebooks to run interactive workloads with EMR Serverless through EMR Studio](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads.html).

**Note**  
You can't attach an EMR Serverless application to a EMR Studio that uses IAM Identity Center trusted identity propagation. 

**Example Attach a Workspace to an EMR Serverless application in JupyterLab**  
Before you can connect a Workspace to an EMR Serverless application, your account administrator must grant you access permissions as described in [Required permissions for interactive workloads](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads.html#interactive-permissions).  

1. Navigate to EMR Studio select your Workspace, then select **Launch Workspace** > **Quick launch**.

1. Inside JupyterLab, open the **Cluster** tab in the left sidebar.

1. Select **EMR Serverless** as a compute option, then select an EMR Serverless application and a runtime role.

1. To attach the cluster to your Workspace, choose **Attach**.
Now when you open this Workspace, you should see your selected application attached.

## Create and attach a new EMR cluster to an EMR Studio Workspace
<a name="emr-studio-create-cluster"></a>

Advanced EMR Studio users can provision new EMR clusters running on Amazon EC2 to use with a Workspace. The new cluster has all of the big data applications that are required for EMR Studio installed by default. 

To create clusters, your Studio administrator must first give you permission using a session policy. For more information, see [Create permissions policies for EMR Studio users](emr-studio-user-permissions.md#emr-studio-permissions-policies).

You can create a new cluster in the **Create a Workspace** dialog box or from the **Cluster** panel in the Workspace UI. Either way, you have two cluster creation options:

1. **Create an EMR cluster** – Create an EMR cluster by choosing the Amazon EC2 instance type and count.

1. **Use a cluster template** – Provision a cluster by selecting a predefined cluster template. This option appears if you have permission to use cluster templates.
**Note**  
If you enabled trusted identity propagation with IAM Identity Center for your Studio, then you must use a template to create a cluster.

**To create an EMR cluster by providing a cluster configuration**

1. Choose a starting point.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-use-clusters.html)

1. Enter a **Cluster name**. Naming the cluster helps you find it later in the EMR Studio Clusters list.

1. For **Amazon EMR release**, Choose an Amazon EMR release version for the cluster.

1. For **Instance**, select the type and number of Amazon EC2 instances for the cluster. For more information about selecting instance types, see [Configure Amazon EC2 instance types for use with Amazon EMR](emr-plan-ec2-instances.md). One instance will be used as the primary node.

1. Select a **Subnet** where EMR Studio can launch the new cluster. Each subnet option is preapproved by your Studio administrator, and your Workspace should be able to connect to a cluster in any listed subnet.

1. Choose an **S3 URI for log storage**.

1. Choose **Create EMR cluster** to provision the cluster. If you use the **Create a Workspace** dialog box, choose **Create a Workspace** to create the Workspace and provision the cluster. After EMR Studio provisions the new cluster, it attaches the cluster to the Workspace.

**To create a cluster using a cluster template**

1. Choose a starting point.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-use-clusters.html)

1. Select a cluster template from the dropdown list. Each available cluster template includes a brief description to help you make a selection.

1. The cluster template you choose may have additional parameters such as Amazon EMR release version or cluster name. You can choose or insert values, or use the default values that your administrator selected.

1. Select a **Subnet** where EMR Studio can launch the new cluster. Each subnet option is preapproved by your Studio administrator, and your Workspace should be able to connect to a cluster in any subnet.

1. Choose **Use cluster template** to provision the cluster and attach it to the Workspace. It will take a few minutes for EMR Studio to create the cluster. If you use the **Create a Workspace** dialog box, choose **Create a Workspace** to create the Workspace and provision the cluster. After EMR Studio provisions the new cluster, it attaches the cluster to your Workspace.

## Detach a compute from an EMR Studio Workspace
<a name="emr-studio-detach-cluster"></a>

To exchange the cluster attached to a Workspace, you can detach a cluster from the Workspace UI.

**To detach a cluster from a Workspace**

1. In the Workspace that you want to detach from a cluster, choose the ** EMR clusters** icon from the left sidebar to open the **Cluster** panel.

1. Under **Select cluster**, choose **Detach** and wait for EMR Studio to detach the cluster. When the cluster is detached, you will see a success message.

**To detach an EMR Serverless application from an EMR Studio Workspace**

To exchange the compute attached to a Workspace, you can detach the application from the Workspace UI. 

1. In the Workspace that you want to detach from a cluster, choose the **Amazon EMR compute** icon from the left sidebar to open the **Compute** panel.

1. Under **Select compute**, choose **Detach** and wait for EMR Studio to detach the application. When the application is detached, you will see a success message.