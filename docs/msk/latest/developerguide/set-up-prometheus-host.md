

# Set up a Prometheus host on an Amazon EC2 instance
<a name="set-up-prometheus-host"></a>

This procedure describes how to set up a Prometheus host using a prometheus.yml file.

1. Download the Prometheus server from [https://prometheus.io/download/#prometheus](https://prometheus.io/download/#prometheus) to your Amazon EC2 instance.

1. Extract the downloaded file to a directory and go to that directory.

1. Create a file with the following contents and name it `prometheus.yml`.

   ```
   # file: prometheus.yml
   # my global config
   global:
     scrape_interval:     60s
   
   # A scrape configuration containing exactly one endpoint to scrape:
   # Here it's Prometheus itself.
   scrape_configs:
     # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
     - job_name: 'prometheus'
       static_configs:
       # 9090 is the prometheus server port
       - targets: ['localhost:9090']
     - job_name: 'broker'
       file_sd_configs:
       - files:
         - 'targets.json'
   ```

1. Use the [ListNodes](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-nodes.html#ListNodes) operation to get a list of your cluster's brokers.

1. Create a file named `targets.json` with the following JSON. Replace {{broker\_dns\_1}}, {{broker\_dns\_2}}, and the rest of the broker DNS names with the DNS names you obtained for your brokers in the previous step. Include all of the brokers you obtained in the previous step. Amazon MSK uses port 11001 for the JMX Exporter and port 11002 for the Node Exporter.

------
#### [ Brokers only ]

   ```
   [
     {
       "labels": {
         "job": "jmx"
       },
       "targets": [
         "{{broker_dns_1}}:11001",
         "{{broker_dns_2}}:11001",
         .
         .
         .
         "{{broker_dns_N}}:11001"
       ]
     },
     {
       "labels": {
         "job": "node"
       },
       "targets": [
         "{{broker_dns_1}}:11002",
         "{{broker_dns_2}}:11002",
         .
         .
         .
         "{{broker_dns_N}}:11002"
       ]
     }
   ]
   ```

------
#### [ Brokers and controllers ]

   ```
   [
     {
       "labels": {
         "job": "jmx"
       },
       "targets": [
         "{{broker_dns_1}}:11001",
         "{{broker_dns_2}}:11001",
         .
         .
         .
         "{{broker_dns_N}}:11001",
         "{{controller_dns_1}}:11001",
         "{{controller_dns_2}}:11001",
         "{{controller_dns_3}}:11001"
       ]
     },
     {
       "labels": {
         "job": "node"
       },
       "targets": [
         "{{broker_dns_1}}:11002",
         "{{broker_dns_2}}:11002",
         .
         .
         .
         "{{broker_dns_N}}:11002"
       ]
     }
   ]
   ```

------
**Note**  
Use the **Brokers only** targets for clusters in ZooKeeper mode. Also use them for KRaft clusters created on Apache Kafka version 4.1 or later, and for clusters migrated from ZooKeeper mode to KRaft mode. These clusters don't have controller DNS endpoints, and `ListNodes` doesn't return endpoints for their controller nodes.  
Only KRaft clusters created on Apache Kafka versions earlier than 4.1 have controller DNS endpoints, and they keep them after a version upgrade. For these clusters, you can optionally add the controller DNS names that `ListNodes` returns as targets. The **Brokers and controllers** tab shows an example.  
You don't need controller metrics to monitor the health of your cluster. Amazon MSK monitors and manages the KRaft controllers for you. For cluster-level health, use Amazon MSK CloudWatch metrics such as `ActiveControllerCount`. For more information, see [Amazon MSK metrics for monitoring Standard brokers with CloudWatch](metrics-details.md) and [Amazon MSK metrics for monitoring Express brokers with CloudWatch](metrics-details-express.md).

1. To start the Prometheus server on your Amazon EC2 instance, run the following command in the directory where you extracted the Prometheus files and saved `prometheus.yml` and `targets.json`.

   ```
   ./prometheus
   ```

1. Find the IPv4 public IP address of the Amazon EC2 instance where you ran Prometheus in the previous step. You need this public IP address in the following step.

1. To access the Prometheus web UI, open a browser that can access your Amazon EC2 instance, and go to `{{Prometheus-Instance-Public-IP}}:9090`, where {{Prometheus-Instance-Public-IP}} is the public IP address you got in the previous step.