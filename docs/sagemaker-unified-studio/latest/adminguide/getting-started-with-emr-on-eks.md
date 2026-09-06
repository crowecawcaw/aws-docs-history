

# Getting started with Amazon EMR on EKS in Amazon SageMaker Unified Studio
<a name="getting-started-with-emr-on-eks"></a>

 Before you begin with Amazon EMR on EKS, you must have a compatible Amazon EKS cluster. If you do not have an existing Amazon EKS cluster, see [Get started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) for more information regarding cost, installation and management of an Amazon EKS cluster. 

 Amazon EMR on EKS and Amazon SageMaker Unified Studio require additional Amazon EKS cluster configurations granting minimum access controls and connectivity. Review your Amazon EKS cluster configuration and ensure all requirements are fulfilled: 

1.  [ Install and configure the Load Balancer Controller for your Amazon EKS cluster ](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html) 

1.  Tag exactly one security group for each Amazon EC2 node ENI with `kubernetes.io/cluster/{{{eks-cluster-name}}}`. 

   1.  Amazon EMR on EKS routes the connection from Amazon SageMaker Unified Studio notebooks to [Apache Livy](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-livy.html) on your Amazon EKS cluster through a Network Load Balancer, and the AWS Load Balancer Controller discovers the cluster security group by looking for a single security group that carries this tag on each node ENI. If the same ENI has more than one security group with this tag, the controller cannot reconcile the `TargetGroupBinding`, no targets register in the load balancer target group, and notebook connections fail (for example, with RemoteDisconnected errors). If you use Karpenter to provision nodes, confirm that your `securityGroupSelectorTerms` configuration does not attach multiple cluster-tagged security groups to a node ENI. 

1.  [ Enable Amazon EKS cluster access for Amazon EMR on EKS and Amazon SageMaker Unified Studio ](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.html) 

 Additionally, Amazon EKS clusters in a different account or Amazon VPC network than your Amazon SageMaker Unified Studio domain require additional configuration. Review your Amazon EKS cluster configuration and ensure all requirements are fulfilled: 

1.  [ Enable cross-account access for Amazon EMR on EKS using Amazon SageMaker Unified Studio associated domains ](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-cross-account-access-using-associated-domains.html) 

1.  [ Enable cross-network access for Amazon SageMaker Unified Studio using VPC peering connections ](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-cross-network-access-using-vpc-peering.html) 

## Configure project profiles in Amazon SageMaker Unified Studio for Amazon EMR on EKS
<a name="configure-project-profile-for-emr-on-eks"></a>

 For data workers to use Amazon EMR on EKS in Amazon SageMaker Unified Studio, administrators must configure project profiles with Amazon EMR on EKS environment blueprint configurations. 

**Note**  
 Administrators can configure multiple environment blueprint configurations using different Amazon EKS clusters in the same project profile. Data workers can view environment blueprint configurations and select a specific Amazon EKS cluster when creating Amazon EMR on EKS resources in a Amazon SageMaker Unified Studio project. 

1.  Navigate to the [Amazon SageMaker Unified Studio management console](https://console.aws.amazon.com/datazone). 

1.  From the navigation bar, select **Domains**. For cross-account Amazon EKS clusters, select **Associated domains**. 

1.  Select the name of the domain you want to configure Amazon EMR on EKS for. 

1.  In the domain management view, navigate to **Project profiles**. 

1.  Search for and select your target project profile. 

1.  In the project profile management view, navigate to the **Blueprint deployment settings** view and select **Blueprint deployment settings**. 

1.  In the **Blueprint** section, select **EmrOnEks** from the dropdown. 

1.  In the **Account and region** section, specify the same AWS account and AWS region as your Amazon EKS cluster. 

1.  In the **Blueprint parameters** section, specify the Amazon EKS cluster ARN as the `eksClusterArn` user parameter value. 

1.  At the bottom of the page, select **Add blueprint deployment settings** to create your Amazon EMR on EKS environment blueprint configuration. 