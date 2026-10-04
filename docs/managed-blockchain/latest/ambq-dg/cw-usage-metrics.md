

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Amazon Managed Blockchain (AMB) Query API usage metrics on Amazon CloudWatch
<a name="cw-usage-metrics"></a>

## API usage metrics on Amazon CloudWatch
<a name="usage-metrics"></a>

The API usage metrics published to CloudWatch correspond to the Amazon Managed Blockchain (AMB) Query service quotas. You can configure alarms to alert you when your usage approaches a service quota. For more information about CloudWatch integration with service quotas, see [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.html) in the *Amazon CloudWatch User Guide*.

AMB Query publishes the following API metrics in the `AWS/Usage` namespace, with the `Amazon Managed Blockchain (AMB) Query` service name.


| Metric | Description | 
| --- | --- | 
| `CallCount` | The total number of calls made to an API in AMB Query. SUM represents the total number of calls to the API during the specified period. | 

 Amazon Managed Blockchain (AMB) Query publishes usage metrics to the `AWS/Usage` namespace with the following dimensions.


| Dimension | Description | 
| --- | --- | 
| Service | The name of the AWS service containing the resource. `Amazon Managed Blockchain (AMB) Query` will always be the value for this dimension. | 
| Type | The type of the entity being reported. `API` will always be the value for this dimension. | 
| Resource | The type of resources being reported. The *name* of the [AMB Query API operation](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Operations.html) used will be the value for this dimension. | 
| Class | The class of the resource being reported. `None` will always be the value for this dimension. | 