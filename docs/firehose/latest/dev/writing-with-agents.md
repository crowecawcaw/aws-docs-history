# Configure Kinesis agent to send data

Amazon Kinesis agent is a standalone Java software application that serves as a reference
implementation to show how you can collect and send data to Firehose. The agent continuously
monitors a set of files and sends new data to your Firehose stream. The agent shows how you can
handle file rotation, checkpointing, and retry upon failures. It shows how you can deliver
your data in a reliable, timely, and simple manner. It also shows how you can emit CloudWatch
metrics to better monitor and troubleshoot the streaming process. To learn more, [awslabs/amazon-kinesis-agent](https://github.com/awslabs/amazon-kinesis-agent "https://github.com/awslabs/amazon-kinesis-agent").

By default, records are parsed from each file based on the newline (`'\n'`)
character. However, the agent can also be configured to parse multi-line records (see [Specify agent configuration settings](agent-config-settings.md "agent-config-settings.md")).

You can install the agent on Linux-based server environments such as web servers, log
servers, and database servers. After installing the agent, configure it by specifying the
files to monitor and the Firehose stream for the data. After the agent is configured, it
durably collects data from the files and reliably sends it to the Firehose stream.

## Prerequisites

Before you start using Kinesis Agent, make sure you meet the following prerequisites.

- Your operating system must be Amazon Linux, or Red Hat Enterprise Linux
  version 7 or later.
- Agent version 2.0.0 or later runs using JRE version 1.8 or later. Agent
  version 1.1.x runs using JRE 1.7 or later.
- If you are using Amazon EC2 to run your agent, launch your EC2 instance.
- The IAM role or AWS credentials that you specify must have permission to
  perform the Amazon Data Firehose [PutRecordBatch](../APIReference/API_PutRecordBatch.md "../APIReference/API_PutRecordBatch.md") operation for the agent to send
  data to your Firehose stream. If you enable CloudWatch monitoring for the agent,
  permission to perform the CloudWatch [PutMetricData](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricData.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricData.md") operation is also
  needed. For more information, see [Controlling access with Amazon Data Firehose](controlling-access.md "controlling-access.md"), [Monitor Kinesis Agent health](agent-health.md "agent-health.md"), and [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").
