# Generate reports

This guide provides step-by-step instructions to configure and manage usage reporting
for your SageMaker HyperPod clusters. Follow these procedures to deploy infrastructure,
generate custom reports, and remove resources when no longer needed.

## Set up usage

reporting

###### Note

Before configuring the SageMaker HyperPod usage report infrastructure in your
SageMaker HyperPod cluster, ensure you have met all prerequisites detailed in this
[`README.md`](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#prerequisites "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#prerequisites").

Usage reporting in HyperPod requires:

- Deploying SageMaker HyperPod usage report AWS resources using an CloudFormation
  stack
- Installing the SageMaker HyperPod usage report Kubernetes operator via a Helm
  chart

You can find comprehensive installation instructions in the [SageMaker HyperPod usage report GitHub repository](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md"). Specifically, follow the
steps in the [Set up](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#set-up-usage-reporting "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#set-up-usage-reporting") section.

## Generate usage reports on

demand

Once the usage reporting infrastructure and Kubernetes operator are installed, job
data for your SageMaker HyperPod cluster is automatically collected and stored in the S3
bucket you configured during setup. The operator continuously captures detailed
usage metrics in the background, creating raw data files in the `raw`
directory of your designated S3 bucket.

To generate an on-demand usage report, you can use the `run.py` script
provided in the [SageMaker HyperPod usage report GitHub repository](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md") to extract and export usage
metrics. Specifically, you can find the script and comprehensive instructions for
generating a report in the [Generate Reports](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#generate-reports "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#generate-reports") section.

The script allows you to:

- Specify custom date ranges for report generation
- Choose between detailed and summary report types
- Export reports in CSV or PDF formats
- Direct reports to a specific S3 location

## Clean up usage

reporting resources

When you no longer need your SageMaker HyperPod usage reporting infrastructure, follow
the steps in [Clean Up Resources](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#clean-up-resources "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#clean-up-resources") to clean up the Kubernetes operator and AWS
resources (in that order). Proper resource deletion helps prevent unnecessary
costs.
