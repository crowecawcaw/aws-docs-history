# Considerations and limitations

Note the following considerations and limitations when you use Lake Formation with Amazon EMR on EKS:

- Amazon EMR on EKS supports fine-grained access control via Lake Formation only for Apache Hive, Apache Iceberg, Apache Hudi, and Delta table Formats. Apache Hive
  formats include Parquet, ORC, and xSV.
- `DynamicResourceAllocation` is enabled by default, and you can't turn off `DynamicResourceAllocation` for Lake Formation jobs. As DRA `spark.dynamicAllocation.maxExecutors` configuration's
  default value is infinity, please configure an appropriate value based on your workload.
- Lake Formation-enabled jobs don’t support usage of customized EMR on EKS Images in System Driver and System Executors.
- You can only use Lake Formation with Spark jobs.
- EMR on EKS with Lake Formation only supports a single Spark session throughout a job.
- EMR on EKS with Lake Formation only supports cross-account table queries shared through
  resource links.
- The following aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Write with Lake Formation granted permissions
  - Access control for nested columns

- EMR on EKS blocks functionalities that might undermine the complete isolation of system driver, including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves custom classes
  - Custom data sources
  - Supply of additional jars for Spark extension, connector, or metastore `ANALYZE TABLE` command

- To enforce access controls, `EXPLAIN PLAN` and DDL operations such as `DESCRIBE TABLE` don't expose restricted
  information.
- Amazon EMR on EKS restricts access to system driver Spark logs on Lake Formation-enabled jobs. Since the system driver runs with more access, events and logs that the
  system driver generates can include sensitive information. To prevent unauthorized users or code from accessing this sensitive data, EMR on EKS disabled
  access to system driver logs. For troubleshooting, contact AWS support.
- If you registered a table location with Lake Formation, the data access path goes through the Lake Formation stored credentials, regardless of the IAM permission for the EMR on EKS job execution
  role. If you misconfigure the role registered with the table location, jobs submitted that use the role with S3 IAM permission to the table location will fail.
- Writing to a Lake Formation table uses IAM permission rather than Lake Formation granted permissions. If your job execution role has the necessary S3 permissions, you can use it to run
  write operations.
  The following are considerations and limitations when using Apache Iceberg:

- You can only use Apache Iceberg with session catalog and not arbitrarily named catalogs.
- Iceberg tables that are registered in Lake Formation only support the metadata tables `history`, `metadata_log_entries`, `snapshots`,
  `files`, `manifests`, and `refs`. Amazon EMR hides the columns that might have sensitive data, such as `partitions`, `path`, and `summaries`.
  This limitation doesn't apply to Iceberg tables that aren't registered in Lake Formation.
- Tables that you don't register in Lake Formation support all Iceberg stored procedures. The `register_table` and `migrate` procedures
  aren't supported for any tables.
- We recommend that you use Iceberg DataFrameWriterV2 instead of V1.
  For more information, see [Understanding Amazon EMR on EKS concepts and terminology](emr-eks-concepts.md "emr-eks-concepts.md")
  and [Enable cluster access for Amazon EMR on EKS](setting-up-cluster-access.md "setting-up-cluster-access.md").

## Disclaimer for data administrators

###### Note

When you grant access to Lake Formation resources to an IAM role for EMR on EKS, you must ensure the EMR cluster administrator or operator is a trusted administrator. This is
particularly relevant for Lake Formation resources that are shared across multiple organizations and AWS accounts.

## Responsibilities for EKS administrators

- The `System` namespace should be protected. No user or resource or entity or tooling would be allowed to have any Kubernetes RBAC permissions on the
  Kubernetes resources in the `System` namespace.
- No user or resource or entity except the EMR on EKS service should have access to `CREATE` access to POD, CONFIG_MAP and SECRET
  in the `User` namespace.
- `System` drivers and `System` executors contain sensitive data. So, Spark events, Spark driver logs, and Spark executor logs in the `System` namespace should not
  be forwarded to external log storage systems.
