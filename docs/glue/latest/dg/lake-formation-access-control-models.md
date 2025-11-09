# AWS Lake Formation access control models

AWS Glue 5.0 supports two models for accessing data through AWS Lake Formation:

###### Topics

- [Using AWS Glue with AWS Lake Formation for Full Table Access](security-access-control-fta.md "security-access-control-fta.md")
- [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md "security-lf-enable.md")
  The following table describes summary of how to choose between Fine-grained access control (FGAC) and Full table access (FTA) for your workload.

| Feature            | Fine-grained access control (FGAC)                                                      | Full table access (FTA) |
| ------------------ | --------------------------------------------------------------------------------------- | ----------------------- |
| Access Level       | Column/row level                                                                        | Full table              |
| Use Case           | Queries and ETL with limited permissions                                                | ETL                     |
| Performance Impact | Requires system/user space transitions for access control<br>evaluation, adding latency | Optimized performance   |
