# Use Amazon Managed Service for Prometheus to monitor Flink jobs

You can integrate Apache Flink with Amazon Managed Service for Prometheus (management portal). Amazon Managed Service for Prometheus supports ingesting metrics from
Amazon Managed Service for Prometheus servers in clusters running on Amazon EKS. Amazon Managed Service for Prometheus works together with a Prometheus server already running on
your Amazon EKS cluster. Running Amazon Managed Service for Prometheus integration with Amazon EMR Flink operator will automatically deploy
and configure a Prometheus server to integrate with Amazon Managed Service for Prometheus.

1. [Create an Amazon Managed Service for Prometheus Workspace](../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md "../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md"). This workspace serves as an ingestion endpoint. You will need the
   remote write URL later.
2. Set up IAM roles for service accounts.

For this method of onboarding, use IAM roles
for the service accounts in the Amazon EKS cluster where the Prometheus server is running.
These roles are also called _service roles_.

If you don't already have the roles, [set up service roles for the ingestion of metrics from Amazon EKS clusters.](../../../prometheus/latest/userguide/set-up-irsa.md "../../../prometheus/latest/userguide/set-up-irsa.md")

Before you continue, create an IAM role called `amp-iamproxy-ingest-role`. 3. Install the Amazon EMR Flink Operator with Amazon Managed Service for Prometheus.
Now that you have an Amazon Managed Service for Prometheus workspace, a dedicated IAM role for Amazon Managed Service for Prometheus, and the necessary permissions,
you can install the Amazon EMR Flink operator.

Create an `enable-amp.yaml` file. This file lets you use a custom configuration to override Amazon Managed Service for Prometheus settings. Make sure to use your own roles.

```
kube-prometheus-stack:
    prometheus:
    serviceAccount:
        create: true
        name: "amp-iamproxy-ingest-service-account"
        annotations:
            eks.amazonaws.com/role-arn: "arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/amp-iamproxy-ingest-role"
    remoteWrite:
        - url: `<AMAZON_MANAGED_PROMETHEUS_REMOTE_WRITE_URL>`
        sigv4:
            region: `<AWS_REGION>`
        queueConfig:
            maxSamplesPerSend: 1000
            maxShards: 200
            capacity: 2500
```

Use the [`Helm Install --set`](https://helm.sh/docs/helm/helm_install/ "https://helm.sh/docs/helm/helm_install/")
command to pass overrides to the `flink-kubernetes-operator` chart.

```
helm upgrade -n `<namespace>` flink-kubernetes-operator \
   oci://public.ecr.aws/emr-on-eks/flink-kubernetes-operator \
   --set prometheus.enabled=true
   -f enable-amp.yaml
```

This command automatically installs a Prometheus reporter in the operator on port 9999. Any future `FlinkDeployment` also exposes a `metrics` port on 9249.

- Flink operator metrics appear in Prometheus under the label `flink_k8soperator_`.
- Flink Task Manager metrics appear in Prometheus under the label `flink_taskmanager_`.
- Flink Job Manager metrics appear in Prometheus under the label `flink_jobmanager_`.
