

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Configure URI accessibility for Gapwalk applications
<a name="ba-runtime-filteringURIs"></a>

This topic describes how to configure the filtering of URIs for Gapwalk applications. This feature does not require an identity provider (IdP).

To block a list of URIs, add the following two lines to the `application-main.yml` of your modernized application, replacing {{URI-1}}, {{URI-2}}, and so on, with the URIs that you want to block.

```
gapwalk-application.security.filterURIs: enabled
gapwalk-application.security.blockedURIs: {{URI-1}}, {{URI-2}}, {{URI-3}}
```