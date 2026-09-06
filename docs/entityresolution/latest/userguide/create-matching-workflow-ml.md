

# Creating a machine learning-based matching workflow
<a name="create-matching-workflow-ml"></a>

*[Machine learning-based matching](glossary.md#ml-matching-defn)* is a preset process that attempts to match records across all of the data that you input. The machine learning-based matching workflow enables you to compare cleartext data to find a broad range of matches using a machine learning model.

**Note**  
The machine learning model doesn't support the comparison of hashed data.

When AWS Entity Resolution processes your data, it assigns:
+ A [Match ID](glossary.md#match-id-defin) to every record.
+ If a record matches one or more other records in your data:
  + The matching-group-level [confidence level](glossary.md#confidence-level-defn) percentage.
  + The [record-level confidence level](glossary.md#record-confidence-level-defn) percentage (ML-based incremental matching only).

You can use the output of an ML-based matching workflow as an input for data service provider matching, or vice-versa to meet your specific goals. For example, you can run an ML-based matching to find matches across your data sources on your own records first. If a subset wasn't matched, you can then run [provider service- based matching](create-matching-workflow-provider.md) to find additional matches.

**Prerequisites**

Before you create an ML-based matching workflow, you must:

1. Create a schema mapping. For more information, see [Creating a schema mapping](create-schema-mapping.md).

1. If using Connect Customer Customer Profiles as your output destination, ensure you have the appropriate permissions configured.

**To create a ML-based matching workflow:**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **Matching**.

1. On the **Matching workflows** page, in the upper right corner, choose **Create matching workflow**.

1. For **Step 1: Specify matching workflow details**, do the following: 

   1. Enter a **Matching workflow name** and an optional **Description**.

   1. For **Data input**, choose an **AWS Region**, **AWS Glue database**, the **AWS Glue table**, and then the corresponding **Schema mapping**.

      You can add up to 20 data inputs.

   1. The **Normalize data** option is selected by default, so that data inputs are normalized before matching. If you don't want to normalize data, deselect the **Normalize data** option.

      Machine learning based-matching only normalizes [Name](glossary.md#normalization-ML-defn-name), [Phone](glossary.md#normalization-ML-defn-phone), and [Email](glossary.md#normalization-ML-defn-email).

   1. To specify the **Service access** permissions, choose an option and take the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow-ml.html)

   1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Choose matching technique**:

   1. For **Matching method**, choose **Machine learning-based matching**.  
![AWS Entity Resolution matching workflow creation interface with options for rule-based or machine learning matching.](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/choose-matching-method-machine-learning.PNG)

   1. For **Processing cadence**, select one of the following options.
      + Choose **Manual** to run a Batch matching workflow, which processes the entire data in your S3 bucket.
      + Choose **Automatic** to run an Incremental matching workflow, which processes only the incremental data in your S3 bucket.

   1. Choose **Next**.

1. For **Step 3: Specify data output and format**:

   1. For **Data output destination and format**, choose the **Amazon S3 location** for the data output and whether the **Data format** will be **Normalized data** or **Original data**.

   1. For **Encryption**, if you choose to **Customize encryption settings**, enter the **AWS KMS key** ARN.

   1. View the **System generated output**.

   1. For **Data output**, decide which fields you want to include, hide, or mask, and then take the recommended actions based on your goals.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow-ml.html)

   1. Choose **Next**.

1. For **Step 4: Review and create**:

   1. Review the selections that you made for the previous steps and edit if necessary.

   1. Choose **Create and run**.

      A message appears, indicating that the matching workflow has been created and that the job has started.

1. On the matching workflow details page, on the **Metrics** tab, view the following under **Last job metrics**:
   + The **Job ID**. 
   + The **Status** of the matching workflow job: **Queued**, **In progress**, **Completed**, **Failed** 
   + The **Time completed** for the workflow job.
   + The number of **Records processed**. 
   + The number of **Records not processed**. 
   + The **Unique match IDs generated**.
   + The number of **Input records**.

   You can also view the job metrics for matching workflow jobs that have been previously run under the **Job history**.

1. After the matching workflow job completes (**Status** is **Completed**), you can go to the **Data output** tab and then select your **Amazon S3 location** to view the results. This information is generated by the matching workflow job and included in the output.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow-ml.html)

1. (**Manual** processing type only) If you have created a **Machine learning-based matching** workflow with the **Manual** processing type, you can run the matching workflow anytime by choosing **Run workflow** on the matching workflow details page.