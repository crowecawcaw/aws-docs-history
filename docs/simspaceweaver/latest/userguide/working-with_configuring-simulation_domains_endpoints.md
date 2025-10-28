End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Network endpoints

Custom and service apps can have network endpoints that external clients can connect
to. You specify a list of port numbers as the value for `ingress_ports` in
the `endpoint_config`. These port numbers are both TCP and UDP. The custom or
service app should bind to the port numbers that you specify in
`ingress_ports`. SimSpace Weaver dynamically allocates port numbers at
runtime and maps these ports to the dynamic ports. You can call the describe-app API after your apps have started to find the
dynamic (actual) port numbers. For more information, see [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md") from the quick start
tutorial.

```
domains:
  MyViewDomain:
    launch_apps_via_start_app_call: {}
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MyViewApp.zip"
      launch_command: ["MyViewApp"]
      required_resource_units:
        compute: 1
      **endpoint\_config:
 ingress\_ports:
 - 7000**

```

###### Note

SimSpace Weaver app SDK
version 1.12.x projects use separate buckets for the app .zip files
and the schema:

- weaver-`lowercase-project-name`-`account-number`-app-zips-`region`
- weaver-`lowercase-project-name`-`account-number`-schemas-`region`

###### Note

`endpoint_config` is an optional property for custom apps and service apps. If you don't specify
an `endpoint_config` then the app won't have a network endpoint.
