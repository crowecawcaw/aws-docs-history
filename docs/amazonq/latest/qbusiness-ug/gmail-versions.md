

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Gmail connector versions
<a name="gmail-versions"></a>

Gmail offers two connector versions to meet different configuration needs:

## Latest Gmail connector (Recommended)
<a name="gmail-new-connector-overview"></a>

**Note**  
The latest connector provides improved accuracy. We recommend using the latest connector for new implementations. The legacy connector remains available for customers requiring specific features not yet supported in the latest connector.

The latest Gmail connector provides a simplified configuration experience with essential features:
+ Configurable crawling of Email and Draft Email content
+ Simplified filtering with only Date Range options
+ Enhanced UI with improved validation and tips
+ Automatic crawling of ACL and identity information

## Legacy Gmail connector
<a name="gmail-original-connector-overview"></a>

The original Gmail connector provides full-featured configuration with advanced options:
+ Complete entity type selection including Message attachments
+ Advanced filtering options including domains, keywords, and labels
+ Custom field mappings for metadata extraction
+ Configurable sync modes and VPC settings
+ Regex pattern matching for complex attachment filtering
+ Manual ACL and identity crawling configuration