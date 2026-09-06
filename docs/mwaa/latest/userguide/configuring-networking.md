

# Apache Airflow access modes
<a name="configuring-networking"></a>

The Amazon Managed Workflows for Apache Airflow console contains built-in options to configure private, public, or both public and private routing to the Apache Airflow webserver on your environment. This guide describes the access modes available for the Apache Airflow webserver on your Amazon Managed Workflows for Apache Airflow environment, and the additional resources you'll need to configure in your Amazon VPC if you choose the private network option.

**Contents**
+ [Apache Airflow access modes](#configuring-networking-onconsole)
  + [Public network](#webserver-options-public-network-onconsole)
  + [Private network](#webserver-options-private-network)
  + [Both public and private network access](#webserver-options-public-and-private-network)
+ [Access modes overview](#configuring-networking-access-overview)
  + [Public network access mode](#access-overview-public)
  + [Private network access mode](#access-overview-private)
  + [Both public and private network access mode](#access-overview-public-and-private)
+ [Setup for access modes](#access-network-choose)
  + [Setup for public network](#access-network-public)
  + [Setup for private network](#access-network-private)
  + [Setup for both public and private network access](#access-network-public-and-private)
+ [Accessing the VPC endpoint for your Apache Airflow webserver (private network access)](#configuring-access-vpce)

## Apache Airflow access modes
<a name="configuring-networking-onconsole"></a>

You can choose private, public, or both public and private routing for your Apache Airflow webserver. To enable private routing, choose **Private network**. This limits user access to an Apache Airflow webserver within an Amazon VPC. To enable public routing, choose **Public network**. This allows users to access the Apache Airflow webserver over the internet. To enable both public and private routing, choose **Both public and private network access**. This allows users to access the Apache Airflow webserver over the internet while workers communicate with the webserver through a private VPC endpoint.

### Public network
<a name="webserver-options-public-network-onconsole"></a>

The following architectural diagram depicts an Amazon MWAA environment with a public webserver.

![This image displays the architecture for an Amazon MWAA environment with a public webserver.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-public-web-server.png)


The public network access mode allows the Apache Airflow UI to be accessed over the internet by users granted access to the [IAM policy for your environment](access-policies.md).

**Important**  
If your environment uses Apache Airflow version 3 or later with the **Public network** access mode, workers must be able to reach the webserver over the internet to communicate task state. If the subnets hosting your workers do not have internet access (for example, private subnets without a NAT gateway), DAG tasks will fail. To resolve this, upgrade to Apache Airflow version 3.2.1 or later and switch to **Both public and private network access** mode, which routes worker communication through a private VPC endpoint.

The following image depicts where to find the **Public network** option on the Amazon MWAA console.

![This image depicts where to find the Public network option on the Amazon MWAA console.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-console-public-network-2026.png)


### Private network
<a name="webserver-options-private-network"></a>

The following architectural diagram depicts an Amazon MWAA environment with a private webserver.

![This image displays the architecture for an Amazon MWAA environment with Private network access.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-private-web-server.png)


The private network access mode limits access to the Apache Airflow UI to users *within your Amazon VPC* that have been granted access to the [IAM policy for your environment](access-policies.md).

When you create an environment with private webserver access, you must package all of your dependencies in a Python wheel archive (`.whl`), then reference the `.whl` in your `requirements.txt`. For instructions on packaging and installing your dependencies using wheel, refer to [Managing dependencies using Python wheel](best-practices-dependencies.md#best-practices-dependencies-python-wheels).

The following image depicts where to find the **Private network** option on the Amazon MWAA console.

![This image depicts where to find the Private network option on the Amazon MWAA console.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-console-private-network-2026.png)


### Both public and private network access
<a name="webserver-options-public-and-private-network"></a>

Available for Apache Airflow version 3.2.1 and later. In Apache Airflow version 3 and later, workers communicate task state to the webserver through the Task API. If your Amazon VPC lacks internet access, workers cannot reach a public webserver, causing DAG tasks to fail. This mode creates both a public network load balancer for browser access to the Apache Airflow UI and a private VPC endpoint for worker-to-webserver communication, allowing workers to reach the webserver without internet access. Refer to the **Public network** and **Private network** architecture diagrams above for each component.

![This image depicts where to find the Both public and private network option on the Amazon MWAA console.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-console-public-private-network-2026.png)


**Note**  
With this mode, browser access to the Apache Airflow UI goes through the public URL. The private VPC endpoint is used by workers for internal communication and is not intended for browser access.

## Access modes overview
<a name="configuring-networking-access-overview"></a>

This section describes the VPC endpoints (AWS PrivateLink) created in your Amazon VPC when you choose the **Public network**, **Private network**, or **Both public and private network access** mode.

### Public network access mode
<a name="access-overview-public"></a>

If you chose the **Public network** access mode for your Apache Airflow webserver, network traffic is publicly routed over the internet.
+ Amazon MWAA creates a VPC interface endpoint for your Amazon Aurora PostgreSQL metadata database. The endpoint is created in the Availability Zones mapped to your private subnets and is independent from other AWS accounts.
+ Amazon MWAA then binds an IP address from your private subnets to the interface endpoints. This is designed to support the best practice of binding a single IP from each Availability Zone of the Amazon VPC.

### Private network access mode
<a name="access-overview-private"></a>

If you chose the **Private network** access mode for your Apache Airflow webserver, network traffic is privately routed *within your Amazon VPC*.
+ Amazon MWAA creates a VPC interface endpoint for your Apache Airflow webserver, and an interface endpoint for your Amazon Aurora PostgreSQL metadata database. The endpoints are created in the Availability Zones mapped to your private subnets and is independent from other AWS accounts.
+ Amazon MWAA then binds an IP address from your private subnets to the interface endpoints. This is designed to support the best practice of binding a single IP from each Availability Zone of the Amazon VPC.

### Both public and private network access mode
<a name="access-overview-public-and-private"></a>

If you chose the **Both public and private network access** mode for your Apache Airflow webserver, network traffic to the Apache Airflow UI is publicly routed over the internet, while worker-to-webserver communication is privately routed within your Amazon VPC.
+ Amazon MWAA creates a VPC interface endpoint for your Apache Airflow webserver (for worker connectivity), and an interface endpoint for your Amazon Aurora PostgreSQL metadata database. The endpoints are created in the Availability Zones mapped to your private subnets and are independent from other AWS accounts.
+ Amazon MWAA then binds an IP address from your private subnets to the interface endpoints. This is designed to support the best practice of binding a single IP from each Availability Zone of the Amazon VPC.
+ The Apache Airflow UI is accessible over the internet via a public network load balancer. Users access the UI the same way as with the **Public network** access mode.

To learn more, refer to [Example use cases for an Amazon VPC and Apache Airflow access mode](networking-about.md#networking-about-network-usecase).

## Setup for access modes
<a name="access-network-choose"></a>

The following section describes the additional setup and configurations you'll need based on the Apache Airflow access mode you've chosen for your environment.

### Setup for public network
<a name="access-network-public"></a>

If you choose the **Public network** option for your Apache Airflow webserver, you can begin using the Apache Airflow UI after you create your environment.

You'll need to take the following steps to configure access for your users, and permission for your environment to use other AWS services.

1. **Add permissions**. Amazon MWAA needs permission to use other AWS services. When you create an environment, Amazon MWAA creates a [service-linked role](mwaa-slr.md) that allows it to use certain IAM actions for Amazon Elastic Container Registry (Amazon ECR), CloudWatch Logs, and Amazon EC2.

   You can add permission to use additional actions for these services, or to use other AWS services by adding permissions to your execution role. To learn more, refer to [Amazon MWAA execution role](mwaa-create-role.md).

1. **Create user policies**. You might need to create multiple IAM policies for your users to configure access to your environment and Apache Airflow UI. To learn more, refer to [Accessing an Amazon MWAA environment](access-policies.md).

### Setup for private network
<a name="access-network-private"></a>

If you choose the **Private network** option for your Apache Airflow webserver, you'll need to configure access for your users, permission for your environment to use other AWS services, and create a mechanism to access the resources in your Amazon VPC from your computer.

1. **Add permissions**. Amazon MWAA needs permission to use other AWS services. When you create an environment, Amazon MWAA creates a [service-linked role](mwaa-slr.md) that allows it to use certain IAM actions for Amazon Elastic Container Registry (Amazon ECR), CloudWatch Logs, and Amazon EC2.

   You can add permission to use additional actions for these services, or to use other AWS services by adding permissions to your execution role. To learn more, refer to [Amazon MWAA execution role](mwaa-create-role.md).

1. **Create user policies**. You might need to create multiple IAM policies for your users to configure access to your environment and Apache Airflow UI. To learn more, refer to [Accessing an Amazon MWAA environment](access-policies.md).

1. **Enable network access**. You'll need to create a mechanism in your Amazon VPC to connect to the VPC endpoint (AWS PrivateLink) for your Apache Airflow webserver. For example, by creating a VPN tunnel from your computer using an AWS Client VPN.

### Setup for both public and private network access
<a name="access-network-public-and-private"></a>

If you choose the **Both public and private network access** option for your Apache Airflow webserver, you can begin using the Apache Airflow UI after you create your environment. No VPN or VPC endpoint access mechanism is required for browser access. The Apache Airflow UI is accessible over the internet. Workers connect to the webserver via the private VPC endpoint automatically.

You'll need to take the following steps to configure access for your users, and permission for your environment to use other AWS services.

1. **Add permissions**. Amazon MWAA needs permission to use other AWS services. When you create an environment, Amazon MWAA creates a [service-linked role](mwaa-slr.md) that allows it to use certain IAM actions for Amazon Elastic Container Registry (Amazon ECR), CloudWatch Logs, and Amazon EC2.

   You can add permission to use additional actions for these services, or to use other AWS services by adding permissions to your execution role. To learn more, refer to [Amazon MWAA execution role](mwaa-create-role.md).

1. **Create user policies**. You might need to create multiple IAM policies for your users to configure access to your environment and Apache Airflow UI. To learn more, refer to [Accessing an Amazon MWAA environment](access-policies.md).

## Accessing the VPC endpoint for your Apache Airflow webserver (private network access)
<a name="configuring-access-vpce"></a>

If you've chosen the **Private network** option, you'll need to create a mechanism in your Amazon VPC to access the VPC endpoint (AWS PrivateLink) for your Apache Airflow webserver. We recommend using the same Amazon VPC, VPC security group, and private subnets as your Amazon MWAA environment for these resources.

If you've chosen **Both public and private network access**, you do not need to create a mechanism to access the Apache Airflow UI. It is accessible over the internet. The private VPC endpoint is used automatically by workers for internal communication.

To learn more, refer to [Managing access for VPC endpoints](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-access.html).