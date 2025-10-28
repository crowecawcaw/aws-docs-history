# AWS IoT Jobs

Use AWS IoT Jobs to define a set of remote operations that can be sent to and run on one or
more devices connected to AWS IoT. For example, you can define a job that instructs a set of
devices to download and install applications, run firmware updates, reboot, rotate
certificates, or perform remote troubleshooting operations.

## Accessing AWS IoT jobs

You can get started with AWS IoT Jobs by using the console or the AWS IoT Core
API.

###### Using the console

Sign in to the AWS Management Console, and go to the AWS IoT console. In the navigation pane,
choose **Manage**, and then choose **Jobs**. You
can create and manage jobs from this section. If you want to create and manage job
templates, in the navigation pane, choose **Job templates**. For
more information, see [Create and manage jobs by using the
AWS Management Console](manage-job-console.md "manage-job-console.md").

###### Using the API or CLI

You can get started by using the AWS IoT Core API operations. For more information,
see [AWS IoT API Reference](../apireference.md "../apireference.md"). The AWS IoT Core API that AWS IoT
jobs is built on is supported by the AWS SDK. For more information, see [AWS SDKs and
Toolkits](https://aws.amazon.com/getting-started/tools-sdks/ "https://aws.amazon.com/getting-started/tools-sdks/").

You can use the AWS CLI to run commands for creating and managing jobs and job
templates. For more information, see [AWS IoT CLI reference](../../../cli/latest/reference/iot/index.md "../../../cli/latest/reference/iot/index.md").

## AWS IoT Jobs Regions and endpoints

AWS IoT Jobs supports control plane and data plane API endpoints that are specific to
your AWS Region. The data plane API endpoints are specific to your AWS account and
AWS Region. For more information about the AWS IoT Jobs endpoints, see [AWS IoT Device Management - jobs data endpoints](../../../general/latest/gr/iot_device_management.md#iot_device_management_region_jobs "../../../general/latest/gr/iot_device_management.md#iot_device_management_region_jobs") in the
_AWS General Reference_.
