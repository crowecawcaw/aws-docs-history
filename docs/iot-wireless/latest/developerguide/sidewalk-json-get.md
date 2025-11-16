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

Use the [`GetDeviceProfile`](../apireference/API_GetDeviceProfile.md "../apireference/API_GetDeviceProfile.md") API operation or the [`get-device-profile`](../../../cli/latest/reference/get-device-profile.md "../../../cli/latest/reference/get-device-profile.md") CLI command to get
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
[`GetDeviceProfile`](../apireference/API_GetDeviceProfile.md "../apireference/API_GetDeviceProfile.md").

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

Use the [`GetWirelessDevice`](../apireference/API_GetWirelessDevice.md "../apireference/API_GetWirelessDevice.md") API operation or the [`get-wireless-device`](../../../cli/latest/reference/get-wireless-device.md "../../../cli/latest/reference/get-wireless-device.md") CLI command to get
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
information about the parameters in the API response, see [`GetWirelessDevice`](../apireference/API_GetWirelessDevice.md "../apireference/API_GetWirelessDevice.md").

**`GetWirelessDevice` API response
(Contents of
`wireless_device.json`)**

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:WirelessDevice/`23456789-abcd-0123-bcde-fabc012345678`",
    "Description": "`test-description`",
    "DestinationName": `"SidewalkDestination"`,
    "Id": "`23456789-abcd-0123-bcde-fabc012345678`",
    "LoRaWAN": "null",
    "Name" : "`test-name`",
    "Positioning": "`Enabled`"
    "Sidewalk": {
        "CertificateId": `"4C7438772D50524F544F54595045"`,
        "DeviceCertificates": [
            {
                "SigningAlg": "Ed25519",
                "Value": "`WUqB/E50VP7oZpHtYoBgpzJXYvhv51y/DBIfzNhrleo4UzOWCsIzbaJwft
 +IPBSUQthDifJDYik0DuU1jLvuR8cpK7YyI7cUD/oZG+4Pro/s3nAIhy
 XmhUlepmbveVxM8boiTiaUlL4iB9DoKrB41pWdHeg7hR8BDrE1m4sf5Q
 9ZUwDy5BqMafeW0RUKZMVunpChji0dwC5VoSSb8IT7V+bKTJXXdZ8lP1
 1jsiuJfwF64Eq1NCe2qKb7gql5u+qBE7vatDOSonwN56I6Ah8HWYRSyJ
 Tk7DSJKknSY7KGyLjs0qMI8L8AeJ++UIO/jOsGnhC6Ku1ba62bEPmIBr
 +889NhOngiIt1+1DrSOO59a1PLYqfVa5ejKq0tzzbyNG/m/oW72kkGGH
 Ruec2zOXEO86kf4X0qzFfTKoo/6lt67XfXIQkO4wApCgJ8AHwHa3xz+d
 h+W6mFwYFRqrQQT8s0SjSuDtLCaqZhnch47MZk7E/itqP4JnJ7RsJHWx
 XsG2gTNlRghfG+zhpKzVVdvVVZeZ22f2WZ2QoGlzXxrW0/b7mqpO2l+8
 fzRYYdqAp1AAADGz+gFBeX/ZNN8VJwnsNfgzj4me1HgVJdUo4W9kvx9c
 r2jHWkC3Oj/bdBTh1+yBjOC53yHlQK/l1GHrEWiWPPnE434LRxnWkwr8
 EHD4oieJxC8fkIxkQfj+gHh`"
            },
            {
                "SigningAlg": "P256r1",
                "Value": "`hDdkJw9L2uMCORjImjMHqzNR6nYYh6QKncSl5GthQNmHmGU8a+SOqDXWwDNt3
 VSntpbTTQl7cMIusqweQo+JPXXWElbGh7eaxPGz4ZeF5yM2cqVNUrQr1l
 X/6lZ+OLuycrFrLzzB9APi0NIMLqV/Rt7XJssHQs2RPcT1ul/2XVpa6zt
 ULJeQi2JwhTb/k48wbh/EvafG/ibrIp4O3ZDa4f+5SVWvbY5eyDDXcohv
 z/OcCtuRjAkzKBCvIjBDnCv1McjVdCO3+utizGntfhAo1RZstnOoRkgVF
 2WuMT9IrUmzYximuTXUmWtjyFSTqgNBZwHWUTlMmjlpLCVzZQWM4zOisX
 UAAALPsP34BS6EzJO5AsS5pC7QTpjBtAbLN9SdXOT9w4H1x8Nkp0ujLxW
 RN37IEy0V9DrPK2w1g74uqWPfUPnSBjtvM55JnQpmm23WQNvHa1Vr6zmW
 DjzjHpcNirPbzXyBlKEhkX4xylaSMnm4UrVXtAMaAJ/csC4HPTKr3dazd
 vEkhwGAAAIFByCjSp/5WHc4AhsyjMvKCsZQiKgiI8ECwjfXBaSZdY4zYs
 RlO3FC428H1atrFChFCZT0Bqt5LPXD38bMSB+vAUJiP8XqiEdXeqf2mYM
 J5ykoDpwkve/cUQfPpjzFQlQfvwjBwiJDANKkOKoNT3bUGz+/f/pyTE+x
 MRdIUBZ1Bw==`"
            }
        ],
        "DeviceProfileId":"`0ff5b0c6-f149-4498-af34-21993acd52a7`",
        "Positioning": {
                        "DestinationName": `"SidewalkLocationDestination"`,
                        },
        "PrivateKeys": [
            {
                "SigningAlg": "Ed25519",
                "Value": "`2c24d4572327f23b9bef38097137c29224a9e979081b3d90124ac9dfa477934e`"
            },
            {
                "SigningAlg": "P256r1",
                "Value": "`38d526f29cfaf142f596deca187bd809ef71bc13435eedc885b63bb825d63def`"
            }
        ],
        "SidewalkManufacturingSn": "`843764270F4BDAE3023918C89A3307AB3351EA761887A40A9DC
 4A5E46B6140D9`",
        "Status": "`PROVISIONED`"
    },
    "Type": "Sidewalk",

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
