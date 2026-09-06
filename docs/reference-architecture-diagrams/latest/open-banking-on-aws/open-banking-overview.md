

# Open Banking on AWS: Overview
<a name="open-banking-overview"></a>

Publication date: **September 7, 2021 ([Diagram history](#ob-overview-history))**

With this architecture, you can open APIs for authorized third parties and implement Open Banking regulations. Third parties access consumer data (account balances, transactions, statements) or initiate payment submissions with customer consent. This supports use cases such as spend analysis, credit decisioning, and ecommerce payments.

## Open Banking overview diagram
<a name="ob-overview-diagram"></a>

![Reference architecture diagram showing the Open Banking ecosystem overview with consumer, third party, Trust Service Provider, and bank components.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/open-banking-on-aws/images/open-banking-overview.png)


The following steps describe the Open Banking ecosystem participants:

1. Access the licensed or accredited third-party application and provide consent for the third party to access consumer data or initiate a payment submission request.

1. Use third parties as authorized institutions that provide value-added services on top of regular banking needs (accounts information, payments). This approach supports use cases such as spend analysis, credit decisioning, and ecommerce payments.

1. Validate the authenticity of banks and third parties through a Trust Service Provider (TSP) authorized by a supervisory government body. The TSP issues digital certificates to third parties.

1. Connect the bank IT environment, including AWS and data center components.

## Further reading
<a name="ob-overview-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ob-overview-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ob-overview-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](open-banking-part1.md#ob-p1-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](open-banking-part2.md#ob-p2-history) | Reference architecture diagram first published. | September 7, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.