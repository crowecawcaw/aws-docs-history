# SET clause

Use the SET clause to define variables that store expression results. You can reuse these variables in SELECT and WHERE clauses, and in substitution templates. This helps you avoid duplicating complex expressions and reduce the number of function calls in your SQL statement.

The SET clause supports [Data types](iot-sql-data-types.md "iot-sql-data-types.md"), [Operators](iot-sql-operators.md "iot-sql-operators.md"), [Functions](iot-sql-functions.md "iot-sql-functions.md"), [Literals](iot-sql-literals.md "iot-sql-literals.md"), [Case statements](iot-sql-case.md "iot-sql-case.md"), [JSON extensions](iot-sql-json.md "iot-sql-json.md"), [Variables](#iot-sql-set-usage "#iot-sql-set-usage"), and [Nested object queries](iot-sql-nested-queries.md "iot-sql-nested-queries.md").

## SET clause syntax

The SET clause must appear before the SELECT clause in your SQL statement. Use the following syntax:

```
SET @variable_name = expression [, @variable_name2 = expression2]
```

Syntax rules:

- Start variable names with `@`
- Variable names can contain letters, numbers, and underscores
- Variable names can be up to 64 characters long
- Multiple variables can be set in a single SET clause, separated by commas
- Each variable can only be assigned once (variables are immutable)
- The SET keyword can only be used once per SQL statement

## Using variables

After you define variables, you can use them in:

- SELECT clauses
- WHERE clauses
- Other SET variable assignments
- Action substitution templates
- Error action substitution templates
- Nested SELECT queries
- Function parameters

Variables are referenced using the same `@variable_name` syntax used in the SET clause. You can also use JSON extension syntax to access properties of variables that contain objects, such as `@variable_name.property`.

## SET clause examples

**Basic variable usage**

The following example shows a payload published on topic `device/data`: `{"temp_fahrenheit": 75, "humidity": 60}`

SQL statement:

```
SET @temp_celsius = (temp_fahrenheit - 32) * 5 / 9
SELECT @temp_celsius AS celsius, humidity FROM 'device/data'
```

Outgoing payload: `{"celsius": 23.89, "humidity": 60}`

**Access members in embedded JSON objects**

The following example shows a payload published on topic `device/data`: `{"device1": {"deviceId":"weather_sensor", "deviceData": {"sensors": {"temp_fahrenheit": 75, "humidity": 60}, "location": [47.606,-122.332]}}}`

SQL statement:

```
SET @device_sensor_data = device1.deviceData.sensors
SELECT @device_sensor_data.temp_fahrenheit AS temp_fahrenheit, @device_sensor_data.humidity as humidity, device1.deviceId as deviceId FROM 'device/data'
```

Outgoing payload: `{"temp_fahrenheit":75,"humidity":60,"deviceId":"weather_sensor"}`

for more information on how to work with JSON extensions, reference [JSON extensions](iot-sql-json.md "iot-sql-json.md")

**Avoiding duplicate function calls**

SET variables help avoid duplicating complex decode operations:

```
SET @decoded_data = decode(encode(*, 'base64'), 'proto', 'schema', 'schema.desc', 'message.proto', 'Message')
SELECT @decoded_data.sensor_id, @decoded_data.reading FROM 'device/protobuf'
WHERE @decoded_data.reading > 100
```

Without SET variables, you would need to repeat the decode function three times, which exceeds the function call limits.

**Multiple variables**

You can define multiple variables in a single SET clause by separating them with commas:

```
SET @user_data = get_user_properties(device_id), @threshold = 50
SELECT @user_data.name, temp_fahrenheit FROM 'sensors/+'
WHERE temp_fahrenheit > @threshold AND @user_data.active = true
```

**Using variables in substitution templates**

Variables can also be used in action substitution templates, allowing you to reuse computed values across both the SQL statement and rule actions.

SQL statement:

```
SET @temp_celsius = (temp_fahrenheit - 32) * 5 / 9
SELECT @temp_celsius AS celsius, humidity FROM 'device/data'
```

Action configuration:

```
{
  "s3": {
    "roleArn": "arn:aws:iam::123456789012:role/testRuleRole",
    "bucketName": "bucket",
    "key": "temperature-data/${device_id}/temp-${@temp_celsius}C.json"
  }
}
```

In this example, the SET variable `@temp_celsius` is used in a substitution template to construct the key field of the S3 action.

**Non-JSON payload usage**

SET variables does not support non-JSON payloads directly, so the payload must be encoded or decoded first:

```
SET @encoded_payload = encode(*, 'base64')
SELECT @encoded_payload AS raw_data FROM 'device/binary'
```

for more information on how to work with non-JSON payloads, reference [Working with binary payloads](binary-payloads.md "binary-payloads.md")

## SET clause limits

The following limits apply to SET variables:

- Maximum of 10 unique variables per SQL statement
- Maximum variable value size of 128 KiB (minified UTF-8 JSON string)
- Maximum total value size of 128 KiB for all variables
- Variable names limited to 64 characters
- Variables can accept JSON payloads directly as is (non-JSON payloads must first be encoded/decoded)
