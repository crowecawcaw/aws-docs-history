

# IpRoute
<a name="API_IpRoute"></a>

Contains the IP address block. This is often the address block of the DNS server used for your self-managed domain. 

## Contents
<a name="API_IpRoute_Contents"></a>

 ** CidrIp **   <a name="DirectoryService-Type-IpRoute-CidrIp"></a>
IP address block in CIDR format, such as 10.0.0.0/24. This is often the address block of the DNS server used for your self-managed domain. For a single IP address, use a CIDR address block with /32. For example, 10.0.0.0/32.  
Type: String  
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([1-9]|[1-2][0-9]|3[0-2]))$`   
Required: No

 ** CidrIpv6 **   <a name="DirectoryService-Type-IpRoute-CidrIpv6"></a>
IPv6 address block in CIDR format, such as 2001:db8::/32. This is often the address block of the DNS server used for your self-managed domain. For a single IPv6 address, use a CIDR address block with /128. For example, 2001:db8::1/128.  
Type: String  
Pattern: `^((([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,7}:)|(([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})|(([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})|(([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})|(([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})|([0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))|(:((:[0-9a-fA-F]{1,4}){1,7}|:)))\/(12[0-8]|1[01][0-9]|[1-9]?[0-9])$`   
Required: No

 ** Description **   <a name="DirectoryService-Type-IpRoute-Description"></a>
Description of the address block.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

## See Also
<a name="API_IpRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/IpRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/IpRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/IpRoute) 