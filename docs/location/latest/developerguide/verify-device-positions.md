# Verify device positions

To check the integrity of a device position use the [VerifyDevicePosition](../APIReference/API_WaypointTracking_VerifyDevicePosition.md "../APIReference/API_WaypointTracking_VerifyDevicePosition.md") API.
This API returns information about the integrity of the device's position,
by evaluating properties such as the device's cell signal, Wi-Fi access point, Ipv4 address, and if a proxy is in use.

## Prerequisites

Before being able to use the listed APIs for device verification, make sure you have the following prerequisite:

- You have created a tracker for the device or devices you want to check. For more information, see [Get started with Amazon Location Service trackers](start-tracking.md "start-tracking.md").

The following example shows a request for the Amazon Location [VerifyDevicePosition](../APIReference/API_WaypointTracking_VerifyDevicePosition.md "../APIReference/API_WaypointTracking_VerifyDevicePosition.md") API.

API
**To verify device positions using the Amazon Location APIs**

Use the `VerifyDevicePosition` operation from the Amazon Location
Tracking APIs.

The following example shows an API request to evaluate the integrity of the position of
a device. Replace
these values with your own device IDs.

```
POST /tracking/v0/trackers/TrackerName/positions/verify HTTP/1.1
Content-type: application/json

{
   "DeviceState": {
      "Accuracy": {
         "Horizontal": number
      },
      "CellSignals": {
         "LteCellDetails": [
            {
               "CellId": number,
               "LocalId": {
                  "Earfcn": number,
                  "Pci": number
               },
               "Mcc": number,
               "Mnc": number,
               "NetworkMeasurements": [
                  {
                     "CellId": number,
                     "Earfcn": number,
                     "Pci": number,
                     "Rsrp": number,
                     "Rsrq": number
                  }
               ],
               "NrCapable": boolean,
               "Rsrp": number,
               "Rsrq": number,
               "Tac": number,
               "TimingAdvance": number
            }
         ]
      },
      "DeviceId": "ExampleDevice",
      "Ipv4Address": "string",
      "Position": [ number ],
      "SampleTime": "string",
      "WiFiAccessPoints": [
         {
            "MacAddress": "string",
            "Rss": number
         }
      ]
   },
   "DistanceUnit": "string"
}
```

###### Note

The **Integrity SDK** provides enhanced
features related to device verification, and it is available for use by request.
To get access to the SDK, contact [Sales Support](https://aws.amazon.com/contact-us/sales-support/?pg=locationprice&cta=herobtn "https://aws.amazon.com/contact-us/sales-support/?pg=locationprice&cta=herobtn").
