# MD_SEC 2:

How do you design workload security for long-term safety?

Certain Māori data may need to be available for generations to come. Consult with Māori
customers and advisers about what data retention policies they recommend according to the
different types of data. These data retention policies can be revisited in the future too.
Regardless of how long you are intending to store this data, all data needs to be properly
secured for the protection of taonga (treasure) for generations to come.

Ransomware is a good example to consider. If you have one copy of your data and you are
subject to a ransomware attack, you may not be able to recover your data. Consider how many
backup copies may be required to protect yourself from this scenario. Design appropriate
access controls to minimise the chance of accidental or malicious deletion or corruption of
back-ups. While it may seem redundant, it's important to store backups across multiple
different types of storage and in multiple different locations. With this strategy, there's
always an available backup, no matter the circumstances. Where irreplaceable digital taonga is
identified, it is important to consider offline replication in addition to the appropriate
data protection and resilience controls.

- **MD_SEC02-BP01: Understand data protection options available through
  your provider to protect data at the level of control your customer wants.**
  Customers control how they configure their environments and secure their content,
  including whether they encrypt their content (at rest and in transit), and what other
  security features and tools they use and how they use them. AWS does not change customer
  configuration settings, as these settings are determined and controlled by the customer.
  AWS customers have the ability to design their security architecture to meet
  their compliance needs. AWS provides the customer autonomy to decide when and how
  security measures are implemented in the cloud, in accordance with each customer's
  business needs. When choosing which option is best, you should understand the risks you
  are trying to mitigate, take into account both the benefits and costs of each solution,
  and choose a solution that meets your requirements. Choose a cloud provider that offers
  contractual restrictions on their access to your data and operational restrictions. AWS,
  for example, is one of those cloud providers who offers both.
- **MD_SEC02-BP02: Understand what encryption options are available to
  protect your data at rest and in transit.** Encryption of data at rest is a
  recommended best practice for protecting your data from unauthorised access. AWS
  provides several options for data encryption. One option is to have AWS create and
  manage encryption keys for you through the AWS Key Management Service. Many AWS services integrate with
  AWS KMS to enable encryption of your data. Another option is to create your own encryption
  keys within AWS KMS. This provides you with more control over your keys. This includes
  control over the key material, the rotation policy, and the permissions that define who
  can use or manage the key. AWS KMS is designed so that no one, not even an AWS employee,
  can retrieve your plaintext KMS keys from the service.
- **MD_SEC02-BP03: Make informed decisions about where data is
  stored**. Māori users of your system may prefer their data to be stored in New
  Zealand. AWS allows customers to control where their data is stored and processed, and
  your content won't be replicated or moved outside of your chosen AWS Region except as
  agreed by you. For customers in Aotearoa New Zealand, the options for storing data within
  New Zealand include the Auckland AWS Local Zone, an AWS Outpost, or the upcoming AWS
  Auckland region. Every commercial AWS region is designed, built, and operated in the
  same way and incorporates the same levels of security. When choosing an AWS
  infrastructure for your workload, take into account the possible trade-offs that may
  exist. For example, an AWS Region has a larger selection of AWS services and higher
  resiliency than an AWS Outpost. However, an AWS Outpost may provide more flexibility
  as to the location where the infrastructure can be placed. There are also costs and budget
  considerations to take into account. Some other considerations related to the location of
  data include:
  - Do you need to make a distinction between where data is processed and where it is
    stored? For example, the data could be stored in a database in New Zealand but
    processed on an EC2 instance in another region (of your choice) as part of an analytics job.
    Alternatively, it could be captured using a web application running on servers in
    Sydney and then saved to a database located in New Zealand.
  - Do you need to duplicate data across locations to meet your customer requirements?
    For example, a data archiving solution could send backups to another AWS Region for
    resiliency and security reasons. An application like a digital archive solution could
    make use of Amazon CloudFront for content distribution to help reduce latency for end users
    when accessing the content. This would require copies of data to be stored at CloudFront
    edge locations, while the primary data is stored in the origin storage service such as
    Amazon S3 or a database.
