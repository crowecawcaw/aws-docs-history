

# RDS PostgreSQL

The following example shows a component configurations in JSON format for RDS PostgreSQL.

```json
{
  "alarmMetrics": [
    {
      "alarmMetricName": "CPUUtilization",
      "monitor": true
    }
  ],
  "logs": [
    {
      "logType": "POSTGRESQL",
      "monitor": true
    }
  ]
}
```