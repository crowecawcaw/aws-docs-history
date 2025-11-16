AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Shipping considerations for Snowball Edge

When you create a job to order a Snowball Edge device, you provide a shipping address and choose shipping speed. Note that the
shipping speed doesn’t indicate how soon you can expect to receive the device from
the day you created the job. Rather, it indicates the time that the device is in transit
between AWS and your shipping address.

It may take up to 4 weeks to provision and prepare the device for your job before it is shipped. This timeline should be factored into your project plan to ensure a seamless transition. While AWS is preparing your device to ship, you can monitor the status of your job through the AWS Snow Family Management Console. For more information, see [Statuses of Snowball Edge jobs](jobstatuses.md "jobstatuses.md").

###### Note

The shipping speed that you choose applies when AWS sends the device to you and when
you return the device to AWS.

Snowball Edge devices can only be used to import or export data
within the AWS Region where the devices are ordered.

For more information on choosing shipping speed and entering your shipping address when creating a job to order a Snowball Edge device, see [Choosing security, shipping, and
notification preferences](create-job-common.md#security-shipping-notification "create-job-common.md#security-shipping-notification"). For more information about returning a Snowball Edge device to AWS, see [Returning the Snowball Edge device](return-device.md "return-device.md").

For information about shipping charges, see [AWS Snowball Edge Pricing](http://aws.amazon.com/snowball-edge/pricing "http://aws.amazon.com/snowball-edge/pricing").

## Region-based shipping restrictions for Snowball Edge

Before you create a job to order a Snowball Edge device, you should sign in to the console from the same AWS Region as your Amazon S3 data. AWS does not ship Snowball Edge between countries within the same AWS Region—for example, from Asia
Pacific (India) to Asia Pacific (Australia).

An exception to shipping between countries is among European Union (EU) member countries.
For data transfers in the European AWS Regions, we only ship devices to the EU member
countries listed:

Austria, Belgium, Bulgaria, Croatia, Republic of Cyprus, Czech Republic, Denmark,
Estonia, Finland, France, Germany, Greece, Hungary, Italy, Ireland, Latvia, Lithuania,
Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain and
Sweden.

Snowball Edge can only be returned to the same AWS Region where the devices were ordered.

Shipments domestically within the same country are permitted. Examples:

- For data transfers in the United Kingdom Region, we ship devices domestically within the UK.
- For data transfers in Asia Pacific (Mumbai), we ship devices within India.

###### Note

AWS doesn't ship Snowball Edge to post office boxes.
