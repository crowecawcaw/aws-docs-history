# Converting unsupported data types

Optionally enable data type conversion in AWS IoT SiteWise for simple arrays and
DateTime data types. AWS IoT SiteWise doesn't support all OPC UA data types. When you send
unsupported data to your AWS IoT Greengrass data stream, that data is lost. However, by
converting the unsupported native data types to strings, you can ingest the data
into AWS IoT SiteWise rather than discarding it. AWS IoT SiteWise serializes your converted data so
that you can later use your own functions to convert the strings back to their
original data type downstream, if needed.

You can update your data type conversion settings for a data source at any
time and each data source can have its own settings.

When you add data sources in the AWS IoT SiteWise console, there are two checkboxes under
**Data type conversion** in **Advanced
Configuration**. You can indicate which data types to convert to
strings.

Additionally, the IoT SiteWise OPC UA collector can accept NaN or null values on the
edge.

- Convert array values with simple data types to JSON strings
- Convert DateTime values to ISO 8601 strings

## Prerequisite

- Use version 2.5.0 or later of the [IoT SiteWise OPC UA collector](../../../greengrass/v2/developerguide/iotsitewise-opcua-collector-component.md "../../../greengrass/v2/developerguide/iotsitewise-opcua-collector-component.md").

## Limitations

These are the limitations for OPC UA data type conversion to strings in
AWS IoT SiteWise.

- Complex data type conversion is not supported.
- String limits after conversion are 1024 bytes. If the string is
  longer than 1024 bytes, the string is rejected by AWS IoT SiteWise.
