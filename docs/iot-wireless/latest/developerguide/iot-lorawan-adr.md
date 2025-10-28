# Using adaptive data rate (ADR) with

AWS IoT Core for LoRaWAN

To optimize the device transmission power consumption while making sure that messages
from the end devices are received at the gateways, AWS IoT Core for LoRaWAN uses adaptive data
rate. Adaptive data rate instructs the end devices to optimize the data rate,
transmission power, and the number of retransmissions while attempting to reduce the
error rate of the packets received at the gateways. For example, if your end device is
located close to the gateways, adaptive data rate reduces the transmission power and
increases the data rate.

###### Topics

- [How adaptive data rate (ADR)
  works](#iot-lorawan-adr-algorithm "#iot-lorawan-adr-algorithm")
- [Configure data rate limits (CLI)](#iot-lorawan-adr-use "#iot-lorawan-adr-use")

## How adaptive data rate (ADR)

works

To enable ADR, your device must set the ADR bit in the frame header. Once the ADR
bit is set, AWS IoT Core for LoRaWAN sends the `LinkADRReq` MAC command and your
devices respond with the `LinkADRAns` command which includes the ACK
status of the ADR command. Once your devices ACK the ADR command, it will then
follow the ADR instructions from AWS IoT Core for LoRaWAN and adjust the transmission parameter
values for optimal data rate.

The AWS IoT Core for LoRaWAN ADR algorithm uses the SINR information in the uplink metadata
history to determine the optimal transmission power and data rate to use for the
devices. The algorithm uses the 20 most recent uplink messages that start once the
ADR bit is set in the frame header. To determine the number of retransmissions, it
uses the packet error rate (PER), which is a percentage of the total number of
packets that are lost. When you use this algorithm, you can only control the range
of data rates, that is, the minimum and maximum limits for the data rates.

## Configure data rate limits (CLI)

By default, AWS IoT Core for LoRaWAN will perform ADR when you set the ADR bit in the frame
header of your LoRaWAN device. You can control the minimum and maximum limits for
the data rate when creating a service profile for your LoRaWAN devices using the
AWS IoT Wireless API operation [`CreateServiceProfile`](../../2020-11-22/apireference/API_CreateServiceProfile.md "../../2020-11-22/apireference/API_CreateServiceProfile.md"), or the AWS CLI command, [`create-service-profile`](../../../cli/latest/reference/iotwireless/create-service-profile.md "../../../cli/latest/reference/iotwireless/create-service-profile.md").

To specify the minimum and maximum limits for the data rate, use the
`DrMin` and `DrMax` parameters with the
`CreateServiceProfile` API operation. The default minimum and maximum
data rate limits are 0 and 15. For example, the following CLI command sets a minimum
data rate limit of 3 and a maximum limit of 12.

To specify the minimum and maximum limits for the transmit power range of LoRaWAN
devices, use the `TxPowerIndexMin` and `TxPowerIndexMax`
parameters with the `CreateServiceProfile` API operation. The default
minimum and maximum power ranges are 0 and 15. The following following CLI command
sets a minimum Transmit Power Index of 3 and a maximum of 12.

###### Note

Regional parameters override service profile settings for minimum and maximum
Transmit Power Index (`TxPowerIndexMin` and
`TxPowerIndexMax`). For example, if you set
`TxPowerIndexMin` to 14 for a device that operates in the US915
Band, the configuration you set won't be applied. To learn more about regional
parameters, see [RP002-1.0.4 Regional Parameters](https://resources.lora-alliance.org/technical-specifications/rp002-1-0-4-regional-parameters "https://resources.lora-alliance.org/technical-specifications/rp002-1-0-4-regional-parameters").

To specify the minimum and maximum number of transmissions, use the
`NbTransMin` and `NbTransMax` parameters with the
`CreateServiceProfile` API operation. The default minimum and maximum
number of transmissions is 0 and 3.

```
aws iotwireless create-service-profile \
    --lorawan DrMin=`3`,DrMax=`12`,TxPowerIndexMin=`3`,TxPowerIndexMax=`12`,NbTransMin=`1`,NbTransMax=`4`
```

Running this command generates an ID and an Amazon Resource Name (ARN) for the
service profile.

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ServiceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```

You can get the values of the parameters specified using the AWS IoT Wireless
API operation [`GetServiceProfile`](../../2020-11-22/apireference/API_GetServiceProfile.md "../../2020-11-22/apireference/API_GetServiceProfile.md"), or the AWS CLI command, [`get-service-profile`](../../../cli/latest/reference/iotwireless/get-service-profile.md "../../../cli/latest/reference/iotwireless/get-service-profile.md").

```
aws iotwireless get-service-profile --id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`
```

Running this command generates the values for the service profile
parameters.

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:651419225604:ServiceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "LoRaWAN": {
        "AddGwMetadata": false,
        "DrMax": 12,
        "DrMin": 3,
        "NbTransMax": 4,
        "NbTransMin": 1,
        "PrAllowed": false,
        "RaAllowed": false,
        "TxPowerIndexMax": 12,
        "TxPowerIndexMin": 3
    }
}
```

If you've created multiple profiles, you can use the API operation, [`ListServiceProfiles`](../../2020-11-22/apireference/API_ListServiceProfiles.md "../../2020-11-22/apireference/API_ListServiceProfiles.md"), or the AWS CLI command, [`list-service-profiles`](../../../cli/latest/reference/iotwireless/list-service-profiles.md "../../../cli/latest/reference/iotwireless/list-service-profiles.md") to list the service profiles in
your AWS account, and then use the `GetServiceProfile` API or the
`get-service-profile` CLI command to retrieve the service profile for
which you customized the data rate limits.
