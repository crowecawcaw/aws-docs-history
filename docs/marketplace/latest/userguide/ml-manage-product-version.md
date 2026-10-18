

# Managing product versions
<a name="ml-manage-product-version"></a>

 As a seller, you can manage your product versions in AWS Marketplace by updating existing version information, adding new versions, or removing versions that are no longer supported. Each version has a unique SageMaker AI ARN and associated information that buyers use to evaluate and deploy your product. 

**Note**  
 Before adding versions, create a product ID and establish pricing. For more information, see [Step 1: Create a new listing](create-new-listing.md). 

## Updating version information
<a name="ml-updating-versions"></a>

 After creating a version, you can modify its associated information such as release notes, usage instructions, and instance recommendations. For more information about instance recommendations, see [Changing the recommended instance types](#ml-recommended-instance-types). 

**Note**  
 Version names and ARNs cannot be modified. These changes require creating a new version. 

1.  Sign in to your seller account in the [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home). 

1.  Go to the **Machine learning product** page and select your product. 

1.  Choose **Request changes** and select **Update version information**. 

1.  Select the version you want to update. 

1.  Choose **Edit version**. 

1.  Modify the necessary fields and choose **Next**. 

1.  Enter your pricing information and choose **Submit**. For more information, see [Step 4: Configure the pricing model](set-pricing-model.md). 

 You can monitor your request from the **Requests** tab of the **Machine learning** products page. For more information on statuses, see [Machine learning product status](ml-product-lifecycle.md#ml-product-status). 

## Changing the recommended instance types
<a name="ml-recommended-instance-types"></a>

 Each version of your product has a recommended instance type for each workload that it supports: real-time inference, batch transform, and, for algorithms, training. Buyers see your recommendations in these places: 
+  On the product detail page, in the pricing table, AWS Marketplace marks the price row for each recommended instance type with a thumbs-up icon and the label **Recommended**, and lists those rows first. The pricing table appears only when the product has a public offer with paid pricing, so free and BYOL products don't show it. The product detail page shows the recommendations from your latest version. 
+  On the fulfillment page, for model packages, the CloudFormation launch option fills in your recommended real-time inference instance type. The AWS CLI commands on that page use your recommended real-time inference and batch transform instance types. 

 To move a recommendation to a different instance type, for example to recommend one instance type for real-time inference and another for batch transform, follow the steps in [Updating version information](#ml-updating-versions). When you edit the version, under **Recommended instance types**, choose the instance type for each workload. The training option appears only for algorithms. 
+ **Recommended instance type for real-time inferences**
+ **Recommended instance type for batch transform**
+ **Recommended instance type for training**

**Note**  
 Each list contains only the instance types that the version's Amazon SageMaker AI resource supports for that workload. AWS Marketplace rejects a recommended instance type that the resource doesn't support. 

 You can also change the recommended instance types with the `UpdateDeliveryOptions` change type. For more information, see [Update version information](https://docs.aws.amazon.com/marketplace/latest/developerguide/ml-update-version.html) in the *AWS Marketplace Catalog API Reference*. 

## Adding new versions
<a name="ml-adding-new-versions"></a>

 You can add new versions of your product to introduce features, updates, or improvements while maintaining access to previous versions. 

1.  Sign in to your seller account in the [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home). 

1.  Go to the **Machine learning product** page and select your product. 

1.  Choose **Versions** and choose **Add new version**. 

1.  Enter information for the new version following the steps in [Step 3: Add initial product version](add-initial-version.md). 

1.  Enter your pricing information and choose **Submit**. For more information, see [Step 4: Configure the pricing model](set-pricing-model.md). 

When you have successfully added a new version, buyers receive an email notification that a new version is available.

## Restricting versions
<a name="ml-restricting-versions"></a>

 When a version becomes outdated or you want to discontinue its availability, you can restrict buyer access to that version while maintaining access to other versions. 

1.  Sign in to your seller account in the [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home). 

1.  Go to the **Machine learning product** page and select your product. 

1.  Choose **Versions** and choose **Restrict versions**. 
**Note**  
 You must always have at least one version available. 

1.  Choose **Submit**. 

 When you have successfully restricted a version, buyers receive an email notification that the version was restricted. 