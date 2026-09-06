

# Looking up a Match ID for a rule-based matching workflow
<a name="find-match-id"></a>

After completing a rule-based matching workflow, you can retrieve the Match ID and associated rule for each processed record. This information helps you understand how records were matched and which rules were applied. The following procedure demonstrates how to access this data using either the AWS Entity Resolution console or the `GetMatchID` API.

------
#### [ Console ]

**To look up a Match ID using the console**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **Matching**.

1. Choose the rule-based matching workflow that has been processed (**Job status** is **Completed**).

1. On the matching workflow details page, choose the **Match IDs** tab.

1. Choose **Look up match ID**.
**Note**  
The **Look up match ID** option is only available for matching workflows that use the **Automatic** processing cadence. If you have selected the **Manual** processing cadence, this option will appear inactive. To use this option, edit your workflow to use the **Automatic** processing cadence. For more information about editing workflows, see [Editing a matching workflow](edit-matching-workflow.md).

1. Do one of the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/find-match-id.html)

1. For **Record attributes**, enter the **Value** for an existing **Match key** to look up for each existing record.
**Tip**  
Enter as many values as you can to help find the Match ID. 

1. The **Normalize data** option is selected by default, so that data inputs are normalized before matching. If you don't want to normalize data, deselect the **Normalize data** option.

1. If you want to view the matching rules expand the **View matching rules**.

1. Choose **Look up**.

   A success message appears, stating that the Match ID was found. 

1. View the corresponding Match ID and the associated rule that was found. 

------
#### [ API ]

**To look up a Match ID using the API**
**Note**  
To call this API successfully, you must have first successfully run a rule-based matching workflow using the [StartMatchingJob API](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartMatchingJob.html).   
For a complete list of supported programming languages, see the [See Also](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchId.html#API_GetMatchId_SeeAlso) section of the [GetMatchID API](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchId.html).

1. Open a terminal or command prompt to make the API request.

1. Create a POST request to the following endpoint: 

   ```
   /matchingworkflows/workflowName/matches
   ```

1. In the request header, set the Content-type to application/json. 

1. In the request URI, specify your `workflowName`. 

   The `workflowName` must: 
   + Be between 1 and 255 characters long 
   + Match the pattern [a-zA-Z\_0-9-]\*

1. For the request body, provide the following JSON: 

   ```
   {
      "applyNormalization": boolean,
      "record": { 
         "string" : "string" 
      }
   }
   ```

   Where: 

   `applyNormalization` (optional) - Set to `true` to normalize attributes defined in the schema 

   `record` (required) - The record to fetch the Match ID for

1. Send the request. 

   If successful, you'll receive a response with status code 200 and a JSON body containing: 

   ```
   {
      "matchId": "string",
      "matchRule": "string"
   }
   ```

   The `matchId` is the unique identifier for this group of matched records, and `matchRule` indicates which rule the record matched on. 

   If the call is unsuccessful, you might receive one of these errors:
   + 403 - AccessDeniedException if you don't have sufficient access
   + 404 - ResourceNotFoundException if the resource can't be found
   + 429 - ThrottlingException if the request was throttled
   + 400 - ValidationException if the input fails validation
   + 500 - InternalServerException if there's an internal service failure

------