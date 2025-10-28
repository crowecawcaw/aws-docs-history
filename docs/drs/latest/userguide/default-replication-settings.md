# AWS DRS default replication

**Default replication** settings are created during the
DRS Service Initialization within a Region.
[Learn more about configuring your Default replication
settings](getting-started-initializing.md "getting-started-initializing.md"). The options configured within the **Default replication** automatically apply to any
newly added Source Server. Any changes made to the **Default replication**
only apply to any Source Server added after the changes were made, they do not automatically update the corresponding
settings on existing Source Servers.

Most Replication Settings can be configured through the Default replication settings:

| Replication setting                                     | Default replication |
| ------------------------------------------------------- | ------------------- |
| Staging area subnet                                     | Supported           |
| Replication server instance type                        | Supported           |
| EBS volume type                                         | Supported           |
| EBS encryption                                          | Supported           |
| Automatically replicate new disks                       | Supported           |
| Always use AWS Elastic Disaster Recovery security group | Supported           |
| Security Group                                          | Supported           |
| Dedicated instance for replication server               | Unsupported         |
| Data Routing (Private IP)                               | Supported           |
| Create public IP                                        | Supported           |
| Network Bandwidth Throttling                            | Supported           |
| Point in time (PIT) policy                              | Supported           |
| MAP program tagging                                     | Supported           |
| Tags                                                    | Supported           |
