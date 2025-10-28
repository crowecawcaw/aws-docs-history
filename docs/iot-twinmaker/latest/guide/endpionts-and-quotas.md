# Endpoints and quotas

## AWS IoT TwinMaker endpoints and quotas

You can find information about AWS IoT TwinMaker endpoints and quotas in the [AWS General Reference](../../../general/latest/gr/iot-twinmaker.md "../../../general/latest/gr/iot-twinmaker.md").

- For information about service endpoints, see [AWS IoT TwinMaker service endpoints](../../../general/latest/gr/iot-twinmaker.md#iot-twinmaker_region "../../../general/latest/gr/iot-twinmaker.md#iot-twinmaker_region").
- For information about quotas, see [AWS IoT TwinMaker service quotas](../../../general/latest/gr/iot-twinmaker.md#limits_iot_twinmaker "../../../general/latest/gr/iot-twinmaker.md#limits_iot_twinmaker").
- For information about API throttling limits, see [AWS IoT TwinMaker API throttling
  limits](../../../general/latest/gr/iot-twinmaker.md#limits_iot_twinmaker_throttling_lim "../../../general/latest/gr/iot-twinmaker.md#limits_iot_twinmaker_throttling_lim").

### Additional information about AWS IoT TwinMaker endpoints

To connect programmatically to AWS IoT TwinMaker, use an endpoint. If you use an HTTP client,
you need to prefix control plane and data plane APIs as follows. However, it is unnecessary
to add a prefix to AWS SDK and AWS Command Line Interface commands because they automatically add the
necessary prefix.

- Use the `api` prefix for control plane APIs. For example,
  `api.iottwinmaker.us-west-1.amazonaws.com`.
- Use the `data` prefix for data plane APIs. For example,
  `data.iottwinmaker.us-west-1.amazonaws.com`.
