# Create the Amazon SNS topic

The steps for creating Amazon SNS topics for work team notifications are similar to the
steps in [Getting
Started](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon SNS Developer Guide_,
with one significant addition—you must add an access policy so that Amazon SageMaker AI can
publish messages to the topic on your behalf.

If you create a work team using the console, the console provides an option to create a
new topic for the team so that you don't have to perform these steps.

###### Important

The Amazon SNS feature is not supported by Amazon A2I. If you subscribe your work team to
an Amazon SNS topic, workers will only receive notifications about Ground Truth labeling jobs.
Workers will not receive notifications about new Amazon A2I human review tasks.

###### To add the policy when you create the topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In **Create topic**, enter the name of your topic and then
   choose **Next steps**.
3. In **Access policy**, choose
   **Advanced**.
4. In the **JSON editor**, find the `Resource`
   property, which displays the topic's ARN.
5. Copy the `Resource` ARN value.
6. Before the final closing brace (`]`), add the following
   policy.

```
    , {
        "Sid": "AwsSagemaker_SnsAccessPolicy",
        "Effect": "Allow",
        "Principal": {
            "Service": "sagemaker.amazonaws.com"
        },
        "Action": "sns:Publish",
        "Resource": "arn:partition:sns:region:111122223333:MyTopic", # ARN of the topic you copied in the previous step
        "Condition": {
            "ArnLike": {
                "aws:SourceArn": "arn:partition:sagemaker:region:111122223333:workteam/*" # Workteam ARN
            },
            "StringEquals": {
                "aws:SourceAccount": "111122223333" # SNS topic account
            }
        }
    }
```

7. Create the topic.
   After you create the topic, it appears in your **Topics** summary
   screen. For more information about creating topics, see [Creating a
   Topic](../../../sns/latest/dg/sns-tutorial-create-topic.md "../../../sns/latest/dg/sns-tutorial-create-topic.md") in the _Amazon SNS Developer
   Guide_.
