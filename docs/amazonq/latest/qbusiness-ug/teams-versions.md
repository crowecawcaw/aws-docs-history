

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Microsoft Teams connector versions
<a name="teams-versions"></a>

You can choose between two Microsoft Teams connector versions:

## Latest Microsoft Teams connector (recommended)
<a name="teams-new-connector-overview"></a>

**Note**  
The latest connector provides improved accuracy. We recommend using the latest connector for new implementations. The legacy connector remains available if you need specific features not yet supported in the latest connector.

The latest Microsoft Teams connector offers a simplified configuration experience with the following features:
+ Chat messages and channel posts syncing
+ Simplified sync scope without channel wiki
+ Date range filters only
+ Enhanced UI layout with improved spacing
+ Application-level permissions for enhanced security
+ Automatic crawling of ACL and identity information

## Legacy Microsoft Teams connector
<a name="teams-original-connector-overview"></a>

The legacy Microsoft Teams connector provides full-featured configuration with advanced options:
+ Complete sync scope including calendar meetings, channel wiki, and attachments
+ Advanced filtering options with team names, channel names, and attachment sections
+ Custom field mappings for metadata extraction
+ Configurable sync modes and VPC settings
+ Regex pattern matching for complex attachment filtering
+ Manual ACL and identity crawling configuration