# Create an EventBridge rule

for a CodeCommit source (console)

###### Important

If you use the console to create or edit your pipeline, your EventBridge rule is
created for you.

###### To create an EventBridge rule for use in CodePipeline operations

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**. Leave the
   default bus selected or choose an event bus. Choose **Create
   rule**.
3. In **Name**, enter a name for your rule.
4. Under **Rule type**, choose **Rule with an event
   pattern**. Choose **Next**.
5. Under **Event source**, choose **AWS events or
   EventBridge partner events**.
6. Under **Sample event type**, choose **AWS
   events**.
7. In **Sample events**, type CodeCommit as the keyword to filter
   on. Choose **CodeCommit Repository State Change**.
8. Under **Creation method**, choose **Customer
   pattern (JSON editor)**.

Paste the event pattern provided below. The following is a sample CodeCommit
event pattern in the **Event** window for a
`MyTestRepo` repository with a branch named
`main`:

```

{
  "source": [
    "aws.codecommit"
  ],
  "detail-type": [
    "CodeCommit Repository State Change"
  ],
  "resources": [
    "arn:aws:codecommit:us-west-2:80398EXAMPLE:MyTestRepo"
  ],
  "detail": {
    "referenceType": [
      "branch"
    ],
    "referenceName": [
      "main"
    ]
  }
}
```

9. In **Targets**, choose
   **CodePipeline**.
10. Enter the pipeline ARN for the pipeline to be started by this rule.

###### Note

You can find the pipeline ARN in the metadata output after you run the
**get-pipeline** command. The pipeline ARN is
constructed in this format:

arn:aws:codepipeline:`region`:`account`:`pipeline-name`

Sample pipeline ARN:

`arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline` 11. To create or specify an IAM service role that grants EventBridge permissions to
invoke the target associated with your EventBridge rule (in this case, the target
is CodePipeline):

    * Choose **Create a new role for this specific
     resource** to create a service role that gives EventBridge
     permissions to your start your pipeline executions.
    * Choose **Use existing role** to enter a service
     role that gives EventBridge permissions to your start your pipeline
     executions.

12. (Optional) To specify source overrides with a specific image ID, use the
    input transformer to pass the data as a JSON parameters. You can also use
    the input transformer to pass pipeline variables.
    - Expand **Additional settings**.

    Under **Configure target input**, choose
    **Configure input transformer**.

    In the dialog window, choose **Enter my own**. In
    the **Input path** box, type the following
    key-value pairs.

    ```
    {"revisionValue": "$.detail.image-digest"}
    ```

    - In the **Template** box, type the following
      key-value pairs.

    ```
    {
        "sourceRevisions": [
            {
                "actionName": "`Source`",
                "revisionType": "`COMMIT_ID`",
                "revisionValue": "<`revisionValue`>"
            }
        ],
        "variables": [
            {
                "name": "`Branch_Name`",
                "value": "`value`"
            }
        ]
    }

    ```

    - Choose **Confirm**.

13. Choose **Next**.
14. On the **Tags** page, choose
    **Next**.
15. On the **Review and create** page, review the rule
    configuration. If you're satisfied with the rule, choose **Create
    rule**.
