# Troubleshoot long ASN issues

If you are experiencing issues with long ASN configurations, use the following steps to troubleshoot:

**BGP session fails with a long ASN**

_Symptoms_: BGP session cannot establish after configuring a long ASN

_Cause_: On-premises router may not support long ASN capability

_Resolution_:

- Verify your router supports RFC 6793
- Check BGP configuration for consistent ASN format
- Review BGP logs for capability negotiation errors

**API responses show ASN as 0**

_Symptoms_: API responses display `asn` field as 0

_Cause_: This is expected behavior when actual ASN exceeds 2,147,483,647

_Resolution_: Use the `asnLong` field in API responses for the correct ASN value

**Migration from ASN to long ASN issues**

_Symptoms_: Connectivity loss during ASN migration

_Cause_: BGP session re-establishment required for ASN changes

_Resolution_:

- Plan migration during maintenance windows
- Update one virtual interface at a time
- Monitor BGP session status during changes
- Verify routing table convergence after migration

If you continue to experience issues with long ASN configurations after following these troubleshooting steps, [contact AWS Support](https://aws.amazon.com/support/createCase "https://aws.amazon.com/support/createCase") with the following information:

- Virtual interface ID or BGP peer ID
- Configured ASN values (both ASN and long ASN)
- Router model and software version
- BGP configuration and logs
- Error messages or symptoms observed
