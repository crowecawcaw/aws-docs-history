# Update a single account

###### Note

Single account provision, update and customization must target an organizational unit (OU)
with AWSControlTowerBaseline enabled. If an OU does not have the AWSControlTowerBaseline enabled, you can activate account auto-enrollment
or use ResetEnabledBaseline and ResetEnabledControl APIs on EnabledBaselines and EnabledControls on that OU to enroll accounts.
There are no single account provisioning limitations when an OU has the AWSControlTowerBaseline enabled.

You can update individual AWS Control Tower accounts in the AWS Control Tower console, or in the Service Catalog
console.

To update a single account in the AWS Control Tower console, see [Update the account in the
console](updating-account-factory-accounts.md#update-account-in-console "updating-account-factory-accounts.md#update-account-in-console").

###### To update a single account in AWS Service Catalog

1. Go to AWS Service Catalog.
2. In the left-pane navigation menu, choose **Provisioned
   products**.
3. On the **Provisioned products** page, select the radio button
   next to the provisioned product you want to update.
4. In the upper right, choose the **Actions** dropdown to
   **Update**.
   To learn more about updating in AWS Service Catalog, see [Update the provisioned product in Service Catalog](update-provisioned-product.md "update-provisioned-product.md")
   and [Updating
   products](../../../servicecatalog/latest/adminguide/productmgmt-update.md "../../../servicecatalog/latest/adminguide/productmgmt-update.md") in the _Service Catalog Administrator
   Guide_.
