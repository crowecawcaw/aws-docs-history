# EDI Cloud Operations roles and responsibilities

The ECO responsible, accountable, consulted, and informed, or RACI, matrix assigns primary responsibility either to you or ECO for
a variety of activities.

Each letter in RACI represents a different party that's involved in the matrix:

- **R** is the responsible party that does the work to achieve the task.
- **A** is the accountable party that gets the work done to complete the task.
- **C** is the consulted party whose opinions are sought, typically as subject matter experts (SMEs); and with whom there's
  bilateral communication.
- **I** is the informed party who's notified about the progress of a task, usually only on task completion.
  ECO manages your EDI on AWS environment. The following table provides an overview of the activities in the lifecycle of an EDI application that runs within
  the managed environment. The "Customer" column represents your roles and responsibilities, and the "AWS" column represents the roles and responsibilities of ECO.

| **Activity**                                                                                                                                                      | **Customer** | **AWS** |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------- |
| **Provisioning**                                                                                                                                                  |
| EDI solution (Operations, Data Platform, and EDI IQ) deployment in the customer's account                                                                         | C, I         | R, A    |
| EDI Data Portal initial admin user creation                                                                                                                       | C, I         | R, A    |
| EDI Data Portal user creation and management                                                                                                                      | R, A         | C       |
| EDI hosted zone creation and management for Data Portal                                                                                                           | R            | I       |
| **Monitoring and Logging**                                                                                                                                        |
| EDI solution monitoring                                                                                                                                           | I            | R, A    |
| AWS infrastructure monitoring                                                                                                                                     | C, I         | R, A    |
| Recording AWS infrastructure change logs                                                                                                                          | I            | R, A    |
| Deploying and managing third-party monitoring tools, such as Dynatrace and New Relic                                                                              | R, A         | C       |
| **Data load and ingestion**                                                                                                                                       |
| Data ingestion and reingestion from the application, the EDI IQ and custom sources—such as CSV, WITSML, Manifest, and Code Pipeline—<br>into the EDI cluster      | R, A         | C       |
| Missing or incorrect data validation and indexing issues                                                                                                          | R            | C       |
| **Disaster recovery**                                                                                                                                             |
| Performing point-in-time backup restoration activities through AWS managed services, such as Amazon Relational Database Service (Amazon RDS), and Amazon DynamoDB | C            | R, A    |
| Backup and restore for EDI entitlement through Amazon OpenSearch Service                                                                                          | C            | R, A    |
| Deploying and reviewing backup plans                                                                                                                              | C            | R, A    |
| Deploying and managing third-party backup tools, such as Commvault                                                                                                | R, A         | C       |
| **Migration**                                                                                                                                                     |
| Migrating data from the existing OSDU® to the EDI environment                                                                                                     | R, A         | C       |
| Data snapshot backup and restore through AWS Disaster Recovery                                                                                                    | R, A         | C       |
| **Upgrades and patching**                                                                                                                                         |
| Upgrading the EDI environment                                                                                                                                     | I            | R       |
| Patching the EDI environment and AWS infrastructure for hotfixes or security vulnerabilities                                                                      | I            | R       |
| Notification for EDI end of life support                                                                                                                          | I            | R       |
| Approval for EDI environment upgrade                                                                                                                              | R            | I       |
| **Incident management**                                                                                                                                           |
| Proactively notifying incidents on the EDI environment and AWS infrastructure that are based on monitoring                                                        | I            | R       |
| Categorizing incident priority                                                                                                                                    | I            | R       |
| Providing incident response                                                                                                                                       | I            | R       |
| Providing incident resolution and infrastructure restore                                                                                                          | C, I         | R       |
| **Documentation and training**                                                                                                                                    |
| Providing customer documentation about the EDI architecture and EDI on AWS operations                                                                             | I            | R       |
| Leading and conducting incident response processes through game days with the customer                                                                            | C, I         | R, A    |
| Participating in incident response processes through game days                                                                                                    | R            | A, C    |
| **Troubleshooting**                                                                                                                                               |
| EDI deployment issues                                                                                                                                             | I            | R       |
| API endpoint connection failures                                                                                                                                  | I            | R       |
| Data ingestion failures                                                                                                                                           | R            | C       |
| EDI environment functionality issues and outages                                                                                                                  | C            | R       |
