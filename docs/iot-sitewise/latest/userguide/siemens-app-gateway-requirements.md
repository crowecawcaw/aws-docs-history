# Requirements for the AWS IoT SiteWise Edge

application

To run AWS IoT SiteWise Edge on Siemens Industrial Edge, you need the following:

- A [Siemens Digital Exchange Platform](https://www.dex.siemens.com/ "https://www.dex.siemens.com/")
  account.
- A Siemens Industrial Edge Hub (iehub) account.
- A Siemens Industrial Edge Management instance.
  - The IE App Configuration Service. To learn more, see [Installing the IE App Configuration Service manually](https://docs.eu1.edge.siemens.cloud/get_started_and_operate/industrial_edge_management/how_to_setup_operate/vm/operation/app_projects/app_configurations/ie_application_configuration_service/installing_the_ie_acs_manually.html "https://docs.eu1.edge.siemens.cloud/get_started_and_operate/industrial_edge_management/how_to_setup_operate/vm/operation/app_projects/app_configurations/ie_application_configuration_service/installing_the_ie_acs_manually.html") in
    the _Siemens Industrial Edge Management_ documentation.

- Access to version 2.0.1 or higher of the AWS IoT SiteWise Edge application. For more
  information, see [Access the AWS IoT SiteWise Edge application](sa-get-app.md "sa-get-app.md").
- Either a Siemens Industrial Edge Device (IED) or a Siemens Industrial Edge virtual Device (IEVD).
  - A minimum of 15 GB disk space for hardware requirements.
  - 1 GB of RAM with an additional 1 GB of swap memory.
  - Device configuration to allow outbound traffic on ports 443 and 8883.
  - A x86-64 bit processor.
  - Siemens Industrial Edge Management version 1.13.10 or higher.
  - Device conformance to Siemens Secure Storage requirements.
    - On virtual devices, IEVD version 1.19 or above.
    - On physical devices, IED-OS version 2.2 or above.

  - The latest version of Docker Compose.
  - Docker Engine version 18.091 or higher.

- Required domain access. For more information, see [AWS IoT SiteWise endpoints](endpoints-and-quotas.md#endpoints "endpoints-and-quotas.md#endpoints").
