# Understanding IPv6 support

All AWS AppConfig APIs fully support IPv4 and IPv6 calls.

**Control plane APIs**

Use the following endpoint for IPv4 and IPv6 dual-stack calls to the [control
plane](../../2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md "../../2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md"):

```
appconfig.`Region`.api.aws
```

For example: appconfig.us-east-1.api.aws

For IPv4 only, use the following URL:

```
appconfig.`Region`.amazonaws.com
```

**Data plane APIs**

For dual-stack calls to the [data
plane](../../2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md "../../2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md"), use the following endpoint:

```
appconfigdata.`Region`.api.aws
```

For example: appconfig.us-east-1.api.aws

For IPv4 only, use the following URL:

```
appconfigdata.`Region`.amazonaws.com
```

###### Note

For more information, see [AWS AppConfig endpoints and quotas](../../../general/latest/gr/appconfig.md "../../../general/latest/gr/appconfig.md") in
the _AWS General Reference_.
