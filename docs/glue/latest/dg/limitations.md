

# Limitations
<a name="limitations"></a>

## Partitioning limitations
<a name="partitioning-limitations"></a>
+  Partition specifications cannot be changed after an integration is created. To use a different partitioning strategy, you must create a new integration. 
+  The maximum number of partition columns is limited to 10. 

## Cross-account integration limitations
<a name="cross-account-limitations"></a>
+  When creating cross-account integrations, AWS Glue Console has a limitation where it doesn't invoke CreateIntegrationTableProperty API for configuring UnnestSpec and PartitionSpec for target AWS Glue tables that are hosted in the account where integration does not exist. 

   **Workaround:** The CreateIntegrationTableProperty API must be invoked by CX from the account where the target database exists. 

## Multiple integrations limitations
<a name="multiple-integrations-limitations"></a>
+  If you need to replicate the same source with different schema unnest/partition configurations, it is required to create a new AWS Glue database for each integration separately. Later invoke CreateIntegrationTableProperty for each table from individual AWS Glue Database with desired schema unnesting and partitioning configurations. 