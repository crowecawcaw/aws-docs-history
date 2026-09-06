

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Find RFCs
<a name="ex-rfc-find-col"></a>

## Find a request for change (RFC) with the console
<a name="ex-rfc-find-con"></a>

To find an RFC by using the AMS console, follow these steps.
**Note**  
This procedure applies only to scheduled RFCs, that is, RFCs that did not use the **ASAP** option.

1. From the left navigation, click **RFCs**.

   The RFCs dashboard opens.

1. Scroll through the list or use the **Filter** option to refine the list.

   The RFC list changes per filter criteria.

1. Choose the Subject link for the RFC you want.

   The RFC details page opens for that RFC with information including RFC ID.

1.  If there are many RFCs in the dashboard, you can use the **Filter** option to search by RFC:
   + **Subject**: The subject line, or title (in the API/CLI) given to the RFC when it was created.
   + **RFC ID**: The identifier for the RFC.
   + **Activity state**: If you know the RFC state, you can choose between **AwsOperatorAssigned** meaning an operator is currently looking at the RFC, **AwsActionPending** meaning that an AMS operator must perform something before the RFC execution can proceed or **CustomerActionPending** meaning that you need to take some action before the RFC execution can proceed.
   + **Status**: If you know the RFC status, you can choose between:
     + **Scheduled**: RFCs that were scheduled.
     + **Canceled**: RFCs that were canceled.
     + **In progress**: RFCs in progress.
     + **Success**: RFCs that executed successfully.
     + **Rejected**: RFCs that were rejected.
     + **Editing**: RFCs that are being edited.
     + **Failure**: RFCs that failed.
     + **Pending approval**: RFCs that cannot proceed until either AMS or you approve. Typically, this indicates that you need to approve the RFC. You will have gotten a service notification of this in your Service Requests list.
   + **Change type**: Pick the **Category**, **Subcategory**, **Item**, and **Operation**, and the change type ID is retrieved for you.
   + **Requested start time** or **Requested end time**: This filter option lets you choose **Before** or **After**, and then enter a **Date** and, optionally, a **Time** (hh:mm and time zone). This filter operates successfully only on scheduled RFCs (not ASAP RFCs).
   + **Status**: Either **Scheduled**, **Canceled**, **In progress**, **Success**, **Rejected**, **Editing**, or **Failure**.
   + **Subject**: The subject (or title, if the RFC was created with the API/CLI) that you gave the RFC.
   + **Change type ID**: Use the identifier for the change type submitted with the RFC.

   The search allows you to add the filters, as shown in the following screenshot.  
![Filter menu showing options such as Subject, RFC ID, Activity state, and Creation time.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/filterRfcAllOptions3.png)

1. Click on the Subject link for the RFC you want.

   The RFC details page opens for that RFC with information including RFC ID.

## Finding a request for change (RFC) with the CLI
<a name="ex-rfc-find-cli"></a>

You can use multiple filters to find an RFC.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

If you don’t write down the RFC ID, and need to find it later, you can use the AMS change management (CM) system to search for it and narrow the results with a filter or query.

1. The CM API [ListRfcSummaries](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcSummaries.html) operation has filters. You can [Filter](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Filter.html) results based on an `Attribute` and `Value` combined in a logical AND operation, or based on an `Attribute`, a `Condition`, and `Values`.  
**RFC filtering**    
<a name="rfc-filtering-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-find-col.html)

   Examples:

   To find the IDs of all the RFCs related to SQS (where SQS is contained in the Item portion of the CT), you can use this command:

   ```
   list-rfc-summaries --query 'RfcSummaries[?contains(Item.Name,`SQS`)].[Category.Id,Subcategory.Id,Type.Id,Item.Id,RfcId]' --output table
   ```

   Which returns something like this:

   ```
   ----------------------------------------------------------------------------
   |                         ListRfcSummaries                                   |
   +----------+--------------------------------+-------+-------+----------------+
   |Deployment| Advanced Stack Components      |SQS    |Create |ct-123h45t6uz7jl|
   |Management| Monitoring & Notification  |SQS    |Update |ct-123h45t6uz7jl|
   +----------+--------------------------------+-------+-------+----------------+
   ```

   Another filter available for `list-rfc-summaries` is `AutomationStatusId`, to look for RFCs that are automated or manual:

   ```
   aws amscm list-rfc-summaries --filter Attribute=AutomationStatusId,Value=Automated
   ```

   Another filter available for `list-rfc-summaries` is `Title` (**Subject** in the console):

   ```
    Attribute=Title,Value={{RFC-TITLE}}
   ```

   Example of the new request structure in JSON that returns RFCs where:
   + (Title CONTAINS the phrase "Windows 2012" OR "Amazon Linux") AND
   + (RfcStatusId EQUALS "Success" OR "InProgress") AND
   + (20170101T000000Z <= RequestedStartTime <= 20170103T000000Z) AND (ActualEndTime <= 20170103T000000Z)

   ```
   {
     "Filters": [
       {
         "Attribute": "Title",
         "Values": ["Windows 2012", "Amazon Linux"],
         "Condition": "Contains"
       },
       {
         "Attribute": "RfcStatusId",
         "Values": ["Success", "InProgress"],
         "Condition": "Equals"
       },
       {
         "Attribute": "RequestedStartTime",
         "Values": ["20170101T000000Z", "20170103T000000Z"],
         "Condition": "Between"
       },
       {
         "Attribute": "ActualEndTime",
         "Values": ["20170103T000000Z"],
         "Condition": "Before"
       }
     ]
   }
   ```
**Note**  
With more advanced `Filters`, AMS intends to deprecate the following fields in an upcoming release:  
Value: The Value field is part of the Filters field. Use the Values field that supports more advanced functionality.
RequestedEndTimeRange: Use the RequestedEndTime inside the Filters field that supports more advanced functionality
RequestedStartTimeRange: Use the RequestedStartTime inside the Filters field that supports more advanced functionality.

   For information about using CLI queries, see [ How to Filter the Output with the --query Option](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html#controlling-output-filter) and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html).

1. If you're using the AMS console:

   Go to the **RFCs** list page. If needed, you can filter on the RFC **Subject**, which is what you entered as the RFC `Title` when you created it.

## Tips
<a name="ex-rfc-find-tip"></a>

**Note**  
This procedure applies only to scheduled RFCs, that is, RFCs that did not use the **ASAP** option.