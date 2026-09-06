

# Advanced configuration for AWS IoT Core Device Location
<a name="device-location-advanced-configuration"></a>

You can use the `AdvancedConfiguration` parameter to customize how AWS IoT Core Device Location resolves the location of your devices. This parameter is supported when using the [GetPositionEstimate](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPositionEstimate.html) API operation or the AWS IoT console.

**Note**  
The `AdvancedConfiguration` parameter is optional and currently supported only for the HTTP API flow. It is not supported for the MQTT or LoRaWAN device location flows.  
Existing integrations that do not use this parameter are not affected and continue to work as before. When the parameter is not specified, the default confidence level of 68 percent is used, which is the default behavior prior to the introduction of this parameter.

**Topics**
+ [WiFiCellular configuration](#device-location-advanced-configuration-wificellular)
+ [Wi-Fi payload example with AdvancedConfiguration](#device-location-advanced-configuration-wifi-example)
+ [Cellular payload example with AdvancedConfiguration](#device-location-advanced-configuration-cellular-example)

## WiFiCellular configuration
<a name="device-location-advanced-configuration-wificellular"></a>

The `WiFiCellular` configuration applies when your measurement data contains Wi-Fi, Cellular or both payload information. Use this configuration to customize the confidence level for the Wi-Fi and Cellular based solvers.

`ConfidencePercent`  
The confidence percentage used when resolving the device location with Wi-Fi or Cellular measurement data. This value determines the probability that the actual device location falls within the reported accuracy radius. Specify an integer value between 50 and 99.  
A higher confidence percentage results in a larger accuracy radius, while a lower confidence percentage results in a smaller accuracy radius. The default confidence level is 68 percent when this parameter is not specified.

**Note**  
The `WiFiCellular` configuration is used only when the measurement data contains Wi-Fi or Cellular information. If the measurement data contains only other types, such as IP address or GNSS, the `WiFiCellular` configuration is ignored.

## Wi-Fi payload example with AdvancedConfiguration
<a name="device-location-advanced-configuration-wifi-example"></a>

The following example shows a Wi-Fi measurement payload with the `AdvancedConfiguration` parameter that sets the confidence level to 95 percent.

```
{
    "Timestamp": {{1664313161}},
    "WiFiAccessPoints": [
        {
            "MacAddress": "{{A0:EC:F9:1E:32:C1}}",
            "Rss": {{-75}}
        },
        {
            "MacAddress": "{{A0:EC:F9:15:72:5E}}",
            "Rss": {{-67}}
        }
    ],
    "AdvancedConfiguration": {
        "WiFiCellular": {
            "ConfidencePercent": {{95}}
        }
    }
}
```

The following GeoJSON payload shows the resolved location with the confidence level set to 0.95, matching the requested 95 percent confidence.

```
{
    "coordinates": [
        23.864079,
        61.44683
    ],
    "type": "Point",
    "properties": {
        "horizontalAccuracy": 22,
        "horizontalConfidenceLevel": 0.95,
        "timestamp": "2026-04-03T00:13:15.134343033Z"
    }
}
```

## Cellular payload example with AdvancedConfiguration
<a name="device-location-advanced-configuration-cellular-example"></a>

The following example shows a cellular measurement payload with the `AdvancedConfiguration` parameter that sets the confidence level to 55 percent.

```
{
    "Timestamp": {{1664313161}},
    "CellTowers": {
        "Gsm": [{
            "Mcc": {{262}},
            "Mnc": {{1}},
            "Lac": {{5126}},
            "GeranCid": {{16504}},
            "GsmLocalId": {
                "Bsic": {{6}},
                "Bcch": {{82}}
            },
            "GsmTimingAdvance": {{1}},
            "RxLevel": {{-110}},
            "GsmNmr": [{
                "Bsic": {{7}},
                "Bcch": {{85}},
                "RxLevel": {{-100}},
                "GlobalIdentity": {
                    "Lac": {{1}},
                    "GeranCid": {{1}}
                }
            }]
        }],
        "Wcdma": [{
            "Mcc": {{262}},
            "Mnc": {{7}},
            "Lac": {{65535}},
            "UtranCid": {{14674663}},
            "WcdmaNmr": [{
                    "Uarfcndl": {{10786}},
                    "UtranCid": {{14674663}},
                    "Psc": {{149}}
                },
                {
                    "Uarfcndl": {{10762}},
                    "UtranCid": {{14674663}},
                    "Psc": {{211}}
                }
            ]
        }],
        "Lte": [{
            "Mcc": {{262}},
            "Mnc": {{2}},
            "EutranCid": {{2898945}},
            "Rsrp": {{-50}},
            "Rsrq": {{-5}},
            "LteNmr": [{
                    "Earfcn": {{6300}},
                    "Pci": {{237}},
                    "Rsrp": {{-60}},
                    "Rsrq": {{-6}},
                    "EutranCid": {{2898945}}
                },
                {
                    "Earfcn": {{6300}},
                    "Pci": {{442}},
                    "Rsrp": {{-70}},
                    "Rsrq": {{-7}},
                    "EutranCid": {{2898945}}
                }
            ]
        }]
    },
    "AdvancedConfiguration": {
        "WiFiCellular": {
            "ConfidencePercent": {{55}}
        }
    }
}
```

The following GeoJSON payload shows the resolved location with the confidence level set to 0.55, matching the requested 55 percent confidence.

```
{
    "coordinates": [
        13.376077,
        52.51823,
        80.1
    ],
    "type": "Point",
    "properties": {
        "verticalAccuracy": 34,
        "verticalConfidenceLevel": 0.55,
        "horizontalAccuracy": 254,
        "horizontalConfidenceLevel": 0.55,
        "timestamp": "2026-04-06T23:43:45.198088456Z"
    }
}
```