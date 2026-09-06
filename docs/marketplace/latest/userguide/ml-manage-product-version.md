

# Managing product versions
<a name="ml-manage-product-version"></a>

 As a seller, you can manage your product versions in AWS Marketplace by updating existing version information, adding new versions, or removing versions that are no longer supported. Each version has a unique SageMaker AI ARN and associated information that buyers use to evaluate and deploy your product. 

**Note**  
 Before adding versions, create a product ID and establish pricing. For more information, see [Step 1: Create a new listing](create-new-listing.md). 

## Updating version information
<a name="ml-updating-versions"></a>

 After creating a version, you can modify its associated information such as release notes, usage instructions, and instance recommendations. 

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