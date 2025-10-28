# Set up

ingestion from an existing Prometheus server in Kubernetes on Fargate

Amazon Managed Service for Prometheus supports ingesting metrics from Prometheus servers in self-managed
Kubernetes clusters running on Fargate. To ingest metrics from Prometheus servers
in Amazon EKS clusters running on Fargate, override the default configs in a config
file named amp_ingest_override_values.yaml as follows:

```
prometheus-node-exporter:
        enabled: false

    alertmanager:
        enabled: false

    serviceAccounts:
      server:
        name: amp-iamproxy-ingest-service-account
        annotations:
          eks.amazonaws.com/role-arn: ${IAM_PROXY_PROMETHEUS_ROLE_ARN}

    server:
      persistentVolume:
        enabled: false
      remoteWrite:
        - url: https://aps-workspaces.${REGION}.amazonaws.com/workspaces/${WORKSPACE_ID}/api/v1/remote_write
          sigv4:
            region: ${REGION}
          queue_config:
            max_samples_per_send: 1000
            max_shards: 200
            capacity: 2500
```

Install Prometheus using the overrides with the following command:

```
helm install prometheus-for-amp prometheus-community/prometheus \
                   -n prometheus \
                   -f amp_ingest_override_values.yaml
```

Note that in the Helm chart configuration we disabled the node exporter and the
alert manager as well as running the Prometheus server deployment.

You can verify the install with the following example test query.

```
$ awscurl --region `region` --service aps "https://aps-workspaces.`region_id`.amazonaws.com/workspaces/`workspace_id`/api/v1/query?query=prometheus_api_remote_read_queries"
    {"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"prometheus_api_remote_read_queries","instance":"localhost:9090","job":"prometheus"},"value":[1648461236.419,"0"]}]}}21
```
