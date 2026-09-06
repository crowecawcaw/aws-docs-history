

# Template Variables, Filters and Macros
<a name="supported-jinja-parameters"></a>

 Amazon MWAA Serverless supports [Jinja templates](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) that come out of the box with Apache Airflow. Please refer below for the supported list of Jinja Variables, and Macros. 

**Topics**
+ [Supported Jinja template Variables](#jinja-variables)
+ [Supported Macros](#jinja-macros)

## Supported Jinja template Variables
<a name="jinja-variables"></a>

 The following table lists the supported Vriabls available for Jinja templating in Amazon MWAA Serverless. 


| Variable | Type | Description | 
| --- | --- | --- | 
| {{ macros }} |  | A reference to the macros package. See Macros below. | 
| {{ task\_instance }} | TaskInstance | The currently running TaskInstance. | 
| {{ ti }} | TaskInstance | Same as {{ task\_instance }}. | 
| {{ params }} | dict[str, Any] | The user-defined params. This can be overridden by the mapping passed to trigger\_dag -c if dag\_run\_conf\_overrides\_params is enabled in airflow.cfg. | 
| {{ ds }} | str | The Dag run's logical date as YYYY-MM-DD. Same as {{ logical\_date \\\| ds }}. | 
| {{ ds\_nodash }} | str | Same as {{ logical\_date \\\| ds\_nodash }}. | 
| {{ ts }} | str | Same as {{ logical\_date \\\| ts }}. Example: 2018-01-01T00:00:00\+00:00. | 
| {{ ts\_nodash }} | str | Same as {{ logical\_date \\\| ts\_nodash }}. Example: 20180101T000000. | 
| {{ macros }} |  |  | 

## Supported Macros
<a name="jinja-macros"></a>

 The following table lists the supported Macros that are supported in Amazon MWAA Serverless. 


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