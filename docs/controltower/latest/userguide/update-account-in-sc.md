

# Update a single account
<a name="update-account-in-sc"></a>

**Note**  
Single account provision, update and customization must target an organizational unit (OU) with AWSControlTowerBaseline enabled. If an OU does not have the AWSControlTowerBaseline enabled, you can activate account auto-enrollment or use ResetEnabledBaseline and ResetEnabledControl APIs on EnabledBaselines and EnabledControls on that OU to enroll accounts. For details of AWSControlTowerBaseline, see: [Baseline types that apply at the OU level](types-of-baselines.md#ou-baseline-types). 

You can update individual AWS Control Tower accounts in the AWS Control Tower console, or in the Service Catalog console.

To update a single account in the AWS Control Tower console, see [Update the account in the console](updating-account-factory-accounts.md#update-account-in-console).

**To update a single account in AWS Service Catalog**

1. Go to AWS Service Catalog.

1. In the left-pane navigation menu, choose **Provisioned products**.

1. On the **Provisioned products** page, select the radio button next to the provisioned product you want to update.

1. In the upper right, choose the **Actions** dropdown to **Update**.

To learn more about updating in AWS Service Catalog, see [Update the provisioned product in Service Catalog](update-provisioned-product.md) and [Updating products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-update.html) in the *Service Catalog Administrator Guide*.