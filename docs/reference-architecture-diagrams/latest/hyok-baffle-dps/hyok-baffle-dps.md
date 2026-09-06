

# Protect Your Data with HYOK Solutions by Baffle DPS
<a name="hyok-baffle-dps"></a>

Publication date: **May 28, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to use Baffle Data Protection Service (DPS) to implement Hold Your Own Key (HYOK) solutions. With Baffle DPS, you can add data-centric protection on AWS.

## Protect Your Data with HYOK Solutions by Baffle DPS
<a name="diagram1"></a>

![Architecture diagram showing HYOK data protection with Baffle DPS on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hyok-baffle-dps/images/hyok-baffle-dps.png)


1. End-of-day point-of-sale (POS) data downloads from wholesale and retail partner systems and saves on-premises.

1. The Baffle DPS data ingestion layer uses the on-premises encryption key with Format-Preserving Encryption (FPE). It tokenizes, anonymizes, and maps data flow before sending it to AWS.

1. A dedicated connection () or AWS Site-to-Site VPN secures the data while in transit.

1. Encrypted data arrives at AWS and stores without the encryption key, in either structured or unstructured format.

1. You can query encrypted data in AWS with various services, but the data remains encrypted.

1. The Baffle DPS data consumption layer uses the on-premises decryption key. It decrypts, de-tokenizes, and maps data flow back to clear-text form.

1. Clear-text data feeds business intelligence or downstream applications.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Key Management Service product page](https://aws.amazon.com/kms/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 28, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.