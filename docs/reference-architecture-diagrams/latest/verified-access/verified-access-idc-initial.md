

# With IAM Identity Center - Initial Request
<a name="verified-access-idc-initial"></a>

Publication date: **February 22, 2023 ([Diagram history](#vai-diagram-history))**

This flow shows how AWS Verified Access handles an initial request that does not have an identity cookie. AWS Verified Access redirects the user to [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) to collect the user identity before validating the request against the application policy.

## AWS Verified Access with IAM Identity Center - initial request flow
<a name="vai-diagram1"></a>

![Architecture diagram showing AWS Verified Access initial request verification flow with IAM Identity Center for user authentication.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/verified-access/images/verified-access-1.png)


The following steps describe the request verification flow:

1. The initial request targets the application domain hosted on an AWS Verified Access endpoint. This request does not have an identity cookie.

1. AWS Verified Access redirects the request to the identity provider, IAM Identity Center, to collect the user identity.

1. The browser redirects to the IAM Identity Center URL. The user completes the sign-in process.

1. IAM Identity Center redirects the user to the application domain to validate the identity token.

1. The browser sends the IAM Identity Center token to the application domain endpoint. AWS Verified Access uses it to set the user identity cookie.

1. AWS Verified Access redirects the user with the identity cookie to the original URI.

1. AWS Verified Access receives the request with the user identity cookie. For each request, it validates the user request against the application policy using the user identity.

1. AWS Verified Access proxies validated requests to application endpoints in the customer Amazon VPC.

## Further reading
<a name="vai-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="vai-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#vai-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](verified-access-idc-subsequent.md#vas-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](verified-access-device-initial.md#vdi-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](verified-access-device-subsequent.md#vds-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.