

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with Amazon EKS in Application Manager
<a name="application-manager-working-EKS"></a>

Application Manager integrates with [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (Amazon EKS) to provide information about the health of your Amazon EKS cluster infrastructure. Application Manager applies a tag to your Amazon EKS cluster using the Amazon Resource Name (ARN) of the cluster as the tag value. Application Manager provides a component runtime view of the compute, networking, and storage resources in a cluster.

**Note**  
You can't manage or view operations information about your Amazon EKS pods or containers in Application Manager. You can only manage and view operations information about the infrastructure hosting your Amazon EKS resources.

**Actions you can perform on this page**  
You can perform the following actions on this page:
+ Choose **Manage cluster** to open the cluster in Amazon EKS.
+ Choose **View all** to view a list of resources in your cluster.
+ Choose **View in CloudWatch** to view resource alarms in Amazon CloudWatch.
+ Choose **Manage nodes** or **Manage Fargate profiles** to view these resources in Amazon EKS.
+ Choose a resource ID to view detailed information about it in the console where it was created.
+ View a list of OpsItems related to your clusters.
+ View a history of runbooks that have been run on your clusters.

**To open an **EKS clusters** application**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Application Manager**.

1. In the **Container clusters** section, choose **EKS clusters**.

1. Choose a cluster in the list. Application Manager opens the **Overview** tab.