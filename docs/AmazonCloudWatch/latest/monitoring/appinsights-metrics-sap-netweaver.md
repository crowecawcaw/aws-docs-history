# SAP NetWeaver

CloudWatch Application Insights supports the following metrics:

| Metric                                  | Description                                                                                                                                         |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| sap_alerts_ResponseTime                 | The SAP response time alert from CCMS (RZ20)>R3Services>Dialog>ResponseTime.                                                                        |
| sap_alerts_ResponseTimeDialog           | The SAP response time dialog alert from CCMS (RZ20)>R3Services>Dialog> ResponseTimeDialog.                                                          |
| sap_alerts_ResponseTimeDialogRFC        | The SAP response time alert from CCMS (RZ20)>R3Services> Dialog>ResponseTimeDialogRFC.                                                              |
| sap_alerts_DBRequestTime                | The SAP response time alert from CCMS (RZ20)>R3Services>Dialog>DBRequestTime.                                                                       |
| sap_alerts_FrontendResponseTime         | The SAP response time alert from CCMS (RZ20)>R3Services > Dialog>FrontEndResponseTime.                                                              |
| sap_alerts_Database                     | The SAP system has logged database-related errors. Alert from SM21 or CCMS (RZ20)>R3Syslog>Database.                                                |
| sap_alerts_QueueTime                    | The SAP queue time alert from CCMS (RZ20)>R3Services>Dialog>QueueTime.                                                                              |
| sap_alerts_AbortedJobs                  | Failed background jobs in SAP system. Alert from (RZ20)>R3Services > Background>AbortedJobs.                                                        |
| sap_alerts_BasisSystem                  | SAP system logged system-level errors. Alert from SM21 or CCMS (RZ20)>R3Syslog>BasisSystem.                                                         |
| sap_alerts_Security                     | The SAP system logged security-related messages. Alert from SM21 or CCMS (RZ20)>R3Syslog>Security.                                                  |
| sap_alerts_System                       | The SAP system logged security or audit-related messages. Alert from SM21 or CCMS (RZ20)>Security>System.                                           |
| sap_alerts_LongRunners                  | There are long running programs in your SAP system. Alert from CCMS (RZ20)>R3Services > Dialog>LongRunners.                                         |
| sap_alerts_SqlError                     | There are SAP database client layer error logs. Alert from CCMS(RZ20)>DatabaseClient>AbapSql>SqlError.                                              |
| sap_alerts_State                        | State alert from CCMS (RZ20)>OS Collector>State.                                                                                                    |
| sap_alerts_Shortdumps                   | Shortdumps alert from ST22 and CCMS (RZ20)>R3Abap>Shortdumps.                                                                                       |
| sap_alerts_Availability                 | Availability alert for SAP application server instance from SM21, SM50, SM51, SM66, and CCMS (RZ20)>InstanceAsTask>Availability.                    |
| sap_dispatcher_queue_high               | The SAPControl Web Service function `GetQueueStatistic` provides the dispatcher queue high count.                                                   |
| sap_dispatcher_queue_max                | The SAPControl Web Service function `GetQueueStatistic` provides the dispatcher queue max count.                                                    |
| sap_dispatcher_queue_now                | The SAPControl Web Service function `GetQueueStatistic` provides the dispatcher queue now count.                                                    |
| sap_dispatcher_queue_reads              | The SAPControl Web Service function `GetQueueStatistic` provides the dispatcher queue reads count.                                                  |
| sap_dispatcher_queue_writes             | The SAPControl Web Service function `GetQueueStatistic` provides the dispatcher queue writes count.                                                 |
| sap_enqueue_server_arguments_high       | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue arguments high.                                                          |
| sap_enqueue_server_arguments_max        | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue arguments max.                                                           |
| sap_enqueue_server_arguments_now        | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue arguments now.                                                           |
| sap_enqueue_server_arguments_state      | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue arguments state.                                                         |
| sap_enqueue_server_backup_requests      | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue backup requests.                                                         |
| sap_enqueue_server_cleanup_requests     | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue cleanup requests.                                                        |
| sap_enqueue_server_dequeue_all_requests | The SAPControl Web Service function `EnqGetStatistic` provides the dequeue all requests.                                                            |
| sap_enqueue_server_dequeue_errors       | The SAPControl Web Service function `EnqGetStatistic` provides the dequeue errors.                                                                  |
| sap_enqueue_server_dequeue_requests     | The SAPControl Web Service function `EnqGetStatistic` provides the dequeue requests.                                                                |
| sap_enqueue_server_enqueue_errors       | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue errors.                                                                  |
| sap_enqueue_server_enqueue_rejects      | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue rejects.                                                                 |
| sap_enqueue_server_enqueue_requests     | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue requests.                                                                |
| sap_enqueue_server_lock_time            | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue lock time.                                                               |
| sap_enqueue_server_lock_wait_time       | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue lock wait time.                                                          |
| sap_enqueue_server_locks_high           | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue locks high.                                                              |
| sap_enqueue_server_locks_max            | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue locks max.                                                               |
| sap_enqueue_server_locks_now            | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue locks now.                                                               |
| sap_enqueue_server_locks_state          | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue locks state.                                                             |
| sap_enqueue_server_owner_high           | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue owner high.                                                              |
| sap_enqueue_server_owner_max            | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue owner max.                                                               |
| sap_enqueue_server_owner_now            | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue owner now.                                                               |
| sap_enqueue_server_owner_state          | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue owner state.                                                             |
| sap_enqueue_server_replication_state    | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue replication state status.                                                |
| sap_enqueue_server_reporting_requests   | The SAPControl Web Service function `EnqGetStatistic` provides the reqporting requests status.                                                      |
| sap_enqueue_server_server_time          | The SAPControl Web Service function `EnqGetStatistic` provides the enqueue server time.                                                             |
| sap_HA_check_failover_config_state      | The SAPControl Web Service function `HACheckFailoverConfig` provides the SAP High Availability status.                                              |
| sap_HA_get_failover_config_HAActive     | The SAPControl Web Service function `HAGetFailoverConfig` provides the SAP High Availability Cluster configuration and status.                      |
| sap_start_service_processes             | The SAPControl Web Service function `GetProcessList` provides the disp+work, IGS, gwrd, icman, message server, and enqueue server processes status. |
