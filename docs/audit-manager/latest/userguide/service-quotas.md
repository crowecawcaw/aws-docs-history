

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Understanding quotas and restrictions for AWS Audit Manager
<a name="service-quotas"></a>



Your AWS account has default quotas, formerly referred to as *limits*, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas can’t be increased. 

Most Audit Manager quotas, but not all, are listed under the AWS Audit Manager namespace in the Service Quotas console. To learn how to request a quota increase, see [Managing your Audit Manager quotas](#managing-your-service-quotas).

**Contents**
+ [Default Audit Manager quotas](#audit-manager-quotas)
+ [Managing your Audit Manager quotas](#managing-your-service-quotas)
+ [Additional resources](#audit-manager-quotas-additional-resources)

## Default Audit Manager quotas
<a name="audit-manager-quotas"></a>

The following AWS Audit Manager quotas are per AWS account per Region.


| Resource | Quota | 
| --- | --- | 
| **Assessments** | Number of active assessments per account: 100 | 
| Controls | Number of custom controls per account: 500 | 
| Evidence | Maximum size of a single manual evidence file: 100 MB<br />Number of daily manual evidence uploads per control: 100 If you need to upload a large amount of manual evidence to a single control, we recommend that you upload your evidence in batches across several days.  | 
| Frameworks | Number of custom frameworks per account: 100 Framework quotas apply to all shared custom frameworks in your framework library, regardless of who created the framework.   | 
| Shared custom framework recipients | Number of active recipient accounts: 100 | 
| API access | Number of transactions per second (TPS) across all APIs: 20 TPS  | 

## Managing your Audit Manager quotas
<a name="managing-your-service-quotas"></a>

AWS Audit Manager is integrated with Service Quotas, an AWS service that enables you to view and manage your quotas from a central location. Service Quotas makes it easy to look up the value of your Audit Manager quotas. 

**To view Audit Manager service quotas using the console**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **AWS Audit Manager**.

1. In the **Service quotas** list, you can see the service quota name, applied quota value (if it's available), AWS default quota value, and whether the quota is adjustable.

1. To view additional information about a service quota, such as the description, choose the quota name.

1. (Optional) To request a quota increase, select the quota that you want to increase, select **Request quota increase**, enter or select the required information, and select **Request**.

## Additional resources
<a name="audit-manager-quotas-additional-resources"></a>

For more information about how to manage your quotas, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

For more information about Service Quotas, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*. 