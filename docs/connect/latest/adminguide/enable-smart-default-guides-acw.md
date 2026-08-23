# Enable smart default guides for after contact work

Connect Customer provides a default Step-by-Step Guide for after contact work (ACW) that
automatically launches when an agent enters the ACW state. This guide standardizes
post-contact workflows by surfacing wrap-up tasks such as disposition codes, contact
summaries, and follow-up actions directly in the agent workspace, without requiring
manual configuration.

New Connect Customer instances created after this feature's launch date automatically include
the smart default Guide. For existing instances, you can enable this capability by
importing the default flow and configuring it to use the AWS managed view.

**To enable smart default guides on an existing
instance:**

1. Copy the flow schema (JSON) provided in the **Flow
   schema** section.
2. In the Connect Customer admin workspace, navigate to **Routing** >
   **Flows**.
3. Choose **Create flow**, then select **Import
   flow** and upload the copied JSON schema as a file.
4. Open the imported flow in the flow designer.
5. Locate the **Show View** block in the flow. Select it to
   open its configuration.
6. Under **View**, a view name might already be displayed, but
   you must select the AWS managed view titled **after contact
   work** from the dropdown.
7. Save and publish the flow.
8. Navigate to the inbound contact flow that handles the contacts you want to
   enable ACW guides for. Add or configure a **Set event
   flow** block and set it to reference the sample after contact
   work flow you imported in the previous steps. Save and publish the inbound
   contact flow.
   Once published, agents handling contacts through that inbound flow will
   automatically receive the guided ACW experience when they enter the after contact
   work state. The guide includes disposition code capture, contact summary review, and
   follow-up tracking. You can customize the flow or view content to match your
   organization's specific wrap-up requirements.

**Flow schema**

```

{
  "Version": "2019-10-30",
  "StartAction": "e4b91d3f-dda6-4ec8-b51a-57bc96e88c52",
  "Metadata": {
    "entryPointPosition": { "x": 40, "y": 40 },
    "ActionMetadata": {
      "e4b91d3f-dda6-4ec8-b51a-57bc96e88c52": {
        "position": { "x": 181.6, "y": 29.6 },
        "parameters": {
          "ViewResource": { "Id": { "displayName": "After Contact Work" } },
          "InvocationTimeLimitSeconds": { "unit": 1 }
        }
      },
      "Save collected data to the current contact": { "position": { "x": 492, "y": 72 }, "isFriendlyName": true, "dynamicParams": [] },
      "Save collected data to the related contact": { "position": { "x": 705.6, "y": 72 }, "isFriendlyName": true, "dynamicParams": [] },
      "06a44c9e-c7dd-4f05-8ac0-f2221bb155d5": { "position": { "x": 776.8, "y": 313.6 } },
      "6f30b2d7-0f15-44b5-8236-3012afa746b3": { "position": { "x": 473.6, "y": 384.8 } },
      "930a4e8d-8727-4783-b23a-4c896387a052": { "position": { "x": 1266.4, "y": 102.4 } }
    },
    "Annotations": [
      {
        "type": "default",
        "id": "835afeaa-9359-40f2-abdd-dfd4d7c89651",
        "content": "This block will render a view in the agent workspace for users to collect information during after contact work.",
        "actionId": "e4b91d3f-dda6-4ec8-b51a-57bc96e88c52",
        "isFolded": true,
        "position": { "x": 240.5, "y": 378 },
        "size": { "height": 295, "width": 300 }
      }
    ],
    "name": "Sample after contact work flow",
    "description": "Sample flow to show guides in after contact work.",
    "type": "contactFlow",
    "status": "PUBLISHED",
    "hash": {}
  },
  "Actions": [
    {
      "Parameters": {
        "ViewResource": { "Id": "arn:aws:connect:eu-central-1:aws:view/after-contact-work:1" },
        "InvocationTimeLimitSeconds": "480",
        "ViewData": {
          "CustomerName": "Jane Doe",
          "Example_Label": "example.com",
          "PhoneNumber": "(880) 953-0129",
          "AdditionalNotes_DefaultValue": "Additional contact details...",
          "AdditionalNotes_Header_Description": "Add any extra information that may be helpful for future reference.",
          "AdditionalNotes_Header_Title": "Additional Notes",
          "Category_DefaultValue": "Support",
          "ContactSummary_Header_Description": "Review and confirm the details of this contact.",
          "ContactSummary_Header_Title": "Contact Summary",
          "ContactSummary_DefaultValue": "During this contact, the customer...",
          "ContactWrapUp_Header_Description": "Complete your contact by selecting a disposition code, reviewing the contact summary, and adding any important notes.",
          "ContactWrapUp_Header_Title": "Contact Wrap-up",
          "Disposition_Header_Description": "Classify this customer interaction.",
          "Disposition_Header_Title": "Disposition codes",
          "Driver_DefaultValue": "Billing inquiries",
          "Example_Url": "https://example.com",
          "Satisfaction_DefaultValue": "Very Satisfied",
          "FollowUp_DefaultValue": "No",
          "Resolved_DefaultValue": "Yes"
        }
      },
      "Identifier": "e4b91d3f-dda6-4ec8-b51a-57bc96e88c52",
      "Type": "ShowView",
      "Transitions": { "NextAction": "6f30b2d7-0f15-44b5-8236-3012afa746b3", "Conditions": [ { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "Condition": { "Operator": "Equals", "Operands": ["Cancel"] } }, { "NextAction": "Save collected data to the current contact", "Condition": { "Operator": "Equals", "Operands": ["Submit"] } } ], "Errors": [ { "NextAction": "6f30b2d7-0f15-44b5-8236-3012afa746b3", "ErrorType": "NoMatchingCondition" }, { "NextAction": "6f30b2d7-0f15-44b5-8236-3012afa746b3", "ErrorType": "NoMatchingError" }, { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "ErrorType": "TimeLimitExceeded" } ] }
    },
    { "Parameters": { "Attributes": { "Category": "$.Views.ViewResultData.Category.0", "Driver": "$.Views.ViewResultData.Driver.0", "Satisfaction": "$.Views.ViewResultData.Satisfaction.0", "FollowUp": "$.Views.ViewResultData.FollowUp.0", "Resolved": "$.Views.ViewResultData.Resolved.0", "ModifiedSummary": "$.Views.ViewResultData.ModifiedSummary", "ContactNotes": "$.Views.ViewResultData.ContactNotes" }, "TargetContact": "Current" }, "Identifier": "Save collected data to the current contact", "Type": "UpdateContactAttributes", "Transitions": { "NextAction": "Save collected data to the related contact", "Errors": [ { "NextAction": "06a44c9e-c7dd-4f05-8ac0-f2221bb155d5", "ErrorType": "NoMatchingError" } ] } },
    { "Parameters": { "Attributes": { "Category": "$.Views.ViewResultData.Category.0", "Driver": "$.Views.ViewResultData.Driver.0", "Satisfaction": "$.Views.ViewResultData.Satisfaction.0", "FollowUp": "$.Views.ViewResultData.FollowUp.0", "Resolved": "$.Views.ViewResultData.Resolved.0", "ModifiedSummary": "$.Views.ViewResultData.ModifiedSummary", "ContactNotes": "$.Views.ViewResultData.ContactNotes" }, "TargetContact": "Related" }, "Identifier": "Save collected data to the related contact", "Type": "UpdateContactAttributes", "Transitions": { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "Errors": [ { "NextAction": "06a44c9e-c7dd-4f05-8ac0-f2221bb155d5", "ErrorType": "NoMatchingError" } ] } },
    { "Parameters": { "SkipWhenDTMFBufferEnabled": "false", "Text": "There was an error saving the data as contact attributes" }, "Identifier": "06a44c9e-c7dd-4f05-8ac0-f2221bb155d5", "Type": "MessageParticipant", "Transitions": { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "Errors": [ { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "ErrorType": "NoMatchingError" } ] } },
    { "Parameters": { "SkipWhenDTMFBufferEnabled": "false", "Text": "We're sorry, an error occurred with the ShowView block" }, "Identifier": "6f30b2d7-0f15-44b5-8236-3012afa746b3", "Type": "MessageParticipant", "Transitions": { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "Errors": [ { "NextAction": "930a4e8d-8727-4783-b23a-4c896387a052", "ErrorType": "NoMatchingError" } ] } },
    { "Parameters": {}, "Identifier": "930a4e8d-8727-4783-b23a-4c896387a052", "Type": "DisconnectParticipant", "Transitions": {} }
  ]
}

```
