# Creating your gateway

The overview sections on this page provide a high-level synopsis of how the Storage Gateway
creation process works. For step-by-step procedures to create a specific type of gateway
using the Storage Gateway console, see the following topics:

- [Create and activate an
  Amazon S3 File Gateway](create-gateway-file.md "create-gateway-file.md")
- [Create and activate
  an Amazon FSx File Gateway](../filefsxw/create-gateway-file.md "../filefsxw/create-gateway-file.md")
- [Create and activate a
  Tape Gateway](../../../storagegateway/latest/tgw/create-tape-gateway.md "../../../storagegateway/latest/tgw/create-tape-gateway.md")
- [Create and
  activate a Volume Gateway](../../../storagegateway/latest/vgw/create-volume-gateway-volume.md "../../../storagegateway/latest/vgw/create-volume-gateway-volume.md")

## Overview - Gateway

Activation

Gateway activation involves setting up your gateway, connecting it to AWS, then
reviewing your settings and activating it.

### Set up gateway

To set up your Storage Gateway, you first choose the type of gateway you want to create
and the host platform on which you will run the gateway virtual appliance. You then
download the gateway virtual appliance template for the platform of your choice and
deploy it in your on-premises environment. You can also deploy your Storage Gateway as a
physical hardware appliance that you order from your preferred reseller, or as an
Amazon EC2 instance in your AWS cloud environment. When you deploy the gateway
appliance, you allocate local physical disk space on the virtualization host.

### Connect to AWS

The next step is to connect your gateway to AWS. To do this, you first choose
the type of service endpoint you want to use for communications between the gateway
virtual appliance and AWS services in the cloud. This endpoint can be accessible
from the public internet, or only from within your Amazon VPC, where you have full
control over the network security configuration. You then specify the gateway's IP
address or its activation key, which you can obtain by connecting to the local
console on the gateway appliance.

### Review and activate

At this point, you'll have an opportunity to review the gateway and connection
options you chose, and make changes if necessary. When everything is set up the way
you want you can activate the gateway. Before you can start using your activated
gateway, you will need to configure some additional settings and create your storage
resources.

## Overview - Gateway

Configuration

After you activate your Storage Gateway, you need to perform some additional configuration. In
this step, you allocate the physical storage you provisioned on the gateway host
platform to be used as either the cache or the upload buffer by the gateway appliance.
You then configure settings to help monitor the health of your gateway using Amazon CloudWatch Logs
and CloudWatch alarms, and add tags to help identify the gateway, if desired. Before you can
start using your activated and configured gateway, you will need to create your storage
resources.

## Overview - Storage Resources

After you activate and configure your Storage Gateway, you need to create cloud storage
resources for it to use. Depending on the type of gateway you created, you will use the
Storage Gateway console to create Volumes, Tapes, or Amazon S3 or Amazon FSx files shares to associate
with it. Each gateway type uses its respective resources to emulate the related type of
network storage infrastructure, and transfers the data you write to it into the AWS
cloud.
