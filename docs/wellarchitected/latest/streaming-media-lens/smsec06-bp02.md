

# SMSEC06-BP02 Select a content protection scheme that meets business objectives
<a name="smsec06-bp02"></a>

Organizations must choose the appropriate content protection technology based on their specific business requirements, content value, target platforms, and commercial obligations. The selection should balance security requirements with user experience, cost considerations, and technical complexity.

**Desired outcome:**
+ Implementation of content protection scheme aligned with business objectives
+ Compliance with licensing and commercial obligations
+ Support for required target platforms and devices
+ Scalable and maintainable content protection architecture

**Common anti-patterns:**
+ Organizations implement the most expensive multi-digital rights management (DRM) solution without assessing whether their content value and licensing agreements actually require hardware-level key protection, wasting resources on unnecessary complexity.
+ Teams select a single DRM system based on familiarity rather than device coverage requirements, resulting in content that can't be delivered to all target devices and requiring costly re-implementation.
+ Organizations store DRM encryption keys alongside content in the same storage system without proper key management separation, creating a single point of compromise that exposes both content and decryption keys.
+ Teams implement clear key encryption for content that licensing agreements explicitly require to be protected by a certified DRM system, violating contractual obligations and risking content withdrawal.
+ Organizations deploy content protection without considering player integrity, allowing tampered or unauthorized players to access DRM-protected streams and extract decryption keys from memory.
+ Teams fail to implement Secure Packager and Encoder Key Exchange (SPEKE) integration with their key provider, manually managing encryption keys in a way that doesn't scale and introduces operational risk of key exposure.

**Benefits of establishing this best practice:**
+ Selecting the appropriate scheme—clear key, single DRM, or multi-DRM—based on content value keeps protection investment proportionate to the revenue at risk from piracy.
+ Evaluating DRM requirements against target device environments confirms that content can reach all intended audiences without playback failures or degraded user experience.
+ Implementing the specific protection level required by content licensing agreements—whether clear key for original content or hardware-level DRM for studio content—reduces the risk of contractual violations.
+ SPEKE-based integration with key providers through AWS Media Services creates a standardized, scalable key exchange mechanism that supports multiple DRM systems without custom integration per provider.
+ Appropriate content protection directly reduces unauthorized consumption and redistribution, protecting subscription revenue and maintaining the value of exclusive content windows.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Common approaches include Clear Key Content Encryption and DRM systems. Both systems use Advanced Encryption Standard (AES)-128 to encrypt the content, but differ in how keys are managed and delivered. If you've licensed content from a third party, you might be commercially obligated to implement a DRM system. This is true of most film and television content. Implement the solution that is in alignment with your business and legal requirements.

**Clear key content encryption and tokenized access**

A clear key implementation is common for applications that don't require *Hollywood-grade* DRM systems, but want a pragmatic content protection scheme that makes it difficult for outright theft or improper sharing of content by paying users. By encrypting content with AES-128 encryption, we can control who can decrypt the content through key access policies. When combined with techniques like Amazon CloudFront Origin Access Control (OAC) and tokenized, temporary, access URLs, you can control who can retrieve the decryption keys and for how long the content endpoint will service requests for encrypted content. This method is called *clear key* because the content key is eventually *in the clear* within the user-space of the client and could theoretically be accessed by an unauthorized user. Though, with tokenized content endpoints, having the key doesn't necessarily mean that an unauthorized user would have access to retrieve and decrypt the content.

On AWS, clear key encryption can be accomplished by generating an AWS Key Management Service (KMS) key and then using the API to create data keys that can be used by an encryptor (typically an encoder or packager) to apply encryption to the content. These data keys are then stored in a scalable persistence layer like Amazon S3 or Amazon DynamoDB. Data key access can be granted to your audience through a combination of Amazon Cognito and Identity and Access Management (IAM) policies for user authentication and authorization. Delivery of these keys should be over an encrypted transport with tokenization.

**DRM systems**

Organizations working in the media and entertainment industry or with high-value content might have strict content protection objectives for content keys, content decryption, or both to be run only within hardware modules or Trusted Execution Environments (TEEs) that exist outside of the user-space on the client. These organizations might also have requirements to facilitate key revocation, offline playback, single-use keys, or multi-key encryption levels for the same asset. These complex organizational objectives can be achieved through the implementation of a DRM system, such as Apple FairPlay, Google Widevine, or Microsoft PlayReady.

While DRM systems add an additional layer of key protection and business control to your content protection, implementation of DRM varies by playback device. Though the industry is making strides to simplify DRM implementations, in practice, it's common to see multiple DRM systems implemented to achieve device compatibility across playback devices—increasing cost and complexity.

With the AWS Media Services, DRM systems are integrated into media processing and origination though the Secure Packager and Encoder Key Exchange or SPEKE. SPEKE provides an open standard proxy interface for any key provider to exchange key material and metadata. You can implement your own key service or use one of many DRM system providers that are part of the AWS Partner Network (APN).

*Secure packager and encoder key exchange architecture with AWS Elemental MediaConvert*

![secure-key-exchange-architecture.png](https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/images/image12.png)




*\\[Caption\\] **The SPEKE architecture is shown with encryption components providing secure streaming delivery to end user players.***

No number of content protection schemes can ever fully protect content from being exploited by an attacker and, in fact, complex schemes can even increase the risk of problems for your paying viewers. Commit time to determine the appropriate content protection schemes for your specific content balancing cost with content value. Be sure to balance cost of additional resources on software licensing or operational burden compared to the business value of the content being protected.

*Comparison of clear key and DRM systems for content protection*

Token-based access is one of the approaches used as the first layer of content protection. It is based on the generation of cryptographically signed tokens scoped to a specific video asset and issued to individual viewers using viewer-specific attributes (for example, source IP address, geo location, browser attributes). In addition to content encryption and DRM, token-based access control can be used in combination with digital rights management (DRM) systems or used as a single protection from unauthorized playback.

**Player integrity**

Take proper measures to limit discovery of the controls put in place to limit usage of a tampered player or unauthorized access to your media assets and distribution system. When you choose to create your own media player, determine which environments will help you check the integrity of your software packages.

Many environments, such as FireOS, Android, iOS, macOS, and Microsoft Windows, provide the capability for developers to sign their application packages as part of the process of uploading them to the environment's software or app store. The purpose of signing application packages is to verify that the package has not been tampered with or compromised between the time you uploaded your application and when the package has been installed on a client device. Although signature checks provide clear assurances that your player has not been tampered with since you signed it, they don't stop the tampering or reverse engineering of your player. Some environments strictly forbid installation of software packages outside the environment's software store, minimizing the risk of loading a compromised player.

### Implementation steps
<a name="implementation-steps"></a>

1. **Review the SPEKE specification:** Review the [SPEKE Specification API and Guide](https://docs.aws.amazon.com/speke/latest/documentation/speke-constraints-v2.html) to determine what encryption solution to use and review guidance provided through other [experiences such as the AWS Blog](https://aws.amazon.com/blogs/media/secure-content-packaging-with-expressplay-drm-and-aws-media-services/).

1. **Review encryption parameters:** Review encryption and SPEKE parameters or guidance within the specific services you will be using such as AWS [Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/speke-encryption-parameters.html).

1. **Set up DRM integration:** Set up your DRM integration or work with an AWS Partner to deploy a solution.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC06-BP01 Collaborate with business and legal stakeholders to align on content protection requirements](smsec06-bp01.html)
+ [SMSEC03-BP01 Implement content or sessions forensics](smsec03-bp01.html)

**Related documents**
+ [Secure Media Delivery at the Edge on AWS](https://aws.amazon.com/solutions/implementations/secure-media-delivery-at-the-edge/)
+ [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/)
+ [SPEKE Specification](https://docs.aws.amazon.com/speke/latest/documentation/)
+ [AWS Partner Network - DRM Solutions](https://aws.amazon.com/partners/find/results/?keyword=DRM)

**Related services**
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
+ [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)