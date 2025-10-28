# Async analysis for topic modeling

To determine the topics in a document set, use the [StartTopicsDetectionJob](../APIReference/API_StartTopicsDetectionJob.md "../APIReference/API_StartTopicsDetectionJob.md")
to start an asynchronous job. You can monitor topics in documents written in English or
Spanish.

###### Topics

- [Before you start](#topics-before "#topics-before")
- [Using the AWS Command Line Interface](#topics-cli "#topics-cli")
- [Using the SDK for Python or SDK for .NET](#topic-java "#topic-java")

## Before you start

Before you start, make sure that you have:

- **Input and output buckets**—Identify
  the Amazon S3 buckets that you want to use for input and output. The buckets must
  be in the same Region as the API that you are calling.
- **IAM service role**—You must have an
  IAM service role with permission to access your input and output buckets.
  For more information, see [Role-based permissions required for
  asynchronous operations](security_iam_id-based-policy-examples.md#auth-role-permissions "security_iam_id-based-policy-examples.md#auth-role-permissions").

## Using the AWS Command Line Interface

The following example demonstrates using the `StartTopicsDetectionJob`
operation with the AWS CLI

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

```
aws comprehend start-topics-detection-job \
                --number-of-topics `topics to return` \
                --job-name "`job name`" \
                --region `region` \
                --cli-input-json file://`path to JSON input file`
```

For the `cli-input-json` parameter you supply the path to a JSON file
that contains the request data, as shown in the following example.

```
{
    "InputDataConfig": {
        "S3Uri": "s3://`input bucket`/`input path`",
        "InputFormat": "ONE_DOC_PER_FILE"
    },
    "OutputDataConfig": {
        "S3Uri": "s3://`output bucket`/`output path`"
    },
    "DataAccessRoleArn": "arn:aws:iam::`account ID`:role/`data access role`"
}
```

If the request to start the topic detection job was successful, you will receive
the following response:

```
{
    "JobStatus": "SUBMITTED",
    "JobId": "`job ID`"
}
```

Use the [ListTopicsDetectionJobs](../APIReference/API_ListTopicsDetectionJobs.md "../APIReference/API_ListTopicsDetectionJobs.md")
operation to see a list of the topic detection jobs that you have submitted. The list includes information about
the input and output locations that you used and the status of each of the detection jobs. The example is
formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\) Unix continuation character at the
end of each line with a caret (^).

```
aws comprehend list-topics-detection-jobs \-- `region`
```

You will get JSON similar to the following in response:

```
{
    "TopicsDetectionJobPropertiesList": [
        {
            "InputDataConfig": {
                "S3Uri": "s3://`input bucket`/`input path`",
                "InputFormat": "ONE_DOC_PER_LINE"
            },
            "NumberOfTopics": `topics to return`,
            "JobId": "`job ID`",
            "JobStatus": "COMPLETED",
            "JobName": "`job name`",
            "SubmitTime": `timestamp`,
            "OutputDataConfig": {
                "S3Uri": "s3://`output bucket`/`output path`"
            },
            "EndTime": `timestamp`
        },
        {
            "InputDataConfig": {
                "S3Uri": "s3://`input bucket`/`input path`",
                "InputFormat": "ONE_DOC_PER_LINE"
            },
            "NumberOfTopics": `topics to return`,
            "JobId": "`job ID`",
            "JobStatus": "RUNNING",
            "JobName": "`job name`",
            "SubmitTime": `timestamp`,
            "OutputDataConfig": {
                "S3Uri": "s3://`output bucket`/`output path`"
            }
        }
    ]
}

```

You can use the [DescribeTopicsDetectionJob](../APIReference/API_DescribeTopicsDetectionJob.md "../APIReference/API_DescribeTopicsDetectionJob.md") operation to get the status of
an existing job. The example is formatted for Unix, Linux, and macOS. For Windows,
replace the backslash (\) Unix continuation character at the end of each line with a
caret (^).

```
aws comprehend describe-topics-detection-job --job-id `job ID`
```

You will get the following JSON in response:

```
{
    "TopicsDetectionJobProperties": {
        "InputDataConfig": {
            "S3Uri": "s3://`input bucket`/`input path`",
            "InputFormat": "ONE_DOC_PER_LINE"
        },
        "NumberOfTopics": `topics to return`,
        "JobId": "`job ID`",
        "JobStatus": "COMPLETED",
        "JobName": "`job name`",
        "SubmitTime": `timestamp`,
        "OutputDataConfig": {
            "S3Uri": "s3://`output bucket`/`ouput path`"
        },
        "EndTime": `timestamp`
    }
}
```

## Using the SDK for Python or SDK for .NET

For SDK examples of how to start a topic modeling job, see [Use StartTopicsDetectionJob with an AWS SDK or CLI](example_comprehend_StartTopicsDetectionJob_section.md "example_comprehend_StartTopicsDetectionJob_section.md").
