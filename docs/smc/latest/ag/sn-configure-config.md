

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# AWS Config in ServiceNow
<a name="sn-configure-config"></a>

This section shows you how to use AWS Config to integrate to ServiceNow.

To allow the Connector to synchronize Config data for a given Region, you must enable AWS Config in that Region. For more information, see [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html).

AWS Service Management Connector for ServiceNow enables ServiceNow administrators to specify select ServiceNow tables as custom resources within AWS Config.

To set up these resources, use the preconfigured files in the Connector. These required files include the custom resource schema. 

**Topics**
+ [Configuring system properties, aggregators, and custom resources](sn-configuration-integ.md)
+ [Validating AWS Config integration in ServiceNow](sn-validate-config.md)
+ [Updating the AWS Load Balancer resource details in the ServiceNow CMDB](update-balancer.md)