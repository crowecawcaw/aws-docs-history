# Configure

alert manager to send alerts to PagerDuty

To configure alert manager to send alerts to PagerDuty, you need to update
your alert manager definition. You can do this using the AWS Management Console, AWS CLI, or
AWS SDKs.

###### Example alert manager configuration

Following, is an example alert manager configuration that sends alerts to
PagerDuty. In the example, replace the `highlighted
 values` with your specific values.

```
alertmanager_config: |
  route:
    receiver: 'pagerduty-receiver'
    group_by: ['alertname']
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 1h
  receivers:
    - name: 'pagerduty-receiver'
      pagerduty_configs:
      - routing_key:
          aws_secrets_manager:
            secret_arn: 'arn:aws:secretsmanager:`aws-region`:`123456789012`:secret:`YOUR_SECRET_NAME`'
            secret_key: '`YOUR_SECRET_KEY`'
            refresh_interval: 5m
        description: '{{ .CommonLabels.alertname }}'
        severity: 'critical'
        details:
          firing: '{{ .Alerts.Firing | len }}'
          status: '{{ .Status }}'
          instance: '{{ .CommonLabels.instance }}'

```

###### Example AWS CLI

Following, is an AWS CLI command used to update your alert manager
definition. In the example, replace the `highlighted
 values` with your specific values.

```

aws amp put-alert-manager-definition \
  --workspace-id `WORKSPACE_ID` \
  --data `file://alertmanager-config.yaml`

```

## Troubleshooting

PagerDuty integration

If alerts are not being sent to PagerDuty, check the following
items:

- Verify that your secret exists and contains the correct PagerDuty
  integration key.
- Confirm that your secret is encrypted with a customer-managed KMS
  key.
- Ensure that the resource policies for both the secret and the KMS
  key grant the necessary permissions to Amazon Managed Service for
  Prometheus.
- Check that the ARN in your alert manager configuration correctly
  references your secret.
- Verify that your PagerDuty integration key is valid and active in
  your PagerDuty account.

Amazon Managed Service for Prometheus supports Amazon CloudWatch Logs, and the following CloudWatch metrics, to help with
troubleshooting. For more information, see [Monitor Amazon Managed Service for Prometheus events with CloudWatch Logs](CW-logs.md "CW-logs.md") and [Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus
resources](AMP-CW-usage-metrics.md "AMP-CW-usage-metrics.md").

- `SecretFetchFailure`
- `AlertManagerNotificationsThrottledByIntegration`
- `AlertManagerNotificationsFailedByIntegration`
