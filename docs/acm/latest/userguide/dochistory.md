

# Document history
<a name="dochistory"></a>



The following table describes the documentation release history of AWS Certificate Manager beginning in 2018.

| Change | Description | Date | 
| --- |--- |--- |
| [Adding best practice for domain name privacy](acm-bestpractices.md#best-practices-domain-name-privacy) | Advises against including confidential or sensitive information in ACM public certificate domain names. | July 29, 2026 | 
| [ACME certificate automation](#dochistory) | Added support for the Automated Certificate Management Environment (ACME) protocol. You can now create ACME endpoints, configure domain validations, and generate external account bindings to automate public certificate issuance for customer-managed infrastructure using standard ACME clients. See [ACME certificate automation](https://docs.aws.amazon.com/acm/latest/userguide/acm-acme.html). | June 18, 2026 | 
| [AWS Workload Credentials Provider](#dochistory) | AWS announces AWS Workload Credentials Provider, a lightweight client-side provider that automates deployment of exported certificates from ACM across AWS and non-AWS workloads. It runs on Windows and Linux and supports NGINX and Apache web servers. See [AWS Workload Credentials Provider](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-automation.html). | June 11, 2026 | 
| [Certificate transparency logging opt-out deprecated](#dochistory) | Certificate transparency logging opt-out is no longer available. All public ACM certificates are automatically recorded in certificate transparency logs. The `CertificateTransparencyLoggingPreference` option is deprecated. With this update, ACM issued public certificates will be compliant with upcoming browser policy changes which require that all TLS server authentication certificates issued after June 15, 2026 are logged to at least one Certificate Transparency log. | June 1, 2026 | 
| [ECDSA Key Usage exception for certificate reimport](#dochistory) | ACM now allows re-import of ECDSA certificates without the `keyEncipherment` Key Usage value, in compliance with RFC 5480. For more information, see [https://docs.aws.amazon.com/acm/latest/userguide/import-reimport.html](https://docs.aws.amazon.com/acm/latest/userguide/import-reimport.html). | April 3, 2026 | 
| [SearchCertificates documentation](#dochistory) | Updated certificate management documentation to use the SearchCertificates API for finding and filtering certificates. See [Search certificates](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-list.html). | March 31, 2026 | 
| [Updated public certificate validity period](#dochistory) | Public ACM certificates are now valid for 198 days, reduced from 13 months (395 days). With this update, ACM issued public certificates will be compliant with upcoming certificate lifetime requirements from the CA/B Forum. Per the new requirements, public certificates issued after March 15th 2026 must have a maximum validity of 200 days. The renewal window for public certificates has been updated to 45 days before expiration. Private certificates remain valid for 13 months (395 days). | February 18, 2026 | 
| [Change to re-importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-prerequisites.html) | ACM allows re-import of a certificate into the same ARN only when the ClientAuth EKU is missing from the previous certificate. This accommodates industry changes where certificate authorities no longer issue certificates with ClientAuth EKU to comply with Chrome's root program requirements. | October 22, 2025 | 
| [Added note about issuing certificates](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-acm-cert) | Added a note to the ACM certificate concept topic detailing changes to ACM certificate issuance with the TLS Web Client Authentication extension. | July 23, 2025 | 
| [Removed reference to authentication extension](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-acm-cert) | Removed the reference to the TLS Web Client Authentication extension from the example certificate. | July 3, 2025 | 
| [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md) | You can export ACM public certificates. | June 17, 2025 | 
| [ACM supports HTTP validation with CloudFront](http-validation.md) | ACM now supports HTTP validation for domain ownership verification when issuing certificates for CloudFront distributions. | April 24, 2025 | 
| [Deprecation of mail exchanger (MX) email validation](email-validation.md) | The ACM console no longer supports mail exchanger (MX). | July 11, 2024 | 
| [Adding best practice around account-level separation](acm-bestpractices.md#best-practices-account-separation) | Use account-level separation in your policies wherever possible. If not possible, you can restrict permissions at the account level or through encryption context condition keys in your policies. | June 11, 2024 | 
| [Upcoming deprecation of WHOIS email verification](email-validation.md) | Added a note about the deprecation of WHOIS email verification starting in June 2024. | February 5, 2024 | 
| [Condition key support added](#dochistory) | Added support for IAM Condition keys when requesting ACM certificates. For a list of supported conditions, see [https://docs.aws.amazon.com/acm/latest/userguide/acm-conditions.html#acm-conditions-supported](https://docs.aws.amazon.com/acm/latest/userguide/acm-conditions.html#acm-conditions-supported). | August 24, 2023 | 
| [ECDSA support added](#dochistory) | Added support for Elliptic Curve Digital Signature Algorithm (ECDSA) when requesting a public ACM certificate. For a list of supported key algorithms, see [https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms). | November 8, 2022 | 
| [New CloudWatch Events](#dochistory) | Added ACM Certificate Expired, ACM Certificate Available, and ACM Certificate Renewal Action Required events. For a list of supported CloudWatch Events, see [https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html). | October 27, 2022 | 
| [Updating key algorithm types for import](#dochistory) | Certificates imported into ACM may now have keys with additional RSA and Elliptic Curve algorithms. For a list of currently supported key algorithms, see [https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-prerequisites.html](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-prerequisites.html). | July 14, 2021 | 
| [Promoting "Monitoring and Logging" as a separate chapter](#dochistory) | Moved monitoring and logging documentation to its own chapter. This change covers CloudWatch Metrics, CloudWatch Events/EventBridge, and CloudTrail. For more information, see [https://docs.aws.amazon.com/acm/latest/userguide/monitoring-and-logging.html](https://docs.aws.amazon.com/acm/latest/userguide/monitoring-and-logging.html). | March 23, 2021 | 
| [Added CloudWatch Metrics and Events support](#dochistory) | Added DaysToExpiry metric and event and supporting APIs. For more information, see [https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-metrics.html](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-metrics.html) and [https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html). | March 3, 2021 | 
| [Added cross-account support](#dochistory) | Added cross-account support for using private CAs from AWS Private CA. For more information, see [https://docs.aws.amazon.com/acm/latest/userguide/ca-access.html](https://docs.aws.amazon.com/acm/latest/userguide/ca-access.html). | August 17, 2020 | 
| [Added region support](#dochistory) | Added region support for the AWS China (Beijing and Ningxia) Regions. For a complete list of supported regions, see [https://docs.aws.amazon.com/general/latest/gr/rande.html#acm-pca_region](https://docs.aws.amazon.com/general/latest/gr/rande.html#acm-pca_region). | March 4, 2020 | 
| [Added renewal workflow testing](#dochistory) | Customers can now manually test the configuration of their ACM managed renewal workflow. For more information, see [Testing ACM's Managed Renewal Configuration](https://docs.aws.amazon.com/acm/latest/userguide/manual-renewal.html). | March 14, 2019 | 
| [Certificate transparency logging now default](#dochistory) | Added ability to publish ACM public certificates into certificate transparency logs by default. | April 24, 2018 | 
| [Launching AWS Private CA](#dochistory) | Launched ACM Private Certificate Manager (CM), and extension of AWS Certificate Manager that allows users to establish a secure managed infrastructure for issuing and revoking private digital certificates. For more information, see [AWS Private Certificate Authority](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html). | April 4, 2018 | 
| [Certificate transparency logging](#dochistory) | Added certificate transparency logging to Best Practices. | March 27, 2018 | 

The following table describes the documentation release history of AWS Certificate Manager prior to 2018.


| Change | Description | Release Date | 
| --- | --- | --- | 
| New content | Added DNS validation to [AWS Certificate Manager DNS validation](dns-validation.md).  | November 21, 2017 | 
| New content | Added new Java code examples to [Use AWS Certificate Manager with the SDK for Java](sdk.md).  | October 12, 2017 | 
| New content | Added information about CAA records to [(Optional) Configure a CAA record](setup.md#setup-caa).  | September 21, 2017 | 
| New content | Added information about .IO domains to [Troubleshoot issues with AWS Certificate Manager](troubleshooting.md).  | July 07, 2017 | 
| New content | Added information about reimporting a certificate to [Reimport a certificate](import-reimport.md).  | July 07, 2017 | 
| New content | Added information about certificate pinning to [Best practices](acm-bestpractices.md) and to [Troubleshoot issues with AWS Certificate Manager](troubleshooting.md).  | July 07, 2017 | 
| New content | Added CloudFormation to [Managed automation with integrated services](acm-services.md).  | May 27, 2017 | 
| Update | Added more information to [Quotas](acm-limits.md).  | May 27, 2017 | 
| New content | Added documentation about [Identity and Access Management for AWS Certificate Manager](security-iam.md).  | April 28, 2017 | 
| Update | Added a graphic to show where validation email is sent. See [AWS Certificate Manager email validation](email-validation.md).  | April 21, 2017 | 
| Update | Added information about setting up email for your domain. See [AWS Certificate Manager email validation](email-validation.md).  | April 6, 2017 | 
| Update | Added information about checking certificate renewal status in the console. See [Check a certificate's renewal status](check-certificate-renewal-status.md).  | March 28, 2017 | 
| Update | Updated the documentation for using Elastic Load Balancing. | March 21, 2017 | 
| New content | Added support for AWS Elastic Beanstalk and Amazon API Gateway. See [Managed automation with integrated services](acm-services.md). | March 21, 2017 | 
| Update | Updated the documentation about [Managed certificate renewal](managed-renewal.md). | February 20, 2017 | 
| New content | Added documentation about [Imported certificates](import-certificate.md). | October 13, 2016 | 
| New content | Added AWS CloudTrail support for ACM actions. See [Using CloudTrail with AWS Certificate Manager](cloudtrail.md). | March 25, 2016 | 
| New guide | This release introduces AWS Certificate Manager. | January 21, 2016 | 