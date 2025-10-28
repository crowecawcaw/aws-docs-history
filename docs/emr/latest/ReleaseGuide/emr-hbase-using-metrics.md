# Using the Metrics Destination

With EMR 7.1, you have the option to send your metrics data to Amazon CloudWatch or Amazon Managed Service for Prometheus. This choice allows you to integrate
seamlessly with different monitoring tools, based on your needs.

## Sending Metrics to Amazon CloudWatch

To send metrics to CloudWatch, use this configuration:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {
      "metrics_destination": "cloudwatch"
    },
    "Configurations": []
  }
]
```

## Sending Metrics to Amazon Managed Service for Prometheus

If you prefer using Prometheus, set the destination and provide the endpoint URL:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {
      "metrics_destination": "prometheus",
      "prometheus_endpoint": "https://aps-workspaces.`region`.amazonaws.com/workspaces/`workspace_id`/api/v1/remote_write"
    },
    "Configurations": []
  }
]
```

Replace `region` with your AWS region and `workspace_id` with your Prometheus workspace ID. This configuration directs
your HBase metrics to Prometheus using the specified endpoint.

With above setup, you can see the below metrics under the **Monitoring** tab.
