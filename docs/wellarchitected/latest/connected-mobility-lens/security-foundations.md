# Security foundations

| CMSEC_1: How are you maintaining consumer privacy during actions such as<br>in-vehicle purchase transactions or data collection? |
| -------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                  |

Vehicles today contain a multitude of sensors which enable many of the features we rely on for both convenience and safety. These sensors collect large amounts of data which must be both transmitted, stored, and potentially correlated between distributed systems which provide this functionality. When building these architectures, it is important to understand all applicable laws and compliance requirements which govern what data is necessary to collect, store or share with third parties, and how it should be anonymized to protect the privacy of consumers and their passengers. The system should be designed with these requirements in early stages and not after the system is in production.

**[CMSEC\_BP1.1] Personally identifiable information (PII) and unique
identifiers (IDs) assigned to a vehicle or consumer should be anonymized.**

Information which can be used to directly or indirectly identify an individual must be protected from disclosure. This information includes but is not limited to name, address, location data, or combination of other data elements such as Vehicle Identification Number (VIN) and International Mobile Equipment Identity (IMEI). This data should be encrypted in transit using secure protocols such as TLS and at rest using your own robust encryption keys or those provided by [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). Restrict access to data for authorized users by classifying data and creating separate views of this data according to the principles of least privilege using [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") or masking sensitive data using third party solutions such as [_DataMasque_](https://aws.amazon.com/blogs/apn/how-to-mask-sensitive-data-on-aws-using-datamasque "https://aws.amazon.com/blogs/apn/how-to-mask-sensitive-data-on-aws-using-datamasque").

**[CMSEC\_BP1.2] Location data collected from navigation systems should
be appropriately secured to protect anonymity.**

Data which can be used to locate a consumer or track travel routes should also be encrypted in transit and at rest. Location data which is sent to third parties should have any PII or IDs scrubbed from the request. In addition, the precision of coordinates for both latitude and longitude can be adjusted to provide additional privacy. As an example, [_Amazon Location Service_](https://aws.amazon.com/location/ "https://aws.amazon.com/location/") supports up to 6 decimal points for these coordinates which is accurate up to approximately 4 inches from the object of interest. As the number of decimal points is decreased so does the precision and depending on the requirements for the service being provided this may be an acceptable threshold.

**[CMSEC\_BP1.3] Data collected from cameras, microphones, biometric,
and other types of sensors should be appropriately secured.**

Sensors should only collect the minimum amount of data required to facilitate their function.
When possible, sensors such as microphones should leverage a wake word or activation of a
tactile button to begin the data collection process. These sensors should also contain idle
timeout logic to limit this collection. Still or video image captures should have
identifying features such as the faces of passengers and pedestrians for example blurred
using a proven process. The AWS blog post [Creating a serverless face blurring service for photos in Amazon S3](https://aws.amazon.com/blogs/compute/creating-a-serverless-face-blurring-service-for-photos-in-amazon-s3/ "https://aws.amazon.com/blogs/compute/creating-a-serverless-face-blurring-service-for-photos-in-amazon-s3/") outlines how this
can be accomplished using Amazon S3. Data should use strong encryption in transit and at rest to
verify privacy when transmitting to OEM or third-party systems. Other types of sensors such
as those that collect biometric data may be subject to other compliance standards such as
the Health Insurance Portability and Accountability Act (HIPAA) and require different
configurations for data handling and retention.

| CMSEC_2: Your risk management program should align to security standards, laws,<br>regulations, and frameworks in the connected vehicle space. |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                |

Your risk management program should be used to capture functional safety,
cybersecurity, privacy, and secure software development requirements throughout the
lifecycle of the vehicle. This can be accomplished by incorporating guidance from automotive
industry specific frameworks such as ISO-21434, information security standards like NIST
800-53 or ISO 27001, and the new UNR-155 and UNR-156 regulations concerning type approval
with regards to cyber security management systems and software update management systems.
These standards, frameworks, and regulations can inform your organization on how to design a
cyber security program that covers both the vehicle and the systems and resources that
interact with vehicles. This requires input and collaboration from a number of
cross-functional areas including but not limited to management, security, and legal to
address the needs that are specific to your organization.
