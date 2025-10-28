End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Custom domain configuration

To specify the properties for a custom domain, replace
`custom-domain-name` with a name of your choice.
The name must be 3-64 characters long and can contain the characters **A** -**Z** , **a** -**z** , **0** -**9** , and **\_ -** (hyphen). Specify the properties of the custom
domain after the name. Repeat this process for each custom domain.

```
  `custom-domain-name`:
    launch_apps_via_start_app_call: {}
    app_config:
      package: "`app-package-s3-uri`"
      launch_command: ["`app-launch-command`"`, "parameter1", ...`]
      required_resource_units:
        compute: `app-resource-units`
      endpoint_config:
        ingress_ports: [`port1, port2, ...`]
    image: "`ecr-repository-uri`"

```

**Properties**

`launch_apps_via_start_app_call`

This property is required to launch your custom apps using the
StartApp API.

_Required:_ Yes

_Type:_ N/A

_Valid values:_
`{}`

## Custom app configuration

The `app_config section` (required) specifies the package, launch
configuration, resource requirements, and network ports for apps in this
custom domain.

```
    app_config:
      package: "`app-package-s3-uri`"
      launch_command: ["`app-launch-command`"`, "parameter1", ...`]
      required_resource_units:
        compute: `app-resource-units`
      endpoint_config:
        ingress_ports: [`port1, port2, ...`]

```

**Properties**

`package`

Specifies the package (zip file) that contains the app
executable/binary. The package must be stored in an Amazon S3 bucket.
Only zip file format is supported.

_Required:_ Yes

_Type:_ String

_Valid values:_
The Amazon S3 URI of the package in an Amazon S3 bucket.
For example, `s3://weaver-myproject-111122223333-app-zips-us-west-2/MyCustomApp.zip`.

`launch_command`

Specifies the executable/binary file name and command-line
parameters to launch the app. Each command-line string token is
an element in the array.

_Required:_ Yes

_Type:_ String array

`required_resource_units`

Specifies the number of resource units that SimSpace Weaver
should allocate to each instance of this app. A _resource unit_ is a fixed amount of
virtual central processing units (vCPUs) and random-access
memory (RAM) on a worker. For more information about resource
units, see [Endpoints and service quotas](service-quotas.md "service-quotas.md"). The
`compute` property specifies a resource unit
allocation for the `compute` family of workers, and
is currently the only valid type of allocation.

_Required:_ Yes

_Type:_ Integer

_Valid values:_
`1`-`4`

`endpoint_config`

Specifies the network endpoints for apps in this domain. The
value of `ingress_ports` specifies the ports that your
custom apps
bind to for incoming client connections. SimSpace Weaver maps
dynamically allocated ports to your specified ingress ports.
Ingress ports are both TCP and UDP. Use the DescribeApp API to find the actual
port number to connect your clients.

_Required:_ No. If you don't specify
endpoint configuration then your custom apps in this domain
won't have network endpoints.

_Type:_ Integer array

_Valid values:_
`1024`-`49152`. Values must be
unique.

## Custom container image

The `image` property (optional) specifies the location of a container image
that SimSpace Weaver uses to run apps in this domain (not supported in versions `1.13` and
`1.12`). Provide the URI to a repository in
Amazon Elastic Container Registry (Amazon ECR) that contains the image. If this property isn't specified but
the `default_image` is specified in the top level `simulation_properties`
section, apps in this domain use the `default_image`. For more information, see
[Custom containers](working-with_custom-containers.md "working-with_custom-containers.md").

```
    image: "`ecr-repository-uri`"
```

**Properties**

`image`

Specifies the location of a container image to run apps in this domain.

_Required:_ No

_Type:_ String

_Valid values:_

- The URI of a repository in Amazon Elastic Container Registry (Amazon ECR) (for example,
  `111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest`)
