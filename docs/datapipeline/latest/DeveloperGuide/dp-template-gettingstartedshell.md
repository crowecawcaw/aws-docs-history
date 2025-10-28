AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Getting started using

ShellCommandActivity

The **Getting Started using ShellCommandActivity** template
runs a shell command script to count the number of GET requests in a log file.
The output is written in a time-stamped Amazon S3 location on every scheduled run of
the pipeline.

The template uses the following pipeline objects:

- ShellCommandActivity
- S3InputNode
- S3OutputNode
- Ec2Resource
