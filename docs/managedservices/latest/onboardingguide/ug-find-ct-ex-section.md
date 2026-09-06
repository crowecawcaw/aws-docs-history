

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Finding a change type, using the query option
<a name="ug-find-ct-ex-section"></a>

This example demonstrates how to use the AMS Console to find the appropriate change type for the RFC that you want to submit.

You can use the console or the API/CLI to find a change type ID (CT) or version. There are two methods, either a search or choosing the classification. For both selection types, You can sort the search by choosing either **Most frequently used**, **Most recently used**, or **Alphabetical**.

**YouTube Video**: [ How do I create an RFC using the AWS Managed Services CLI and where can I find the CT Schema?](https://www.youtube.com/watch?v=IluDFwnJJFU&list=PLhr1KZpdzukc_VXASRqOUSM5AJgtHat6-&index=3&t=150s) 

In the AMS console, on the **RFCs** -> **Create RFC** page:
+ With **Browse by change type** selected (the default), either:
  + Use the **Quick create** area to select from AMS's most popular CTs. Click on a label and the **Run RFC** page opens with the **Subject** option auto-filled for you. Complete the remaining options as needed and click **Run** to submit the RFC. 
  + Or, scroll down to the **All change types** area and start typing a CT name in the option box, you don't have to have the exact or full change type name. You can also search for a CT by change type ID, classification, or execution mode (automated or manual) by entering the relevant words.

    With the default **Cards** view selected, matching CT cards appear as you type, select a card and click **Create RFC**. With the **Table** view selected, choose the relevant CT and click **Create RFC**. Both methods open the **Run RFC** page.
+ Alternatively, and to explore change type choices, click **Choose by category** at the top of the page to open a series of drop-down option boxes.
+ Choose **Category**, a **Subcategory**, an **Item**, and an **Operation**. The information box for that change type appears a panel appears at the bottom of the page.
+ When you're ready, press **Enter**, and a list of matching change types appears.
+ Choose a change type from the list. The information box for that change type appears at the bottom of the page.
+ After you have the correct change type, choose **Create RFC**.
**Note**  
The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources** page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for authentication; for example, `aws amsskms {{ams-cli-command}} --profile SAML`. You may also need to add the `--region` option as all AMS commands run out of us-east-1; for example `aws amscm {{ams-cli-command}} --region=us-east-1`.
**Note**  
The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1` when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

To search for a change type using the AMS CM API (see [ListChangeTypeClassificationSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeClassificationSummaries.html)) or CLI:

You can use a filter or query to search. The ListChangeTypeClassificationSummaries operation has [Filters](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeClassificationSummaries.html#amscm-ListChangeTypeClassificationSummaries-request-Filters) options for `Category`, `Subcategory`, `Item`, and `Operation`, but the values must match the existing values exactly. For more flexible results when using the CLI, you can use the `--query` option. 


**Change type filtering with the AMS CM API/CLI**  
<a name="ct-filtering-table"></a>
<table>
<thead>
  <tr><th>Attribute</th><th>Valid values</th><th>Valid/Default condition</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td>ChangeTypeId</td><td>Any string representing a ChangeTypeId (For ex: ct-abc123xyz7890)</td><td>Equals</td><td>For change type IDs, see the <a href="https://docs.aws.amazon.com/managedservices/latest/ctref/index.html">Change Type Reference</a>.<br />For change type IDs, see Finding a Change Type or CSIO.</td></tr>
  <tr><td>Category</td><td rowspan="4">Any free-form text</td><td rowspan="4">Contains</td><td rowspan="4">Regular expressions in each individual field are not supported. Case insensitive search</td></tr>
  <tr><td>Subcategory</td></tr>
  <tr><td>Item</td></tr>
  <tr><td>Operation</td></tr>
</tbody>
</table>


1. Here are some examples of listing change type classifications:

   The following command lists all change type categories.

   ```
   aws amscm list-change-type-categories
   ```

   The following command lists the subcategories belonging to a specified category.

   ```
   aws amscm list-change-type-subcategories --category {{CATEGORY}}
   ```

   The following command lists the items belonging to a specified category and subcategory.

   ```
   aws amscm list-change-type-items --category {{CATEGORY}} --subcategory {{SUBCATEGORY}}
   ```

1. Here are some examples of searching for change types with CLI queries:

   The following command searches CT classification summaries for those that contain "S3" in the Item name and creates output of the category, subcategory, item, operation, and change type ID in table form. 

   ```
   aws amscm list-change-type-classification-summaries --query "ChangeTypeClassificationSummaries [?contains(Item, 'S3')].[Category,Subcategory,Item,Operation,ChangeTypeId]" --output table
   ```

   ```
   +---------------------------------------------------------------+
   |               ListChangeTypeClassificationSummaries           |
   +----------+-------------------------+--+------+----------------+
   |Deployment|Advanced Stack Components|S3|Create|ct-1a68ck03fn98r|
   +----------+-------------------------+--+------+----------------+
   ```

1. You can then use the change type ID to get the CT schema and examine the parameters. The following command outputs the schema to a JSON file named CreateS3Params.schema.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1a68ck03fn98r" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateS3Params.schema.json
   ```

   For information about using CLI queries, see [How to Filter the Output with the --query Option](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html#controlling-output-filter) and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html).

1. After you have the change type ID, we recommend verifying the version for the change type to make sure it's the latest version. Use this command to find the version for a specified change type:

   ```
   aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CHANGE_TYPE_ID}}
   ```

   To find the `AutomationStatus` for a specific change type, run this command:

   ```
   aws amscm --profile saml get-change-type-version --change-type-id {{CHANGE_TYPE_ID}} --query "ChangeTypeVersion.{AutomationStatus:AutomationStatus.Name}"
   ```

   To find the `ExpectedExecutionDurationInMinutes` for a specific change type, run this command:

   ```
   aws amscm --profile saml get-change-type-version --change-type-id ct-14027q0sjyt1h --query "ChangeTypeVersion.{ExpectedDuration:ExpectedExecutionDurationInMinutes}"
   ```