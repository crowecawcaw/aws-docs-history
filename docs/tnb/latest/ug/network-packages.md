# Network packages for AWS TNB

A network package is a .zip file in CSAR (Cloud Service Archive) format. It defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.​

The network package contains the following files:

- A network descriptor file (`nsd.yaml`) in TOSCA format as described by
  ETSI SOL007.

The `nsd.yaml` file contains references to uploaded [function
packages](function-packages.md "function-packages.md") with their descriptor IDs.

- User data scripts, if any.
- Lifecycle hook scripts, if any.
- Plugins' `values.yaml` configuration files, if any.

###### Tasks

- [Create a network package in AWS TNB](create-network-package.md "create-network-package.md")
- [View a network package in AWS TNB](view-network-package.md "view-network-package.md")
- [Download a network package from
  AWS TNB](download-network-package.md "download-network-package.md")
- [Delete a network package from AWS TNB](delete-network-package.md "delete-network-package.md")
