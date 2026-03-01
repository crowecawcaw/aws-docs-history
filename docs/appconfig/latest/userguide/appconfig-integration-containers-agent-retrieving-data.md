# Retrieving configuration data for applications running in Amazon ECS and Amazon EKS

You can retrieve configuration data from AWS AppConfig Agent for applications running in
Amazon ECS and Amazon EKS by using an HTTP localhost call. The following examples use
`curl` with an HTTP client. You can call the agent using any available HTTP
client supported by your application language or available libraries.

###### Note

To retrieve configuration data if your application uses a forward slash, for example
"test-backend/test-service", you will need to use URL encoding.

**To retrieve the full content of any deployed
configuration**

```
$ curl "http://localhost:2772/applications/`application_name`/environments/`environment_name`/configurations/`configuration_name`"
```

**To retrieve a single flag and its attributes from an AWS AppConfig
configuration of type `Feature Flag`**

```
$ curl "http://localhost:2772/applications/`application_name`/environments/`environment_name`/configurations/`configuration_name`?flag=`flag_name`"
```

**To access multiple flags and their attributes from an AWS AppConfig
configuration of type `Feature Flag`**

```

$ curl "http://localhost:2772/applications/`application_name`/environments/`environment_name`/configurations/`configuration_name`?flag=`flag_name_one`&flag=`flag_name_two`"
```

The call returns configuration metadata in HTTP headers, including the configuration
version, content type, and configuration version label (if applicable). The body of the
agent response contains the configuration content. Here is an example:

```

HTTP/1.1 200 OK
Configuration-Version: 1
Content-Type: application/json
Date: Tue, 18 Feb 2025 20:20:16 GMT
Content-Length: 31

My test config
```
