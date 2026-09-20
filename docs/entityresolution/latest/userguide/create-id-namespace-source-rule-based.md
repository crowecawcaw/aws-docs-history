

# Creating an ID namespace source (rule-based)
<a name="create-id-namespace-source-rule-based"></a>

This topic describes the process of creating an ID namespace source using the **rule-based** method. This method uses matching rules to translate first-party data from a source to a target in an ID mapping workflow.

**Note**  
If the input data is the source, then it must have a schema mapping and an associated AWS Glue database.

**To create an ID namespace source (rule-based)**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Data preparation**, choose **ID namespaces**.

1. On the **ID namespaces** page, in the upper right corner, choose **Create ID namespace**.

1. For **Details**, do the following:

   1. For **ID namespace name**, enter a unique name.

   1. (Optional) For **Description**, enter an optional description.

   1. For **ID namespace type**, choose **Source**.

1. For the **ID namespace method**, choose **Rule-based**.

1. For **Data input**, choose the **Input type** that you want to use and then take the recommended actions.


<table>
<thead>
  <tr><th>Input type</th><th>Recommended actions</th></tr>
</thead>
<tbody>
  <tr><td>An existing schema mapping </td><td> <ol><li> Choose <b>Schema mapping</b>. </li><li> Choose the <b>AWS Region</b>, <b>AWS Glue database</b>, the <b>AWS Glue table</b>, and the <b>Schema mapping</b> from the dropdown list. <br />You can add up to 19 data inputs. </li></ol>  If your data table has a DELETE column, the schema mapping's type must be <code>String</code> and you can't have a <code>matchKey</code> and <code>groupName</code>.  </td></tr>
  <tr><td>An existing matching workflow </td><td> <ol><li> Choose the <b>Matching workflow</b>. </li><li>  Choose the account that’s associated with the ID namespace: either <b>Your AWS account</b> or <b>Another AWS account</b>. </li><li> Depending on the type of account, select the <b>Matching workflow name</b> or enter the<b> Matching workflow ARN</b>. </li></ol> </td></tr>
</tbody>
</table>


1. For **Rule parameters**, do the following.

   1. Specify the **Rule controls** by choosing one of the following options based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow rules from both the source and the target</td><td><b>No preference</b></td></tr>
  <tr><td>Choose whether a source, target, or both can provide rules in an ID mapping workflow</td><td><b>Limited rules</b></td></tr>
</tbody>
</table>


      **Rule controls** must be compatible between the source and the target to be used in an ID mapping workflow. For example, if a source ID namespace limits rules to the target but the target ID namespace limits rules to the source, this results in an error.

   1. Specify the **Matching rules** by choosing one of the following options based on your data input type.


<table>
<thead>
  <tr><th>Data input type</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td><b>Schema mapping</b></td><td>Choose <b>Add another rule</b> to add a matching rule. You can apply up to 25 <b>Matching rules</b> to define your match criteria. </td></tr>
  <tr><td><b>Matching workflow</b></td><td>Choose either <b>Use rules from matching workflow</b> or <b>Provide new rules</b> to define your <b>Matching rules</b>.</td></tr>
</tbody>
</table>


1. For **Comparison and matching parameters**, do the following.

   1. Specify the **Comparison type** by choosing one of the following options based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow any comparison type to be used when you create the ID mapping workflow.</td><td><b>No preference</b></td></tr>
  <tr><td>Find any combination of matches across data stored in multiple input fields, regardless of whether the data is in the same or different input field.</td><td><b>Multiple input fields</b></td></tr>
  <tr><td>Limit comparison within a single input field, when similar data stored across multiple input fields shouldn't be matched.</td><td><b>Single input field</b></td></tr>
</tbody>
</table>


   1. Specify the **Record matching type** by choosing one of the following options based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow any comparison type to be used when you create the ID mapping workflow.</td><td><b>No preference</b></td></tr>
  <tr><td>Limit the record matching type to store only one matching record in the source for each matched record in the target when you create the ID mapping workflow. </td><td><b>Limited record matching </b><br />and<br /><b>One source to one target</b></td></tr>
  <tr><td>Limit the record matching type to store all matching records in the source for each matched record in the target when you create the ID mapping workflow. </td><td><b>Limited record matching </b><br />and<br /><b>Many sources to one target</b></td></tr>
</tbody>
</table>

**Note**  
You must specify compatible limitations for the source and target ID namespaces. For example, if a source ID namespace limits rules to the target but the target ID namespace limits rules to the source, this results in an error.

1. Specify the **Service access permissions** by choosing an **Existing service role name** from the dropdown list.

1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

1. Choose **Create ID namespace**.

 The ID namespace source is created. You are now ready to [create an ID namespace target](create-id-namespace-target.md).