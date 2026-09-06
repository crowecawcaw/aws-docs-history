

# Amazon EMR service ports
<a name="emr-service-ports"></a>

**Note**  
The following are interfaces and service ports for components on Amazon EMR. This is not a complete list of service ports. Non-default services, such as SSL ports and different types of protocols, are not listed.

**Important**  
Use caution when you edit security group rules to open ports. Be sure to add rules that only allow traffic from trusted and authenticated clients for the protocols and ports that are required to run your workloads.



- **Hadoop**
  - **Service description:** HTTP KMS REST API
  - **Service running by default:** Yes
  - **Port:** 9600
  - **Configuration key:** hadoop.kms.http.port

- **HDFS**
  - **Service description:** Namenode Web UI / **Service running by default:** Yes / **Port:** 9870 / **Configuration key:** dfs.namenode.http-address
  - **Service description:** Namenode RPC / **Service running by default:** Yes / **Port:** 8020 / **Configuration key:** dfs.namenode.rpc-address
  - **Service description:** DataNode Web UI / **Service running by default:** Yes / **Port:** 9864 / **Configuration key:** dfs.datanode.http.address
  - **Service description:** Datanode HTTP for data transfer / **Service running by default:** Yes / **Port:** 9866 / **Configuration key:** dfs.datanode.address
  - **Service description:** Datanode RPC for data transfer / **Service running by default:** Yes / **Port:** 9867 / **Configuration key:** dfs.datanode.ipc.address

- **Hive**
  - **Service description:** HiveServer2 Thrift / **Service running by default:** Yes / **Port:** 10000 / **Configuration key:** hive.server2.thrift.port
  - **Service description:** HiveServer2 HTTP / **Service running by default:** No / **Port:** 10001 / **Configuration key:** hive.server2.thrift.http.port
  - **Service description:** HiveServer2 Web UI / **Service running by default:** Yes / **Port:** 10002 / **Configuration key:** hive.server2.webui.port
  - **Service description:** Hive Metastore / **Service running by default:** Yes / **Port:** 9083 / **Configuration key:** hive.metastore.port / metastore.thrift.port
  - **Service description:** WebHCat / **Service running by default:** No / **Port:** 50111 / **Configuration key:** templeton.port
  - **Service description:** LLAP daemon management service (RPC) / **Service running by default:** No / **Port:** 15004 / **Configuration key:** hive.llap.management.rpc.port
  - **Service description:** YARN shuffle port for LLAP-daemon-hosted shuffle / **Service running by default:** No / **Port:** 15551 / **Configuration key:** hive.llap.daemon.yarn.shuffle.port
  - **Service description:** The LLAP daemon RPC / **Service running by default:** No / **Port:** Dynamic / **Configuration key:** hive.llap.daemon.rpc.port
  - **Service description:** LLAP daemon Web UI / **Service running by default:** No / **Port:** 15002 / **Configuration key:** hive.llap.daemon.web.port
  - **Service description:** LLAP daemon output service / **Service running by default:** No / **Port:** 15003 / **Configuration key:** hive.llap.daemon.output.service.port

- **Oozie**
  - **Service description:** 
  - **Service running by default:** Yes
  - **Port:** 11000
  - **Configuration key:** 

- **Presto (PrestoDB and Trino)**
  - **Service description:** Coordinator Web UI
  - **Service running by default:** Yes
  - **Port:** 8889
  - **Configuration key:** http-server.http.port

- **Tez**
  - **Service description:** Tez UI
  - **Service running by default:** Yes
  - **Port:** 8080
  - **Configuration key:** 

- **YARN**
  - **Service description:** Shuffle / **Service running by default:** Yes / **Port:** 13562 / **Configuration key:** mapreduce.shuffle.port
  - **Service description:** Localizer RPC / **Service running by default:** Yes / **Port:** 8040 / **Configuration key:** yarn.nodemanager.localizer.address
  - **Service description:**  / **Service running by default:** Yes / **Port:** 8041 / **Configuration key:** 
  - **Service description:** NM Webapp address / **Service running by default:** Yes / **Port:** 8042 / **Configuration key:** yarn.nodemanager.webapp.address
  - **Service description:** RM web application / **Service running by default:** Yes / **Port:** 8088 / **Configuration key:** yarn.resourcemanager.webapp.address
  - **Service description:**  / **Service running by default:** Yes / **Port:** 8025 / **Configuration key:** 
  - **Service description:** Scheduler / **Service running by default:** Yes / **Port:** 8030 / **Configuration key:** yarn.resourcemanager.scheduler.address
  - **Service description:** applications manager interface / **Service running by default:** Yes / **Port:** 8032 / **Configuration key:** yarn.resourcemanager.address
  - **Service description:** RM admin interface / **Service running by default:** Yes / **Port:** 8033 / **Configuration key:** yarn.resourcemanager.admin.address
  - **Service description:** JobHistory Server Web UI / **Service running by default:** Yes / **Port:** 19888 / **Configuration key:** mapreduce.jobhistory.webapp.address
  - **Service description:** JobHistory Server Admin Web UI / **Service running by default:** Yes / **Port:** 10033 / **Configuration key:** mapreduce.jobhistory.admin.address
  - **Service description:** JobHistory Server (RPC) / **Service running by default:** Yes / **Port:** 10020 / **Configuration key:** mapreduce.jobhistory.address
  - **Service description:** Application Timeline Server (RPC) / **Service running by default:** Yes / **Port:** 10200 / **Configuration key:** yarn.timeline-service.address
  - **Service description:** Application Timeline Server HTTP Web UI / **Service running by default:** Yes / **Port:** 8188 / **Configuration key:** yarn.timeline-service.webapp.address
  - **Service description:** Application Timeline Server HTTPS Web UI / **Service running by default:** No / **Port:** 8190 / **Configuration key:** yarn.timeline-service.webapp.https.address
  - **Service description:**  / **Service running by default:** Yes / **Port:** 20888 / **Configuration key:** 

- **Zookeeper**
  - **Service description:** Client port / **Service running by default:** Yes / **Port:** 2181 / **Configuration key:** 
  - **Service description:**  / **Service running by default:** Yes / **Port:** 37301 / **Configuration key:** 
  - **Service description:**  / **Service running by default:** Yes / **Port:** 8341 / **Configuration key:** 

