Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Long-term pricing for Snowball Edge devices

When ordering a Snowball Edge device, you can choose the pricing option to best fit your use case. Pricing is available in two ways: on-demand for each day you have the device or prepaid, long-term pricing in monthly, one-, or three-year terms based on the device type. You may choose to automatically renew your long-term pricing option for one- or three-year terms so that a new prepaid period begins when the previous period ends to avoid interruption of your use of the device. The monthly long-term pricing option will automatically renew while the device is in your possession. For more information about ordering a device, see [Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md") in this guide.

In addition to budgetary convenience, long-term pricing allows you to swap Snowball Edge devices during the pricing period when you operational requirements change. For example, you can request to swap devices so that the new device includes a new AMI or new data from Amazon S3 or to replace a failed device. See [Swapping Snowball Edge devices during the long-term pricing period](#ltp-swap "#ltp-swap").

###### Note

If you request to swap or replace a Snowball Edge device under 1 Year or 3 Year Commit Pricing Plan for any reason other than hardware or a software issue attributed to AWS Snow service, you will be charged a Device Cycling Fee. This Device Cycling Fee is determined as the Monthly fee (for Snowball Edge Compute Optimized) or On-Demand Job Fee for your configuration.

For more information on long-term pricing, see [Optimizing cost with long-term pricing options for AWS Snowball Edge](https://aws.amazon.com/blogs/storage/optimizing-cost-with-long-term-pricing-options-for-aws-snowball/ "https://aws.amazon.com/blogs/storage/optimizing-cost-with-long-term-pricing-options-for-aws-snowball/"). For AWS Snowball Edge pricing for your AWS Region, see [AWS Snowball Edge Pricing](https://aws.amazon.com/snowball/pricing/ "https://aws.amazon.com/snowball/pricing/").

## Swapping Snowball Edge devices during the long-term pricing period

Swapping Snowball Edge devices during the long-term pricing period involves ordering a new device and immediately returning the current device.

1. Create a new job for the replacement Snowball Edge device. The replacement device must be for the same job type and have the same compute and storage options as the device you have. See [Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md") in this guide.
2. Immediately return the device you have. See [Powering off the Snowball Edge](turnitoff.md "turnitoff.md") and [Returning the Snowball Edge device](return-device.md "return-device.md"). AWS will manage the device replacement logistics, and there will be a device cycling fee assessed for this swap.
