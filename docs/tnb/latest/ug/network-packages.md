

# Network packages for AWS TNB
<a name="network-packages"></a>

A network package is a .zip file in CSAR (Cloud Service Archive) format. It defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.​

The network package contains the following files:
+ A network descriptor file (`nsd.yaml`) in TOSCA format as described by ETSI SOL007.

  The `nsd.yaml` file contains references to uploaded [function packages](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html) with their descriptor IDs.
+ User data scripts, if any.
+ Lifecycle hook scripts, if any.
+ Plugins' `values.yaml` configuration files, if any.

**Topics**
+ [Create a network package in AWS TNB](create-network-package.md)
+ [View a network package in AWS TNB](view-network-package.md)
+ [Download a network package from AWS TNB](download-network-package.md)
+ [Delete a network package from AWS TNB](delete-network-package.md)