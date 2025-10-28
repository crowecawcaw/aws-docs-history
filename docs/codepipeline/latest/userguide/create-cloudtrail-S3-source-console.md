# Create an EventBridge rule for an

Amazon S3 source (console)

Before you set up a rule in EventBridge, you must create an AWS CloudTrail trail. For more
information, see [Creating a Trail in the Console](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md").

###### Important

If you use the console to create or edit your pipeline, your EventBridge rule and
AWS CloudTrail trail are created for you.

###### To create a trail

1. Open the AWS CloudTrail console.
2. In the navigation pane, choose **Trails**.
3. Choose **Create trail**. For **Trail
   name**, enter a name for your trail.
4. Under **Storage location**, create or specify the bucket
   to be used to store the log files. By default, Amazon S3 buckets and objects are
   private. Only the resource owner (the AWS account that created the bucket)
   can access the bucket and its objects. The bucket must have a resource
   policy that allows AWS CloudTrail permissions to access the objects in the
   bucket.
5. Under **Trail log bucket and folder**, specify an Amazon S3
   bucket and the object prefix (folder name) to log data events for all
   objects in the folder. For each trail, you can add up to 250 Amazon S3 objects.
   Complete the required encryption key information and choose
   **Next**.
6. For **Event type**, choose **Management
   events**.
7. For **Management events**, choose
   **Write**. The trail records Amazon S3 object-level API
   activity (for example, `GetObject` and `PutObject`) on
   the specified bucket and prefix.
8. Choose **Write**.
9. If you're satisfied with the trail, choose **Create
   trail**.

###### To create an EventBridge rule that targets your pipeline with an Amazon S3 source

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
7. In **Sample events**, type S3 as the keyword to filter
   on. Choose **AWS API call via CloudTrail**.
8. Under **Creation method**, choose **Customer
   pattern (JSON editor)**.

Paste the event pattern provided below. Make sure to add the bucket name
and S3 object key (or key name) which uniquely identifies the object in the
bucket as `requestParameters`. In this example, a rule is created
for a bucket named
`amzn-s3-demo-source-bucket`
and an object key of `my-files.zip`. When you use the
**Edit** window to specify resources, your rule is
updated to use a custom event pattern.

The following is a sample event pattern to copy and paste:

```
{
    "source": [
        "aws.s3"
    ],
    "detail-type": [
        "AWS API Call via CloudTrail"
    ],
    "detail": {
        "eventSource": [
            "s3.amazonaws.com"
        ],
        "eventName": [
            "CopyObject",
            "CompleteMultipartUpload",
            "PutObject"
        ],
        "requestParameters": {
            "bucketName": [
                "amzn-s3-demo-source-bucket"
            ],
            "key": [
                "my-files.zip"
            ]
        }
    }
}
```

9. Choose **Next**.
10. In **Target types**, choose **AWS
    service**.
11. In **Select a target**, choose
    **CodePipeline**. In **Pipeline ARN**,
    enter the pipeline ARN for the pipeline to be started by this rule.

###### Note

To get the pipeline ARN, run the **get-pipeline**
command. The pipeline ARN appears in the output. It is constructed in
this format:

arn:aws:codepipeline:`region`:`account`:`pipeline-name`

Sample pipeline ARN:

arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline 12. To create or specify an IAM service role that grants EventBridge permissions to
invoke the target associated with your EventBridge rule (in this case, the target
is CodePipeline):

    * Choose **Create a new role for this specific
     resource** to create a service role that gives EventBridge
     permissions to your start your pipeline executions.
    * Choose **Use existing role** to enter a service
     role that gives EventBridge permissions to your start your pipeline
     executions.

13. (Optional) To specify source overrides with a specific image ID, use the
    input transformer to pass the data as a JSON parameters. You can also use
    the input transformer to pass pipeline variables.
    - Expand **Additional settings**.

    Under **Configure target input**, choose
    **Configure input transformer**.

    In the dialog window, choose **Enter my own**. In
    the **Input path** box, type the following
    key-value pairs.

    ```
    {"revisionValue": "$.detail.object.version-id"}
    ```

    - In the **Template** box, type the following
      key-value pairs.

    ```


                                    {
        "sourceRevisions": [
            {
                "actionName": "``Source``",
                "revisionType": "`S3_OBJECT_VERSION_ID`",
                "revisionValue": "<`revisionValue`>"
            }
        ],
         "variables": [
            {
                "name": "`Variable_Name`",
                "value": "`Variable_Value`"
            }
        ]
    }

    ```

    - Choose **Confirm**.

14. Choose **Next**.
15. On the **Tags** page, choose
    **Next**.
16. On the **Review and create** page, review the rule
    configuration. If you're satisfied with the rule, choose **Create
    rule**.
