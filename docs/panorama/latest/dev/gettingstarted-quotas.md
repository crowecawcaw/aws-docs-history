End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Service quotas

AWS Panorama applies quotas to the resources that you create in your account and the applications that you deploy.
If you use AWS Panorama in multiple AWS Regions, quotas apply separately to each Region. AWS Panorama quotas are not
adjustable.

Resources in AWS Panorama include devices, application node packages, and application instances.

######

- **Devices** – Up to 50 registered appliances per Region.
- **Node packages** – 50 packages per Region, with up to 20 versions per
  package.
- **Application instances** – Up to 10 applications per device. Each
  application can monitor up to 8 camera streams. Deployments are limited to 200 per day for each device.
  When you use the AWS Panorama Application CLI, AWS Command Line Interface, or AWS SDK with the AWS Panorama service, quotas apply to the number of API
  calls that you make. You can make up to 5 requests total per second. A subset of API operations that create or
  modify resources apply an additional limit of 1 request per second.

For a complete list of quotas, visit the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/panorama/quotas "https://console.aws.amazon.com/servicequotas/home/services/panorama/quotas"), or see [AWS Panorama endpoints and quotas](../../../general/latest/gr/panorama.md "../../../general/latest/gr/panorama.md") in the Amazon Web Services General Reference.
