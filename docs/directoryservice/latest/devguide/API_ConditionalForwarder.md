# ConditionalForwarder

Points to a remote domain with which you are setting up a trust relationship.
Conditional forwarders are required in order to set up a trust relationship with another
domain.

## Contents

**DnsIpAddrs**

The IP addresses of the remote DNS server associated with RemoteDomainName. This is the
IP address of the DNS server that your conditional forwarder points to.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**DnsIpv6Addrs**

The IPv6 addresses of the remote DNS server associated with RemoteDomainName. This is the
IPv6 address of the DNS server that your conditional forwarder points to.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**RemoteDomainName**

The fully qualified domain name (FQDN) of the remote domains pointed to by the
conditional forwarder.

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`

Required: No

**ReplicationScope**

The replication scope of the conditional forwarder. The only allowed value is
`Domain`, which will replicate the conditional forwarder to all of the domain
controllers for your AWS directory.

Type: String

Valid Values: `Domain`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ConditionalForwarder.md "../../../goto/SdkForCpp/ds-2015-04-16/ConditionalForwarder.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ConditionalForwarder.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ConditionalForwarder.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ConditionalForwarder.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ConditionalForwarder.md")
