

# Creating a rule-based matching workflow with the Advanced rule type
<a name="rule-based-mw-advanced"></a>

**Prerequisites**

Before you create a rule-based matching workflow, you must:

1. Create a schema mapping. For more information, see [Creating a schema mapping](create-schema-mapping.md).

1. If using Connect Customer Customer Profiles as your output destination, ensure you have the appropriate permissions configured.

The following procedure demonstrates how to create a rule-based matching workflow with the **Advanced** rule type using either the AWS Entity Resolution console or the `CreateMatchingWorkflow` API.

------
#### [ Console ]

**To create a rule-based matching workflow with the **Advanced** rule type using the console**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **Matching**.

1. On the **Matching workflows** page, in the upper right corner, choose **Create matching workflow**.

1. For **Step 1: Specify matching workflow details**, do the following: 

   1. Enter a **Matching workflow name** and an optional **Description**.

   1. For **Data input**, choose an **AWS Region**, **AWS Glue database**, the **AWS Glue table**, and then the corresponding **Schema mapping**.

      You can add up to 19 data inputs.
**Note**  
To use **Advanced** rules, your schema mappings must meet the following requirements:  
Each input field must be mapped to a unique match key, unless the fields are grouped together.
If input fields are grouped together, they can share the same match key.  
For example, the following schema mapping would be valid for **Advanced** rules:  
`firstName: { matchKey: 'name', groupName: 'name' }`  
`lastName: { matchKey: 'name', groupName: 'name' }`  
In this case, the `firstName` and `lastName` fields are grouped together and share the same name match key, which is allowed.  
Review your schema mappings and update them to follow this one-to-one matching rule, unless the fields are properly grouped, in order to use **Advanced** rules.
If your data table has a DELETE column, the schema mapping's type must be `String` and you can't have a `matchKey` and `groupName`. 

   1. The **Normalize data** option is selected by default, so that data inputs are normalized before matching. If you don't want to normalize data, deselect the **Normalize data** option.
**Note**  
Normalization is only supported for the following scenarios in **Create schema mapping**:   
If the following **Name** sub-types are grouped: **First name**, **Middle name**, **Last name**.
If the following **Address** sub-types are grouped: **Street address 1**, **Street address 2**, **Street address 3**, **City**, **State**, **Country**, **Postal code**.
If the following **Phone** sub-types are grouped: **Phone number**, **Phone country code**.

   1. To specify the **Service access** permissions, choose an option and take the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/rule-based-mw-advanced.html)

   1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Choose matching technique**:

   1. For **Matching method**, choose **Rule-based matching**.

   1. For **Rule type**, choose **Advanced**.  
![Choose matching technique screen with the Advanced rule-based matching option selected.](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/choose-matching-method-rule-based-advanced.PNG)

   1. For **Processing cadence**, select one of the following options.
      + Choose **Manual** to run a workflow on demand for a bulk update 
      + Choose **Automatic** to run a workflow as soon as new data is in your S3 bucket 
**Note**  
If you choose **Automatic**, ensure that you have Amazon EventBridge notifications turned on for your S3 bucket. For instructions on enabling Amazon EventBridge using the S3 console, see [Enabling Amazon EventBridge](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications-eventbridge.html) in the *Amazon S3 User Guide*.

   1. For **Matching rules**, enter a **Rule name** and then build the **Rule condition** by choosing the appropriate matching functions and operators from the dropdown list based on your goal.

      You can create up to 25 rules.
**Note**  
AWS Entity Resolution also supports [transitive matching](transitive-matching.md), which processes records across all rule levels to connect match groups transitively. Transitive matching is available as an API-only feature. When transitive matching is enabled, the **EmptyValues=Ignore** modifier is not supported. For more information, see [Using transitive matching](transitive-matching.md).

      You must combine a fuzzy matching function (**Cosine**, **Levenshtein**, or **Soundex**) with an exact matching function (**Exact**, **ExactManyToMany**) using the **AND** operator.

      You can use the following table to help decide what type of function or operator you want to use, depending on your goal.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/rule-based-mw-advanced.html)  
**Example Rule condition that matches on phone numbers and email**  

      The following is an example of a rule condition that matches records on phone numbers (**Phone** match key) and email addresses (**Email address** match key):

      `Exact(Phone,EmptyValues=Process) AND Levenshtein("Email address",2)`  
![Example of a rule condition that matches records on phone numbers and email addresses.](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/matching-rule-condition-example.png)

      The **Phone** match key uses the **Exact** matching function to match identical strings. The **Phone** match key processes empty values in matching using the **EmptyValues=Process** modifier.

      The **Email address** match key uses the **Levenshtein** matching function to match data with misspellings using the default Levenshtein Distance algorithm threshold of 2. The **Email** match key doesn't use any optional modifiers.

      The **AND** operator combines the **Exact** matching function and the **Levenshtein** matching function.  
**Example Rule condition that uses ExactManyToMany to perform matchkey matching**  

      The following is an example of a rule condition that matches records on three address fields (**HomeAddress** match key, **BillingAddress** match key, and **ShippingAddress** match key to find potential matches by checking if any if any of them have identical values. 

      The `ExactManyToMany` operator evaluates all possible combinations of the specified address fields to identify exact matches between any two or more addresses. For example, it would detect if the `HomeAddress` matches either the `BillingAddress` or `ShippingAddress`, or if all three addresses match exactly.

      ```
      ExactManyToMany(HomeAddress, BillingAddress, ShippingAddress)
      ```  
**Example Rule condition that uses clustering**  

      In Advanced Rule Based Matching with fuzzy conditions, the system first groups records into clusters based on exact matches. Once these initial clusters are formed, the system applies fuzzy matching filters to identify additional matches within each cluster. For optimal performance, you should select exact match conditions based on your data patterns to create well-defined initial clusters. 

      The following is an example of a rule condition that combines multiple exact matches with a fuzzy match requirement. It uses `AND` operators to check that three fields — `FullName`, Date of Birth (`DOB`), and `Address` — match exactly between records. It also allows for minor variations in the `InternalID` field using a Levenshtein distance of `1`. The Levenshtein distance measures the minimum number of single-character edits required to change one string into another. A distance of 1 means it will match `InternalIDs` that differ by only one character (like a single typo, deletion, or insertion). This combination of conditions helps identify records that are very likely to represent the same entity, even if there are small discrepancies in the identifier.

      ```
      Exact(FullName) AND Exact(DOB) AND Exact(Address) and Levenshtein(InternalID, 1)
      ```

   1. Choose **Next**.

1. For **Step 3: Specify data output and format**:

   1. For **Data output destination and format**, choose the **Amazon S3 location** for the data output and whether the **Data format** will be **Normalized data** or **Original data**.

   1. For **Encryption**, if you choose to **Customize encryption settings**, enter the **AWS KMS key** ARN.

   1. View the **System generated output**.

   1. For **Data output**, decide which fields you want to include, hide, or mask, and then take the recommended actions based on your goals.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/rule-based-mw-advanced.html)

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

1. After the matching workflow job completes (**Status** is **Completed**), you can go to the **Data output** tab and then select your **Amazon S3 location** to view the results.

1. (**Manual** processing type only) If you have created a **Rule-based matching** workflow with the **Manual** processing type, you can run the matching workflow anytime by choosing **Run workﬂow** on the matching workflow details page.

1. (**Automatic** processing type only) If your data table has a DELETE column, then: 
   + Records set to {{true}} in the DELETE column are deleted.
   + Records set to {{false}} in the DELETE column are ingested into S3.

   For more information, see [Step 1: Prepare first-party data tables](prepare-input-data.md#prepare-first-party-tables).

------
#### [ API ]

**To create a rule-based matching workflow with the **Advanced** rule type using the API**
**Note**  
By default, the workflow uses standard (batch) processing. To use incremental (automatic processing, you must explicitly configure it.

1. Open a terminal or command prompt to make the API request.

1. Create a POST request to the following endpoint: 

   ```
   /matchingworkflows
   ```

1. In the request header, set the Content-type to application/json. 
**Note**  
For a complete list of supported programming languages, see the *[AWS Entity Resolution API Reference](https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html)*. 

1. For the request body, provide the following required JSON parameters: 

   ```
   {
      "description": "{{string}}",
      "incrementalRunConfig": { 
         "incrementalRunType": "{{string}}"
      },
      "inputSourceConfig": [ 
         { 
            "applyNormalization": {{boolean}},
            "inputSourceARN": "{{string}}",
            "schemaName": "{{string}}"
         }
      ],
      "outputSourceConfig": [ 
         { 
            "applyNormalization": {{boolean}},
            "KMSArn": "{{string}}",
            "output": [ 
               { 
                  "hashed": boolean,
                  "name": "{{string}}"
               }
            ],
            "outputS3Path": "{{string}}"
         }
      ],
      "resolutionTechniques": { 
         "providerProperties": { 
            "intermediateSourceConfiguration": { 
               "intermediateS3Path": "{{string}}"
            },
            "providerConfiguration": {{JSON value}},
            "providerServiceArn": "{{string}}"
         },
         "resolutionType": "RULE_MATCHING",
         "ruleBasedProperties": { 
            "attributeMatchingModel": "{{string}}",
            "matchPurpose": "{{string}}",
            "rules": [ 
               { 
                  "matchingKeys": [ "{{string}}" ],
                  "ruleName": "{{string}}"
               }
            ]
         },
         "ruleConditionProperties": { 
            "rules": [ 
               { 
                  "condition": "{{string}}",
                  "ruleName": "{{string}}"
               }
            ]
         }
      },
      "roleArn": "{{string}}",
      "tags": { 
         "string" : "{{string}}" 
      },
      "workflowName": "{{{{string}}}}"
   }
   ```

   Where:
   + `workflowName` (required) – Must be unique and between 1–255 characters matching pattern [a-zA-Z\_0-9-]\*
   + `inputSourceConfig` (required) – List of 1–20 input source configurations
   + `outputSourceConfig` (required) – Exactly one output source configuration
   + `resolutionTechniques` (required) – Set to "RULE\_MATCHING" as the resolutionType for rule-based matching
   + `roleArn` (required) – IAM role ARN for workflow execution
   + `ruleConditionProperties` (required) – List of rule conditions and the name of the matching rule.

   Optional parameters include:
   + `description` – Up to 255 characters
   + `incrementalRunConfig` – Incremental run type configuration
   + `tags` – Up to 200 key-value pairs

1. (Optional) To use incremental processing instead of the default standard (batch) processing, add the following parameter to the request body: 

   ```
   "incrementalRunConfig": {
      "incrementalRunType": "AUTOMATIC"
   }
   ```

1. Send the request.

1. If successful, you'll receive a response with status code 200 and a JSON body containing: 

   ```
   {
      "workflowArn": "string",
      "workflowName": "string",
      // Plus all configured workflow details
   }
   ```

1. If the call is unsuccessful, you might receive one of these errors:
   + 400 – ConflictException if the workflow name already exists
   + 400 – ValidationException if the input fails validation
   + 402 – ExceedsLimitException if account limits are exceeded
   + 403 – AccessDeniedException if you don't have sufficient access
   + 429 – ThrottlingException if the request was throttled
   + 500 – InternalServerException if there's an internal service failure

------