# AWS Config in ServiceNow

This section shows you how to use AWS Config to integrate to ServiceNow.

To allow the Connector to synchronize Config data for a given Region, you must
enable AWS Config in that Region. For more information, see [Setting Up AWS Config with the Console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md").

AWS Service Management Connector for ServiceNow enables ServiceNow administrators
to specify select ServiceNow tables as custom resources within AWS Config.

To set up these resources, use the preconfigured files in the Connector. These
required files include the custom resource schema.

###### Topics

- [Configuring system properties, aggregators, and custom resources](sn-configuration-integ.md "sn-configuration-integ.md")
- [Validating AWS Config integration in
  ServiceNow](sn-validate-config.md "sn-validate-config.md")
- [Updating the AWS Load Balancer resource
  details in the ServiceNow CMDB](update-balancer.md "update-balancer.md")
