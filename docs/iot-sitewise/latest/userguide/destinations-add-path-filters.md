# Add path filters to AWS IoT SiteWise Edge

destinations

Add path filters to a destination. Path filters use MQTT topic syntax, where
`#` is a wildcard character that matches any number of levels, and `+`
is a wildcard character that matches a single level. You can add multiple destinations to a
gateway, each with its own set of path filters subscribed to your equipment telemetry.

Siemens Industrial Edge gateways use a prefix for compatibility. For more information, see [Prefixes for path filters](sitewise-edge-on-siemens.md#siemens-path-filters "sitewise-edge-on-siemens.md#siemens-path-filters").

Console

###### To add path filters

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the gateway to which you want to add path filters.
4. In the **Path filters** section under **Add
   destination**, choose **Add path filter**.
5. Enter the path filter that you want this destination to subscribe to. You can
   use wildcard characters (`#` and `+`) to subscribe to multiple
   paths.
6. Choose **Add path filter** to add the path filter to the
   list.
7. Repeat steps to add additional path filters, if needed.
8. Once you have added all of the required path filters, choose
   **Create**.

AWS CLI for self-hosted gateways

###### Example : Path filter configuration

```

{
  "destinations": [
    {
      ...
    }
  ],
  "filters": [
    {
      "type": "PATH",
      "config": {
        "paths": [
          "home/+/sensor1/temperature",
          "home/livingroom/sensor1/temperature",
          "home/livingroom/sensor1/temperature",
          "building/#"
        ]
      }
    }
  ]
}
```

AWS CLI for Siemens IEgateways

###### Example : Prefix configuration for path filters

Capture all data by using both the data (`ie/d`) and metadata
(`ie/m`) prefixes for each path filter.

```

{
  "destinations": [
    {
      ...
    }
  ],
  "filters": [
    {
      "type": "PATH",
      "config": {
        "paths": [
          "ie/d/home/+/sensor12/temperature",
          "ie/m/home/livingroom/sensor12/temperature",
          "ie/d/home/livingroom/sensor13/temperature2",
          "ie/m/home/livingroom/sensor13/temperature2",
          "ie/d/building/#",
          "ie/m/building/#"
        ]
      }
    }
  ]
}
```

###### Note

Copy path filters between destinations by downloading list of path filters. For more
information, see [Download all path filters in a
destination (console)](destinations-manage.md#destinations-download-list "destinations-manage.md#destinations-download-list").

## Upload path filters in bulk

To upload path filters in bulk, use a CSV or text file. AWS IoT SiteWise automatically removes
exact duplicates when you upload files. For example, `windfarm/site1/` and
`windfarm/site1/` are exact duplicates that AWS IoT SiteWise catches because the string
is exactly the same. Partial duplicates are not removed and result in additional charges.
For example, `windfarm/#` and `windfarm/site1` are overlapping topics
because `windfarm/site1` is already encompassed by
`windfarm/#`.

###### Note

Avoid duplicates to prevent additional charges. The uploaded file must be in either
.csv or .txt format. It can't contain any headers and should consist of a single column.
In the column, list your path filters, with each filter on a separate line. No other
information should be included in the file.

###### File upload requirements

These are additional path filter requirements.

- You can upload one .csv or .txt file. Other file formats are not supported.
- CSV (.csv) files cannot have headers and should only contain one column.
- You can have one path filter on each line.
- The uploaded files cannot be empty.
- When using `#` as a wildcard, it must be the last character in the topic
  filter. For example, `topic/#` or as a standalone character at a particular
  topic level. However, note that `#` can also be used as a regular character
  within a topic level name, such as `factory/machine#1/topic`. For more
  information see [Special characters in path filter
  names](gw-destinations.md#path-filters-special-characters "gw-destinations.md#path-filters-special-characters")
  - You can also use the `+` character. For example, use
    `factory/+/temp` to get all temperatures for factories instead of
    `factory/machine2/temp` and `factory/machine3/temp`
    individually.
