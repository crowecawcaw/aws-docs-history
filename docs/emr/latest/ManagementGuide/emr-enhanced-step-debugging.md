# Enhanced step debugging with Amazon EMR

If an Amazon EMR step fails and you submitted your work using the Step API operation
with an AMI of version 5.x or later, Amazon EMR can identify and return the root cause of
the step failure in some cases, along with the name of the relevant log file and a
portion of the application stack trace via API. For example, the following failures
can be identified:

- A common Hadoop error such as the output directory already exists, the
  input directory does not exist, or an application runs out of memory.
- Java errors such as an application that was compiled with an incompatible
  version of Java or run with a main class that is not found.
- An issue accessing objects stored in Amazon S3.
  This information is available using the [DescribeStep](../../../ElasticMapReduce/latest/API/API_DescribeStep.md "../../../ElasticMapReduce/latest/API/API_DescribeStep.md") and [ListSteps](../../../ElasticMapReduce/latest/API/API_ListSteps.md "../../../ElasticMapReduce/latest/API/API_ListSteps.md") API operations. The
  [FailureDetails](../../../ElasticMapReduce/latest/API/API_FailureDetails.md "../../../ElasticMapReduce/latest/API/API_FailureDetails.md") field
  of the [StepSummary](../../../ElasticMapReduce/latest/API/API_StepSummary.md "../../../ElasticMapReduce/latest/API/API_StepSummary.md") returned
  by those operations. To access the FailureDetails information, use the AWS CLI,
  console, or AWS SDK.

Console
The new Amazon EMR console doesn't offer step debugging. However, you can
view cluster termination details with the following steps.

###### To view failure details with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then select the
   cluster that you want to view.
3. Note the **Status** value in the
   **Summary** section of the cluster details
   page. If the status is **Terminated with
   errors**, hover over the text to view cluster
   failure details.

CLI

###### To view failure details with the AWS CLI

- To get failure details for a step with the AWS CLI, use the
  `describe-step` command.

```
aws emr describe-step --cluster-id j-1K48XXXXXHCB --step-id s-3QM0XXXXXM1W
```

The output will look similar to the following:

```
{
  "Step": {
    "Status": {
      "FailureDetails": {
        "LogFile": "s3://amzn-s3-demo-bucket/logs/j-1K48XXXXXHCB/steps/s-3QM0XXXXXM1W/stderr.gz",
        "Message": "org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory s3://amzn-s3-demo-bucket/logs/beta already exists",
        "Reason": "Output directory already exists."
      },
      "Timeline": {
        "EndDateTime": 1469034209.143,
        "CreationDateTime": 1469033847.105,
        "StartDateTime": 1469034202.881
      },
      "State": "FAILED",
      "StateChangeReason": {}
    },
    "Config": {
      "Args": [
        "wordcount",
        "s3://amzn-s3-demo-bucket/input/input.txt",
        "s3://amzn-s3-demo-bucket/logs/beta"
      ],
      "Jar": "s3://amzn-s3-demo-bucket/jars/hadoop-mapreduce-examples-2.7.2-amzn-1.jar",
      "Properties": {}
    },
    "Id": "s-3QM0XXXXXM1W",
    "ActionOnFailure": "CONTINUE",
    "Name": "ExampleJob"
  }
}
```
