AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Viewing your collected

data

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor
end of support](../../../dms/latest/userguide/dms_fleet.md "../../../dms/latest/userguide/dms_fleet.md").

You can view the data that your Application Discovery Service Agentless Collector
(Agentless Collector) collected in the Migration Hub console by following the steps
in [Viewing servers in the AWS Migration Hub console](view-servers.md "view-servers.md").

You can also view the collected metrics for database and analytics servers in the
AWS DMS console by taking the following steps.

###### To view the data discovered by the database and analytics data collection module

in the AWS DMS console

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Inventory** under **Discover**. The
   **Inventory** page opens.
3. Choose **Analyze inventories** to determine database schema
   properties, such as similarity and complexity.
4. Choose the **Schemas** tab to see the results of
   analysis.
   You can use the AWS DMS console to identify duplicate schemas, determine the migration
   complexity, and export the inventory information for the future analysis. For more
   information, see [Using inventories for analysis in AWS DMS
   Fleet Advisor](../../../dms/latest/userguide/fa-inventory.md "../../../dms/latest/userguide/fa-inventory.md").
