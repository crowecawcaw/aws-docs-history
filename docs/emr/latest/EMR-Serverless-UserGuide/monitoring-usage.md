# EMR Serverless usage metrics

You can use Amazon CloudWatch usage metrics to provide visibility into the resources that
your account uses. Use these metrics to visualize your service usage on CloudWatch graphs
and dashboards.

EMR Serverless usage metrics correspond to Service Quotas. You can configure alarms
that alert you when your usage approaches a service quota. For more information, refer to
[Service Quotas and Amazon CloudWatch
alarms](../../../servicequotas/latest/userguide/configure-cloudwatch.md "../../../servicequotas/latest/userguide/configure-cloudwatch.md") in the _Service Quotas User Guide_.

For more information about EMR Serverless service quotas, refer to [Endpoints and quotas for
EMR Serverless](endpoints-quotas.md "endpoints-quotas.md").

## Service quota usage metrics for

EMR Serverless

EMR Serverless publishes the following service quota usage metrics in the
`AWS/Usage` namespace.

| Metric          | Description                                                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ResourceCount` | The total number of the specified resource that is<br>running on your account. The resource is defined by the<br>[dimensions](#usage-metrics-dimensions "#usage-metrics-dimensions") that are associated with the<br>metric. |

## Dimensions for EMR Serverless

service quota usage metrics

You can use the following dimensions to refine the usage metrics that
EMR Serverless publishes.

| Dimension  | Value          | Description                                                |
| ---------- | -------------- | ---------------------------------------------------------- |
| `Service`  | EMR Serverless | The name of the AWS service that contains the<br>resource. |
| `Type`     | Resource       | The type of entity that EMR Serverless is reporting.       |
| `Resource` | vCPU           | The type of resource that EMR Serverless is<br>tracking.   |
| `Class`    | None           | The class of resource that EMR Serverless is<br>tracking.  |
