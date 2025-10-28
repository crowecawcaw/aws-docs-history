# Obtain device JSON files for

provisioning

After you've added your Sidewalk device to AWS IoT Core for Amazon Sidewalk, download the
JSON file that contains the information required to provision your end device. You
can retrieve this information using the AWS IoT console or the AWS CLI. For more
information about how to provision the device, see [Provisioning and registering
your end device](https://docs.sidewalk.amazon/provisioning/ "https://docs.sidewalk.amazon/provisioning/") in the _Amazon Sidewalk
documentation_.

## Obtain JSON file

(console)

To obtain the JSON file for provisioning your Sidewalk device:

1. Go to the [Sidewalk
   devices hub](https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk "https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk").
2. Choose the device that you added to AWS IoT Core for Amazon Sidewalk to view its
   details.
3. Obtain the JSON file by choosing **Download device JSON
   file** in the details page of the device that you
   added.

A `certificate.json` file will be downloaded that contains
the required information for provisioning your end device. The following
shows a sample JSON file. It contains the device certificates, private
keys, the Sidewalk manufacturing serial number (SMSN), and the
`DeviceTypeID`.

```
{
  "p256R1": "`grg8izXoVvQ86cPVm0GMyWuZYHEBbbH ... DANKkOKoNT3bUGz+/f/pyTE+xMRdIUBZ1Bw==`",
  "eD25519": "`grg8izXoVvQ86cPVm0GMyWuZYHEBbbHD ... UiZmntHiUr1GfkTOFMYqRB+Aw==`",
  "metadata": {
    "devicetypeid": "`fe98`",
    "applicationDeviceArn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:WirelessDevice/`897ce68e-3ca2-4ed0-85a2-30b0666c4052`",
    "applicationDeviceId": "`897ce68e-3ca2-4ed0-85a2-30b0666c4052`",
    "smsn": "`82B83C8B35E856F43CE9C3D59B418CC96B996071016DB1C3BE5901F0F3071A4A`",
    "devicePrivKeyP256R1": "`3e704bf8d319b3a475179f1d68c60737b28c708f845d0198f2d00d00c88ee018`",
    "devicePrivKeyEd25519": "`17dacb3a46ad9a42d5c520ca5f47f0167f59ce54d740aa13918465faf533b8d0`"
  },
  "applicationServerPublicKey": "`5ce29b89c2e3ce6183b41e75fe54e45f61b8bb320efbdd2abd7aefa5957a316b`"
}
```

In the details page of your Sidewalk device, you'll also see
information about:

- The device ID, its Amazon Resource Name (ARN), and details about any
  AWS IoT thing that the device is associated with.
- The device profile and destination details.
- The time at which the last uplink message was received from the
  device.
- The status that indicates whether your device has been provisioned or
  registered.

## Obtain JSON file (CLI)

To obtain the JSON files for provisioning your Sidewalk end device
using the AWS IoT Core for Amazon Sidewalk API or the AWS CLI, save the API response from retrieving
information about your device profile and wireless device as JSON files, such as
`wireless_device.json` and
`device_profile.json` temporarily.
You'll use them for provisioning your Sidewalk device.

The following shows how to retrieve the JSON files.

###### Topics

- [Step 1: Get device profile
  information as JSON file](#iot-sidewalk-profile-get "#iot-sidewalk-profile-get")
- [Step 2: Get Sidewalk device
  information as JSON file](#iot-sidewalk-get-device "#iot-sidewalk-get-device")

### Step 1: Get device profile

information as JSON file

Use the [`GetDeviceProfile`](../../2020-11-22/apireference/API_GetDeviceProfile.md "../../2020-11-22/apireference/API_GetDeviceProfile.md") API operation or the [`get-device-profile`](../../../cli/latest/reference/get-device-profile.md "../../../cli/latest/reference/get-device-profile.md") CLI command to get
information about your device profile that you added to your account for
AWS IoT Core for Amazon Sidewalk. To retrieve information about your device profile, specify
the profile ID.

The API will then return information about the device profile matching the
specified identifier and the device ID. You save this response information
as a file, and give it a name such as
`device_profile.json`.

The following shows an example CLI command:

```
aws iotwireless get-device-profile \
    --id "`12345678-a1b2-3c45-67d8-e90fa1b2c34d`" > `device_profile.json`
```

Running this command returns the parameters of your device profile, the
application server public key, and the `DeviceTypeID`. The
following shows a JSON file that contains a sample response information from
the API. For more information about the parameters in the API response, see
[`GetDeviceProfile`](../../2020-11-22/apireference/API_GetDeviceProfile.md "../../2020-11-22/apireference/API_GetDeviceProfile.md").

**`GetDeviceProfile` API response (Contents
of
`device_profile.json`)**

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:DeviceProfile/`12345678-a1b2-3c45-67d8-e90fa1b2c34d`",
    "Id": "`12345678-a1b2-3c45-67d8-e90fa1b2c34d`",
    "Name": `"Sidewalk_profile"`,
    "LoRaWAN": null,
    "Sidewalk":
    {
        "ApplicationServerPublicKey": "`a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234`",
        "DAKCertificateMetadata": [
            {
                "DeviceTypeId: "`fe98`",
                "CertificateId": `"43564A6D2D50524F544F54595045"`,
                "FactorySupport": false,
                "MaxAllowedSignature": 1000
            }
        ],
        "QualificationStatus": false
    }
}
```

### Step 2: Get Sidewalk device

information as JSON file

Use the [`GetWirelessDevice`](../../2020-11-22/apireference/API_GetWirelessDevice.md "../../2020-11-22/apireference/API_GetWirelessDevice.md") API operation or the [`get-wireless-device`](../../../cli/latest/reference/get-wireless-device.md "../../../cli/latest/reference/get-wireless-device.md") CLI command to get
information about your Sidewalk device that you added to your account
for AWS IoT Core for Amazon Sidewalk. To get information about your end device, provide the
identifier of the wireless device that you obtained when adding your device.

The API will then return information about the device matching the
specified identifier and the device ID. Save this response information as a
JSON file. Give the file a meaningful name, such as
`wireless_device.json`.

The following shows an example of running the command using the
CLI:

```
aws iotwireless get-wireless-device --identifier-type WirelessDeviceId \
    --identifier `"23456789-abcd-0123-bcde-fabc012345678"` > `wireless_device.json`
```

Running this command returns the device details, device certificates,
private keys, and the Sidewalk manufacturing serial number (SMSN).
The following shows an example output of running this command. For more
information about the parameters in the API response, see [`GetWirelessDevice`](../../2020-11-22/apireference/API_GetWirelessDevice.md "../../2020-11-22/apireference/API_GetWirelessDevice.md").

**`GetWirelessDevice` API response
(Contents of
`wireless_device.json`)**

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:WirelessDevice/`23456789-abcd-0123-bcde-fabc012345678`",
    "Id": "`23456789-abcd-0123-bcde-fabc012345678`",
    "DestinationName": `"SidewalkDestination"`,
    "Type": "Sidewalk",
    "Sidewalk": {
        "CertificateId": `"4C7438772D50524F544F54595045"`,
        "DeviceCertificates": [
            {
                "SigningAlg": "Ed25519",
                "Value": `"hDdkJw9L2uMCORjImjMHqzNR6nYYh6QKncSl5GthQNl7NKe4ounb5UMQtLjnm7zOUPYOqghCeVOLCBUiQe2ZiMBEW18JDUXIhffPobqZgohK91+LKFJ10X/F+GeltcafZcFKhS+O5NPcVNR/fHYaf/cn5iUbRwlz/T+ODXvGdwkBkgDyFgoUJgn7JdzFjaneE5qzTWXUbL79i1sXToGGjP8hiD9jJhidPWhIswleydAWgO1OZGA4CjzIaSGVM1VtaLB0VDphAkEpjMkZrtVDH3S8U1vDZTVi6YSbnkYZgfWv/uMMBfgAeL8Tdv5LkFIPIB3ZX9zt8zzmAuFRzI4MuNjWfIDnOF6AKu37WWU6/QYhZoQrW9D/wndiCcsRGl+ANn367r/HE02Re4DOiCfs9f2rjc4LT1LKt7g/KW2ii+W+9HYvvY0bBAI+AHx6Cx4j+djabTsvrgW2k6NU2zUSM7bdDP3z2a2+Z4WzBji/jYwt/OP8rpsy5Ee4ywXUfCsfQ0rKOr0zay6yh27p3I3MZle2oCO4JIlqK0VbIQqsXzSSyp6XXS0lhmuGugZ1AAADGz+gFBeX/ZNN8VJwnsNfgzj4me1HgVJdUo4W9kvx9cr2jHWkC3Oj/bdBTh1+yBjOC53yHlQK/l1GHrEWiWPPnE434LRxnWkwr8EHD4oieJxC8fkIxkQfj+gHhU79Z+oAAYAAAzsnf9SDIZPoDXF0TdC9POqTgld0oXDl2XPaVD4CvvLearrOSlFv+lsNbC4rgZn23MtIBM/7YQmJwmQ+FXRup6Tkubg1hpz04J/09dxg8UiZmntHiUr1GfkTOFMYqRB+Aw=="`
            },
            {
                "SigningAlg": "P256r1",
                "Value": `"hDdkJw9L2uMCORjImjMHqzNR6nYYh6QKncSl5GthQNmHmGU8a+SOqDXWwDNt3VSntpbTTQl7cMIusqweQo+JPXXWElbGh7eaxPGz4ZeF5yM2cqVNUrQr1lX/6lZ+OLuycrFrLzzB9APi0NIMLqV/Rt7XJssHQs2RPcT1ul/2XVpa6ztULJeQi2JwhTb/k48wbh/EvafG/ibrIBIx9v7/dwGRAPKHq7Uwb9hHnhpa8qNOUtjeUdIwJNh9vCBFX9s22t4PdortoFxbXo9C149PDDD4wqUHJGYlCsVX/Sqqjf7Aug3h5dwdYN6cDgsuuiOm0+aBcXBGpkh7OxVxlwXkIP+11dt23TkrSUKd0B01sc9Mc/0yEBCzx5RutKBwsefzyOl4vQX3AHgV7oD/XV73THMgGiDxQ55CPaaxN/pm791VkQ76BSZaBeF+Su6tg0k/eQneklt8Du5uqkyBHVxy8MvxsBIMZ73vIFwUrLHjDeq3+nOOyQqSBMnrHKU2mAwN3zb2LolwjPkKNOh1+NNnv99L2pBcNCnhnoBULWmWAZNXJpMx9QrcSwI9AHylcgUbGQJgf9Ryun+BgewzYNdWrXyKkp4O3ZDa4f+5SVWvbY5eyDDXcohvz/OcCtuRjAkzKBCvIjBDnCv1McjVdCO3+utizGntfhAo1RZstnOoRkgVF2WuMT9IrUmzYximuTXUmWtjyFSTqgNBZwHWUTlMmjlpLCVzZQWM4zOisXUAAALPsP34BS6EzJO5AsS5pC7QTpjBtAbLN9SdXOT9w4H1x8Nkp0ujLxWRN37IEy0V9DrPK2w1g74uqWPfUPnSBjtvM55JnQpmm23WQNvHa1Vr6zmWDjzjHpcNirPbzXyBlKEhkX4xylaSMnm4UrVXtAMaAJ/csC4HPTKr3dazdvEkhwGAAAIFByCjSp/5WHc4AhsyjMvKCsZQiKgiI8ECwjfXBaSZdY4zYsRlO3FC428H1atrFChFCZT0Bqt5LPXD38bMSB+vAUJiP8XqiEdXeqf2mYMJ5ykoDpwkve/cUQfPpjzFQlQfvwjBwiJDANKkOKoNT3bUGz+/f/pyTE+xMRdIUBZ1Bw=="`
            }
        ],
        "DeviceProfileId": `"0ff5b0c6-f149-4498-af34-21993acd52a7"`,
        "PrivateKeys": [
            {
                "SigningAlg": "Ed25519",
                "Value": `"2c24d4572327f23b9bef38097137c29224a9e979081b3d90124ac9dfa477934e"`
            },
            {
                "SigningAlg": "P256r1",
                "Value": `"38d526f29cfaf142f596deca187bd809ef71bc13435eedc885b63bb825d63def"`
            }
        ],
        "SidewalkManufacturingSn": `"843764270F4BDAE3023918C89A3307AB3351EA761887A40A9DC4A5E46B6140D9"`,
        "Status": "PROVISIONED"
    },

    ...

}
```

## Next steps

Store the JSON files,
`wireless_device.json` and
`device_profile.json` temporarily,
as you'll use them in the next step to provision and register your end device
for connecting to the hardware platform. For more information, see [Provisioning and
registering your end device](https://docs.sidewalk.amazon/provisioning/ "https://docs.sidewalk.amazon/provisioning/") in the _Amazon Sidewalk documentation_.
