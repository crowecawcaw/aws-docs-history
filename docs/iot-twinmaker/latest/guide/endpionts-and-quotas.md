

# Endpoints and quotas
<a name="endpionts-and-quotas"></a>

## AWS IoT TwinMaker endpoints and quotas
<a name="w2aac53b5"></a>

You can find information about AWS IoT TwinMaker endpoints and quotas in the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/iot-twinmaker).
+ For information about service endpoints, see [AWS IoT TwinMaker service endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-twinmaker#iot-twinmaker_region).
+ For information about quotas, see [AWS IoT TwinMaker service quotas](https://docs.aws.amazon.com/general/latest/gr/iot-twinmaker#limits_iot_twinmaker).
+ For information about API throttling limits, see [AWS IoT TwinMaker API throttling limits](https://docs.aws.amazon.com/general/latest/gr/iot-twinmaker#limits_iot_twinmaker_throttling_lim).

### Additional information about AWS IoT TwinMaker endpoints
<a name="additional-endpoint-info"></a>

To connect programmatically to AWS IoT TwinMaker, use an endpoint. If you use an HTTP client, you need to prefix control plane and data plane APIs as follows. However, it is unnecessary to add a prefix to AWS SDK and AWS Command Line Interface commands because they automatically add the necessary prefix.
+ Use the `api` prefix for control plane APIs. For example, `api.iottwinmaker.us-west-1.amazonaws.com`.
+ Use the `data` prefix for data plane APIs. For example, `data.iottwinmaker.us-west-1.amazonaws.com`.