# Update a blueprint

The following procedures describe how to update custom blueprints and how to deploy
them.

###### To update your custom blueprints

1. Update your CloudFormation template or Terraform tar.gz file (blueprint) with your new
   configurations.
2. Save the updated blueprint as a new version in AWS Service Catalog.

###### To deploy your updated blueprint

1. Navigate to the **Organization** page in the AWS Control Tower
   console.
2. Filter the **Organization** page by blueprint name and
   version.
3. Follow the **Update account** process, and deploy the latest
   blueprint version in your account.
   **If a blueprint update is unsuccessful**

AWS Control Tower allows blueprint updates when the provisioned product is in the `AVAILABLE` state. If your provisioned product is in a `TAINTED` state, the update will fail. We recommend the following workaround:

1. In the AWS Service Catalog console, manually update the `TAINTED` provisioned product to change the state to `AVAILABLE`. For more information, see [Updating provisioned products](../../../servicecatalog/latest/userguide/enduser-update.md "../../../servicecatalog/latest/userguide/enduser-update.md").
2. Then, follow the update account process from AWS Control Tower to fix the blueprint deployment error.
   _We recommend this manual step because:_ When you remove a blueprint, it can cause resources in the member account to be removed. Removing resources may affect your existing workloads. For this reason, we recommend this method rather than the alternative way of updating a blueprint—which is by removing and replacing the original blueprint—especially if you are running production workloads.
