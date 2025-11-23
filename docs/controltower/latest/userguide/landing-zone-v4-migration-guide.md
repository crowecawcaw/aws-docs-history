# Landing Zone v4.0 migration guide

AWS Control Tower Landing Zone 4.0 introduces a major overhaul of the landing zone architecture, offering a flexible dedicated
controls experience and fully optional service integrations. Key enhancements include the ability to selectively enable
AWS Config, AWS CloudTrail, SecurityRoles, and AWS Backup integrations, with dedicated resources for AWS Config and AWS CloudTrail for
improved isolation.

The release removes mandatory organizational structure requirements, allowing customers to define their own, while
introducing a new `ConfigBaseline` for detective controls support without the requiring the comprehensive
`AWSControlTowerBaseline`. A service-linked Config Aggregator replaces previous aggregation methods,
streamlining compliance data collection.

Additionally, the manifest field becomes optional, enabling minimalist landing zone deployments focused solely on AWS Organizations
integration and control enablement. These changes provide greater customization options while maintaining robust
governance capabilities, allowing customers to tailor AWS Control Tower to their specific needs more effectively.
