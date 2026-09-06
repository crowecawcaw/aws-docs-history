

# Routing traffic to Amazon OpenSearch Service domain endpoint
<a name="routing-to-open-search-service"></a>

Amazon OpenSearch Service is is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud. An OpenSearch Service Service domain is synonymous with an OpenSearch Service cluster. Domains are clusters with the settings, instance types, instance counts, and storage resources that you specify. For more information, see [What is Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) in the *Amazon OpenSearch Service Developer Guide.*

## Prerequisites
<a name="routing-to-open-search-service-prerequisites"></a>

To get started, you need the following:

An OpenSearch Service domain that has a custom domain name, such as example.com that matches the name of the Route 53 record that you want to create.

For more information, see the following topics:
+ [Getting started](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) in the *Amazon OpenSearch Service Developer Guide*.
+ [Creating a custom endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/customendpoint.html) in the *Amazon OpenSearch Service Developer Guide*.

## Configuring Amazon Route 53 to route traffic to an Amazon OpenSearch Service domain endpoint
<a name="routing-to-open-search-service-configuring"></a>

To use Route 53 to route traffic to OpenSearch Service you first get the domain endpoint provided by OpenSearch Service. This dual stack endpoint is provided only if custom endpoint is enabled on an OpenSearch Service domain with dual-stack network mode. For more information, see [Create a custom endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/customendpoint.html) in the *Amazon OpenSearch Service Developer Guide*.<a name="routing-to-open-search-procedure"></a>

**To route traffic to an OpenSearch Service endpoint**

1. Go to [https://aws.amazon.com](https://aws.amazon.com) and choose **Sign In to the Console**.

1. Under **Analytics**, choose **Amazon OpenSearch Service**.

1. Under **Managed clusters** choose **Domains**.

1. On the **Domains** page choose the name of the domain that you want to route traffic to.

1. On the domain detail page copy the value for the **Domain endpoint v2 (dual stack)**.

1. Open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the linked name of the hosted zone for the domain that you want to use to route traffic to your OpenSearch Service endpoint. The domain name must match the custom endpoint defined in OpenSearch Service.

1. Choose **Create record**.

   You can use the wizard to create the records or choose **Switch to quick create**.

1. Specify the following values:  
**Routing policy**  
Choose the applicable routing policy. For more information, see [Choosing a routing policy](routing-policy.md).  
**Record name**  
Enter the domain name that you want to use to route traffic to your OpenSearch Service domain endpoint. The default value is the name of the hosted zone.  
For example, if the name of the hosted zone is example.com and you want to use **acme.example.com** to route traffic to your distribution, enter **acme**.  
**Alias**  
If you are using the **Quick create** record creation method, turn on **Alias**.  
**Value/Route traffic to**  
Choose **Alias to OpenSearch Service domain endpoint**. Choose the Region that the OpenSearch Service domain was created in, and choose the value that you got in step 5.  
**Record type**  
Choose **A – IPv4 address**, **AAAA – IPv6 address** or both for dual-stack.  
**Evaluate target health**  
Choose **No**. For information about evaluating target health, see [Evaluate target health](resource-record-sets-values-alias.md#rrsets-values-alias-evaluate-target-health).

1. Choose **Create records**.