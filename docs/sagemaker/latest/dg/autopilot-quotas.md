# Autopilot quotas

There are quotas that limit the resources available to you when using Amazon SageMaker Autopilot. Some of these
limits are increasable and some are not.

###### Note

The resource quotas documented in the following sections are valid for versions of
Amazon SageMaker Studio Classic 3.22.2 and higher. For information on updating your version of SageMaker
Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md "studio-tasks-update.md").

###### Topics

- [Quotas that you can increase](#autopilot-quotas-limits-increasable "#autopilot-quotas-limits-increasable")
- [Resource quotas](#autopilot-quotas-resource-limits "#autopilot-quotas-resource-limits")

## Quotas that you can increase

The following table contains the resource limits for quotas you can increase:

| Resource                                | Regions                                                                 | Default limits | Can be increased up to |
| --------------------------------------- | ----------------------------------------------------------------------- | -------------- | ---------------------- |
| Size of input dataset                   | All                                                                     | 100 GB         | Hundreds of GBs        |
| Size of a single Parquet file\*         | All                                                                     | 2 GB           | N/A                    |
| Target dataset size for subsampling\*\* | All                                                                     | 5 GB           | Hundreds of GBs        |
| Number of concurrent Autopilot jobs     | us-east-1, us-east-2,us-west-2, ap-northeast-1, eu-west-1, eu-central-1 | 4              | Hundreds               |
| Number of concurrent Autopilot jobs     | ap-northeast-2, ap-southeast-2, eu-west-2, ap-southeast-1               | 2              | Hundreds               |
| Number of concurrent Autopilot jobs     | All other Regions                                                       | 1              | Tens                   |

###### Note

\*This 2 GB size limit is for a single compressed Parquet file. You can provide a Parquet
dataset that includes multiple compressed Parquet files up to the input dataset maximum
size. After the files are decompressed, they may each expand to a larger size.

\*\*Autopilot automatically subsamples input datasets that are larger than the target dataset
size while accounting for class imbalance and preserving rare class labels.

###### To request a quota increase:

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas "https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas").
2. Select your quota increase, then choose **Request increase at account
   level**.
3. In the **Increase quota value**, enter the new limit value that you
   are requesting.
4. Choose **Request**.

## Resource quotas

The following table contains the runtime resource limits for an Amazon SageMaker Autopilot job in an
AWS Region.

| Resource                             | Limit per Autopilot job |
| ------------------------------------ | ----------------------- |
| Maximum runtime for an Autopilot job | 30 days                 |
