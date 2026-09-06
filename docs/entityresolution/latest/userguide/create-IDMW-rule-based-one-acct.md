

# Creating an ID mapping workflow (rule-based)
<a name="create-IDMW-rule-based-one-acct"></a>

This topic describes the process of creating an ID mapping workflow for one AWS account that uses matching rules to translate first-party data from a source to a target.

**To create a rule-based ID mapping workflow for one AWS account**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **ID mapping**.

1. On the **ID mapping workflows** page, in the upper right corner, choose **Create ID mapping workflow**.

1. For **Step 1: Specify ID mapping workflow details**, do the following.

   1. Enter an **ID mapping workflow name** and an optional **Description**.

      ![The name and description fields on the Specify ID mapping workflow page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-ID-mapping-details-name.png)

   1. For the **ID mapping method**, choose **Rule-based**.

   1. (Optional) To process only new, updated, or deleted records in the workflow, select **Enable incremental processing**.

      ![The ID mapping section of the Specify ID mapping workflow page with the Enable incremental process checkbox selected.](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/id-mapping-method-enable-inc-proc.png)

      AWS Entity Resolution processes only new, updated, or deleted records in either the Source or Target ID namespace, rather than recreating the entire ID mapping table.

      When you choose incremental processing and your data table has a DELETE column, AWS Entity Resolution handles records differently based on the DELETE column value.
      + Records marked as `true` in the DELETE column are removed from the ID mapping table.
      + Records marked as `false` in the DELETE column are ingested into Amazon S3.

      If you leave this option unselected, AWS Entity Resolution runs the default batch processing ID mapping workflow on the ID mapping table. 

   1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Specify source and target**, do the following.

   1. For **Source**, choose the scenario that applies to you and then take the recommended action.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-rule-based-one-acct.html)

   1. For **Target**, select an existing **Matching workflow** from the dropdown list.

   1. For **Rule parameters**, do the following.

      1. Specify the **Rule controls** by choosing one of the following options based on your source type.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-rule-based-one-acct.html)

      1. For **Comparison and matching parameters**, the **Comparison type** is automatically set to **Multiple input fields**. 

         This is because both participants had selected this option previously. 

   1. Specify the **Record matching type** by choosing one of the following options based on your goal.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-rule-based-one-acct.html)
**Note**  
You must specify compatible limitations for the source and target ID namespaces.

   1. To specify the **Service access** permissions, choose an option and take the recommended action.

      ![The Service access options on the Specify source and target page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-source-target-service-access.PNG)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-IDMW-rule-based-one-acct.html)

1. Choose **Next**.

1. For **Step 3: Specify data output location – *optional***, do the following.

   1. For **Data output destination**, do the following:

      1. Choose the **Amazon S3 location** for the data output.

      1. For **Encryption**, if you choose to **Customize encryption settings**, then enter the **AWS KMS key** ARN or choose **Create an AWS KMS key**.

   1. Choose **Next**.

1. For **Step 4: Review and create**, do the following.

   1. Review the selections that you made for the previous steps and edit them if necessary.

   1. Choose **Create**.

      A message appears, indicating that the ID mapping workflow has been created.

After you create the ID mapping workflow, you're ready to [run an ID mapping workflow](run-id-mapping-workflow.md).