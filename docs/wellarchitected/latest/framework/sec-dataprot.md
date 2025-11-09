# Data protection

Before architecting any system, foundational practices that
influence security should be in place. For example, data
classification provides a way to categorize organizational data
based on levels of sensitivity, and encryption protects data by
way of rendering it unintelligible to unauthorized access. These
tools and techniques are important because they support
objectives such as preventing financial loss or complying with
regulatory obligations.

In AWS, the following practices facilitate protection of data:

- As an AWS customer you maintain full control over your data.
- AWS makes it easier for you to encrypt your data and manage
  keys, including regular key rotation, which can be easily
  automated by AWS or maintained by you.
- Detailed logging that contains important content, such as file
  access and changes, is available.
- AWS has designed storage systems for exceptional resiliency. For
  example, Amazon S3 Standard, S3 Standard–IA, S3 One Zone-IA, and
  Amazon Glacier are all designed to provide 99.999999999%
  durability of objects over a given year. This durability level
  corresponds to an average annual expected loss of 0.000000001%
  of objects.
- Versioning, which can be part of a larger data lifecycle
  management process, can protect against accidental overwrites,
  deletes, and similar harm.
- AWS never initiates the movement of data between Regions.
  Content placed in a Region will remain in that Region unless you
  explicitly use a feature or leverage a service that provides
  that functionality.

The following questions focus on these considerations for
security.

| SEC 7:  How do you classify your data?                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Classification provides a way to categorize data, based on criticality and<br>sensitivity in order to help you determine appropriate protection and retention<br>controls. |

| SEC 8:  How do you protect your data at rest?                                                                             |
| ------------------------------------------------------------------------------------------------------------------------- |
| Protect your data at rest by implementing multiple controls, to reduce the<br>risk of unauthorized access or mishandling. |

| SEC 9:  How do you protect your data in transit?                                                                     |
| -------------------------------------------------------------------------------------------------------------------- |
| Protect your data in transit by implementing multiple controls to reduce the<br>risk of unauthorized access or loss. |

AWS provides multiple means for encrypting data at rest and in
transit. We build features into our services that make it easier
to encrypt your data. For example, we have implemented server-side
encryption (SSE) for Amazon S3 to make it easier for you to store
your data in an encrypted form. You can also arrange for the
entire HTTPS encryption and decryption process (generally known
as SSL termination) to be handled by Elastic Load Balancing (ELB).
