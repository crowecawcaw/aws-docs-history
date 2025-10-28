# Use the AWS CLI to perform Amazon Kinesis Data Streams operations

This section shows you how to perform basic Amazon Kinesis Data Streams operations using the AWS Command Line Interface. You
will learn fundamental Kinesis Data Streams data flow principles and the steps necessary to put and get
data from an Kinesis data stream.

If you are new to Kinesis Data Streams, start by becoming familiar with the concepts and terminology
presented in [Amazon Kinesis Data Streams Terminology and concepts](key-concepts.md "key-concepts.md").

###### Topics

- [Tutorial: Install and configure the AWS CLI for
  Kinesis Data Streams](kinesis-tutorial-cli-installation.md "kinesis-tutorial-cli-installation.md")
- [Tutorial: Perform basic Kinesis Data Streams operations using the
  AWS CLI](fundamental-stream.md "fundamental-stream.md")
  For CLI access, you need an access key ID and a secret access key.
  Use temporary credentials instead of long-term access keys when possible.
  Temporary credentials include an access key ID, a secret access key, and a
  security token that indicates when the credentials expire. For more information,
  see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.

You can find detailed
step-by-step IAM and security key set up instructions at [Create an IAM
User](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-an-iam-user "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-an-iam-user").

In this section, the specific commands discussed are given verbatim, except where
specific values are necessarily different for each run. Also, the examples are using the
US West (Oregon) region, but the steps in this section work in any of [the regions where Kinesis Data Streams is supported](../../../general/latest/gr/rande.md#ak_region "../../../general/latest/gr/rande.md#ak_region").
