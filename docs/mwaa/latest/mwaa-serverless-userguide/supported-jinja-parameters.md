

# Template variables, filters, and macros
<a name="supported-jinja-parameters"></a>

 Amazon MWAA Serverless supports [Jinja templates](https://airflow.apache.org/docs/apache-airflow/3.0.6/templates-ref.html) that come out of the box with Apache Airflow. The following tables list the supported Jinja variables and macros. 

**Topics**
+ [Supported Jinja template variables](#jinja-variables)
+ [Supported macros](#jinja-macros)

## Supported Jinja template variables
<a name="jinja-variables"></a>

 The following table lists the variables that you can use for Jinja templating in Amazon MWAA Serverless. 


| Variable | Type | Description | 
| --- | --- | --- | 
| {{ macros }} |  | A reference to the macros package. For more information, see [Supported macros](#jinja-macros). | 
| {{ task\_instance }} | TaskInstance | The currently running TaskInstance. | 
| {{ ti }} | TaskInstance | Same as {{ task\_instance }}. | 
| {{ params }} | dict[str, Any] | The user-defined params. This can be overridden by the mapping passed to trigger\_dag -c if dag\_run\_conf\_overrides\_params is enabled in airflow.cfg. | 
| {{ ds }} | str | The Dag run's logical date as YYYY-MM-DD. Same as {{ logical\_date \\\| ds }}. | 
| {{ ds\_nodash }} | str | Same as {{ logical\_date \\\| ds\_nodash }}. | 
| {{ ts }} | str | Same as {{ logical\_date \\\| ts }}. Example: 2018-01-01T00:00:00\+00:00. | 
| {{ ts\_nodash }} | str | Same as {{ logical\_date \\\| ts\_nodash }}. Example: 20180101T000000. | 
| {{ var.value.{{key}} }} | str | The value of the Apache Airflow variable {{key}}. To return a default when the variable doesn't exist, use {{ var.value.get('{{key}}', '{{default}}') }}. For more information about where Apache Airflow reads variables from, see [How Amazon MWAA Serverless looks up connections and variables](connections.md#connections-lookup-order). | 
| {{ var.json.{{key}} }} | Any | The Apache Airflow variable {{key}}, parsed as JSON. | 
| {{ conn.{{conn\_id}} }} | Connection | The Apache Airflow connection {{conn\_id}}. Access its fields as attributes, such as {{ conn.{{conn\_id}}.host }} or {{ conn.{{conn\_id}}.port }}. | 

## Supported macros
<a name="jinja-macros"></a>

 The following table lists the macros that Amazon MWAA Serverless supports. 


| Macro | Type | 
| --- | --- | 
| macros.datetime | The standard lib's datetime.datetime | 
| macros.timedelta | The standard lib's datetime.timedelta | 
| macros.dateutil | A reference to the dateutil package | 
| macros.time | The standard lib's time | 
| macros.uuid | The standard lib's uuid | 
| macros.random | The standard lib's random.random | 
| datetime\_diff\_for\_humans | datetime\_diff\_for\_humans(dt, since=None): Return a human-readable/approximate difference between datetimes. When only one datetime is provided, the comparison will be based on now. | 
| ds\_add | ds\_add(ds, days): Add or subtract days from a YYYY-MM-DD. | 
| ds\_format | ds\_format(ds, input\_format, output\_format): Output datetime string in a given format. | 
| random | The standard lib's random.random | 