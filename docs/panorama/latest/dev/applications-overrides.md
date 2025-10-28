End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Deploy-time configuration with overrides

You configure parameters and abstract nodes during deployment. If you use the AWS Panorama console to deploy, you can
specify a value for each parameter and choose a camera stream as input. If you use the AWS Panorama API to deploy
applications, you specify these settings with an overrides document.

An overrides document is similar in structure to an application manifest. For parameters with basic types, you
define a node. For camera streams, you define a node and a package that maps to a registered camera stream. Then you
define an override for each node that specifies the node from the application manifest that it replaces.

###### Example overrides.json

```
{
    "nodeGraphOverrides": {
        "nodes": [
            {
                "name": "my_camera",
                "interface": "123456789012::exterior-south.exterior-south"
            },
            {
                "name": "my_region",
                "interface": "string",
                "value": "us-east-1"
            }
        ],
        "packages": [
            {
                "name": "123456789012::exterior-south",
                "version": "1.0"
            }
        ],
        "nodeOverrides": [
            {
                "replace": "camera_node",
                "with": [
                    {
                        "name": "my_camera"
                    }
                ]
            },
            {
                "replace": "region",
                "with": [
                    {
                        "name": "my_region"
                    }
                ]
            }
        ],
        "envelopeVersion": "2021-01-01"
    }
}
```

In the preceding example, the document defines overrides for one string parameter and an abstract camera node.
The `nodeOverrides` tells AWS Panorama which nodes in this document override which in the application
manifest.
