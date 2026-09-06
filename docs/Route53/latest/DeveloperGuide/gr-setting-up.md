

# Setting up account access for Route 53 Global Resolver
<a name="gr-setting-up"></a>

Before you start using Route 53 Global Resolver, you need an AWS account and the appropriate permissions to access Route 53 Global Resolver resources. This includes creating IAM users and roles with the necessary permissions.

This section guides you through the steps required to configure users and roles to access Route 53 Global Resolver.

**Topics**
+ [Creating policies and roles](#gr-setting-up-permissions)
+ [Network considerations](#gr-setting-up-network)

## Creating policies and roles
<a name="gr-setting-up-permissions"></a>

Configure AWS Identity and Access Management (IAM) permissions so your team can deploy and manage Route 53 Global Resolver resources. You can use administrative permissions for full access or read-only permissions for monitoring and viewing configurations.

All Route 53 Global Resolver API operations require appropriate IAM permissions. If you don't have the required permissions, API calls will return `AccessDeniedException` (401) or `UnauthorizedException` (401) errors.

### Administrative permissions
<a name="gr-setting-up-permissions-admin"></a>

If you're setting up Route 53 Global Resolver for the first time or managing all aspects of the service, you need administrative permissions. You can use these AWS managed policies:
+ `AmazonRoute53GlobalResolverFullAccess` - Provides full access to Route 53 Global Resolver resources, including creating, updating, and deleting global resolvers, DNS views, firewall rules, and domain lists
+ `AmazonRoute53FullAccess` - Required if you plan to use private hosted zone forwarding
+ `CloudWatchLogsFullAccess` - Required if you plan to send logs to Amazon CloudWatch
+ `AmazonS3FullAccess` - Required if you plan to import firewall domain lists from Amazon S3 or send logs to Amazon S3

### Read-only permissions
<a name="gr-setting-up-permissions-readonly"></a>

If you only need to view Route 53 Global Resolver configurations and logs, you can use these AWS managed policies:
+ `AmazonRoute53GlobalResolverReadOnlyAccess` - Provides read-only access to Route 53 Global Resolver resources, including viewing global resolvers, DNS views, firewall rules, domain lists, and access sources
+ `AmazonRoute53ReadOnlyAccess` - Required to view private hosted zone associations
+ `CloudWatchReadOnlyAccess` - Required to view logs in Amazon CloudWatch
+ `AmazonS3ReadOnlyAccess` - Required to view firewall domain list files stored in Amazon S3

## Network considerations
<a name="gr-setting-up-network"></a>

Before implementing Route 53 Global Resolver, consider the following network requirements:

Client IP ranges  
This is only required when using access source-based authentication. Identify the IP address ranges (CIDR blocks) for all clients that will use Route 53 Global Resolver. You'll need these for configuring rules for your access source.

DNS protocols  
Determine which DNS protocols your clients will use:  
+ **Do53** - Standard DNS over port 53 (UDP/TCP)
+ **DoH** - DNS-over-HTTPS for encrypted queries
+ **DoT** - DNS-over-TLS for encrypted queries

Firewall and security groups  
Ensure your network firewalls and security groups allow outbound traffic to Route 53 Global Resolver anycast IP addresses on the appropriate ports (53 for Do53, 443 for DoH, 853 for DoT).