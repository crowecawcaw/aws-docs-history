# HNSEC05-BP02 Use MACsec encryption for dedicated

connections

Dedicated connections allow hybrid network connectivity over a
private network link. MACsec encrypts traffic at Layer 2 to securely
pass high bandwidth workloads between cloud and on-premises
infrastructure. It provides native, point-to-point encryption to
protect data communications. To use MACsec, both the dedicated
connection and your on-premises equipment must support it.

**Desired outcome:** Encrypt
high-speed data traffic between cloud and your data center to
protect sensitive workloads from interception or tampering.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Delivers encryption for high bandwidth connections
- Secures data in transit without sacrificing performance
- Enables compliance with industry and regulatory standards

## Implementation guidance

- Use dedicated connection links that support MACsec.
- Enable MACsec on both the dedicated connection port and your
  on-premises network device.
- Regularly validate and monitor MACsec status and connection
  health.

## Resources

- [MAC
  Security in Direct Connect](../../../directconnect/latest/UserGuide/MACsec.md "../../../directconnect/latest/UserGuide/MACsec.md")
