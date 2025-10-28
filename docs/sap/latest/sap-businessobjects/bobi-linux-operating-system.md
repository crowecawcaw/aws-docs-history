# Operating System

Customers can choose to bring their license subscriptions or use AWS Marketplace to purchase licenses. Operating systems such as [SUSE Linux Enterprise Server for SAP](https://www.suse.com/products/sles-for-sap/ "https://www.suse.com/products/sles-for-sap/") and [Red Hat Enterprise Linux for SAP with HA and Update Services](https://aws.amazon.com/blogs/awsforsap/now-available-new-rhel-for-sap-with-ha-and-us-in-aws-marketplace/ "https://aws.amazon.com/blogs/awsforsap/now-available-new-rhel-for-sap-with-ha-and-us-in-aws-marketplace/") are optimized for running SAP and come with high availability solution for SAP NetWeaver and SAP HANA database. For supported operating systems, see [SAP Note 1656099.](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099")

## SLES

If you plan to use Bring Your Own Subscription (BYOS) images provided by SUSE, ensure that you have the registration code required to register your instance with SUSE to access repositories for software updates. For details, see [SUSE Linux Enterprise Server on Amazon EC2 - FAQs](https://aws.amazon.com/partners/suse/faqs/ "https://aws.amazon.com/partners/suse/faqs/").

## RHEL

If you plan to use the BYOS model with RHEL and the Red Hat Cloud Access Gold Images, ensure your subscription has access to the [Red Hat Cloud Access](https://access.redhat.com/articles/3490141 "https://access.redhat.com/articles/3490141") program. For details, see [Red Hat Enterprise Linux on Amazon EC2 - FAQs](https://aws.amazon.com/partners/redhat/faqs/ "https://aws.amazon.com/partners/redhat/faqs/") and [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access "https://www.redhat.com/en/technologies/cloud-computing/cloud-access").

## Amazon Machine Image (AMI)

A base AMI is required to launch an Amazon EC2 instance. Depending on your choice of operating system, ensure that you have access to the appropriate AMI in your target Region for the deployment.

If you are using AWS CLI, you must provide the AMI ID when you launch the instance.
