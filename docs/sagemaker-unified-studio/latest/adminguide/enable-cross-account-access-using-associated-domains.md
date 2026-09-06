

# Enable cross-account access for Amazon EMR on EKS using Amazon SageMaker Unified Studio associated domains
<a name="enable-cross-account-access-using-associated-domains"></a>

 Amazon EMR on EKS virtual clusters require an Amazon EKS cluster residing in the same account. As an admin, you can make use of Amazon SageMaker Unified Studio associated domains to bring Amazon EKS clusters from any account and use with any Amazon SageMaker Unified Studio domain. 

 Enabling cross-account access for Amazon EMR on EKS using Amazon SageMaker Unified Studio associated domains requires high privilege access to both Amazon EKS cluster account and Amazon SageMaker Unified Studio domain account. 

## Step 1: Submit associated domain request from the Amazon SageMaker Unified Studio domain account
<a name="submit-associated-domain-request-from-the-domain-account"></a>

1.  Navigate to the [Amazon SageMaker Unified Studio management console](https://console.aws.amazon.com/datazone). 

1.  From the navigation bar, select **Domains**. 

1.  Select the name of the domain you want to configure Amazon EMR on EKS for. 

1.  In the domain management view, navigate to **Account associations**. 

1.  Select the **Request association** button. 

1.  In the request domain association view, under accounts, provide the Amazon EKS cluster account. 

1.  Select the **Request assocation** button to submit. 

## Step 2: Accept and configure associated domain in the Amazon EKS cluster account
<a name="accept-and-configure-associated-domain-in-the-cluster-account"></a>

1.  Navigate to the [Amazon SageMaker Unified Studio management console](https://console.aws.amazon.com/datazone). 

1.  Select **Associated domains**. 

1.  Under **Requests**, select the name of the domain you requested domain association for. 

1.  In the domain association request view, select **Accept association**. 

1.  After domain association succeeds, select the domain name to navigate the domain management view. 

1.  In the domain management view, select **Blueprints**. 

1.  In the Tooling section, select **Enable** and configure the associated Tooling environment. 

1.  In the Blueprints section, select **EmrOnEks**, enable and configure the associated EmrOnEks environment. 

**Note**  
 The IAM role designated as the provisioning role must have access to the Amazon EKS cluster. See [ Enable Amazon EKS cluster access for Amazon EMR on EKS and Amazon SageMaker Unified Studio ](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.html) 