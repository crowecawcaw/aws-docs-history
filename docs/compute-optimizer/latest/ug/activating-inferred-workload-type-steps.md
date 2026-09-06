

# Activating inferred workload type
<a name="activating-inferred-workload-type-steps"></a>

This section provides you with instructions on how to activate the inferred workload type feature for member accounts of an AWS Organization or an individual AWS account holder.

## Prerequisites
<a name="inferred-prerequisites"></a>

Make sure that you have the appropriate permissions to activate the inferred workload type feature. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](security-iam.md#enhanced-infrastructure-metrics-permissions).

## Procedure
<a name="inferred-activate"></a>

**To activate the inferred workload type feature for member accounts of an AWS Organization or an individual AWS account holder**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane. Then, choose the **Inferred workload type** tab.

1. If you’re an individual AWS account holder, skip to step 4. 

   If you’re the account manager or delegated administrator of your organization, you can manage all member accounts or an individual member account for inferred workload type. 
   + To opt in all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt in an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt in for rightsizing preferences. Then, choose **Set account level**.  
![Account level preferences](http://docs.aws.amazon.com/compute-optimizer/latest/ug/images/iwt-accounts.png)

1. Choose **Edit**.

1. To deactivate the inferred workload type preference in an AWS Region, unselect the **Activate** checkbox. Then, choose **Save**.

1. (Optional) If you want to activate the inferred workload type preference in an AWS Region select the **Activate** checkbox. Then, choose **Save**..

1. (Optional) To add a new inferred workload type preference in an AWS Region, choose **Add a preference**. Then, select a **Region** and the **Activate** checkbox. Finally, choose **Save**.

## Additional resources
<a name="inferred-resources"></a>
+ [Opting out of external metrics ingestion](deactivate-external-metrics-ingestion.md)
+ [External metrics ingestion](external-metrics-ingestion.md)