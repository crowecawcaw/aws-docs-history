

# Tutorial: Listen for AWS Batch job events using EventBridge
<a name="batch_cwet"></a>

In this tutorial, you set up a simple AWS Lambda function that listens for AWS Batch job events and writes them out to a CloudWatch Logs log stream.

## Prerequisites
<a name="cwet_prereqs"></a>

This tutorial assumes that you have a working compute environment and job queue that are ready to accept jobs. If you don't have a running compute environment and job queue to capture events from, follow the steps in [Getting started with AWS Batch tutorials](Batch_GetStarted.md) to create one. At the end of this tutorial, you can optionally submit a job to this job queue to test that you have configured your Lambda function correctly. 

**Topics**
+ [Prerequisites](#cwet_prereqs)
+ [Tutorial: Create the Lambda function](cwet_create_lam.md)
+ [Tutorial: Register the event rule](cwet_register_event_rule.md)
+ [Tutorial: Test your configuration](cwet_test.md)