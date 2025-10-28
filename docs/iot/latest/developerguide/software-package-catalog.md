# AWS IoT Device Management Software Package Catalog

With AWS IoT Device Management Software Package Catalog, you can maintain an inventory of software packages and their versions. You can associate package versions to individual things and AWS IoT dynamic thing groups,
and deploy them through in-house processes or [AWS IoT jobs](iot-jobs.md "iot-jobs.md").

A software package contains one or more package versions, which is a collection of files that can be deployed as a single unit. Package versions can contain firmware, operating system updates, device applications, configurations, and security patches. As the software evolves over time, you can create a new package version and deploy it to your fleet.

The AWS IoT software package hub is located within AWS IoT Core. You can use the hub to centrally register and maintain your software package inventory and metadata, which creates a catalog of software packages and their versions. You can choose to group devices based on software packages and package versions deployed on the device. This feature provides the opportunity to keep device-side package inventory as a named shadow, associate and group devices based on versions, and visualize package version distribution across the fleet by using fleet metrics.

If you have an in-house software deployment system established, you can continue to use that process to deploy your package versions. If you don’t have a deployment process established or if you prefer, we recommend using [AWS IoT jobs](iot-jobs.md "iot-jobs.md") to use the features in the Software Package Catalog. For more information, see [Preparing AWS IoT jobs](preparing-jobs-for-service-package-catalog.md "preparing-jobs-for-service-package-catalog.md").

###### This chapter contains the following sections:

- [Preparing to use Software Package Catalog](preparing-to-use-software-package-catalog.md "preparing-to-use-software-package-catalog.md")
- [Preparing security](preparing-security.md "preparing-security.md")
- [Preparing fleet indexing](preparing-fleet-indexing.md "preparing-fleet-indexing.md")
- [Preparing AWS IoT Jobs](preparing-jobs-for-service-package-catalog.md "preparing-jobs-for-service-package-catalog.md")
- [Getting started with Software Package Catalog](getting-started-with-software-package-catalog.md "getting-started-with-software-package-catalog.md")
