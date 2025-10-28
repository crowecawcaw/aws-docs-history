AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# How Amazon EC2 instance recommendations work

in AWS Migration Hub

This feature recommends the most cost-effective Amazon Elastic Compute Cloud instance type that can
satisfy your existing server specifications and utilization requirements while taking
into account your selected instance preferences. The server specifications that are used
to generate your recommendations are:

- Number of processors
- Number of logical cores
- Total amount of RAM
- Operating system family
- Usage data including peak, average, and percentiles of CPU and RAM
  Amazon EC2 instance recommendations returns the best Amazon EC2 instance type match based on
  server specification as well as the performance dimensions you provided. To match the
  performance dimensions, the service adjusts the server’s specification by multiplying
  the original CPU and RAM values by the usage percentage.
