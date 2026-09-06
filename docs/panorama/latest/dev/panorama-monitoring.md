

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html). 

# Monitoring AWS Panorama resources and applications
<a name="panorama-monitoring"></a>

You can monitor AWS Panorama resources in the AWS Panorama console and with Amazon CloudWatch. The AWS Panorama Appliance connects to the AWS Cloud over the internet to report its status and the status of connected cameras. While it is on, the appliance also sends logs to CloudWatch Logs in real time.

The appliance gets permission to use AWS IoT, CloudWatch Logs, and other AWS services from a service role that you create the first time that you use the AWS Panorama console. For more information, see [AWS Panorama service roles and cross-service resources](permissions-services.md).

For help troubleshooting specific errors, see [Troubleshooting](panorama-troubleshooting.md).

**Topics**
+ [Monitoring in the AWS Panorama console](monitoring-console.md)
+ [Viewing AWS Panorama logs](monitoring-logging.md)
+ [Monitoring appliances and applications with Amazon CloudWatch](monitoring-metrics.md)