# Add a partner data source in SiteWise Edge

To connect a partner data source to your SiteWise Edge gateway, add it as a data
source. When you add it as a data source, AWS IoT SiteWise will deploy a private AWS IoT Greengrass
component to your SiteWise Edge gateway.

## Prerequisites

To add a partner data source, you must do the following:

- For EasyEdge and CloudRail, create an account with the
  partner, then bind the accounts.
- [Set up Docker on your
  SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md")

## Create a SiteWise Edge gateway with a

partner data source

If you want to create a new SiteWise Edge gateway, complete the steps in [Create a self-hosted SiteWise Edge gateway](create-gateway-ggv2.md "create-gateway-ggv2.md").
After you’ve created SiteWise Edge gateway follow the steps in [Add a partner data source to an
existing SiteWise Edge gateway](#cpa-existing-gateway "#cpa-existing-gateway") to
add a partner data source.

## Add a partner data source to an

existing SiteWise Edge gateway

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Choose the SiteWise Edge gateway you want to connect the partner data
   source to.
4. Under **Data sources**, choose **Add data
   source**.
5. On the **Add data source** screen, choose a
   **Source type**, to select the partner that
   connects your SiteWise Edge gateway. Each data source has its own
   configuration options. There are two categories of data sources:
   AWS sources and Partner sources.

Using a partner data source, you can select one
source per gateway. For a list of data source partner integration
options, see [SiteWise Edge gateway partner data
source options](connect-partner-data-source.md "connect-partner-data-source.md"). Note that you can
add up to 100 OPC UA data sources (AWS sources). To get started
with OPC UA data sources, see [OPC UA data sources for AWS IoT SiteWise Edge
gateways](configure-sources-opcua.md "configure-sources-opcua.md"). 6. Enter a name for the source. 7. Select your data source's tab below and follow the configuration
procedure.

CloudRail
Much of the CloudRail configuration is done in the
CloudRail portal after saving the data source for your
SiteWise Edge gateway. However, authorizing the connection is
required.

###### Note

The CloudRail connection is only available on
Linux.

    1. [Create
     a CloudRail account](https://devices.cloudrail.com/signup "https://devices.cloudrail.com/signup") to get started with
     connecting to AWS IoT SiteWise.
    2. Ensure that Docker is installed on your gateway. For more information, see [Set up Docker on your
     SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md").
    3. Read the **Authorize access and deployment** agreement, then choose **Authorize**. Checking the box grants the AWS partner access to your data source and allows AWS to deploy on the partner's component.

###### Note

The **Measurement Prefix –
_optional_** is set
within your CloudRail portal.

###### Note

Partner software is developed, maintained, and supported by the AWS partner. AWS is not responsible for the interface, configuration, or software.

For more information, see
[CloudRail](connect-partner-data-source.md#cp-cloudrail "connect-partner-data-source.md#cp-cloudrail").

EasyEdge
Much of the EasyEdge configuration is done in the
EasyEdge portal after saving the data source for your
SiteWise Edge gateway. However, authorizing the connection is
required.

###### Note

The EasyEdge connection is only available on
Linux.

    1. [Create an EasyEdge account](https://accounts.easyedge.io/signup?partner=aws "https://accounts.easyedge.io/signup?partner=aws") to get
     started with connecting to AWS IoT SiteWise.
    2. Ensure that Docker is installed on your gateway. For more information, see [Set up Docker on your
     SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md").
    3. Read the **Authorize access and deployment** agreement, then choose **Authorize**. Checking the box grants the AWS partner access to your data source and allows AWS to deploy on the partner's component.

###### Note

The **Measurement Prefix –
_optional_** is set
within your EasyEdge portal.

###### Note

Partner software is developed, maintained, and supported by the AWS partner. AWS is not responsible for the interface, configuration, or software.

For more information, see
[EasyEdge](connect-partner-data-source.md#cp-easyedge "connect-partner-data-source.md#cp-easyedge").

Litmus Edge
You can activate the Litmus configuration in two
ways. Activate Litmus Edge directly through AWS IoT SiteWise
using information from the Litmus Edge Manager portal.
Or, you can manually activate Litmus Edge for AWS IoT SiteWise
through Litmus Edge Manager.

###### Note

The Litmus Edge connection is only available on
Linux.

 

###### To activate using a Litmus Edge activation code

on AWS IoT SiteWise

Use this procedure when adding a Litmus Edge data
source with a Litmus Edge activation code on the
AWS IoT SiteWise console.

    1. Select **Activate now using a
     code**. Additional configuration options
     appear.
    2. Enter the Litmus Edge Manager to connect
     Litmus Edge to your SiteWise Edge gateway. For more
     information, see [Step 3a: Set Data and Device Management
     Endpoint](https://docs.litmus.io/edgemanager/quickstart-guide/activate-an-edge-device/step-3-activation-request "https://docs.litmus.io/edgemanager/quickstart-guide/activate-an-edge-device/step-3-activation-request") in the Litmus Edge Manager
     documentation.
    3. Provide the Litmus Edge Manager activation
     code to activate Litmus Edge on AWS IoT SiteWise
    4. Optionally, provide AWS IoT SiteWise with the
     **Litmus Edge Manager CA
     certificate**. The certificate prevents
     Litmus Edge from activating on an unauthorized
     Litmus Edge Manager.
    5. Ensure that Docker is installed on your gateway. For more information, see [Set up Docker on your
     SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md").

     ###### Note

    AWS IoT SiteWise deploys the partner application as a Docker container. The application
     is deployed with `NET_ADMIN` capability so that the Litmus Edge
     Docker container can be managed through Litmus Edge Manager. Litmus Edge
     requires this privileged access to run on your devices. For more information
     about the Litmus Edge Docker requirements, see [Docker Installation](https://docs.litmus.io/litmusedge-v1/quickstart-guide/installation-and-deployments/docker-installation "https://docs.litmus.io/litmusedge-v1/quickstart-guide/installation-and-deployments/docker-installation") in the *QuickStart Guide* in
     the Litmus Edge documentation.
    6. Read the **Authorize access and deployment** agreement, then choose **Authorize**. Checking the box grants the AWS partner access to your data source and allows AWS to deploy on the partner's component.

 

###### To activate manually through Litmus Edge

    1. Select **Activate later on
     Litmus Edge**.
    2. Ensure that Docker is installed on your gateway. For more information, see [Set up Docker on your
     SiteWise Edge gateway](cpa-install-docker.md "cpa-install-docker.md").

     ###### Note

    AWS IoT SiteWise deploys the partner application as a Docker container. The application
     is deployed with `NET_ADMIN` capability so that the Litmus Edge
     Docker container can be managed through Litmus Edge Manager. Litmus Edge
     requires this privileged access to run on your devices. For more information
     about the Litmus Edge Docker requirements, see [Docker Installation](https://docs.litmus.io/litmusedge-v1/quickstart-guide/installation-and-deployments/docker-installation "https://docs.litmus.io/litmusedge-v1/quickstart-guide/installation-and-deployments/docker-installation") in the *QuickStart Guide* in
     the Litmus Edge documentation.
    3. Read the **Authorize access and deployment** agreement, then choose **Authorize**. Checking the box grants the AWS partner access to your data source and allows AWS to deploy on the partner's component.
    4. After the deployment is complete, follow the
     [Access the Litmus Edge Web UI](https://docs.litmus.io/litmusedge/quickstart-guide/access-the-litmus-edge-web-ui "https://docs.litmus.io/litmusedge/quickstart-guide/access-the-litmus-edge-web-ui")
     instructions in the Litmus Edge
     *QuickStart
     Guide* documentation. ###### Note

Partner software is developed, maintained, and supported by the AWS partner. AWS is not responsible for the interface, configuration, or software.

For more
information, see [Litmus Edge](connect-partner-data-source.md#cp-litmus "connect-partner-data-source.md#cp-litmus"). 8. Choose **Save**.
