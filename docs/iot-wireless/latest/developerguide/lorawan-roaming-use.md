# How to use AWS IoT Core for LoRaWAN public network

support

To use Everynet's public network support, you enable certain roaming parameters
when creating the service profile. In this beta release, these parameters are
available when you use the AWS IoT Wireless API, or the AWS CLI. The following
sections show the parameters you must enable, and how to enable public network using
the AWS CLI.

###### Note

You can enable public network support only when creating a new service
profile. You can't update an existing profile to enable public network using
these parameters.

###### Topics

- [Roaming parameters](#lorawan-roaming-parameters "#lorawan-roaming-parameters")
- [Enable public network support for
  devices](#lorawan-roaming-enable "#lorawan-roaming-enable")
- [View coverage information](#lorawan-roaming-coverage "#lorawan-roaming-coverage")

## Roaming parameters

Specify the following parameters when creating a service profile for your
device. Specify these parameters when adding a service profile from the [Profiles](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles") hub of the
AWS IoT console, or using the AWS IoT Wireless API operation, [`CreateServiceProfile`](../apireference/API_CreateServiceProfile.md "../apireference/API_CreateServiceProfile.md"), or the AWS CLI command, [`create-service-profile`](../../../cli/latest/reference/iotwireless/create-service-profile.md "../../../cli/latest/reference/iotwireless/create-service-profile.md").

###### Note

AWS IoT Core for LoRaWAN does not support handover roaming. When creating the service
profile, you can't enable the `HrAllowed` parameter that
specifies whether to use handover roaming.

- Roaming activation allowed (`RaAllowed`): This parameter
  specifies whether to enable roaming activation. Roaming activation
  enables an end device to activate under the coverage of a vNS. When
  using the roaming feature, `RaAllowed` must be set to
  `true`.
- Passive roaming allowed (`PrAllowed`): This parameter
  specifies whether to enable passive roaming. When using the roaming
  feature, `PrAllowed` must be set to `true`.

## Enable public network support for

devices

To enable public LoRaWAN network support on your devices, run the following
procedure.

###### Note

You can enable the public network capability only for OTAA devices. This
feature is not supported for devices that use ABP as the activation
method.

1. ###### Create service profile with roaming parameters

Create a service profile by enabling the roaming parameters.

###### Note

When you create a device profile for the device that you'll
associate with this service profile, we recommend that you specify a
large value for the `RxDelay1` parameter, at least
greater than 2s.

    * ###### Using the AWS IoT console


    Go to the [Profiles](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles") hub
     of the AWS IoT console and choose **Add service
     profile**. When creating the profile, choose
     **Enable public network**.
    * ###### Using the AWS IoT Wireless API


    To enable roaming when creating a service profile, use the
     [CreateServiceProfile](../apireference/API_CreateServiceProfile.md "../apireference/API_CreateServiceProfile.md") API operation or the
     [`create-service-profile`](../../../cli/latest/reference/iotwireless/create-service-profile.md "../../../cli/latest/reference/iotwireless/create-service-profile.md") CLI
     command, as shown in example below.



    ```
    aws iotwireless create-service-profile \
        --region `us-east-1` \
        --name `roamingprofile1` \
        --lorawan '{"AddGwMetadata":true,"PrAllowed":true,"RaAllowed":true}'
    ```

    Running this command returns the ARN and ID of the service
     profile as output.



    ```
    {
        "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:ServiceProfile/`12345678-a1b2-3c45-67d8-e90fa1b2c34d`",
        "Id": "`12345678-a1b2-3c45-67d8-e90fa1b2c34d`"
    }
    ```

2. ###### Check roaming parameters in service profile

To check the roaming parameters that you specified, you can view the
service profile in the console, or using the
`get-service-profile` CLI command, as shown in example
below.

    * ###### Using the AWS IoT console


    Go to the [Profiles](https://console.aws.amazon.com/iot/home#/wireless/profiles "https://console.aws.amazon.com/iot/home#/wireless/profiles") hub
     of the AWS IoT console and choose the profile that you
     created. In the **Profile configuration**
     tab of the details page, you'll see
     **RaAllowed** and
     **PrAllowed** set to
     `true`.
    * ###### Using the AWS IoT Wireless API


    To view the roaming parameters that you enabled, use the
     [GetServiceProfile](../apireference/API_GetServiceProfile.md "../apireference/API_GetServiceProfile.md") API operation or the [`get-service-profile`](../../../cli/latest/reference/iotwireless/get-service-profile.md "../../../cli/latest/reference/iotwireless/get-service-profile.md") CLI
     command, as shown in example below.



    ```
    aws iotwireless get-service-profile \
        --region `us-east-1` \
        --id `12345678-a1b2-3c45-67d8-e90fa1b2c34d`
    ```

    Running this command returns the service profile details as
     output, including the values for roaming parameters,
     `RaAllowed` and `PrAllowed`.



    ```
    {
        "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:ServiceProfile/`12345678-a1b2-3c45-67d8-e90fa1b2c34d`",
        "Id": `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`,
        "Name": `"roamingprofile1"`
        "LoRaWAN": {
            "UlRate": 60,
            "UlBucketSize": 4096,
            "DlRate": 60,
            "DlBucketSize": 4096,
            "AddGwMetadata": true,
            "DevStatusReqFreq": 24,
            "ReportDevStatusBattery": false,
            "ReportDevStatusMargin": false,
            "DrMin": 0,
            "DrMax": 15,
            "PrAllowed": true,
            "RaAllowed": true,
            "NwkGeoLoc": false,
            "TargetPer": 5,
            "MinGwDiversity": 1
        }
    }
    ```

3. ###### Attach service profile to devices

Attach the service profile that you created with the roaming
parameters to your end devices. You can also create a device profile and
add a destination for your wireless devices. You'll use this destination
to route uplink messages that are sent from your device. For more
information about creating device profiles and a destination, see [Add device profiles](lorawan-define-profiles.md#lorawan-device-profiles "lorawan-define-profiles.md#lorawan-device-profiles") and [Add destinations to
AWS IoT Core for LoRaWAN](lorawan-create-destinations.md "lorawan-create-destinations.md").

    * ###### Onboarding new devices


    If you haven't already onboarded your devices, you specify
     this service profile to be used when adding your device to
     AWS IoT Core for LoRaWAN. The following command shows how you can use
     the `create-wireless-device` CLI command to add a
     device using the ID of the service profile that you created.
     For information about adding the service profile using the
     console, see [Add your wireless device
     specification to AWS IoT Core for LoRaWAN using the console](lorawan-end-devices-add.md#lorawan-end-device-spec-console "lorawan-end-devices-add.md#lorawan-end-device-spec-console").



    ```
    aws iotwireless create-wireless-device --cli-input-json `file://createdevice.json`
    ```

    The following shows the contents of the file
     ``createdevice.json``.


    **Contents of
     createdevice.json**



    ```
    {
        "Name": `"DeviceA"`,
        "Type": LoRaWAN,
        "DestinationName": `"RoamingDestination1"`,
        "LoRaWAN": {
            "DeviceProfileId": `"ab0c23d3-b001-45ef-6a01-2bc3de4f5333"`,
            "ServiceProfileId": `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`,
            "OtaaV1_1": {
                "AppKey": `"3f4ca100e2fc675ea123f4eb12c4a012"`,
                "JoinEui": `"b4c231a359bc2e3d"`,
                "NwkKey": `"01c3f004a2d6efffe32c4eda14bcd2b4"`
            },
            "DevEui": `"ac12efc654d23fc2"`
        },
    }
    ```

    The output of running this command produces the ARN and ID of
     the wireless device as output.



    ```
    {
        "Arn": "arn:aws:iotwireless:`us-east-1:123456789012`:WirelessDevice/`1ffd32c8-8130-4194-96df-622f072a315f`",
        "Id": "`1ffd32c8-8130-4194-96df-622f072a315f`"
    }
    ```
    * ###### Updating existing devices


    If you have already onboarded your devices, you can update
     your existing wireless devices to use this service profile.
     The following command shows how you can use the
     `update-wireless-device` CLI command to
     update a device using the ID of the service profile that you
     created.



    ```
    aws iotwireless update-wireless-device \
        --id `"1ffd32c8-8130-4194-96df-622f072a315f"` \
        --service-profile-id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"` \
        --description `"Using roaming service profile A"`
    ```

    This command doesn't produce any output. You can use the
     `GetWirelessDevice` API or the
     `get-wireless-device` CLI command to get the
     updated information.

4. ###### Connect device to cloud using Everynet

As roaming has been enabled, your device must now perform a join to
obtain a new `DevAddr`. If you're using OTAA, your LoRaWAN
device sends a join request and the Network Server can allow the
request. It can then connect to the AWS Cloud using the network
coverage provided by Everynet. For instructions on how to perform the
activation procedure or join for your device, see the device
documentation.

###### Note

    * You can enable the roaming capability and connect to the
     public network only for devices that use OTAA as the
     activation method. ABP devices aren't supported. For
     instructions on how to perform the activation procedure or
     join for your device, see the device documentation. See
     [Activation modes](lorawan-manage-end-devices.md#lorawan-activation-modes "lorawan-manage-end-devices.md#lorawan-activation-modes").
    * To disable the roaming capability for your devices, you
     can disassociate the devices from this service profile, and
     then associate them with another service profile that has
     the roaming parameters set to `false`. After
     switching to this service profile, your devices must perform
     another join so that they don't continue running on the
     public network.

5. ###### Exchange uplink and downlink messages

After your device has joined to AWS IoT Core for LoRaWAN, you can start
exchanging messages between your device and the Cloud.

    * ###### View uplink messages


    When you send uplink messages from your devices,
     AWS IoT Core for LoRaWAN delivers these messages to your AWS account
     using the destination that you configured earlier. These
     messages will be sent from your device to the Cloud over
     Everynet's network.


    You can use either view the messages using the AWS IoT rule name
     or use the MQTT client to subscribe to the MQTT topic that was
     specified when creating the destination. For more information
     about the rule name and other destination details that you
     specify, see [Add a destination using the
     console](lorawan-create-destinations.md#lorawan-create-destination-console "lorawan-create-destinations.md#lorawan-create-destination-console").


    For more information about viewing uplink message and the
     format, see [View format of uplink messages sent
     from LoRaWAN devices](lorawan-uplink-metadata-format.md "lorawan-uplink-metadata-format.md").
    * ###### Send downlink messages


    You can queue and send downlink messages to your devices
     from the console, or by using the AWS IoT Wireless API
     command, `SendDataToWirelessDevice`, or the AWS CLI
     command, `send-data-to-wireless-device`. For
     information about queuing and sending downlink messages, see
     [Queue downlink messages to send to
     LoRaWAN devices](lorawan-downlink-queue.md "lorawan-downlink-queue.md").


    The following code shows an example of how you can send a
     downlink message using the
     `send-data-to-wireless-device` CLI command. You
     specify the ID of the wireless device to receive the data, the
     payload, whether to use the acknowledge mode, and the wireless
     metadata.



    ```
    aws iotwireless send-data-to-wireless-device \
        --id `"1ffd32c8-8130-4194-96df-622f072a315f"` \
        --transmit-mode "1" \
        --payload-data `"SGVsbG8gVG8gRGV2c2lt"` \
        --wireless-metadata LoRaWAN={FPort=1}
    ```

    The output of running this command generates a
     `MessageId` for the downlink message.


    ###### Note

    In some cases, even if you receive the
     `MessageId`, packets can get dropped. For
     information about troubleshooting such scenarios and
     resolving them, see [Troubleshoot downlink
     message queue errors](lorawan-downlink-queue.md#lorawan-downlink-queue-troubleshoot "lorawan-downlink-queue.md#lorawan-downlink-queue-troubleshoot").



    ```
    {
        MessageId: `"6011dd36-0043d6eb-0072-0008"`
    }
    ```

## View coverage information

After you've enabled the public network, you can view the network coverage
information in the AWS IoT console. Go to the [**Coverage**](https://console.aws.amazon.com/iot/home#/wireless/network-coverage "https://console.aws.amazon.com/iot/home#/wireless/network-coverage") hub of the AWS IoT console and then
search for locations to see the coverage information of your devices on the
map.

###### Note

This feature uses the Amazon Location Service to display the coverage information of your
devices on an Amazon Location map. Before using Amazon Location maps, review the Terms
and Conditions for Amazon Location Service. Note that AWS may transmit
your API queries to your chosen third party data provider, which may be
outside of the AWS Region that you are currently using. For more
information, see [AWS Service
Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").
