# Amazon Managed Blockchain (AMB) Query API usage metrics on Amazon CloudWatch

## API usage metrics on Amazon CloudWatch

The API usage metrics published to CloudWatch correspond to the Amazon Managed Blockchain (AMB) Query service quotas. You can configure alarms
to alert you when your usage approaches a service quota. For more information about CloudWatch
integration with service quotas, see [AWS usage metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md") in the _Amazon CloudWatch User Guide_.

AMB Query publishes the following API metrics in the `AWS/Usage` namespace, with the `Amazon Managed Blockchain Query` service name.

| Metric      | Description                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `CallCount` | The total number of calls made to an API in AMB Query. SUM represents the total number of calls to the API during the specified period.                                                                       | Amazon Managed Blockchain (AMB) Query publishes usage metrics to the `AWS/Usage` namespace with the following dimensions. |
| Dimension   | Description                                                                                                                                                                                                   |
| ---         | ---                                                                                                                                                                                                           |
| Service     | The name of the AWS service containing the resource. `Amazon Managed Blockchain Query` will always be the value for this dimension.                                                                           |
| Type        | The type of the entity being reported. `API` will always be the value for this dimension.                                                                                                                     |
| Resource    | The type of resources being reported. The _name_ of the [AMB Query API operation](../AMBQ-APIReference/API_Operations.md "../AMBQ-APIReference/API_Operations.md") used will be the value for this dimension. |
| Class       | The class of the resource being reported. `None` will always be the value for this dimension.                                                                                                                 |
