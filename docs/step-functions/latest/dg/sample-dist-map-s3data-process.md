# Process data in an Amazon S3 bucket with Distributed Map

This sample project demonstrates how you can use the [Distributed Map state](state-map-distributed.md "state-map-distributed.md") to process large-scale data, for example,
analyze historical weather data and identify the weather station that has the highest average temperature on the planet each month. The weather data is
recorded in over 12,000 CSV files, which in turn are stored in an Amazon S3 bucket.

This sample project includes two *Distributed Map state*s named **Distributed S3 copy NOA Data** and **ProcessNOAAData**.
**Distributed S3 copy NOA Data** iterates over the CSV files in a public Amazon S3 bucket named **noaa-gsod-pds** and copies
them to an Amazon S3 bucket in your AWS account. **ProcessNOAAData** iterates over the copied files and includes a Lambda function that
performs the temperature analysis.

The sample project first checks the contents of the Amazon S3 bucket with a call to the [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md") API action. Based on the number of [keys](../../../AmazonS3/latest/API/API_ListObjectsV2.md#AmazonS3-ListObjectsV2-response-MaxKeys "../../../AmazonS3/latest/API/API_ListObjectsV2.md#AmazonS3-ListObjectsV2-response-MaxKeys") returned in response to this call, the sample
project takes one of the following decisions:

- If the key count is more than or equal to 1, the project transitions to the **ProcessNOAAData** state. This _Distributed Map state_ includes a
  Lambda function named **TemperatureFunction** that finds the weather station that had the highest average temperature
  each month. This function returns a dictionary with `year-month` as the key and a dictionary that contains information about the weather
  station as the value.
- If the returned key count doesn't exceed 1, the **Distributed S3 copy NOA Data** state lists all objects from the public bucket
  **noaa-gsod-pds** and iteratively copies the individual objects to another bucket in your account in batches of 100. An [Inline Map](state-map-inline.md "state-map-inline.md") performs the iterative copying of the objects.

After all objects are copied, the project transitions to the **ProcessNOAAData** state for processing the weather data.
The sample project finally transitions to a reducer Lambda function that performs a final aggregation of the results returned by the
**TemperatureFunction** function and writes the results to an Amazon DynamoDB table.

With Distributed Map, you can run up to 10,000 parallel child workflow executions at a time. In this sample project, the maximum concurrency of
**ProcessNOAAData** Distributed Map is set at 3000 that limits it to 3000 parallel child workflow executions.

This sample project creates the state machine, the supporting AWS resources, and configures the related IAM permissions. Explore this sample project
to learn about using the Distributed Map for orchestrating large-scale, parallel workloads, or use it as a starting point for your own projects.

###### Important

This sample project is only available in the US East (N. Virginia) Region.

## Step 1: Create the state machine

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") and choose **Create state machine**.
2. Choose **Create from template** and find the related starter template. Choose **Next** to continue.
3. Choose how to use the template:
   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.
   2. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

4. Choose **Use template** to continue with your selection.

###### Note

_Standard charges apply for services deployed to your account._

## Step 2: Run the demo state machine

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.
2. Wait for the AWS CloudFormation stack to deploy. This can take up to 10 minutes.
3. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

###### Congratulations!

You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.
