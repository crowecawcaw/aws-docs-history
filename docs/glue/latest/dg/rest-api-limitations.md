

# Limitations
<a name="rest-api-limitations"></a>

The following are limitations for the REST API connector
+  REST API connector is only available through the AWS API, CLI, or SDK. You cannot configure REST connectors through the console. 
+  The AWS Glue REST ConnectionType can only be configured to READ data from the REST API-based data source. The connection can only be used as a SOURCE in AWS Glue ETL jobs. 
+  The connector does not support field selection. 
+  The connector does not support JSON POST body filtering. Use query parameter or filter string modes instead. 
+  The filter configuration model cannot express complex native query languages that require entity-dependent branching. 
+  The connector does not support custom partition logic (such as primary key partitioning) through configuration. 
+  The connector does not support custom proxies or custom certificates for VPC REST connections. 