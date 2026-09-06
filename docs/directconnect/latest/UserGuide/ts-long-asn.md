

# Troubleshoot long ASN issues
<a name="ts-long-asn"></a>

If you are experiencing issues with long ASN configurations, use the following steps to troubleshoot:

**BGP session fails with a long ASN**  
*Symptoms*: BGP session cannot establish after configuring a long ASN  
*Cause*: On-premises router may not support long ASN capability  
*Resolution*:  
+ Verify your router supports RFC 6793
+ Check BGP configuration for consistent ASN format
+ Review BGP logs for capability negotiation errors

**API responses show ASN as 0**  
*Symptoms*: API responses display `asn` field as 0  
*Cause*: This is expected behavior when actual ASN exceeds 2,147,483,647  
*Resolution*: Use the `asnLong` field in API responses for the correct ASN value

**Migration from ASN to long ASN issues**  
*Symptoms*: Connectivity loss during ASN migration  
*Cause*: BGP session re-establishment required for ASN changes  
*Resolution*:  
+ Plan migration during maintenance windows
+ Update one virtual interface at a time
+ Monitor BGP session status during changes
+ Verify routing table convergence after migration

If you continue to experience issues with long ASN configurations after following these troubleshooting steps, [contact AWS Support](https://aws.amazon.com/support/createCase) with the following information:
+ Virtual interface ID or BGP peer ID
+ Configured ASN values (both ASN and long ASN)
+ Router model and software version
+ BGP configuration and logs
+ Error messages or symptoms observed