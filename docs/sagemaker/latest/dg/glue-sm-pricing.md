# AWS Glue interactive session pricing

When you use AWS Glue interactive sessions on Studio or Studio Classic notebooks, you
are charged separately for resource usage on AWS Glue and Studio notebooks.

AWS charges for AWS Glue interactive sessions based on how long the session is active
and the number of Data Processing Units (DPU) used. You are charged an hourly rate for
the number of DPUs used to run your workloads, billed in increments of one second. AWS Glue
interactive sessions assigns a default of five DPUs and requires a minimum of two DPUs.
There is also a one-minute minimum billing duration for each interactive session. To see
the AWS Glue rates and pricing examples, or to estimate your costs using the AWS Pricing
Calculator, see [AWS Glue pricing](https://aws.amazon.com/glue/pricing "https://aws.amazon.com/glue/pricing") .

Your Studio or Studio Classic notebook runs on an Amazon EC2 instance and you are charged
for the instance type you choose, based on the duration of use. Studio Classic assign you a
default EC2 instance type of `ml-t3-medium` when you select the
`SparkAnalytics` image and associated kernel. You can change the instance
type for of your Studio Classic notebook to suit your workload. For information about
Studio and Studio Classic pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing "https://aws.amazon.com/sagemaker/pricing").
