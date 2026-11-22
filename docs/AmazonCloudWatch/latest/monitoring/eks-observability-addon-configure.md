

# Configuring the add-on and the Helm chart

The add-on and the Helm chart use the same configuration values. The following examples turn on OTel Container Insights and change the gRPC port of the OTLP endpoint.

## Configuring the Amazon EKS add-on
<a name="eks-observability-addon-configure-addon"></a>

Pass the configuration values as JSON in `--configuration-values`. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":true},"otlp":{"grpc":{"port":14317}}}' \
  --resolve-conflicts OVERWRITE
```

**Important**  
The `--resolve-conflicts OVERWRITE` flag replaces any existing add-on configuration. To preserve existing settings, merge them with your new configuration before you run the command.

To see the configuration values that an add-on version accepts, run the following command. Replace {{version}} with the add-on version.

```bash
aws eks describe-addon-configuration \
  --addon-name amazon-cloudwatch-observability \
  --addon-version {{version}}
```

## Configuring the Helm chart
<a name="eks-observability-addon-configure-helm"></a>

Pass the configuration values in a values file or with `--set`.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.enabled=true \
  --set otlp.grpc.port=14317
```