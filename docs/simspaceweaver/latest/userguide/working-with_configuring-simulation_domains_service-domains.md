End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Configuring service domains

The presence of `launch_apps_per_worker:` in a domain configuration indicates that it
is a service domain that has service apps. SimSpace Weaver starts and stops service
apps for you. When SimSpace Weaver starts and stops an app, the app is considered to
have a _managed lifecycle_ . SimSpace Weaver currently
supports starting 1 or 2 service apps on each and every worker.

###### Example of a domain configured to launch 1 service app on each worker

```

domains:
  MyServiceDomain:
    **launch\_apps\_per\_worker:
 count: 1**
    app_config:
      package: "s3://weaver-myproject-111122223333-app-zips-us-west-2/PlayerConnectionServiceApp.zip"
      launch_command: ["PlayerConnectionServiceApp"]
      required_resource_units:
        compute: 1
      endpoint_config:
        ingress_ports:
          - 9000
          - 9001

```

###### Example of a domain configured to launch 2 service apps on each worker

```

domains:
  MyServiceDomain:
    **launch\_apps\_per\_worker:
 count: 2**
    app_config:
      package: "s3://weaver-myproject-111122223333-app-zips-us-west-2/PlayerConnectionServiceApp.zip"
      launch_command: ["PlayerConnectionServiceApp"]
      required_resource_units:
        compute: 1
      endpoint_config:
        ingress_ports:
          - 9000
          - 9001

```
