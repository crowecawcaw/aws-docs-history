# Amazon EMR service ports

###### Note

The following are interfaces and service ports for components on Amazon EMR. This
is not a complete list of service ports. Non-default services, such as SSL ports
and different types of protocols, are not listed.

###### Important

Use caution when you edit security group rules to open ports. Be sure to add
rules that only allow traffic from trusted and authenticated clients for the
protocols and ports that are required to run your workloads.

| Component                               | Service description | Service running by default | Port                                        | Configuration key         |
| --------------------------------------- | ------------------- | -------------------------- | ------------------------------------------- | ------------------------- | ------------------------------------------------ | --- | ----- | ------------------------------------------ |
| Hadoop                                  | HTTP KMS REST API   | Yes                        | 9600                                        | hadoop.kms.http.port      |
| HDFS                                    | Namenode Web UI     | Yes                        | 9870                                        | dfs.namenode.http-address |
| Namenode RPC                            | Yes                 | 8020                       | dfs.namenode.rpc-address                    |                           | DataNode Web UI                                  | Yes | 9864  | dfs.datanode.http.address                  |
| Datanode HTTP for data transfer         | Yes                 | 9866                       | dfs.datanode.address                        |                           | Datanode RPC for data transfer                   | Yes | 9867  | dfs.datanode.ipc.address                   |
| Hive                                    | HiveServer2 Thrift  | Yes                        | 10000                                       | hive.server2.thrift.port  |
| HiveServer2 HTTP                        | No                  | 10001                      | hive.server2.thrift.http.port               |                           | HiveServer2 Web UI                               | Yes | 10002 | hive.server2.webui.port                    |
| Hive Metastore                          | Yes                 | 9083                       | hive.metastore.port / metastore.thrift.port |                           | WebHCat                                          | No  | 50111 | templeton.port                             |
| LLAP daemon management service (RPC)    | No                  | 15004                      | hive.llap.management.rpc.port               |                           | YARN shuffle port for LLAP-daemon-hosted shuffle | No  | 15551 | hive.llap.daemon.yarn.shuffle.port         |
| The LLAP daemon RPC                     | No                  | Dynamic                    | hive.llap.daemon.rpc.port                   |                           | LLAP daemon Web UI                               | No  | 15002 | hive.llap.daemon.web.port                  |
| LLAP daemon output service              | No                  | 15003                      | hive.llap.daemon.output.service.port        |
| Oozie                                   |                     | Yes                        | 11000                                       |                           |
| Tez                                     | Tez UI              | Yes                        | 8080                                        |                           |
| YARN                                    | Shuffle             | Yes                        | 13562                                       | mapreduce.shuffle.port    |
| Localizer RPC                           | Yes                 | 8040                       | yarn.nodemanager.localizer.address          |                           |                                                  | Yes | 8041  |                                            |
| NM Webapp address                       | Yes                 | 8042                       | yarn.nodemanager.webapp.address             |                           | RM web application                               | Yes | 8088  | yarn.resourcemanager.webapp.address        |
|                                         | Yes                 | 8025                       |                                             |                           | Scheduler                                        | Yes | 8030  | yarn.resourcemanager.scheduler.address     |
| applications manager interface          | Yes                 | 8032                       | yarn.resourcemanager.address                |                           | RM admin interface                               | Yes | 8033  | yarn.resourcemanager.admin.address         |
| JobHistory Server Web UI                | Yes                 | 19888                      | mapreduce.jobhistory.webapp.address         |                           | JobHistory Server Admin Web UI                   | Yes | 10033 | mapreduce.jobhistory.admin.address         |
| JobHistory Server (RPC)                 | Yes                 | 10020                      | mapreduce.jobhistory.address                |                           | Application Timeline Server (RPC)                | Yes | 10200 | yarn.timeline-service.address              |
| Application Timeline Server HTTP Web UI | Yes                 | 8188                       | yarn.timeline-service.webapp.address        |                           | Application Timeline Server HTTPS Web UI         | No  | 8190  | yarn.timeline-service.webapp.https.address |
|                                         | Yes                 | 20888                      |                                             |
| Zookeeper                               | Client port         | Yes                        | 2181                                        |                           |
|                                         | Yes                 | 37301                      |                                             |                           |                                                  | Yes | 8341  |                                            |
