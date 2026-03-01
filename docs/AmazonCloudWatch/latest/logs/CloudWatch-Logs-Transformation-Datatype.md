# Datatype converter processors

This section contains information about the datatype converter processors that you can use with a log event
transformer.

###### Contents

- [typeConverter](CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-typeConverter "CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-typeConverter")
- [datetimeConverter](CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-datetimeConverter "CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-datetimeConverter")

## typeConverter

Use the `typeConverter` processor to convert a value type
associated with the specified key to the specified type. It's a casting
processor that changes the types of the specified fields. Values can be
converted into one of the following datatypes: `integer`,
`double`, `string` and `boolean`.

| Field   | Description                                                                                 | Required? | Default | Limits                                             |
| ------- | ------------------------------------------------------------------------------------------- | --------- | ------- | -------------------------------------------------- |
| entries | Array of entries. Each item in the array must contain<br>`key` and `type` fields.           | Yes       |         | Maximum entries: 10                                |
| key     | The key with the value that is to be converted to a different<br>type                       | Yes       |         | Maximum length: 128<br>Maximum nested key depth: 3 |
| type    | The type to convert to. Valid values are<br>`integer`, `double`, `string`<br>and `boolean`. | Yes       |         |                                                    |

**Example**

Take the following example log event:

```
{
    "name": "value",
    "status": "200"
}
```

The transformer configuration is this, using `typeConverter` with
`parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "typeConverter": {
            "entries": [
                {
                    "key": "status",
                    "type": "integer"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
    "name": "value",
    "status": 200
}
```

## datetimeConverter

Use the `datetimeConverter` processor to convert a datetime string
into a format that you specify.

| Field          | Description                                                                                                                                                                                                                                                                                                                                 | Required? | Default                       | Limits                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------- | -------------------------------------------------- |
| source         | The key to apply the date conversion to.                                                                                                                                                                                                                                                                                                    | Yes       |                               | Maximum entries: 10                                |
| matchPatterns  | A list of patterns to match against the `source`<br>field                                                                                                                                                                                                                                                                                   | Yes       |                               | Maximum entries: 5                                 |
| target         | The JSON field to store the result in.                                                                                                                                                                                                                                                                                                      | Yes       |                               | Maximum length: 128<br>Maximum nested key depth: 3 |
| targetFormat   | The datetime format to use for the converted data in the<br>target field.                                                                                                                                                                                                                                                                   | No        | `yyyy-MM-dd'T'HH:mm:ss.SSS'Z` | Maximum length:64                                  |
| sourceTimezone | The time zone of the source field.<br>For a list of possible values, see [Java Supported Zone Ids and<br>Offsets](https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets "https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets"). | No        | UTC                           | Minimum length:1                                   |
| targetTimezone | The time zone of the target field.<br>For a list of possible values, see [Java Supported Zone Ids and<br>Offsets](https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets "https://howtodoinjava.com/java/date-time/supported-zone-ids-offsets/#3-java-supported-zone-ids-and-offsets"). | No        | UTC                           | Minimum length:1                                   |
| locale         | The locale of the source field.<br>For a list of possible values, see [Locale getAvailableLocales() Method in Java with<br>Examples](https://www.geeksforgeeks.org/locale-getavailablelocales-method-in-java-with-examples/ "https://www.geeksforgeeks.org/locale-getavailablelocales-method-in-java-with-examples/").                      | Yes       |                               | Minimum length:1                                   |

**Example**

Take the following example log event:

```
{"german_datetime": "Samstag 05. Dezember 1998 11:00:00"}
```

The transformer configuration is this, using `dateTimeConverter`
with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "dateTimeConverter": {
            "source": "german_datetime",
            "target": "target_1",
            "locale": "de",
            "matchPatterns": ["EEEE dd. MMMM yyyy HH:mm:ss"],
            "sourceTimezone": "Europe/Berlin",
            "targetTimezone": "America/New_York",
            "targetFormat": "yyyy-MM-dd'T'HH:mm:ss z"
        }
    }
]
```

The transformed log event would be the following.

```
{
    "german_datetime": "Samstag 05. Dezember 1998 11:00:00",
    "target_1": "1998-12-05T17:00:00 MEZ"
}
```
