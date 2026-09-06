

# Managing access tokens for encrypted authentication
<a name="gr-managing-access-tokens"></a>

Access tokens provide encrypted authentication for DoH and DoT protocols. Unlike IP-based access sources, tokens work regardless of client location and offer enhanced security through encryption and expiration controls.

## Creating access tokens
<a name="gr-creating-access-tokens"></a>

Follow these steps to create access tokens to authenticate client devices that use DoH or DoT protocols.

1. Open the Route 53 Global Resolver console and navigate to your DNS view.

1. In the **Access source** section, choose **Create access token**.

1. For **Name**, enter a descriptive name that identifies the token's purpose, such as `mobile-devices` or `remote-workers-q4`.

1. For **Expiration**, set when the token should expire. We recommend 90 days or less for security. Consider your token distribution and renewal capabilities when setting the expiration period.

1. Choose **Create access token**.

1. Distribute the token securely to your client devices using your organization's secure communication channels.

## Configuring client devices with access tokens
<a name="gr-configuring-client-devices"></a>

Configure client devices to use access tokens for authentication with your Route 53 Global Resolver infrastructure.

**DoH configuration**  
To configure DoH with access tokens, you need your global resolver's DNS name or IP addresses:  

1. Use the GetGlobalResolver API to retrieve connectivity details for your resolver.

1. Note the `ipv4Addresses` (for example, 3.3.3.3, 3.3.3.4) and `dnsName` (for example, a1bc234567890a.route53globalresolver.global.on.aws).

1. Include the token as a URL parameter in the DoH endpoint using the DNS name:

   ```
   https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<token-value>
   ```
Replace `<token-value>` with the actual token that you generated.

**DoT configuration**  
For DoT queries with access tokens, include the token in an EDNS0 option with the following specifications:  
+ **Option Code:** `0xffa0`
+ **Option Data:** The access token in string format
The specific implementation depends on your DoT client software and how it handles EDNS0 options.

## Token lifecycle management
<a name="gr-token-lifecycle-management"></a>

Manage token expiration and renewal to maintain secure access for your client devices.
+ **Monitor expiration dates** - Track token expiration dates and plan renewals in advance.
+ **Renew before expiration** - Create new tokens before old ones expire to avoid service interruption.
+ **Rotate tokens regularly** - Replace tokens periodically even before expiration for enhanced security.
+ **Revoke compromised tokens** - Delete tokens immediately if you suspect they have been compromised.

Consider implementing automated token renewal processes for large deployments to reduce administrative overhead.