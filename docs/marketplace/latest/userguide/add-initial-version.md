

# Adding the initial version

 This page guides you through adding the initial version of your product. Your product may have multiple versions throughout its lifecycle, and each version is identified by a unique SageMaker AI ARN. 

You add the initial version in **Step 2: Delivery configuration** of the **Complete your listing** progress bar.

**Tip**  
Step 2 also has an optional card, **Prepare your product in SageMaker AI**, that links to the topics in [Preparing your product in SageMaker AI](ml-prepare-your-product-in-sagemaker.md).

**To add the initial version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 2: Delivery configuration**, on the **Add version** card, choose **Start**.

   You can instead choose the **Delivery** tab, and then choose **Add version**.

1. On the **Configure SageMaker AI resource** page, under **Amazon Resource Names (ARNs)**, for **Amazon SageMaker AI ARN**, enter the ARN of your model package or algorithm.
   +  Example model package ARN: `arn:aws:sagemaker:{{<region>}}:{{<account-id>}}:model-package/{{<model-package-name>}}` 

     To find your model package ARN, see [My marketplace model packages](https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources).
   +  Example algorithm ARN: `arn:aws:sagemaker:{{<region>}}:{{<account-id>}}:algorithm/{{<algorithm-name>}}` 

     To find your algorithm resource ARN, see [My algorithms](https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources).

   When you leave the field, **Resource type** shows **Model package** or **Algorithm**. The resource must have the status `Completed` in SageMaker AI, and the identity that you signed in with must have permission to describe it. If the page shows an error, see [I get an error message when I enter the ARN of my model package or algorithm](ml-troubleshooting.md#troubleshooting_pc_add_version_messages).

1. For **IAM access role ARN**, enter the ARN of the role that gives AWS Marketplace access to your resource, for example `arn:aws:iam::{{<account-id>}}:role/{{<role-name>}}`. For more information, see [Required permissions](ml-publishing-prereq.md#ml-permissions-required).

1. (Optional) Expand **Tags**, and add tags to the request.

1. Choose **Next**.

   If AWS Partner Central is still reading your resource, the wizard moves to the next page when the read succeeds.

**To provide version details for the initial version**

1. On the **Provide version details** page, enter the following, and then choose **Next**:
   + Under **Version information**, a **Version name** and **Release notes**. Buyers see the version name on the product detail page, so make it unique.
   + Under **Usage instructions**, clear instructions for using your model effectively, such as best practices, how to handle common edge cases, or performance optimization suggestions.

1. On the **Define input and output parameters** page, enter the following, and then choose **Next**:
   + Under **Model input details**, a **Model input summary** and, optionally, **Input limitations**. For **Real-time input data sample** and **Batch job input data sample**, choose a **Data sample format** of **URL** or **Text**, and then enter the URL or the sample text.
   + (Optional) Under **Input parameters**, choose **Add input parameter** for each input parameter that your product supports. Enter a **Parameter name** and an **Input parameter description**. Optionally, enter **Input parameter constraints**. Select **This parameter is required** if buyers must provide the parameter.
   + (Optional) Under **Custom attributes (invocation parameters)**, choose **Add custom attribute** for each custom invocation parameter that your product supports. Enter an **Attribute name** and an **Attribute description**. Select **This attribute is required** if buyers must provide the attribute.
   + Under **Model output details**, a **Model output summary**. For **Real-time output data sample** and **Batch job output data sample**, choose a **Data sample format**, and then enter the URL or the sample text.
   + (Optional) Under **Output parameters**, choose **Add output parameter** for each output parameter that your product returns. Enter an **Output parameter name** and a **Description of output parameter**. Select **This parameter is required** if your product always returns the parameter.

   Each of the three lists holds up to 24 entries. For what to include, see [Requirements for inputs and outputs](ml-listing-requirements-and-best-practices.md#ml-requirements-for-inputs-and-outputs).

1. On the **Configure instances and resources** page, do the following, and then choose **Next**:
   + Under **Recommended instance types**, choose a **Recommended instance type for real-time inference** and a **Recommended instance type for batch transform**. For an algorithm, also choose a **Recommended instance type for training**. Each list contains only the instance types that your SageMaker AI resource supports for that workload. If the resource supports no instance type for a workload, leave that choice empty.

     Buyers see these instance types marked as **Recommended** in the pricing table on the product detail page. You can change them after you publish the version. For more information, see [Changing the recommended instance types](ml-manage-product-version.md#ml-recommended-instance-types).
   + Under **Git repository and notebook links**, a **Sample notebook URL** and a **Git repository URL**. Sample notebooks should include how to invoke your model. Your Git repository should include notebooks, data files, and other developer tools.

1. On the **Review and submit** page, choose **Add version**.

   To change a page before you submit, choose **Edit** in its section.

Your change request appears on the product's **Change history** tab as **Add version** followed by your version name. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Edit** and **Add version** on the **Delivery** tab are unavailable.

The wizard shows a **Set prices** page before **Review and submit** only when your product already has a public offer with paid usage pricing. For a new product, you set pricing later, in **Step 3: Procurement configuration**. For more information about the **Set prices** page, see [Adding new versions](ml-manage-product-version.md#ml-adding-new-versions).

After the version is added and Step 2 is complete, choose **Advance to procurement configuration**, and then choose **Confirm and continue** in the **Transition to Limited** dialog box. This moves your product to **Limited** visibility, and you can continue with **Step 3: Procurement configuration**.

To leave the wizard without submitting, choose **Cancel**, and then choose **Cancel request** in the **Cancel new request** dialog box. AWS Partner Central doesn't save your entries. To stay in the wizard, choose **Back to request**.


**Field limits**  

| Field | Limit | 
| --- | --- | 
| Version name | Required. Up to 64 characters. Can't start with a space. | 
| Release notes | Required. Up to 30,000 characters. Can't start with a space. | 
| Usage instructions, Model input summary, Model output summary | Required. Up to 10,000 characters each. | 
| Real-time and batch data samples, for input and output | Required. A URL or text of up to 10,000 characters. A URL must start with https://. | 
| Input limitations | Optional. Up to 1,000 characters. | 
| Parameter and attribute names | Required for each entry. Up to 100 characters. Printable ASCII characters only. | 
| Parameter and attribute descriptions | Required for each entry. Up to 1,000 characters. | 
| Input parameter constraints | Optional. Up to 1,500 characters. | 
| Input parameters, Custom attributes (invocation parameters), Output parameters | Up to 24 entries in each list. | 
| Sample notebook URL, Git repository URL | Required. Up to 2,000 characters. Must start with https://. | 

AWS Partner Central shows a character count for each field that has a limit. The same limits apply when you update a version.