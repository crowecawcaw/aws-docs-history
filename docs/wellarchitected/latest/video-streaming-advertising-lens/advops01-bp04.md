# ADVOPS01-BP04 Establish data governance and compliance operations

Advertising data management requires robust governance and
compliance procedures, especially in a multi-Region
environment. This best practice verifies adherence to
regional data privacy laws while maintaining operational
efficiency across global advertising operations.

## Implementation guidance

- For data residency compliance alignment:
  - Implement landing zone controls for different
    geographical Regions
  - Configure data boundary controls using AWS Control
    Tower
  - Set up guardrails for data movement between Regions
  - Monitor and enforce data locality requirements

- For data governance:
  - Establish data classification policies for
    advertising data types
  - Implement data retention and archival procedures
  - Set up access controls and encryption policies
  - Configure audit logging and compliance reporting

- For regulatory compliance alignment:
  - Implement GDPR requirements for EU user data
  - Set up consent management systems
  - Monitor compliance with regional advertising laws

## Key AWS services

- AWS Control Tower
- AWS Organizations
- AWS Config
- AWS CloudTrail
- Amazon Macie
- AWS Local Zones
- AWS Identity and Access Management

## Resources

- [Best Practices for managing data residency in AWS Local Zones using landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/ "https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/")
- [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/")
- [Scale
  across borders: build a multi-Region architecture while
  maintaining data residency](https://community.aws/content/2dhVhtsciD5gVBlCKUlHoszrDzU/scale-beyond-borders?lang=en#aws-reference-architecture-for-multiregion-with-data-residency "https://community.aws/content/2dhVhtsciD5gVBlCKUlHoszrDzU/scale-beyond-borders?lang=en#aws-reference-architecture-for-multiregion-with-data-residency")
