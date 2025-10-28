# Validating Prometheus setup on the head node of a HyperPod cluster

After you have successfully set up your HyperPod cluster installed with the
exporter packages, check if Prometheus is properly set up on the head node of your
HyperPod cluster.

1. Connect to the head node of your cluster. For instructions on accessing a
   node, see [Accessing your
   SageMaker HyperPod cluster nodes](sagemaker-hyperpod-run-jobs-slurm-access-nodes.md "sagemaker-hyperpod-run-jobs-slurm-access-nodes.md").
2. Run the following command to verify the Prometheus config and service file
   created by the lifecycle script `install_prometheus.sh` is running on
   the controller node. The output should show the Active status as
   `active (running)`.

```
`$` `sudo systemctl status prometheus`
`• prometheus service - Prometheus Exporter
Loaded: loaded (/etc/systemd/system/prometheus.service; enabled; preset:disabled)
Active: `active (running)` since DAY YYYY-MM-DD HH:MM:SS UTC; Ss ago
Main PID: 12345 (prometheus)
Tasks: 7 (limit: 9281)
Memory: 35M
CPU: 234ms
CGroup: /system.slice/prometheus.service
 -12345 /usr/bin/prometheus--config.file=/etc/prometheus/prometheus.yml`
```

3. Validate the Prometheus configuration file as follows. The output must be
   similar to the following, with three exporter configured with the right compute
   node IP addresses.

```
`$` `cat /etc/prometheus/prometheus.yml`
`global:
 scrape_interval: 15s
 evaluation_interval: 15s
 scrape_timeout: 15s

scrape_configs:
 - job_name: 'slurm_exporter'
 static_configs:
 - targets:
 - 'localhost:8080'
 - job_name: 'dcgm_exporter'
 static_configs:
 - targets:
 - '<ComputeNodeIP>:9400'
 - '<ComputeNodeIP>:9400'
 - job_name: 'efa_node_exporter'
 static_configs:
 - targets:
 - '<ComputeNodeIP>:9100'
 - '<ComputeNodeIP>:9100'

remote_write:
 - url: <AMPReoteWriteURL>
 queue_config:
 max_samples_per_send: 1000
 max_shards: 200
 capacity: 2500
 sigv4:
 region: <Region>`
```

4. To test if Prometheus is exporting Slurm, DCGM, and EFA metrics properly, run
   the following `curl` command for Prometheus on port
   `:9090` on the head node.

```
`$` `curl -s http://localhost:9090/metrics | grep -E 'slurm|dcgm|efa'`
```

With the metrics exported to Amazon Managed Service for Prometheus Workspace through the Prometheus remote
write configuration from the controller node, you can proceed to the next topic
to set up Amazon Managed Grafana dashboards to display the metrics.
