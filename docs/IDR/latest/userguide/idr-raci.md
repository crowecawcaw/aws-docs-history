# Roles and responsibilities in Incident Detection and Response

The AWS Incident Detection and Response RACI (Responsible, Accountable, Consulted, and
Informed) table outlines the roles and responsibilities for various activities related to
incident detection and response. This table helps define the involvement of the customer and the
AWS Incident Detection and Response team for tasks such as data collection, operations readiness
review, account configuration, incident management, and post-incident review.

| **Activity**                                                             | **Customer** | **Incident Detection and Response** |
| ------------------------------------------------------------------------ | ------------ | ----------------------------------- |
| **Data collection**                                                      |
| Customer and workload introduction                                       | Consulted    | Responsible                         |
| Architecture                                                             | Responsible  | Accountable                         |
| Operations                                                               | Responsible  | Accountable                         |
| Determine CloudWatch alarms to be configured                             | Responsible  | Accountable                         |
| Define incident response plan                                            | Responsible  | Accountable                         |
| Completing onboarding questionnaire                                      | Responsible  | Accountable                         |
| **Operations readiness review**                                          |
| Conduct well architected review (WAR) on workload                        | Consulted    | Responsible                         |
| Validate incident response                                               | Consulted    | Responsible                         |
| Validate alarm matrix                                                    | Consulted    | Responsible                         |
| Identify key AWS services being used by the workload                     | Accountable  | Responsible                         |
| **Account configuration**                                                |
| Create IAM role in customer account                                      | Responsible  | Informed                            |
| Install managed EventBridge rule using created role                      | Informed     | Responsible                         |
| Test CloudWatch alarms                                                   | Responsible  | Accountable                         |
| Verify that customer alarms engage the incident detection and response   | Informed     | Responsible                         |
| Update alarms                                                            | Responsible  | Consulted                           |
| Update runbooks                                                          | Consulted    | Responsible                         |
| **Incident management**                                                  |
| Proactively notify Incidents detected by Incident Detection and Response | Informed     | Responsible                         |
| Provide incident response                                                | Informed     | Responsible                         |
| Provide incident resolution / infrastructure restore                     | Responsible  | Consulted                           |
| **Post-incident review**                                                 |
| Request post-incident review                                             | Responsible  | Informed                            |
| Provide post-incident review                                             | Informed     | Responsible                         |
