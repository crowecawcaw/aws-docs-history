# Virtual routers

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

Virtual routers handle traffic for one or more virtual services within your mesh. After
you create a virtual router, you can create and associate routes for your virtual router
that direct incoming requests to different virtual nodes.

![Virtual router diagram showing HTTP route with prefix and targets B and B' for different service versions.](images/virtual_router.png)
Any inbound traffic that your virtual router expects should be specified as a
_listener_.

## Creating a virtual router

AWS Management Console

###### To create a virtual router using the AWS Management Console

###### Note

When creating a Virtual Router, you must add a namespace selector
with a label to identify the list of namespaces to associate Routes
to the created Virtual Router.

1. Open the App Mesh console at [https://console.aws.amazon.com/appmesh/](https://console.aws.amazon.com/appmesh/ "https://console.aws.amazon.com/appmesh/").
2. Choose the mesh that you want to create the virtual router in. All
   of the meshes that you own and that have been [shared](sharing.md "sharing.md") with you are listed.
3. Choose **Virtual routers** in the left
   navigation.
4. Choose **Create virtual router**.
5. For **Virtual router name**, specify a name for
   your virtual router. Up to 255 letters, numbers, hyphens, and
   underscores are allowed.
6. (Optional) For **Listener** configuration,
   specify a **Port** and
   **Protocol** for your virtual router. The
   `http` listener permits connection transition to
   websockets. You can click **Add
   Listener** to add multiple listeners. The **Remove** button will remove that
   listener.
7. Choose **Create virtual router** to
   finish.

AWS CLI
**To create a virtual router using the
AWS CLI.**

Create a virtual router using the following command and input JSON
(replace the `red` values with your own):

1. ```
   aws appmesh create-virtual-router \
        --cli-input-json file://create-virtual-router.json
   ```

````
2. Contents of **example**
 create-virtual-router.json
3. ```
{
    "meshName": "meshName",
    "spec": {
        "listeners": [
            {
                "portMapping": {
                    "port": 80,
                    "protocol": "http"
                }
            }
        ]
    },
    "virtualRouterName": "routerName"
}
````

4. Example output:

```
{
    "virtualRouter": {
        "meshName": "meshName",
        "metadata": {
            "arn": "arn:aws:appmesh:`us-west-2`:210987654321:mesh/meshName/virtualRouter/routerName",
            "createdAt": "2022-04-06T11:49:47.216000-05:00",
            "lastUpdatedAt": "2022-04-06T11:49:47.216000-05:00",
            "meshOwner": "123456789012",
            "resourceOwner": "210987654321",
            "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "version": 1
        },
        "spec": {
            "listeners": [
                {
                    "portMapping": {
                        "port": 80,
                        "protocol": "http"
                    }
                }
            ]
        },
        "status": {
            "status": "ACTIVE"
        },
        "virtualRouterName": "routerName"
    }
}

```

For more information on creating a virtual router with the AWS CLI for
App Mesh, see the [create-virtual-router](../../../cli/latest/reference/appmesh/create-virtual-router.md "../../../cli/latest/reference/appmesh/create-virtual-router.md") command in the AWS CLI reference.

## Deleting a virtual router

###### Note

You cannot delete a virtual router if it has any [routes](routes.md "routes.md") or if it is specified as a provider for any [virtual service](virtual_services.md "virtual_services.md").

AWS Management Console

###### To delete a virtual router using the AWS Management Console

1. Open the App Mesh console at [https://console.aws.amazon.com/appmesh/](https://console.aws.amazon.com/appmesh/ "https://console.aws.amazon.com/appmesh/").
2. Choose the mesh that you want to delete a virtual router from. All
   of the meshes that you own and that have been [shared](sharing.md "sharing.md") with you are listed.
3. Choose **Virtual routers** in the left
   navigation.
4. In the **Virtual Routers** table, choose the
   virtual router that you want to delete and select
   **Delete** in the top right corner. To delete a
   virtual router, your account ID must be listed in either the
   **Mesh owner** or the **Resource
   owner** columns of the virtual router.
5. In the confirmation box, type `delete` and
   then click on **Delete**.

AWS CLI

###### To delete a virtual router using the AWS CLI

1. Use the following command to delete your virtual router (replace
   the `red` values with your own):

```
aws appmesh delete-virtual-router \
     --mesh-name `meshName` \
     --virtual-router-name `routerName`
```

2. Example output:

```
{
    "virtualRouter": {
        "meshName": "meshName",
        "metadata": {
            "arn": "arn:aws:appmesh:`us-west-2`:210987654321:mesh/meshName/virtualRouter/routerName",
            "createdAt": "2022-04-06T11:49:47.216000-05:00",
            "lastUpdatedAt": "2022-04-07T10:49:53.402000-05:00",
            "meshOwner": "123456789012",
            "resourceOwner": "210987654321",
            "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "version": 2
        },
        "spec": {
            "listeners": [
                {
                    "portMapping": {
                        "port": 80,
                        "protocol": "http"
                    }
                }
            ]
        },
        "status": {
            "status": "DELETED"
        },
        "virtualRouterName": "routerName"
    }
}

```

For more information on deleting a virtual router with the AWS CLI for
App Mesh, see the [delete-virtual-router](../../../cli/latest/reference/appmesh/delete-virtual-router.md "../../../cli/latest/reference/appmesh/delete-virtual-router.md") command in the AWS CLI reference.
