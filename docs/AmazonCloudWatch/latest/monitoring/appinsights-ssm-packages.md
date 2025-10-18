# AWS Systems Manager (SSM) packages used by
 CloudWatch Application Insights

The packages listed in this section are used by Application Insights, and can be
 independently managed and deployed with AWS Systems Manager Distributor. For more
 information about SSM Distributor, see [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") in the *AWS Systems Manager User Guide*.

###### Packages:

* [AWSObservabilityExporter-JMXExporterInstallAndConfigure](#configure-java "#configure-java")
* [AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure](#appinsights-ssm-sap-prometheus "#appinsights-ssm-sap-prometheus")
* [AWSObservabilityExporter-HAClusterExporterInstallAndConfigure](#appinsights-ssm-sap-prometheus-ha "#appinsights-ssm-sap-prometheus-ha")
* [AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure](#appinsights-ssm-sap-host-exporter "#appinsights-ssm-sap-host-exporter")
* [AWSObservabilityExporter-SQLExporterInstallAndConfigure](#appinsights-ssm-sql-prometheus "#appinsights-ssm-sql-prometheus")

## `AWSObservabilityExporter-JMXExporterInstallAndConfigure`


You can retrieve workload-specific Java metrics from [Prometheus JMX exporter](https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters "https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters") for Application Insights to configure and monitor
 alarms. In the Application Insights console, on the **Manage
 monitoring** page, select **JAVA application**
 from the **Application tier** dropdown. Then under
 **JAVA Prometheus exporter configuration**, select your
 **Collection method** and **JMX port
 number**. 


To use [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") to package, install, and configure the AWS-provided
 Prometheus JMX exporter package independently of Application Insights, complete the
 following steps.



###### Prerequisites for using the Prometheus JMX exporter SSM package


* SSM agent version 2.3.1550.0 or later installed
* The JAVA\_HOME environment variable is set

###### Install and configure the
 `AWSObservabilityExporter-JMXExporterInstallAndConfigure`
 package


The `AWSObservabilityExporter-JMXExporterInstallAndConfigure`
 package is an SSM Distributor package that you can use to install and
 configure [Prometheus
 JMX Exporter](https://github.com/prometheus/jmx_exporter "https://github.com/prometheus/jmx_exporter"). When Java metrics are sent by the Prometheus JMX
 exporter, the CloudWatch agent can be configured to retrieve the metrics for the
 CloudWatch service.



1. Based on your preferences, prepare the [Prometheus JMX exporter YAML configuration file](https://github.com/prometheus/jmx_exporter#configuration "https://github.com/prometheus/jmx_exporter#configuration") located in
 the Prometheus GitHub repository. Use the example configuration and
 option descriptions to guide you.
2. Copy the Prometheus JMX exporter YAML configuration file encoded as
 Base64 to a new SSM parameter in [SSM Parameter
 Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters").
3. Navigate to the [SSM Distributor](https://console.aws.amazon.com/systems-manager/distributor "https://console.aws.amazon.com/systems-manager/distributor") console
 and open the **Owned by Amazon** tab. Select
 **AWSObservabilityExporter-JMXExporterInstallAndConfigure**
 and choose **Install one time**.
4. Update the SSM parameter you created in the first step by replacing
 "Additional Arguments" with the following:



```
{
  "SSM_EXPORTER_CONFIGURATION": "{{ssm:`<SSM_PARAMETER_STORE_NAME>`}}",
  "SSM_EXPOSITION_PORT": "9404"
}
```

###### Note

Port 9404 is the default port used to send Prometheus JMX metrics.
 You can update this port.

###### Example: Configure CloudWatch agent to retrieve Java metrics

1. Install the Prometheus JMX exporter, as described in the previous
 procedure. Then verify that it is correctly installed on your instance
 by checking the port status.


Successful installation on Windows instance example



```
PS C:\> curl http://localhost:9404 (http://localhost:9404/)
StatusCode : 200
StatusDescription : OK
Content : # HELP jvm_info JVM version info
```

Successful installation on Linux instance example



```
$ curl localhost:9404
# HELP jmx_config_reload_failure_total Number of times configuration have failed to be reloaded.
# TYPE jmx_config_reload_failure_total counter
jmx_config_reload_failure_total 0.0
```
2. Create the Prometheus service discovery YAML file. The following
 example service discovery file performs the following:




	* Specifies the Prometheus JMX exporter host port as
	 `localhost: 9404`.
	* Attaches labels (`Application`,
	 `ComponentName`, and `InstanceId`) to
	 the metrics, which can be set as CloudWatch metric dimensions.

```
$ cat prometheus_sd_jmx.yaml 
- targets:
  - 127.0.0.1:9404
  labels:
    Application: `myApp`
    ComponentName: arn:aws:elasticloadbalancing:`us-east-1:123456789012`:loadbalancer/app/sampl-Appli-MMZW8E3GH4H2/aac36d7fea2a6e5b
    InstanceId: `i-12345678901234567`
```
3. Create the Prometheus JMX exporter configuration YAML file. The
 following example configuration file specifies the following:




	* The metrics retrieval job interval and timeout period.
	* The metrics retrieval jobs (`jmx` and
	 `sap`), also known as scraping, which include the
	 job name, maximum time series returned at a time, and service
	 discovery file path.

```
$ cat prometheus.yaml 
global:
  scrape_interval: 1m
  scrape_timeout: 10s
scrape_configs:
  - job_name: jmx
    sample_limit: 10000
    file_sd_configs:
      - files: ["/tmp/prometheus_sd_jmx.yaml"]
  - job_name: sap
    sample_limit: 10000
    file_sd_configs:
      - files: ["/tmp/prometheus_sd_sap.yaml"]
```
4. Verify that the CloudWatch agent is installed on your Amazon EC2 instance and
 that the version is 1.247346.1b249759 or later. To install the CloudWatch
 agent on your EC2 instance, see [Installing the CloudWatch Agent](install-CloudWatch-Agent-on-EC2-Instance.md "install-CloudWatch-Agent-on-EC2-Instance.md"). To verify the version, see
 [Finding information about CloudWatch agent versions](troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-agent-version "troubleshooting-CloudWatch-Agent.md#CloudWatch-Agent-troubleshooting-agent-version").
5. Configure the CloudWatch agent. For more information about how to configure
 the CloudWatch agent configuration file, see [Manually create or edit the CloudWatch agent configuration
 file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md"). The following example CloudWatch agent configuration file
 performs the following:




	* Specifies the Prometheus JMX exporter configuration file
	 path.
	* Specifies the target log group to which to publish EMF metric
	 logs.
	* Specifies two sets of dimensions for each metric name.
	* Sends 8 (4 metric names \* 2 sets of dimensions per metric
	 name) CloudWatch metrics.

```
{
   "logs":{
      "logs_collected":{
         ....
      },
      "metrics_collected":{
         "prometheus":{
            "cluster_name":"prometheus-test-cluster",
            "log_group_name":"prometheus-test",
            "prometheus_config_path":"/tmp/prometheus.yaml",
            "emf_processor":{
               "metric_declaration_dedup":true,
               "metric_namespace":"CWAgent",
               "metric_unit":{
                  "jvm_threads_current":"Count",
                  "jvm_gc_collection_seconds_sum":"Second",
                  "jvm_memory_bytes_used":"Bytes"
               },
               "metric_declaration":[
                  {
                     "source_labels":[
                        "job"
                     ],
                     "label_matcher":"^jmx$",
                     "dimensions":[
                        [
                           "InstanceId",
                           "ComponentName"
                        ],
                        [
                           "ComponentName"
                        ]
                     ],
                     "metric_selectors":[
                        "^java_lang_threading_threadcount$",
                        "^java_lang_memory_heapmemoryusage_used$",
                        "^java_lang_memory_heapmemoryusage_committed$"
                     ]
                  }
               ]
            }
         }
      }
   },
   "metrics":{
      ....
   }
}
```

## `AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure`


You can retrieve workload-specific SAP HANA metrics from [Prometheus HANA database exporter](https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters "https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters") for Application Insights to configure and
 monitor alarms. For more information, see [Set up your SAP HANA database
 for monitoring](appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up "appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up") in this guide.


To use [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") to package, install, and configure the AWS-provided
 Prometheus HANA database exporter package independently of Application Insights, complete
 the following steps.



###### Prerequisites for using the Prometheus HANA database exporter SSM
 package


* SSM agent version 2.3.1550.0 or later installed
* SAP HANA database
* Linux operating system (SUSE Linux, RedHat Linux)
* A secret with SAP HANA database monitoring credentials, using
 AWS Secrets Manager. Create a secret using the key/value pairs format, specify the
 key username, and enter the database user for the value. Add a second
 key password, and then enter the password for the value. For more
 information about how to create secrets, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html "https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html") in the *AWS Secrets Manager User
 Guide*. The secret must be formatted as follows:



```
{
  "username": "`<database_user>`",
  "password": "`<database_password>`"
}
```

###### Install and configure the
 `AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure`
 package


The
 `AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure`
 package is an SSM Distributor package that you can use to install and
 configure [Prometheus
 HANA database Exporter](https://github.com/prometheus/jmx_exporter "https://github.com/prometheus/jmx_exporter"). When HANA database metrics are sent by
 the Prometheus HANA database exporter, the CloudWatch agent can be configured to
 retrieve the metrics for the CloudWatch service.



1. Create an SSM parameter in [SSM Parameter Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters") to
 store the Exporter configurations. The following is an example parameter
 value.



```
{\"exposition_port\":9668,\"multi_tenant\":true,\"timeout\":600,\"hana\":{\"host\":\"localhost\",\"port\":30013,\"aws_secret_name\":\"HANA_DB_CREDS\",\"scale_out_mode\":true}}
```

###### Note

In this example, the export runs only on the Amazon EC2 instance with
 the active `SYSTEM` database, and it will remain idle on
 the other EC2 instances in order to avoid duplicate metrics. The
 exporter can retrieve all of the database tenant information from
 the `SYSTEM` database.
2. Create an SSM parameter in [SSM Parameter Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters") to
 store the Exporter metrics queries. The package can accept more than one
 metrics parameter. Each parameter must have a valid JSON object format.
 The following is an example parameter value:



```
{\"SELECT MAX(TIMESTAMP) TIMESTAMP, HOST, MEASURED_ELEMENT_NAME CORE, SUM(MAP(CAPTION, 'User Time', TO_NUMBER(VALUE), 0)) USER_PCT, SUM(MAP(CAPTION, 'System Time', TO_NUMBER(VALUE), 0)) SYSTEM_PCT, SUM(MAP(CAPTION, 'Wait Time', TO_NUMBER(VALUE), 0)) WAITIO_PCT, SUM(MAP(CAPTION, 'Idle Time', 0, TO_NUMBER(VALUE))) BUSY_PCT, SUM(MAP(CAPTION, 'Idle Time', TO_NUMBER(VALUE), 0)) IDLE_PCT FROM sys.M_HOST_AGENT_METRICS WHERE MEASURED_ELEMENT_TYPE = 'Processor' GROUP BY HOST, MEASURED_ELEMENT_NAME;\":{\"enabled\":true,\"metrics\":[{\"name\":\"hanadb_cpu_user\",\"description\":\"Percentage of CPU time spent by HANA DB in user space, over the last minute (in seconds)\",\"labels\":[\"HOST\",\"CORE\"],\"value\":\"USER_PCT\",\"unit\":\"percent\",\"type\":\"gauge\"},{\"name\":\"hanadb_cpu_system\",\"description\":\"Percentage of CPU time spent by HANA DB in Kernel space, over the last minute (in seconds)\",\"labels\":[\"HOST\",\"CORE\"],\"value\":\"SYSTEM_PCT\",\"unit\":\"percent\",\"type\":\"gauge\"},{\"name\":\"hanadb_cpu_waitio\",\"description\":\"Percentage of CPU time spent by HANA DB in IO mode, over the last minute (in seconds)\",\"labels\":[\"HOST\",\"CORE\"],\"value\":\"WAITIO_PCT\",\"unit\":\"percent\",\"type\":\"gauge\"},{\"name\":\"hanadb_cpu_busy\",\"description\":\"Percentage of CPU time spent by HANA DB, over the last minute (in seconds)\",\"labels\":[\"HOST\",\"CORE\"],\"value\":\"BUSY_PCT\",\"unit\":\"percent\",\"type\":\"gauge\"},{\"name\":\"hanadb_cpu_idle\",\"description\":\"Percentage of CPU time not spent by HANA DB, over the last minute (in seconds)\",\"labels\":[\"HOST\",\"CORE\"],\"value\":\"IDLE_PCT\",\"unit\":\"percent\",\"type\":\"gauge\"}]}}
```

For more information about metrics queries, see the [`SUSE / hanadb_exporter`](https://github.com/SUSE/hanadb_exporter/blob/master/metrics.json "https://github.com/SUSE/hanadb_exporter/blob/master/metrics.json") repo on
 GitHub.
3. Navigate to the [SSM Distributor](https://console.aws.amazon.com/systems-manager/distributor "https://console.aws.amazon.com/systems-manager/distributor") console
 and open the **Owned by Amazon** tab. Select
 **AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure\***
 and choose **Install one time**.
4. Update the SSM parameter you created in the first step by replacing
 "Additional Arguments" with the following:



```
{
  "SSM_EXPORTER_CONFIG": "{{ssm:<*SSM_CONFIGURATIONS_PARAMETER_STORE_NAME>*}}",
  "SSM_SID": "<SAP_DATABASE_SID>",
  "SSM_EXPORTER_METRICS_1": "{{ssm:<SSM_FIRST_METRICS_PARAMETER_STORE_NAME>}}",
  "SSM_EXPORTER_METRICS_2": "{{ssm:<SSM_SECOND_METRICS_PARAMETER_STORE_NAME>}}"
}
```
5. Select the Amazon EC2 instances with SAP HANA database, and choose
 **Run**.

## `AWSObservabilityExporter-HAClusterExporterInstallAndConfigure`


You can retrieve workload-specific High Availability (HA) cluster metrics from
 [Prometheus HANA cluster exporter](https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters "https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters") for Application Insights to configure and
 monitor alarms for an SAP HANA database High Availability setup. For more
 information, see [Set up your SAP HANA database
 for monitoring](appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up "appinsights-tutorial-sap-hana.md#appinsights-tutorial-sap-hana-set-up") in this guide.


To use [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") to package, install, and configure the AWS-provided
 Prometheus HA cluster exporter package independently of Application Insights, complete the
 following steps.



###### Prerequisites for using the Prometheus HA cluster exporter SSM
 package


* SSM agent version 2.3.1550.0 or later installed
* HA cluster for Pacemaker, Corosync, SBD, and DRBD
* Linux operating system (SUSE Linux, RedHat Linux)

###### Install and configure the
 `AWSObservabilityExporter-HAClusterExporterInstallAndConfigure`
 package


The
 `AWSObservabilityExporter-HAClusterExporterInstallAndConfigure`
 package is an SSM Distributor package that you can use to install and
 configure Prometheus HA Cluster Exporter. When cluster metrics are sent by
 the Prometheus HANA database exporter, the CloudWatch agent can be configured to
 retrieve the metrics for the CloudWatch service.



1. Create an SSM parameter in [SSM Parameter Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters") to
 store the Exporter configurations in JSON format. The following is an
 example parameter value.



```
{\"port\":\"9664\",\"address\":\"0.0.0.0\",\"log-level\":\"info\",\"crm-mon-path\":\"/usr/sbin/crm_mon\",\"cibadmin-path\":\"/usr/sbin/cibadmin\",\"corosync-cfgtoolpath-path\":\"/usr/sbin/corosync-cfgtool\",\"corosync-quorumtool-path\":\"/usr/sbin/corosync-quorumtool\",\"sbd-path\":\"/usr/sbin/sbd\",\"sbd-config-path\":\"/etc/sysconfig/sbd\",\"drbdsetup-path\":\"/sbin/drbdsetup\",\"enable-timestamps\":false}
```

For more information about the exporter configurations, see the [`ClusterLabs / ha_cluster_exporter`](https://github.com/ClusterLabs/ha_cluster_exporter/blob/master/ha_cluster_exporter.yaml "https://github.com/ClusterLabs/ha_cluster_exporter/blob/master/ha_cluster_exporter.yaml") repo on
 GitHub.
2. Navigate to the [SSM Distributor](https://console.aws.amazon.com/systems-manager/distributor "https://console.aws.amazon.com/systems-manager/distributor") console
 and open the **Owned by Amazon** tab. Select
 **AWSObservabilityExporter-HAClusterExporterInstallAndConfigure\***
 and choose **Install one time**.
3. Update the SSM parameter you created in the first step by replacing
 "Additional Arguments" with the following:



```
{
  "SSM_EXPORTER_CONFIG": "{{ssm:<*SSM_CONFIGURATIONS_PARAMETER_STORE_NAME>*}}"
}
```
4. Select the Amazon EC2 instances with SAP HANA database, and choose
 **Run**.

## `AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure`


You can retrieve workload-specific SAP NetWeaver metrics from [Prometheus SAP host exporter](https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters "https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters") for Application Insights to
 configure and monitor alarms for SAP NetWeaver Distributed and High
 Availability deployments.


To use [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") to package, install, and configure the SAP host exporter package independently of Application Insights, complete the
 following steps.



###### Prerequisites for using the Prometheus SAP host exporter SSM
 package


* SSM agent version 2.3.1550.0 or later installed
* SAP NetWeaver application servers
* Linux operating system (SUSE Linux, RedHat Linux)

###### Install and configure the
 `AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure`
 package


The
 `AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure`
 package is an SSM Distributor package that you can use to install and
 configure SAP NetWeaver Prometheus metrics exporter. When SAP NetWeaver metrics are sent by
 the Prometheus exporter, the CloudWatch agent can be configured to
 retrieve the metrics for the CloudWatch service.



1. Create an SSM parameter in [SSM Parameter Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters") to
 store the Exporter configurations in JSON format. The following is an
 example parameter value.



```
{\"address\":\"0.0.0.0\",\"port\":\"9680\",\"log-level\":\"info\",\"is-HA\":false}
```



	* **address**
	
	
	The target address to which to send the Prometheus metrics. The default value is `localhost`.
	* **port**
	
	
	The target port to which to send the Prometheus metrics. The default value is `9680`.
	* **is-HA**
	
	
	`true` for SAP NetWeaver High Availability deployments.
	 For all other deployments the value is
	 `false`.
2. Navigate to the [SSM Distributor](https://console.aws.amazon.com/systems-manager/distributor "https://console.aws.amazon.com/systems-manager/distributor") console
 and open the **Owned by Amazon** tab. Select
 **AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure**
 and choose **Install one time**.
3. Update the SSM parameter you created in the first step by replacing
 "Additional Arguments" with the following:



```
{
  "SSM_EXPORTER_CONFIG": "{{ssm:`<SSM_CONFIGURATIONS_PARAMETER_STORE_NAME>`}}",
  "SSM_SID": "`<SAP_DATABASE_SID>`",
  "SSM_INSTANCES_NUM": "`<instances_number seperated by comma>`"
}                   
```

**Example**



```
{
  "SSM_EXPORTER_CONFIG": "{{ssm:exporter_config_paramter}}",
  "SSM_INSTANCES_NUM": "11,12,10",
  "SSM_SID": "PR1"
}
```
4. Select the Amazon EC2 instances with SAP NetWeaver applications, and choose
 **Run**.

###### Note

The Prometheus exporter services the SAP NetWeaver metrics on a local
 endpoint. The local endpoint can be accessed by only the operating system
 users on the Amazon EC2 instance. Therefore, after the exporter package is
 installed, the metrics are available to all of the operating system users.
 The default local endpoint is `localhost:9680/metrics`.


## `AWSObservabilityExporter-SQLExporterInstallAndConfigure`


You can retrieve workload-specific SQL Server metrics from [Prometheus SQL exporter](https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters "https://prometheus.io/docs/instrumenting/exporters/#third-party-exporters") for Application Insights to monitor key metrics. 


To use [AWS Systems Manager
 Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html") to package, install, and configure the SQL exporter package independently of Application Insights, complete the
 following steps.



###### Prerequisites for using the Prometheus SQL exporter SSM
 package


* SSM agent version 2.3.1550.0 or later installed
* Amazon EC2 instance running SQL Server on Windows with SQL Server user authentication enabled.
* A SQL Server user with the following permissions:



```
GRANT VIEW ANY DEFINITION TO
```


```
GRANT VIEW SERVER STATE TO
```
* A secret containing the database connection string using AWS Secrets Manager. For more
 information about how to create secrets, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html "https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html")
 in the *AWS Secrets Manager User Guide*. The secret must be formatted as follows:



```
{
  "data_source_name":"sqlserver://`<username>`:`<password>`@localhost:1433"
}
```

###### Note

If the password or username contains special characters, you must percent encode the special characters to ensure a successful connection to the database.

###### Install and configure the
 `AWSObservabilityExporter-SQLExporterInstallAndConfigure`
 package


The `AWSObservabilityExporter-SQLExporterInstallAndConfigure`
 package is an SSM Distributor package that you can use to install and
 configure SQL Prometheus metrics exporter. When metrics are sent by
 the Prometheus exporter, the CloudWatch agent can be configured to
 retrieve the metrics for the CloudWatch service.



1. Based on your preferences, prepare the SQL Exporter YAML configuration. The following sample configuration has a single metric configured. Use the 
 [example configuration](https://github.com/burningalchemist/sql_exporter/blob/master/examples/sql_exporter.yml "https://github.com/burningalchemist/sql_exporter/blob/master/examples/sql_exporter.yml") to update the configuration with additional 
 metrics or create your own configuration.



```
---
global:
  scrape_timeout_offset: 500ms
  min_interval: 0s
  max_connections: 3
  max_idle_connections: 3
target:
  aws_secret_name: <SECRET_NAME>
  collectors:
    - mssql_standard
collectors:
  - collector_name: mssql_standard
    metrics: 
    - metric_name: mssql_batch_requests
      type: counter
      help: 'Number of command batches received.'
      values: [cntr_value]
      query: |
        SELECT cntr_value
        FROM sys.dm_os_performance_counters WITH (NOLOCK)
        WHERE counter_name = 'Batch Requests/sec'
                    
```
2. Copy the Prometheus SQL exporter YAML configuration file encoded as
 Base64 to a new SSM parameter in [SSM Parameter
 Store](https://console.aws.amazon.com/systems-manager/parameters "https://console.aws.amazon.com/systems-manager/parameters").
3. Navigate to the [SSM Distributor](https://console.aws.amazon.com/systems-manager/distributor "https://console.aws.amazon.com/systems-manager/distributor") console
 and open the **Owned by Amazon** tab. Select
 **AWSObservabilityExporter-SQLExporterInstallAndConfigure**
 and choose **Install one time**.
4. Replace the "Additional Arguments" with the following information. The
 `SSM_PARAMETER_NAME` is the name of the parameter you created in Step
 2.



```
{
  "SSM_EXPORTER_CONFIGURATION": 
    "{{ssm:`<SSM_PARAMETER_STORE_NAME>`}}",
    "SSM_PROMETHEUS_PORT": "`9399`",
    "SSM_WORKLOAD_NAME": "`SQL`"                         
}
```
5. Select the Amazon EC2 instance with the SQL Server database, then choose run.
