

# Installing GuardDuty security agent manually on Amazon EKS resources
<a name="eksrunmon-deploy-security-agent"></a>

This section describes how you can deploy the GuardDuty security agent for the first time for specific EKS clusters. Before you proceed with this section, make sure you have already set up the prerequisites and enabled Runtime Monitoring for your accounts. The GuardDuty security agent (EKS add-on) will not work if you do not enable Runtime Monitoring. 

Choose your preferred access method to deploy the GuardDuty security agent for the first time.

------
#### [ Console ]

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose your **Cluster name**.

1. Choose the **Add-ons** tab.

1. Choose **Get more add-ons**.

1. On the **Select add-ons** page, choose **Amazon GuardDuty EKS Runtime Monitoring**.

1. GuardDuty recommends choosing the latest and default agent **Version**.

1. On the **Configure selected add-on settings** page, use the default settings. If the **Status** of your EKS add-on is **Requires activation**, choose **Activate GuardDuty**. This action will open the GuardDuty console to configure Runtime Monitoring for your accounts.

1. After you've configured Runtime Monitoring for your accounts, switch back to the Amazon EKS console. The **Status** of your EKS add-on should have changed to **Ready to install**. 

1. 

**(Optional) Providing EKS add-on configuration schema**

   For the add-on **Version**, if you choose **v1.5.0** or above, Runtime Monitoring supports configuring specific parameters of the GuardDuty agent. For information about parameter ranges, see [Configure EKS add-on parameters](guardduty-configure-security-agent-eks-addon.md).

   1. Expand **Optional configuration settings** to view the configurable parameters and their expected value and format.

   1. Set the parameters. The values must be in the range provided in [Configure EKS add-on parameters](guardduty-configure-security-agent-eks-addon.md).

   1. Choose **Save changes** to create the add-on based on the advanced configuration.

   1. For **Conflict resolution method**, the option that you choose will be used to resolve a conflict when you update the value of a parameter to a non-default value. For more information about the listed options, see [resolveConflicts](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html#AmazonEKS-UpdateAddon-request-resolveConflicts) in the *Amazon EKS API Reference*.

1. Choose **Next**.

1. On the **Review and create** page, verify all the details, and choose **Create**.

1. Navigate back to the cluster details and choose the **Resources** tab. 

1. You can view the new pods with the prefix **aws-guardduty-agent**. 

------
#### [ API/CLI ]

You can configure the Amazon EKS add-on agent (`aws-guardduty-agent`) using either of the following options:
+ Run [CreateAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAddon.html) for your account.
+ 
**Note**  
For the add-on `version`, if you choose **v1.5.0 or above**, Runtime Monitoring supports configuring specific parameters of the GuardDuty agent. For more information, see [Configure EKS add-on parameters](guardduty-configure-security-agent-eks-addon.md).

  Use the following values for the request parameters:
  + For `addonName`, enter `aws-guardduty-agent`.

    You can use the following AWS CLI example when using configurable values supported for add-on versions `v1.5.0` or above. Make sure to replace the placeholder values highlighted in red and the associated `Example.json` with the configured values.

    ```
    aws eks create-addon --region {{us-east-1}} --cluster-name {{myClusterName}} --addon-name aws-guardduty-agent --addon-version {{v1.16.0-eksbuild.2}} --configuration-values {{'file://example.json'}}
    ```  
**Example.json**  

    ```
    {
    	"priorityClassName": "aws-guardduty-agent.priorityclass-high",
    	"dnsPolicy": "Default",
    	"resources": {
    		"requests": {
    			"cpu": "237m",
    			"memory": "512Mi"
    		},
    		"limits": {
    			"cpu": "2000m",
    			"memory": "2048Mi"
    		}
    	}	
    }
    ```
  + For information about supported `addonVersion`, see [Kubernetes versions supported by GuardDuty security agent](prereq-runtime-monitoring-eks-support.md#gdu-agent-supported-k8-version).
+ Alternatively, you can use AWS CLI. For more information, see [create-addon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-addon.html).

------

**Private DNS names for VPC endpoint**  
By default, the security agent resolves and connects to the private DNS name of the VPC endpoint. For a non-FIPS endpoint, your private DNS will appear in the following format:  
Non-FIPS endpoint – `guardduty-data.{{us-east-1}}.amazonaws.com`  
The AWS Region, {{us-east-1}}, will change based on your Region.