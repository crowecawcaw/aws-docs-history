

# Managing product versions

 As a seller, you can manage your product versions in AWS Marketplace by updating existing version information, adding new versions, or removing versions that are no longer supported. Each version has a unique SageMaker AI ARN and associated information that buyers use to evaluate and deploy your product. 

**Note**  
 You add the first version in **Step 2: Delivery configuration**, before you set up pricing in **Step 3: Procurement configuration**. When you add a later version to a product whose public offer has paid usage pricing, you also price any new instance types. For more information, see [Creating and publishing your listing](create-new-listing.md). 

## Viewing versions
<a name="ml-viewing-versions"></a>

The **Versions** table on your product's **Delivery** tab lists each version with its **Version name** and **Version visibility**:
+ **Limited**: The version isn't publicly discoverable on AWS Marketplace. Only allowlisted AWS accounts can use it.
+ **Public**: The version is publicly discoverable on AWS Marketplace and available for purchase to all buyers.
+ **Restricted**: The version is publicly discoverable on AWS Marketplace, but new buyers can't purchase it.

To open a version's details page, choose the version name. The details page shows the version's SageMaker AI resource, usage information, inputs, outputs, and recommended instance types. To open the resource in the SageMaker AI console, choose **View in SageMaker AI**.

## Updating version information
<a name="ml-updating-versions"></a>

 After creating a version, you can modify its release notes, usage instructions, model input and output details, input parameters, custom attributes, output parameters, Git repository and notebook links, and recommended instance types. For more information about instance recommendations, see [Changing the recommended instance types](#ml-recommended-instance-types). 

**Note**  
 You can change the version name only while your product has **Limited** visibility. You can't change the SageMaker AI ARN or the resource type. These changes require creating a new version. You can't update a restricted version, or any version while your product is in **Draft** or has **Restricted** visibility. 

**To update version information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** table, select the version.

1. Choose **Edit**, and then choose **Update version**.

   You can also choose the version name, and then choose **Edit version** on the version details page.

1. On the **Update version information** page, change the fields that you want to update.

   Under **Select version**, **Version** shows the version that you chose. Restricted versions aren't listed. The field limits are the same as when you add a version. For more information, see [Adding the initial version](add-initial-version.md).

1. Choose **Save and submit**.

   The button is available after you change at least one field.

Your change request appears on the product's **Change history** tab as **Update version information**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Edit** and **Add version** on the **Delivery** tab are unavailable.

Updating a version doesn't change your prices. To change prices, see [Updating product pricing](ml-update-public-offer.md).

## Changing the recommended instance types
<a name="ml-recommended-instance-types"></a>

 Each version of your product has a recommended instance type for each workload that it supports: real-time inference, batch transform, and, for algorithms, training. Buyers see your recommendations in these places: 
+  On the product detail page, in the pricing table, AWS Marketplace marks the price row for each recommended instance type with a thumbs-up icon and the label **Recommended**, and lists those rows first. The pricing table appears only when the product has a public offer with paid pricing, so free products don't show it. The product detail page shows the recommendations from your latest version. 
+  On the fulfillment page, for model packages, the CloudFormation launch option fills in your recommended real-time inference instance type. The AWS CLI commands on that page use your recommended real-time inference and batch transform instance types. 

 To move a recommendation to a different instance type, for example to recommend one instance type for real-time inference and another for batch transform, follow the steps in [Updating version information](#ml-updating-versions). When you edit the version, under **Recommended instance types**, choose an instance type in each of the following fields. The training field appears only for algorithms. 
+ **Recommended instance type for real-time inference**
+ **Recommended instance type for batch transform**
+ **Recommended instance type for training**

**Note**  
 Each list contains only the instance types that the version's Amazon SageMaker AI resource supports for that workload. AWS Marketplace rejects a recommended instance type that the resource doesn't support. 

 You can also change the recommended instance types with the `UpdateDeliveryOptions` change type. For more information, see [Update version information](https://docs.aws.amazon.com/marketplace/latest/developerguide/ml-update-version.html) in the *AWS Marketplace Catalog API Reference*. 

## Adding new versions
<a name="ml-adding-new-versions"></a>

 You can add new versions of your product to introduce features, updates, or improvements while maintaining access to previous versions. 

**To add a new version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** table, choose **Add version**.

1. Complete the wizard pages through **Configure instances and resources**, as described in [Adding the initial version](add-initial-version.md).

1. If the wizard shows a **Set prices** page, under **Pricing per instance type**, enter an hourly price for each new instance type, and then choose **Next**.

   The wizard shows this page only when your product has a public offer with paid usage pricing. If your public offer is free, the wizard skips this page and adds the new instance types at no charge.
   + The **Instance types** table lists each instance type that the version's SageMaker AI resource supports, with a price column for each workload: training (algorithms only), real-time inference, and batch transform.
   + Prices already on your public offer are read-only. Every other price is required.
   + To use one price for a whole column, enter it under **Pricing tool**, and then choose **Apply to all**. You can still edit each price afterward.
   + Each price must be from 0 to 100,000,000, with up to 3 decimal places.
   + If your offer charges per inference request, the table has no real-time inference column. Real-time inference stays charged at your per-inference price.

1. On the **Review and submit** page, choose **Add version**.

Your change request appears on the product's **Change history** tab as **Add version** followed by the version name. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Edit** and **Add version** on the **Delivery** tab are unavailable.

When your product has a public offer, the same request also updates the usage pricing on that offer. The request fails if a public version already uses the version name, if another version already uses the same SageMaker AI resource, or if the resource type differs from your product's other versions.

When you have successfully added a new version, buyers receive an email notification that a new version is available.

## Restricting versions
<a name="ml-restricting-versions"></a>

 When a version becomes outdated or you want to discontinue its availability, you can restrict buyer access to that version while maintaining access to other versions. 

New buyers can't subscribe to or deploy a restricted version. Buyers with an active subscription keep access, and AWS Marketplace guidelines require you to support them for 90 days. Restricting a version also restricts any pricing dimension that only that version uses.

The following rules apply:
+ You can restrict only versions that have **Public** visibility.
+ At least one version must stay **Public**, so you can't restrict every public version.
+ You can restrict up to 50 versions in one request.
+ You can't restrict versions while your product is in **Draft**.
+ You can't undo a restriction in AWS Partner Central.

**To restrict versions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** table, select the versions that you want to restrict.

1. Choose **Edit**, and then choose **Restrict version**.

   When you select more than one version, the option is **Restrict versions**. To restrict one version, you can also open its version details page and choose **Restrict version**.

1. In the confirmation dialog box, choose **Restrict version** or **Restrict versions**.

Your change request appears on the product's **Change history** tab as **Restrict version**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Edit** and **Add version** on the **Delivery** tab are unavailable.

 When you have successfully restricted a version, buyers receive an email notification that the version was restricted. 