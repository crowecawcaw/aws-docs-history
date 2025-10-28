End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Troubleshooting AWS IoT Analytics

See the following section to troubleshoot errors and find and possible solutions to resolve
issues with AWS IoT Analytics.

###### Topics

- [How do I know if my messages are getting into AWS IoT Analytics?](#getting-data "#getting-data")
- [Why is my pipeline losing messages? How do I fix it?](#pipeline-no-data "#pipeline-no-data")
- [Why is there no data in my data store?](#datastore-no-data "#datastore-no-data")
- [Why does my dataset just show \_\_dt?](#dataset-no-data "#dataset-no-data")
- [How do I code an event driven by the dataset
  completion?](#event-driven-dataset "#event-driven-dataset")
- [How do I correctly configure my notebook instance
  to use AWS IoT Analytics?](#configure-notebook-instance "#configure-notebook-instance")
- [Why can't I create notebooks in an instance?](#notebook-instance "#notebook-instance")
- [Why aren't I seeing my datasets in Quick Suite?](#sq-no-dataset "#sq-no-dataset")
- [Why am I not seeing the containerize button
  on my existing Jupyter Notebook?](#containerization-jupyter-notebook "#containerization-jupyter-notebook")
- [Why is my containerization plugin
  installation failing?](#containerization-installation-fails "#containerization-installation-fails")
- [Why is my containerization plugin throwing an
  error?](#containerization-error "#containerization-error")
- [Why don't I see my variables during the
  containerization?](#containerization-no-variables "#containerization-no-variables")
- [What variables can I add to my container as an
  input?](#add-variables-to-container "#add-variables-to-container")
- [How do I set my container output as an
  input for subsequent analysis?](#containerization-subsequent-analysis "#containerization-subsequent-analysis")
- [Why is my container dataset failing?](#container-dataset-fails "#container-dataset-fails")

## How do I know if my messages are getting into AWS IoT Analytics?

Check if the rule to inject data into the channel through the rules-engine is configured
correctly.

```
aws iot get-topic-rule --rule-name `your-rule-name`
```

The response should look like the following.

```
{
    "ruleArn": "arn:aws:iot:us-west-2:`your-account-id`:rule/`your-rule-name`",
    "rule": {
        "awsIotSqlVersion": "2016-03-23",
        "sql": "SELECT * FROM 'iot/`your-rule-name`'",
        "ruleDisabled": false,
        "actions": [
            {
                "iotAnalytics": {
                    "channelArn": "arn:aws:iotanalytics:`region`:`your_account_id`:channel/`your-channel-name`"
                }
            }
        ],
        "ruleName": "`your-rule-name`"
    }
}
```

Make sure the region and channel name used in the rule are correct. To ensure your data is
reaching the rules engine and the rule is being executed correctly, you might want to add a new
target to store incoming messages in the Amazon S3 bucket temporarily.

## Why is my pipeline losing messages? How do I fix it?

- An activity has received an invalid JSON input:

All activities, except Lambda activities, specially require a valid JSON string as input.
If the JSON received by an activity is invalid, then the message is dropped and does not make
its way into the data store. Make sure you are ingesting valid JSON messages into the service.
In case of binary input, make sure the first activity in your pipeline is a Lambda activity
that converts the binary data to valid JSON before passing it to the next activity or storing
it in the data store. For more information, see [Lambda function example 2](pipeline-activities.md#aws-iot-analytics-pipeline-activities-lambda-ex2 "pipeline-activities.md#aws-iot-analytics-pipeline-activities-lambda-ex2").

- A Lambda function invoked by a Lambda activity has insufficient permissions:

Make sure that each Lambda function in a Lambda activity has permission to be invoked from
the AWS IoT Analytics service. You can use the following AWS CLI command to grant permission.

```
aws lambda add-permission --function-name <name> --region <region> --statement-id <id> --principal iotanalytics.amazonaws.com --action lambda:InvokeFunction
```

- A filter or removeAttribute activity is incorrectly defined:

Make sure the definitions if any `filter` or `removeAttribute`
activities are correct. If you filter out a message or remove all attributes from a message,
that message is not added to the data store.

## Why is there no data in my data store?

- There is a delay between data ingestion and data availability:

It might take several minutes after data is ingested into a channel before that data is
available in the data store. The time varies based on the number of pipeline activities and the
definition of any custom Lambda activities in your pipeline.

- Messages are being filtered out in your pipeline:

Make sure you are not dropping messages in the pipeline. (See the previous question and
response.)

- Your dataset query is incorrect:

Make sure the query that generates the dataset from the data store is correct. Remove any
unnecessary filters from the query to ensure your data reaches your data store.

## Why does my dataset just show `__dt`?

- This column is added by the service automatically and contains the approximate ingestion
  time of the data. It may be used to optimize your queries. If your dataset contains nothing but
  this, see the previous question and response.

## How do I code an event driven by the dataset

completion?

- You must set up polling based on the `describe-dataset` command to check if the
  status of the dataset with a particular timestamp is **SUCCEEDED**.

## How do I correctly configure my notebook instance

to use AWS IoT Analytics?

Follow these steps to make sure the IAM role you are using to create the notebook
instance has the required permissions:

1. Go to the SageMaker AI console and create a notebook instance.
2. Fill in the details and choose **create a new role**. Make a note of the
   role ARN.
3. Create the notebook instance. This also creates a role that SageMaker AI can use.
4. Go to the IAM console and modify the newly created SageMaker AI role. When you open that role,
   it should have a managed policy.
5. Click **add inline policy**, choose **IoTAnalytics** as
   the service, and under read permission, select **GetDatasetContent**.
6. Review the policy, add a policy name, and then create it. The newly created role now has
   policy permission to read a dataset from AWS IoT Analytics.
7. Go to AWS IoT Analytics console and create notebooks in the notebook instance.
8. Wait for the notebook instance to be in the "In Service" state.
9. Choose **create notebooks**, and select the notebook instance you
   created. This creates a Jupyter notebook with the selected template that can access your
   datasets.

## Why can't I create notebooks in an instance?

- Make sure you create a notebook instance with the correct IAM policy. (Follow the steps in
  the previous question.)
- Make sure the notebook instance is in the "In Service" state. When you create an instance,
  it starts in a "Pending" state. It usually takes about five minutes for it to go into the "In
  Service" state. If the notebook instance goes into the "Failed" state after about five minutes,
  check the permissions again.

## Why aren't I seeing my datasets in Quick Suite?

Quick Suite might need permission to read your AWS IoT Analytics dataset content. To give permission, follow
these steps.

1. Choose your account name in the upper‐right corner of Quick Suite and choose
   **Manage QuickSight**.
2. In
   the left navigation
   pane,
   choose **Security & permissions**. Under **QuickSight access to
   AWS services**, verify that access is granted to AWS IoT Analytics.
   1. If AWS IoT Analytics doesn't have access, choose **Add or remove**.
   2. Choose the box next to **AWS IoT Analytics** and then select
      **Update**. This gives Quick Suite permission to read your dataset content.

3. Try again to visualize your data.

Make sure that you choose the same AWS Region for both AWS IoT Analytics and Quick Suite. Otherwise, you
might have issues accessing the AWS resources. For the list of supported Regions, see [AWS IoT Analytics endpoints and quotas](../../../general/latest/gr/iot-analytics.md "../../../general/latest/gr/iot-analytics.md") and [Quick Suite endpoints and quotas](../../../general/latest/gr/quicksight.md "../../../general/latest/gr/quicksight.md") in the
_Amazon Web Services General Reference_.

## Why am I not seeing the containerize button

on my existing Jupyter Notebook?

- This is caused by a missing AWS IoT Analytics Containerization Plugin. If you created you SageMaker
  notebook instance before August 23, 2018, you need to manually install the plugin by following
  the instructions in [Containerizing a
  notebook](automate.md#aws-iot-analytics-automate-containerize "automate.md#aws-iot-analytics-automate-containerize").
- If you don't see the containerize button after creating the SageMaker notebook instance
  from the AWS IoT Analytics console or manually installing it, contact AWS IoT Analytics technical support.

## Why is my containerization plugin

installation failing?

- Usually, the plugin installation fails because of missing permissions in the SageMaker
  notebook instance. For the required permissions for the notebook instance, see [Permissions](automate.md#aws-iot-analytics-automate-permissions "automate.md#aws-iot-analytics-automate-permissions")
  and add the required permissions to the notebook instance role. If the problem persists, create
  a new notebook instance from the AWS IoT Analytics console.
- You can safely ignore the following message in the log if it appears during installation
  of the plugin: "To initialize this extension in the browser every time the notebook (or other
  app) loads."

## Why is my containerization plugin throwing an

error?

- Containerization can fail and generate errors for multiple reasons. Make sure that you're
  using the correct kernel before containerizing your notebook. Containerized kernels begin with
  the "Containerized" prefix.
- Since the plugin creates and saves a docker image in an ECR repository, make sure that
  your notebook instance role has sufficient permissions to read, list and create ECR
  repositories. For the required permissions for the notebook instance, see [Permissions](automate.md#aws-iot-analytics-automate-permissions "automate.md#aws-iot-analytics-automate-permissions")
  and add the required permissions to the notebook instance role.
- Also make sure that the name of the repository complies with ECR requirements. ECR
  repository names must start with a letter and can contain only lower-case letters, numbers,
  hyphens, underscores, and forward slashes.
- If the containerization process fails with the error:"This instance has insufficient free
  space to run containerization" try using a larger instance to resolve the issue.
- If you see connection errors or an image creation error, please retry. If the problem
  persists, restart the instance and install the latest plugin version.

## Why don't I see my variables during the

containerization?

- The AWS IoT Analytics containerization plugin automatically recognizes all variables in your notebook
  after it runs the notebook with the "Containerized" kernel. Use one of the containerized
  kernels to run the notebook, and then perform containerization.

## What variables can I add to my container as an

input?

- You can add any variable whose value you want to modify during the runtime as an input to
  your container. This enables your to run the same container with different parameters that need
  to be supplied at the time of dataset creation. The AWS IoT Analytics containerization Jupyter plugin
  simplifies this process by automatically recognizing the variables in the notebook and making
  them available as part of the containerization process.

## How do I set my container output as an

input for subsequent analysis?

- A specific S3 location where the executed artifacts can be stored is created for each run
  of your container dataset. To access this output location, create a variable with type
  `outputFileUriValue` in your container dataset. The value of this variable should
  be an S3 path that is used for storing your additional output files. To access these saved
  artifacts in subsequent runs, you can use the `getDatasetContent` API and pick the
  appropriate output file required for the subsequent run.

## Why is my container dataset failing?

- Make sure that you're passing the correct `executionRole` to the container
  dataset. The trust policy of the `executionRole` must include both
  `iotanalytics.amazonaws.com` and `sagemaker.amazonaws.com`.
- If you see `AlgorithmError` as the reason for the failure, try to debug your
  container code manually. This happens if there is a bug in the container code or the execution
  role doesn't have permission to execute the container. If you containerized by using the AWS IoT Analytics
  Jupyter plugin, create a new SageMaker notebook instance with the same role as the
  executionRole of the containerDataset and try running the notebook manually. If the container
  was created outside of the Jupyter plugin, try manually running the code and limiting the
  permission to the executionRole.
