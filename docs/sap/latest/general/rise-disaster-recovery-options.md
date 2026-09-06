

# Disaster recovery options
<a name="rise-disaster-recovery-options"></a>

You can implement a disaster recovery solution by replicating data into a second AWS Region. Your SAP workloads are protected in the event of rare occurrence of local or regional failures.

RISE with SAP S/4HANA Cloud, private edition offers the following two options.
+  **Short distance disaster recovery** or Metro disaster recovery – RISE with SAP uses multiple Availability Zones in an AWS Region. Unique AWS region with three or more Availability Zones provide the option of short distance disaster recovery in every AWS regions.
+  **Long distance disaster recovery** or Regional disaster recovery – RISE with SAP uses a secondary AWS Region as standby for failover systems. Owing to the physical distance between two AWS Regions, data is replicated asynchronously between two AWS Regions.

For more details, see SAP documentation [SAP Service Description: Disaster Recovery and Customer Invoked Failover](https://assets.cdn.sap.com/agreements/product-policy/hec/service-description/sap-service-description-disaster-recovery-and-customer-invoked-failover-english-v7-2022.pdf).