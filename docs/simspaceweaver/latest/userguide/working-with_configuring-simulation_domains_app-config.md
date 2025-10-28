End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# App configuration

You specify the configuration of an app (`app_config`) as part of the configuration for
its domain. All types of domains use these same app configuration properties.

```

    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MyViewApp.zip"
      launch_command: ["MyViewApp"]
      required_resource_units:
        compute: 1

```

###### Note

SimSpace Weaver app SDK
version 1.12.x projects use separate buckets for the app .zip files
and the schema:

- weaver-`lowercase-project-name`-`account-number`-app-zips-`region`
- weaver-`lowercase-project-name`-`account-number`-schemas-`region`
  The `package` property specifies the S3 URI of a zip file in an S3 bucket. The zip file
  contains the app executable (also called a _binary_ )
  and any other resources that it needs (such as libraries). Each instance of the app
  executable runs in a Docker container on a worker.

The `launch_command` property specifies the name of the executable and any command-line
options to run the app. The value of `launch_command` is an array. Each token of the
entire launch command string is an element in the array.

###### Example

- For the launch command: `MyTestApp --option1 value1`
- Specify: `launch_command: ["MyTestApp", "-option1", "value1"]`
  The `required_resource_units` property specifies the number of compute resource units
  that SimSpace Weaver should allocate to this app. A compute resource unit is a fixed
  amount of processing capacity (vCPU) and memory (RAM) on a worker. You can increase this
  value to increase the amount of computing power available to the app when it runs on a
  worker. There is a limited number of compute resource units on each worker. For more
  information, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").
