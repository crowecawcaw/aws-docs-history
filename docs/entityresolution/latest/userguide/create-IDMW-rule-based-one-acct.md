

# Creating an ID mapping workflow (rule-based)
<a name="create-IDMW-rule-based-one-acct"></a>

This topic describes the process of creating an ID mapping workflow for one AWS account that uses matching rules to translate first-party data from a source to a target.

**To create a rule-based ID mapping workflow for one AWS account**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **ID mapping**.

1. On the **ID mapping workflows** page, in the upper right corner, choose **Create ID mapping workflow**.

1. For **Step 1: Specify ID mapping workflow details**, do the following.

   1. Enter an **ID mapping workflow name** and an optional **Description**.

      ![The name and description fields on the Specify ID mapping workflow page](https://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-ID-mapping-details-name.png)

   1. For the **ID mapping method**, choose **Rule-based**.

   1. (Optional) To process only new, updated, or deleted records in the workflow, select **Enable incremental processing**.

      ![The ID mapping section of the Specify ID mapping workflow page with the Enable incremental process checkbox selected.](https://docs.aws.amazon.com/entityresolution/latest/userguide/images/id-mapping-method-enable-inc-proc.png)

      AWS Entity Resolution processes only new, updated, or deleted records in either the Source or Target ID namespace, rather than recreating the entire ID mapping table.

      When you choose incremental processing and your data table has a DELETE column, AWS Entity Resolution handles records differently based on the DELETE column value.
      + Records marked as `true` in the DELETE column are removed from the ID mapping table.
      + Records marked as `false` in the DELETE column are ingested into Amazon S3.

      If you leave this option unselected, AWS Entity Resolution runs the default batch processing ID mapping workflow on the ID mapping table. 

   1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Specify source and target**, do the following.

   1. For **Source**, choose the scenario that applies to you and then take the recommended action. 


<table>
<thead>
  <tr><th>Scenario</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td>Use your own AWS Glue database, AWS Glue table, and schema mapping in the ID mapping workflow.</td><td><ol><li>  Choose <b>Schema mapping</b>. </li><li> Select an <b>AWS Region</b>, <b>AWS Glue database</b>, the <b>AWS Glue table</b>, and then the corresponding <b>Schema mapping</b>. </li></ol>You can add up to 19 data inputs.</td></tr>
  <tr><td>Use an existing matching workflow that points to the record data you want to use in the ID mapping workflow.</td><td> <ol><li>  Choose <b>Matching workflow</b>. </li><li> Select an existing <b>Matching workflow</b> from the dropdown list. </li></ol> </td></tr>
</tbody>
</table>


   1. For **Target**, select an existing **Matching workflow** from the dropdown list.

   1. For **Rule parameters**, do the following.

      1. Specify the **Rule controls** by choosing one of the following options based on your source type.


<table>
<thead>
  <tr><th>Source type</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td><b>Matching workflow</b></td><td>Specify the <b>Rule controls</b> by choosing whether a <b>Source</b>, <b>Target</b>, or both can provide rules in an ID mapping workflow.<br /><b>Rule controls</b> must be compatible between the source and the target to be used in an ID mapping workflow. <br />For example, if a source ID namespace limits rules to the target but the target ID namespace limits rules to the source, this results in an error.</td></tr>
  <tr><td><b>Schema mapping</b> </td><td>Skip this step.</td></tr>
</tbody>
</table>


      1. For **Comparison and matching parameters**, the **Comparison type** is automatically set to **Multiple input fields**. 

         This is because both participants had selected this option previously. 

   1. Specify the **Record matching type** by choosing one of the following options based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Limit the record matching type to store only one matching record in the source for each matched record in the target when you create the ID mapping workflow. </td><td><b>One source to one target</b></td></tr>
  <tr><td>Limit the record matching type to store all matching records in the source for each matched record in the target when you create the ID mapping workflow. </td><td><b>Many sources to one target</b></td></tr>
</tbody>
</table>

**Note**  
You must specify compatible limitations for the source and target ID namespaces.

   1. To specify the **Service access** permissions, choose an option and take the recommended action.

      ![The Service access options on the Specify source and target page](https://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-source-target-service-access.PNG)


<table>
<thead>
  <tr><th>Option</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td><b>Create and use a new service role</b></td><td> <ul><li> AWS Entity Resolution creates a service role with the required policy for this table. </li><li> The default <b>Service role name</b> is <code>entityresolution-id-mapping-workflow-&lt;timestamp&gt;</code>. </li><li> You must have permissions to create roles and attach policies. </li><li> If your input data is encrypted, choose the <b>This data is encrypted by a KMS key</b> option. Then, enter an <b>AWS KMS key</b> that is used to decrypt your data input. </li></ul> </td></tr>
  <tr><td><b>Use an existing service role</b></td><td> <ol><li> Choose an <b>Existing service role name</b> from the dropdown list. <br />The list of roles are displayed if you have permissions to list roles. <br />If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use. <br />If there are no existing service roles, the option to <b>Use an existing service role</b> is unavailable. </li><li> View the service role by choosing the <b>View in IAM</b> external link. <br />By default, AWS Entity Resolution doesn't attempt to update the existing role policy to add necessary permissions. </li></ol> </td></tr>
</tbody>
</table>


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