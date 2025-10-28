# What is a remote operation?

###### Note

Over-the-air (OTA) updates are not available in the following regions:

- Europe (Spain)
- Asia Pacific (Malaysia)
  A remote operation is any update or action you can perform on a physical device,
  virtual device, or endpoint that can be done remotely without the need for the physical
  presence of an operator or technician. The remote operation is performed using an
  over-the-air (OTA) update so your devices don't have to be physically present. Managing
  your device fleet in the AWS Cloud allows you to perform remote operations on your
  devices when they are registered with AWS IoT Core.

AWS IoT Device Management Jobs offers a scalable approach for performing remote actions on your
devices registered with AWS IoT Core. A job is created in the AWS Cloud and pushed out to
all targeted devices using an OTA update via the MQTT or HTTP protocol.

AWS IoT Device Management Jobs provide you the capability to perform remote operations such as
factory resets, device reboots, and software OTA updates in a secure, scalable, and more
cost-effective way.

For more information on AWS IoT Core, see [What is AWS IoT?](what-is-aws-iot.md "what-is-aws-iot.md").

For more information on AWS IoT Device Management Jobs, see [What is AWS IoT Jobs?](jobs-what-is.md "jobs-what-is.md").

## Benefits of using AWS IoT Device Management Jobs for remote

operations

Using AWS IoT Device Management Jobs to perform your remote operations streamlines the management of
your device fleet. The following list highlights some of the key benefits for using
AWS IoT Device Management Jobs to perform your remote operations:

- **Seamless integration with other
  AWS services**
  - AWS IoT Device Management Jobs integrates closely with the following value-added
    AWS services and features:
    - **Amazon S3**: Store your remote
      operation instructions in a secure Amazon S3 bucket where you
      control the access permissions for that content. Using an
      Amazon S3 bucket provides a scalable and durable storage solution
      that natively intergrates with AWS IoT Device Management Software Package Catalog allowing AWS IoT Device Management
      Jobs to reference and substitute in update instructions. For
      more information, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md").
    - **Amazon CloudWatch**: Monitor and log
      the remote operation implementation status of the job
      execution for each device in addition to other device
      activity to track and analyze the overall job performance in
      AWS IoT Device Management Jobs. For more information, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
      Monitoring jobs logs and capturing historical data for
      troubleshooting. How it works with jobs.
    - **AWS IoT Device Shadow service**: Maintain a
      digital representation of your AWS IoT thing via a device
      shadow using AWS IoT Device Management Jobs so your device's state is available
      to applications and other services regardless of device
      connectivity. For more information, see [AWS IoT Device Shadow service](iot-device-shadows.md "iot-device-shadows.md").

- **Security best practices**
  - **Permission control**: Control the
    access permissions to your remote operating instructions using Amazon S3
    and determine which IAM users can deploy your remote operating
    instructions to your device fleet using AWS IoT policies and
    IAM user roles.
    - For more information on AWS IoT policies, see [Create an AWS IoT policy](create-iot-resources.md#create-iot-policy "create-iot-resources.md#create-iot-policy").
    - For more information on IAM user roles, see [Identity and access management for AWS IoT](security-iam.md "security-iam.md").

- **Scalability**
  - **Targeted job deployment**: Control
    which devices receive the job document from a job with a targeted
    job deployment using specific device grouping criteria entered in
    your job document when creating the job. Creating an AWS IoT thing for
    each device and storing that information in the AWS IoT registry
    allows you to perform targeted searches using fleet indexing. You
    can create custom groups based on the fleet indexing search results
    to support your target job deployment. For more information, see
    [Managing devices with AWS IoT](iot-thing-management.md "iot-thing-management.md"). Use jobs to do snapshot vs
    continuous jobs.
  - **Job status**: Track the status of
    the job document rollout to your device fleet and overall job status
    from a device fleet level in addition to the individual
    implementation status of the job document on each device. For more
    information, see [Jobs and job execution states](iot-jobs-lifecycle.md "iot-jobs-lifecycle.md").
  - **New device scalability**: Easily
    deploy your job document to a new device by adding it to an
    existing, custom group created using fleet indexing via a continuous
    job. This will save you time over having to deploy the job document
    to each new device separately. Or, you can use a more
    targeted approach with a snapshot shot by deploying a job document
    to a predetermined group of devices once and then the job is
    completed.

- **Flexibility**
  - **Job configurations**: Customize
    your job and job document with the optional job configurations
    rollout, scheduling, abort, timeout, and retry to meet your specific
    needs. For more information, see [Job
    configurations](jobs-configurations.md "jobs-configurations.md").

- **Cost effective**
  - Introduce a more efficient cost structure for maintaining your
    device fleet by leveraging AWS IoT Device Management Jobs to deploy critical updates
    and perform routine maintenance tasks. A do-it-yourself (DIY)
    solution to maintain your device fleet includes recurring, variable
    costs such as infrastructure required to host and manage the DIY
    solution, labor costs to develop, maintain, and scale the DIY
    solution, and data transmission costs. Leveraging the transparent,
    fixed cost structure of AWS IoT Device Management Jobs, you know exactly what each job
    execution for a device will cost in addition to the data
    transmission costs required to facilitate the job document rollout
    to your device fleet and tracking the job execution status for each
    device. For more information, see [AWS IoT Core pricing](iot-price.md "iot-price.md").
