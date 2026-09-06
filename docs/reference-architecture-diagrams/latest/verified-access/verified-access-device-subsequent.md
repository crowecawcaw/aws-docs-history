

# With IAM Identity Center and Device Trust Provider - After Initial Request
<a name="verified-access-device-subsequent"></a>

Publication date: **February 22, 2023 ([Diagram history](#vds-diagram-history))**

This flow shows how AWS Verified Access handles subsequent requests when the application domain is already in the browser extension's trusted domain list. The browser extension automatically includes the device information cookie with each request.

## AWS Verified Access with IAM Identity Center and device trust - subsequent request flow
<a name="vds-diagram1"></a>

![Architecture diagram showing AWS Verified Access subsequent request flow with device trust provider where the browser extension automatically includes device information.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/verified-access/images/verified-access-4.png)


The following steps describe the request verification flow:

1. The application domain is in the browser extension's allow list. The browser extension sets the device information cookie.

1. The user sends the initial request to the AWS Verified Access endpoint. The identity cookie and device information cookie are included with the request to the application domain.

1. AWS Verified Access receives the request with the user identity cookie and device information cookie. For each request, it validates the user request against the policy using both the user identity and device posture.

1. AWS Verified Access proxies validated requests to application endpoints in the customer Amazon VPC.

**Note**  
The identity cookie has a lifetime associated with it. When that lifetime expires, the user must re-authenticate with IAM Identity Center. The local device agent continuously gathers device posture information for each request.

## Further reading
<a name="vds-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="vds-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](verified-access-idc-initial.md#vai-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](verified-access-idc-subsequent.md#vas-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](verified-access-device-initial.md#vdi-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 
| [Initial publication](#vds-diagram-history) | Reference architecture diagram first published. | February 22, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.