

# Activating savings estimation mode
<a name="activate-savings-estimation-mode"></a>

This section provides you with instructions on how to activate or deactivate the savings estimation mode preference for member accounts within specific AWS Regions.

## Procedure
<a name="sem-configure"></a>

**To activate savings estimation mode**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane.

1. Choose the **Savings estimation mode** tab. Then, choose **Edit**.  
![Choose the Edit button](http://docs.aws.amazon.com/compute-optimizer/latest/ug/images/sem-edit.png)

1. In the pop-up window that appears, select the AWS Regions where you want to activate the savings estimation mode preference. Then, choose **Save**.  
![Select the AWS Regions and save](http://docs.aws.amazon.com/compute-optimizer/latest/ug/images/sem-activate-save.png)

1. (Optional) Unselect the AWS Regions where you want to deactivate the savings estimation mode preference.

When you activate the savings estimation mode preference, it can take up to 24 hours for your new recommendations with specific discounts to appear. You can view your specific discount recommendations in the **Estimated monthly savings (after discounts)** column of a given AWS resource. For more information, see [ Estimated monthly savings and savings opportunity](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-savings-calculation).