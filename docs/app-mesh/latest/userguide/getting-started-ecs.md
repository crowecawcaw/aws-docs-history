# Getting started with AWS App Mesh and Amazon ECS

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

This topic helps you use AWS App Mesh with an actual service that is running on Amazon ECS. This tutorial covers
basic features of several App Mesh resource types.

## Scenario

To illustrate how to use App Mesh, assume that you have an application with the
following characteristics:

- Consists of two services named `serviceA` and
  `serviceB`.
- Both services are registered to a namespace named
  `apps.local`.
- `ServiceA` communicates with `serviceB` over HTTP/2,
  port 80.
- You have already deployed version 2 of `serviceB` and registered
  it with the name `serviceBv2` in the `apps.local`
  namespace.

You have the following requirements:

- You want to send 75 percent of the traffic from `serviceA` to
  `serviceB` and 25 percent of the traffic to `serviceBv2`
  first. By only sending 25 percent to `serviceBv2`, you can validate
  that it's bug free before you send 100 percent of the traffic from `serviceA`.
- You want to be able to easily adjust the traffic weighting so that 100 percent
  of the traffic goes to `serviceBv2` once it is proven to be reliable.
  Once all traffic is being sent to `serviceBv2`, you want to discontinue
  `serviceB`.
- You do not want to have to change any existing application code or service
  discovery registration for your actual services to meet the previous
  requirements.

To meet your requirements, you decide to create an App Mesh service mesh with
virtual services, virtual nodes, a virtual router, and a route. After implementing your
mesh, you update your services to use the Envoy proxy. Once updated, your services
communicate with each other through the Envoy proxy rather than directly with each
other.

## Prerequisites

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

- An existing understanding of App Mesh concepts. For more information, see [What Is AWS App Mesh?](what-is-app-mesh.md "what-is-app-mesh.md").
- An existing understanding of Amazon ECSs concepts. For more information, see [What is
  Amazon ECS](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md") in the Amazon Elastic Container Service Developer Guide.
- App Mesh supports Linux services that are registered with DNS, AWS Cloud Map, or both. To use this
  getting started guide, we recommend that you have three existing services that are registered
  with DNS. The procedures in this topic assume that the existing services are named
  `serviceA`, `serviceB`, and `serviceBv2` and that all
  services are discoverable through a namespace named `apps.local`.

You can create a service mesh and its resources even if the services don't exist, but
you cannot use the mesh until you have deployed actual services. For more information about
service discovery on Amazon ECS, see [Service
Discovery](../../../AmazonECS/latest/developerguide/service-discovery.md "../../../AmazonECS/latest/developerguide/service-discovery.md"). To create an Amazon ECS service with service discovery, see [Tutorial: Creating a Service Using Service
Discovery](../../../AmazonECS/latest/developerguide/create-service-discovery.md "../../../AmazonECS/latest/developerguide/create-service-discovery.md"). If you don't already have services running, you can [Create an Amazon ECS service with service
discovery](../../../AmazonECS/latest/developerguide/create-service-discovery.md "../../../AmazonECS/latest/developerguide/create-service-discovery.md").

## Step 1: Create a mesh and virtual

service

A service mesh is a logical boundary for network traffic between the services that reside
within it. For more information, see [Service Meshes](meshes.md "meshes.md"). A
virtual service is an abstraction of an actual service. For more information, see [Virtual services](virtual_services.md "virtual_services.md").

Create the following resources:

- A mesh named `apps`, since all of the services in the scenario are
  registered to the `apps.local` namespace.
- A virtual service named `serviceb.apps.local`, since the virtual
  service represents a service that is discoverable with that name, and you
  don't want to change your code to reference another name. A virtual service
  named `servicea.apps.local` is added in a later step.

You can use the AWS Management Console or the AWS CLI version 1.18.116 or higher or
2.0.38 or higher to complete the following steps. If using the AWS CLI,
use the `aws --version` command to check your installed AWS CLI version. If you
don't have version 1.18.116 or higher or 2.0.38 or
higher installed, then you must [install
or update the AWS CLI](../../../cli/latest/reference/appmesh/cli-chap-install.md "../../../cli/latest/reference/appmesh/cli-chap-install.md"). Select the tab for the tool that you want to
use.

AWS Management Console

1. Open the App Mesh console first-run wizard at [https://console.aws.amazon.com/appmesh/get-started](https://console.aws.amazon.com/appmesh/get-started "https://console.aws.amazon.com/appmesh/get-started").
2. For **Mesh name**, enter
   `apps`.
3. For **Virtual service name**, enter
   `serviceb.apps.local`.
4. To continue, choose **Next**.

AWS CLI

1. Create a mesh with the `create-mesh` command.

```
`aws appmesh create-mesh --mesh-name apps`
```

2. Create a virtual service with the `create-virtual-service` command.

```
`aws appmesh create-virtual-service --mesh-name apps --virtual-service-name serviceb.apps.local --spec {}`
```

## Step 2: Create a virtual node

A virtual node acts as a logical pointer to an actual service. For more information, see
[Virtual nodes](virtual_nodes.md "virtual_nodes.md").

Create a virtual node named `serviceB`, since one of the virtual nodes
represents the actual service named `serviceB`. The actual service that the
virtual node represents is discoverable through `DNS` with a hostname of
`serviceb.apps.local`. Alternately, you can discover actual services
using AWS Cloud Map. The virtual node will listen for traffic using the HTTP/2 protocol on port 80. Other protocols are also supported, as are health checks. You will create virtual
nodes for `serviceA` and `serviceBv2` in a later step.

AWS Management Console

1. For **Virtual node name**, enter
   `serviceB`.
2. For **Service discovery method**, choose
   **DNS** and enter
   `serviceb.apps.local` for **DNS
   hostname**.
3. Under **Listener configuration**, choose
   **http2** for **Protocol** and
   enter `80` for
   **Port**.
4. To continue, choose **Next**.

AWS CLI

1. Create a file named `create-virtual-node-serviceb.json`
   with the following contents:

```
{
    "meshName": "apps",
    "spec": {
        "listeners": [
            {
                "portMapping": {
                    "port": 80,
                    "protocol": "http2"
                }
            }
        ],
        "serviceDiscovery": {
            "dns": {
                "hostname": "serviceB.apps.local"
            }
        }
    },
    "virtualNodeName": "serviceB"
}
```

2. Create the virtual node with the [create-virtual-node](../../../cli/latest/reference/appmesh/create-virtual-node.md "../../../cli/latest/reference/appmesh/create-virtual-node.md") command using the JSON file as
   input.

```
`aws appmesh create-virtual-node --cli-input-json file://create-virtual-node-serviceb.json`
```

## Step 3: Create a virtual router and

route

Virtual routers route traffic for one or more virtual services within your mesh. For more
information, see [Virtual routers](virtual_routers.md "virtual_routers.md") and [Routes](routes.md "routes.md").

Create the following resources:

- A virtual router named `serviceB`, since the
  `serviceB.apps.local` virtual service does not initiate outbound
  communication with any other service. Remember that the virtual service that you
  created previously is an abstraction of your actual
  `serviceb.apps.local` service. The virtual service sends traffic
  to the virtual router. The virtual router listens for traffic using the
  HTTP/2 protocol on port 80. Other protocols are also supported.
- A route named `serviceB`. It routes 100 percent of its traffic
  to the `serviceB` virtual node. The weight is in a later
  step once you add the `serviceBv2` virtual node. Though not
  covered in this guide, you can add additional filter criteria for the route and
  add a retry policy to cause the Envoy proxy to make multiple attempts to send
  traffic to a virtual node when it experiences a communication problem.

AWS Management Console

1. For **Virtual router name,** enter
   `serviceB`.
2. Under **Listener configuration**, choose
   **http2** for **Protocol** and
   specify `80` for
   **Port**.
3. For **Route name**, enter
   `serviceB`.
4. For **Route type**, choose
   **http2**.
5. For **Virtual node name** under **Target
   configuration**, select `serviceB` and enter
   `100` for
   **Weight**.
6. Under **Match configuration**, choose
   a **Method**.
7. To continue, choose **Next**.

AWS CLI

1. Create a virtual router.
   1. Create a file named
      `create-virtual-router.json` with the
      following contents:

   ```
   {
       "meshName": "apps",
       "spec": {
           "listeners": [
               {
                   "portMapping": {
                       "port": 80,
                       "protocol": "http2"
                   }
               }
           ]
       },
       "virtualRouterName": "serviceB"
   }
   ```

   2. Create the virtual router with the [create-virtual-router](../../../cli/latest/reference/appmesh/create-virtual-router.md "../../../cli/latest/reference/appmesh/create-virtual-router.md") command using the JSON
      file as input.

   ```
   `aws appmesh create-virtual-router --cli-input-json file://create-virtual-router.json`
   ```

2. Create a route.
   1. Create a file named `create-route.json` with
      the following contents:

   ```
   {
       "meshName" : "apps",
       "routeName" : "serviceB",
       "spec" : {
           "httpRoute" : {
               "action" : {
                   "weightedTargets" : [
                       {
                           "virtualNode" : "serviceB",
                           "weight" : 100
                       }
                   ]
               },
               "match" : {
                   "prefix" : "/"
               }
           }
       },
       "virtualRouterName" : "serviceB"
   }
   ```

   2. Create the route with the [create-route](../../../cli/latest/reference/appmesh/create-route.md "../../../cli/latest/reference/appmesh/create-route.md") command using the JSON file as
      input.

   ```
   `aws appmesh create-route --cli-input-json file://create-route.json`
   ```

## Step 4: Review and create

Review the settings against the previous instructions.

AWS Management Console
Choose **Edit** if you need to make changes in any
section. Once you are satisfied with the settings, choose **Create
mesh**.

The **Status** screen shows you all of the mesh resources
that were created. You can see the created resources in the console by
selecting **View mesh**.

AWS CLI
Review the settings of the mesh you created with the [describe-mesh](../../../cli/latest/reference/appmesh/describe-mesh.md "../../../cli/latest/reference/appmesh/describe-mesh.md") command.

```
`aws appmesh describe-mesh --mesh-name apps`
```

Review the settings of the virtual service that you created with the
[describe-virtual-service](../../../cli/latest/reference/appmesh/describe-virtual-service.md "../../../cli/latest/reference/appmesh/describe-virtual-service.md") command.

```
`aws appmesh describe-virtual-service --mesh-name apps --virtual-service-name serviceb.apps.local`
```

Review the settings of the virtual node that you created with the [describe-virtual-node](../../../cli/latest/reference/appmesh/describe-virtual-node.md "../../../cli/latest/reference/appmesh/describe-virtual-node.md") command.

```
`aws appmesh describe-virtual-node --mesh-name apps --virtual-node-name serviceB`
```

Review the settings of the virtual router that you created with the [describe-virtual-router](../../../cli/latest/reference/appmesh/describe-virtual-router.md "../../../cli/latest/reference/appmesh/describe-virtual-router.md") command.

```
`aws appmesh describe-virtual-router --mesh-name apps --virtual-router-name serviceB`
```

Review the settings of the route that you created with the [describe-route](../../../cli/latest/reference/appmesh/describe-route.md "../../../cli/latest/reference/appmesh/describe-route.md") command.

```
`aws appmesh describe-route --mesh-name apps \
 --virtual-router-name serviceB --route-name serviceB`
```

## Step 5: Create additional

resources

To complete the scenario, you need to:

- Create one virtual node named `serviceBv2` and another named
  `serviceA`. Both virtual nodes listen for requests over HTTP/2
  port 80. For the `serviceA` virtual node, configure a backend of
  `serviceb.apps.local`. All outbound traffic from the
  `serviceA` virtual node is sent to the virtual service named
  `serviceb.apps.local`. Though not covered in this guide, you can
  also specify a file path to write access logs to for a virtual node.
- Create one additional virtual service named `servicea.apps.local`,
  which sends all traffic directly to the `serviceA` virtual
  node.
- Update the `serviceB` route that you created in a previous step to
  send 75 percent of its traffic to the `serviceB` virtual node and 25
  percent of its traffic to the `serviceBv2` virtual node. Over time,
  you can continue to modify the weights until `serviceBv2` receives
  100 percent of the traffic. Once all traffic is sent to `serviceBv2`,
  you can shut down and discontinue the `serviceB` virtual node and actual service. As
  you change weights, your code does not require any modification, because the
  `serviceb.apps.local` virtual and actual service names don't
  change. Recall that the `serviceb.apps.local` virtual service sends
  traffic to the virtual router, which routes the traffic to the virtual nodes.
  The service discovery names for the virtual nodes can be changed at any
  time.

AWS Management Console

1. In the left navigation pane, select
   **Meshes**.
2. Select the `apps` mesh that you created in a previous
   step.
3. In the left navigation pane, select **Virtual
   nodes**.
4. Choose **Create virtual node**.
5. For **Virtual node name**, enter
   `serviceBv2`, for **Service
   discovery method**, choose **DNS**,
   and for **DNS hostname**, enter
   `servicebv2.apps.local`.
6. For **Listener configuration**, select
   **http2** for **Protocol** and
   enter `80` for
   **Port**.
7. Choose **Create virtual node**.
8. Choose **Create virtual node** again. Enter
   `serviceA` for the **Virtual node
   name**. For **Service discovery
   method**, choose **DNS**, and for
   **DNS hostname**, enter
   `servicea.apps.local`.
9. For **Enter a virtual service name** under
   **New backend**, enter
   `serviceb.apps.local`.
10. Under **Listener configuration**, choose
    **http2** for **Protocol**,
    enter `80` for **Port**, and
    then choose **Create virtual node**.
11. In the left navigation pane, select **Virtual
    routers** and then select the `serviceB`
    virtual router from the list.
12. Under **Routes**, select the route named
    `ServiceB` that you created in a previous step, and
    choose **Edit**.
13. Under **Targets**, **Virtual node
    name**, change the value of **Weight**
    for `serviceB` to `75`.
14. Choose **Add target**, choose
    `serviceBv2` from the dropdown list, and set the value of
    **Weight** to `25`.
15. Choose **Save**.
16. In the left navigation pane, select **Virtual
    services** and then choose **Create virtual
    service**.
17. Enter `servicea.apps.local` for
    **Virtual service name**, select
    **Virtual node** for
    **Provider**, select `serviceA` for
    **Virtual node**, and then choose
    **Create virtual service.**

AWS CLI

1. Create the `serviceBv2` virtual node.
   1. Create a file named
      `create-virtual-node-servicebv2.json` with
      the following contents:

   ```
   {
       "meshName": "apps",
       "spec": {
           "listeners": [
               {
                   "portMapping": {
                       "port": 80,
                       "protocol": "http2"
                   }
               }
           ],
           "serviceDiscovery": {
               "dns": {
                   "hostname": "serviceBv2.apps.local"
               }
           }
       },
       "virtualNodeName": "serviceBv2"
   }
   ```

   2. Create the virtual node.

   ```
   `aws appmesh create-virtual-node --cli-input-json file://create-virtual-node-servicebv2.json`
   ```

2. Create the `serviceA` virtual node.
   1. Create a file named
      `create-virtual-node-servicea.json` with the
      following contents:

   ```
   {
      "meshName" : "apps",
      "spec" : {
         "backends" : [
            {
               "virtualService" : {
                  "virtualServiceName" : "serviceb.apps.local"
               }
            }
         ],
         "listeners" : [
            {
               "portMapping" : {
                  "port" : 80,
                  "protocol" : "http2"
               }
            }
         ],
         "serviceDiscovery" : {
            "dns" : {
               "hostname" : "servicea.apps.local"
            }
         }
      },
      "virtualNodeName" : "serviceA"
   }

   ```

   2. Create the virtual node.

   ```
   `aws appmesh create-virtual-node --cli-input-json file://create-virtual-node-servicea.json`
   ```

3. Update the `serviceb.apps.local` virtual service that
   you created in a previous step to send its traffic to the
   `serviceB` virtual router. When the virtual service
   was originally created, it did not send traffic anywhere, since the
   `serviceB` virtual router had not been created
   yet.
   1. Create a file named
      `update-virtual-service.json` with the
      following contents:

   ```
   {
      "meshName" : "apps",
      "spec" : {
         "provider" : {
            "virtualRouter" : {
               "virtualRouterName" : "serviceB"
            }
         }
      },
      "virtualServiceName" : "serviceb.apps.local"
   }
   ```

   2. Update the virtual service with the [update-virtual-service](../../../cli/latest/reference/appmesh/update-virtual-service.md "../../../cli/latest/reference/appmesh/update-virtual-service.md") command.

   ```
   `aws appmesh update-virtual-service --cli-input-json file://update-virtual-service.json`
   ```

4. Update the `serviceB` route that you created in a
   previous step.
   1. Create a file named `update-route.json` with
      the following contents:

   ```
   {
      "meshName" : "apps",
      "routeName" : "serviceB",
      "spec" : {
         "http2Route" : {
            "action" : {
               "weightedTargets" : [
                  {
                     "virtualNode" : "serviceB",
                     "weight" : 75
                  },
                  {
                     "virtualNode" : "serviceBv2",
                     "weight" : 25
                  }
               ]
            },
            "match" : {
               "prefix" : "/"
            }
         }
      },
      "virtualRouterName" : "serviceB"
   }
   ```

   2. Update the route with the [update-route](../../../cli/latest/reference/appmesh/update-route.md "../../../cli/latest/reference/appmesh/update-route.md") command.

   ```
   `aws appmesh update-route --cli-input-json file://update-route.json`
   ```

5. Create the `serviceA` virtual service.
   1. Create a file named
      `create-virtual-servicea.json` with the
      following contents:

   ```
   {
      "meshName" : "apps",
      "spec" : {
         "provider" : {
            "virtualNode" : {
               "virtualNodeName" : "serviceA"
            }
         }
      },
      "virtualServiceName" : "servicea.apps.local"
   }
   ```

   2. Create the virtual service.

   ```
   `aws appmesh create-virtual-service --cli-input-json file://create-virtual-servicea.json`
   ```

###### Mesh summary

Before you created the service mesh, you had three actual services named
`servicea.apps.local`, `serviceb.apps.local`, and
`servicebv2.apps.local`. In addition to the actual services, you now
have a service mesh that contains the following resources that represent the actual
services:

- Two virtual services. The proxy sends all traffic from the
  `servicea.apps.local` virtual service to the
  `serviceb.apps.local` virtual service through a virtual router.
- Three virtual nodes named `serviceA`, `serviceB`, and
  `serviceBv2`. The Envoy proxy uses the service discovery
  information configured for the virtual nodes to look up the IP addresses of the
  actual services.
- One virtual router with one route that instructs the Envoy proxy to route 75
  percent of inbound traffic to the `serviceB` virtual node and 25
  percent of the traffic to the `serviceBv2` virtual node.

## Step 6: Update services

After creating your mesh, you need to complete the following tasks:

- Authorize the Envoy proxy that you deploy with each Amazon ECS task to read the configuration of
  one or more virtual nodes. For more information about how to authorize the proxy, see [Proxy authorization](proxy-authorization.md "proxy-authorization.md").
- Update each of your existing Amazon ECS task definitions to use the Envoy proxy.

###### Credentials

The Envoy container requires AWS Identity and Access Management credentials for signing requests that are sent to the
App Mesh service. For Amazon ECS tasks deployed with the Amazon EC2 launch type, the credentials can come from
the [instance role](../../../AmazonECS/latest/developerguide/instance_IAM_role.md "../../../AmazonECS/latest/developerguide/instance_IAM_role.md") or from a [task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md"). Amazon ECS tasks deployed with
Fargate on Linux containers don't have access to the Amazon EC2 metadata server that supplies
instance IAM profile credentials. To supply the credentials, you must attach an IAM task role
to any tasks deployed with the Fargate on Linux containers type.

If a task is deployed with the Amazon EC2 launch type and access is blocked to the Amazon EC2 metadata server,
as described in the _Important_ annotation in [IAM Role for Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md"), then a task IAM role must also
be attached to the task. The role that you assign to the instance or task must have an IAM policy
attached to it as described in [Proxy
authorization](proxy-authorization.md "proxy-authorization.md").

###### To update your task definition using the AWS CLI

You use Amazon ECS AWS CLI command [`register-task-definition`](../../../cli/latest/reference/ecs/register-task-definition.md "../../../cli/latest/reference/ecs/register-task-definition.md"). The example task definition below shows how
to configure App Mesh for your service.

###### Note

Configuring App Mesh for Amazon ECS through the console is unavailable.

###### Proxy configuration

To configure your Amazon ECS service to use App Mesh, your service's task definition must
have the following proxy configuration section. Set the proxy configuration
`type` to `APPMESH` and the `containerName` to
`envoy`. Set the following property values accordingly.

`IgnoredUID`

The Envoy proxy doesn't route traffic from processes that use this user ID.
You can choose any user ID that you want for this property value, but this ID must
be the same as the `user` ID for the Envoy container in your task
definition. This matching allows Envoy to ignore its own traffic without using the
proxy. Our examples use `1337` for historical
purposes.

`ProxyIngressPort`

This is the inbound port for the Envoy proxy container. Set this value to
`15000`.

`ProxyEgressPort`

This is the outbound port for the Envoy proxy container. Set this value to
`15001`.

`AppPorts`

Specify any inbound ports that your application containers listen on. In this
example, the application container listens on port
`9080`. The port that you specify
must match the port configured on the virtual node listener.

`EgressIgnoredIPs`

Envoy doesn't proxy traffic to these IP addresses. Set this value to
`169.254.170.2,169.254.169.254`, which ignores the Amazon EC2 metadata
server and the Amazon ECS task metadata endpoint. The metadata endpoint provides IAM
roles for tasks credentials. You can add additional addresses.

`EgressIgnoredPorts`

You can add a comma separated list of ports. Envoy doesn't proxy traffic to
these ports. Even if you list no ports, port 22 is ignored.

###### Note

The maximum number of outbound ports that can be ignored is 15.

```
"proxyConfiguration": {
	"type": "APPMESH",
	"containerName": "envoy",
	"properties": [{
			"name": "IgnoredUID",
			"value": "`1337`"
		},
		{
			"name": "ProxyIngressPort",
			"value": "15000"
		},
		{
			"name": "ProxyEgressPort",
			"value": "15001"
		},
		{
			"name": "AppPorts",
			"value": "`9080`"
		},
		{
			"name": "EgressIgnoredIPs",
			"value": "169.254.170.2,169.254.169.254"
		},
		{
			"name": "EgressIgnoredPorts",
			"value": "`22`"
		}
	]
}
```

###### Application container Envoy dependency

The application containers in your task definitions must wait for the Envoy proxy to
bootstrap and start before they can start. To make sure this happens, you set a
`dependsOn` section in each application container definition to wait for the
Envoy container to report as `HEALTHY`. The following code shows an application
container definition example with this dependency. All of the properties in the following
example are required. Some of the property values are also required, but some are
`replaceable`.

```
{
	"name": "`appName`",
	"image": "`appImage`",
	"portMappings": [{
		"containerPort": `9080`,
		"hostPort": `9080`,
		"protocol": "tcp"
	}],
	"essential": true,
	"dependsOn": [{
		"containerName": "envoy",
		"condition": "HEALTHY"
	}]
}
```

**Envoy container definition**

Your Amazon ECS task definitions must contain an App Mesh Envoy container image.

All [supported](../../../general/latest/gr/appmesh.md "../../../general/latest/gr/appmesh.md")
Regions can replace `Region-code` with any Region other than
`me-south-1`, `ap-east-1`, `ap-southeast-3`, `eu-south-1`, `il-central-1`, and `af-south-1`.

Standard

```
840364872350.dkr.ecr.`region-code`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

FIPS-compliant

```
840364872350.dkr.ecr.`region-code`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod-fips
```

`me-south-1`

Standard

```
772975370895.dkr.ecr.me-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`ap-east-1`

Standard

```
856666278305.dkr.ecr.ap-east-1.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`ap-southeast-3`

Standard

```
909464085924.dkr.ecr.ap-southeast-3.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`eu-south-1`

Standard

```
422531588944.dkr.ecr.eu-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`il-central-1`

Standard

```
564877687649.dkr.ecr.il-central-1.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`af-south-1`

Standard

```
924023996002.dkr.ecr.af-south-1.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod
```

`Public repository`

Standard

```
public.ecr.aws/appmesh/aws-appmesh-envoy:v1.34.4.0-prod
```

FIPS-compliant

```
public.ecr.aws/appmesh/aws-appmesh-envoy:v1.34.4.0-prod-fips
```

###### Important

Only version v1.9.0.0-prod or later is supported for use with App Mesh.

You must use the App Mesh Envoy container image until the Envoy project team merges changes that support App Mesh. For additional details, see the [GitHub roadmap
issue](https://github.com/aws/aws-app-mesh-roadmap/issues/10 "https://github.com/aws/aws-app-mesh-roadmap/issues/10").

All of the properties in the following example are required. Some of the property values are
also required, but some are `replaceable`.

###### Note

- The Envoy container definition must be marked as `essential`.
- We recommend allocating `512` CPU units and at least `64`
  MiB of memory to the Envoy container. On Fargate the lowest you will be able to set
  is `1024` MiB of memory.
- The virtual node name for the Amazon ECS service must be set to the value of the
  `APPMESH_RESOURCE_ARN` property. This property requires version
  `1.15.0` or later of the Envoy image. For more information, see
  [Envoy image](envoy.md "envoy.md").
- The value for the `user` setting must match the
  `IgnoredUID` value from the task definition proxy configuration. In
  this example, we use `1337`.
- The health check shown here waits for the Envoy container to bootstrap properly
  before reporting to Amazon ECS that the Envoy container is healthy and ready for the
  application containers to start.
- By default, App Mesh uses the name of the resource you specified in
  `APPMESH_RESOURCE_ARN` when Envoy is referring to itself in metrics
  and traces. You can override this behavior by setting the
  `APPMESH_RESOURCE_CLUSTER` environment variable with your own name.
  This property requires version `1.15.0` or later of the Envoy image. For
  more information, see [Envoy image](envoy.md "envoy.md").
  The following code shows an Envoy container definition example.

```
{
	"name": "envoy",
	"image": "`840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod",
	"essential": true,
	"environment": [{
		"name": "APPMESH_RESOURCE_ARN",
		"value": "arn:aws:appmesh:`us-west-2`:`111122223333`:mesh/`apps`/virtualNode/`serviceB`"
	}],
	"healthCheck": {
		"command": [
			"CMD-SHELL",
			"curl -s http://localhost:9901/server_info | grep state | grep -q LIVE"
		],
		"startPeriod": `10`,
		"interval": `5`,
		"timeout": `2`,
		"retries": `3`
	},
	"user": "`1337`"
}
```

###### Example task definitions

The following example Amazon ECS task definitions show how to merge the examples from above
into a task definition for `taskB`. Examples are provided for creating tasks for
both Amazon ECS launch types with or without using AWS X-Ray. Change the
`replaceable` values, as appropriate, to create task
definitions for the tasks named `taskBv2` and `taskA` from the
scenario. Substitute your mesh name and virtual node name for the
`APPMESH_RESOURCE_ARN` value and a list of ports that your application
listens on for the proxy configuration `AppPorts` value. By default, App Mesh uses
the name of the resource you specified in `APPMESH_RESOURCE_ARN` when Envoy is
referring to itself in metrics and traces. You can override this behavior by setting the
`APPMESH_RESOURCE_CLUSTER` environment variable with your own name. All of
the properties in the following examples are required. Some of the property values are also
required, but some are `replaceable`.

If you're running an Amazon ECS task as described in the Credentials section, then you need
to add an existing [task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md"), to
the examples.

###### Important

Fargate must use a port value greater than 1024.

###### Example JSON for Amazon ECS task definition - Fargate on Linux containers

```
{

   "family" : "`taskB`",
   "memory" : "`1024`",
   "cpu" : "`0.5 vCPU`",
   "proxyConfiguration" : {
      "containerName" : "envoy",
      "properties" : [
         {
            "name" : "ProxyIngressPort",
            "value" : "15000"
         },
         {
            "name" : "AppPorts",
            "value" : "`9080`"
         },
         {
            "name" : "EgressIgnoredIPs",
            "value" : "169.254.170.2,169.254.169.254"
         },
         {
            "name": "EgressIgnoredPorts",
            "value": "`22`"
         },
         {
            "name" : "IgnoredUID",
            "value" : "`1337`"
         },
         {
            "name" : "ProxyEgressPort",
            "value" : "15001"
         }
      ],
      "type" : "APPMESH"
   },
   "containerDefinitions" : [
      {
         "name" : "`appName`",
         "image" : "`appImage`",
         "portMappings" : [
            {
               "containerPort" : `9080`,
               "protocol" : "tcp"
            }
         ],
         "essential" : true,
         "dependsOn" : [
            {
               "containerName" : "envoy",
               "condition" : "HEALTHY"
            }
         ]
      },
      {
         "name" : "envoy",
         "image" : "`840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod",
         "essential" : true,
         "environment" : [
            {
               "name" : "APPMESH_VIRTUAL_NODE_NAME",
               "value" : "mesh/`apps`/virtualNode/`serviceB`"
            }
         ],
         "healthCheck" : {
            "command" : [
               "CMD-SHELL",
               "curl -s http://localhost:9901/server_info | grep state | grep -q LIVE"
            ],
            "interval" : `5`,
            "retries" : `3`,
            "startPeriod" : `10`,
            "timeout" : `2`
         },
         "memory" : `500`,
         "user" : "`1337`"
      }
   ],
   "requiresCompatibilities" : [ "FARGATE" ],
   "taskRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskRole`",
   "executionRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskExecutionRole`",
   "networkMode" : "awsvpc"
}
```

###### Example JSON for Amazon ECS task definition with AWS X-Ray - Fargate on Linux containers

X-Ray allows you to collect data about requests that an application serves and provides
tools that you can use to visualize traffic flow. Using the X-Ray driver for Envoy enables
Envoy to report tracing information to X-Ray. You can enable X-Ray tracing using the [Envoy configuration](envoy.md "envoy.md"). Based on the configuration, Envoy sends tracing
data to the X-Ray daemon running as a [sidecar](../../../xray/latest/devguide/xray-daemon-ecs.md "../../../xray/latest/devguide/xray-daemon-ecs.md")
container and the daemon forwards the traces to the X-Ray service. Once the traces are
published to X-Ray, you can use the X-Ray console to visualize the service call graph and
request trace details. The following JSON represents a task definition to enable X-Ray
integration.

```
{


   "family" : "`taskB`",
   "memory" : "`1024`",
   "cpu" : "`512`",
   "proxyConfiguration" : {
      "containerName" : "envoy",
      "properties" : [
         {
            "name" : "ProxyIngressPort",
            "value" : "15000"
         },
         {
            "name" : "AppPorts",
            "value" : "`9080`"
         },
         {
            "name" : "EgressIgnoredIPs",
            "value" : "169.254.170.2,169.254.169.254"
         },
         {
            "name": "EgressIgnoredPorts",
            "value": "`22`"
         },
         {
            "name" : "IgnoredUID",
            "value" : "`1337`"
         },
         {
            "name" : "ProxyEgressPort",
            "value" : "15001"
         }
      ],
      "type" : "APPMESH"
   },
   "containerDefinitions" : [
      {
         "name" : "`appName`",
         "image" : "`appImage`",
         "portMappings" : [
            {
               "containerPort" : `9080`,
               "protocol" : "tcp"
            }
         ],
         "essential" : true,
         "dependsOn" : [
            {
               "containerName" : "envoy",
               "condition" : "HEALTHY"
            }
         ]
      },
      {

         "name" : "envoy",
         "image" : "`840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod",
         "essential" : true,
         "environment" : [
            {
               "name" : "APPMESH_VIRTUAL_NODE_NAME",
               "value" : "mesh/`apps`/virtualNode/`serviceB`"
            },
            {
               "name": "ENABLE_ENVOY_XRAY_TRACING",
               "value": "1"
            }
         ],
         "healthCheck" : {
            "command" : [
               "CMD-SHELL",
               "curl -s http://localhost:9901/server_info | grep state | grep -q LIVE"
            ],
            "interval" : `5`,
            "retries" : `3`,
            "startPeriod" : `10`,
            "timeout" : `2`
         },
         "memory" : `500`,
         "user" : "`1337`"
      },
      {
         "name" : "xray-daemon",
         "image" : "amazon/aws-xray-daemon",
         "user" : "`1337`",
         "essential" : true,
         "cpu" : "`32`",
         "memoryReservation" : "`256`",
         "portMappings" : [
            {
               "containerPort" : 2000,
               "protocol" : "udp"
            }
         ]
      }
   ],
   "requiresCompatibilities" : [ "FARGATE" ],
   "taskRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskRole`",
   "executionRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskExecutionRole`",
   "networkMode" : "awsvpc"
}
```

###### Example JSON for Amazon ECS task definition - EC2 launch type

```
{
  "family": "`taskB`",
  "memory": "`256`",
  "proxyConfiguration": {
    "type": "APPMESH",
    "containerName": "envoy",
    "properties": [
      {
        "name": "IgnoredUID",
        "value": "`1337`"
      },
      {
        "name": "ProxyIngressPort",
        "value": "15000"
      },
      {
        "name": "ProxyEgressPort",
        "value": "15001"
      },
      {
        "name": "AppPorts",
        "value": "`9080`"
      },
      {
        "name": "EgressIgnoredIPs",
        "value": "169.254.170.2,169.254.169.254"
      },
      {
        "name": "EgressIgnoredPorts",
        "value": "`22`"
      }
    ]
  },
  "containerDefinitions": [
    {
      "name": "`appName`",
      "image": "`appImage`",
      "portMappings": [
        {
          "containerPort": `9080`,
          "hostPort": `9080`,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "dependsOn": [
        {
          "containerName": "envoy",
          "condition": "HEALTHY"
        }
      ]
    },
    {
      "name": "envoy",
      "image": "`840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod",
      "essential": true,
      "environment": [
        {
          "name": "APPMESH_VIRTUAL_NODE_NAME",
          "value": "mesh/`apps`/virtualNode/`serviceB`"
        }
      ],
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "curl -s http://localhost:9901/server_info | grep state | grep -q LIVE"
        ],
        "startPeriod": `10`,
        "interval": `5`,
        "timeout": `2`,
        "retries": `3`
      },
      "user": "`1337`"
    }
  ],
  "requiresCompatibilities" : [ "EC2" ],
  "taskRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskRole`",
  "executionRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskExecutionRole`",
  "networkMode": "awsvpc"
}
```

###### Example JSON for Amazon ECS task definition with AWS X-Ray - EC2 launch type

```
{
  "family": "`taskB`",
  "memory": "`256`",
   "cpu" : "`1024`",
  "proxyConfiguration": {
    "type": "APPMESH",
    "containerName": "envoy",
    "properties": [
      {
        "name": "IgnoredUID",
        "value": "`1337`"
      },
      {
        "name": "ProxyIngressPort",
        "value": "15000"
      },
      {
        "name": "ProxyEgressPort",
        "value": "15001"
      },
      {
        "name": "AppPorts",
        "value": "`9080`"
      },
      {
        "name": "EgressIgnoredIPs",
        "value": "169.254.170.2,169.254.169.254"
      },
      {
        "name": "EgressIgnoredPorts",
        "value": "`22`"
      }
    ]
  },
  "containerDefinitions": [
    {
      "name": "`appName`",
      "image": "`appImage`",
      "portMappings": [
        {
          "containerPort": `9080`,
          "hostPort": `9080`,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "dependsOn": [
        {
          "containerName": "envoy",
          "condition": "HEALTHY"
        }
      ]
    },
    {
      "name": "envoy",
      "image": "`840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy:v1.34.4.0-prod",
      "essential": true,
      "environment": [
        {
          "name": "APPMESH_VIRTUAL_NODE_NAME",
          "value": "mesh/`apps`/virtualNode/`serviceB`"
        },
        {
         "name": "ENABLE_ENVOY_XRAY_TRACING",
         "value": "1"
        }
      ],
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "curl -s http://localhost:9901/server_info | grep state | grep -q LIVE"
        ],
        "startPeriod": `10`,
        "interval": `5`,
        "timeout": `2`,
        "retries": `3`
      },
      "user": "`1337`"
    },
    {
      "name": "xray-daemon",
      "image": "amazon/aws-xray-daemon",
      "user": "`1337`",
      "essential": true,
      "cpu": 32,
      "memoryReservation": 256,
      "portMappings": [
        {
          "containerPort": 2000,
          "protocol": "udp"
        }
      ]
    }
  ],
  "requiresCompatibilities" : [ "EC2" ],
  "taskRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskRole`",
  "executionRoleArn" : "arn:aws:iam::`123456789012`:role/`ecsTaskExecutionRole`",
  "networkMode": "awsvpc"
}
```

## Advanced topics

### Canary deployments using App Mesh

Canary deployments and releases help you switch traffic between an old version of an application
and a newly deployed version. It also monitors the health of the newly deployed version. If there
are any problems with the new version, the canary deployment can automatically switch traffic back
to the old version. Canary deployments give you the ability to switch traffic between application
versions with more control.

For more information about how to implement canary deployments for Amazon ECS using App Mesh, see [Create a pipeline with canary deployments for Amazon ECS using App Mesh](https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-ecs-using-aws-app-mesh/ "https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-ecs-using-aws-app-mesh/")

###### Note

For more examples and walkthroughs for App Mesh, see the [App Mesh examples repository](https://github.com/aws/aws-app-mesh-examples "https://github.com/aws/aws-app-mesh-examples").
