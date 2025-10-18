# HSM types in AWS CloudHSM

AWS CloudHSM also offers two hardware security module (HSM) types:
 *hsm1.medium* and *hsm2m.medium*. Review the details
 on this page before deciding which HSM type is right for your needs. 

In addition to cluster modes, AWS CloudHSM offers two HSM types: *hsm1.medium* and *hsm2m.medium*. 
 Each HSM type uses different hardware, and each cluster can only contain one type of HSM. The following table lists the major differences between the two:



| Differentiating feature | hsm1.medium | hsm2m.medium |
| --- | --- | --- |
| **Cluster mode compatibility** | Available for clusters in FIPS mode. | Available for clusters in FIPS or non-FIPS mode. |
| **Network type compatibility** | Not available | Available for clusters in FIPS or non-FIPS mode. |
| **Backup compatibility** | Can be used to backup and restore to **hsm1.medium** and **hsm2m.medium** clusters in FIPS mode. | Can only be used to backup and restore **hsm2m.medium** clusters. |
| **Key capacity** | 3,300 per cluster. | 16,666 total keys, with asymmetric keys having a maximum of 3,333 per cluster. |
| **[Client SDKs](use-hsm.md "use-hsm.md")** | Supports all Client SDKs. | Supports all Client SDKs. |
| **[Client SDK versions](client-history.md "client-history.md")** | Compatible with SDK version 3.1.0 and later. | Compatible with Client SDK version 5.9.0 and later. |
| **Region availability**  | CloudHSM no longer supports creating new clusters in any AWS Region. For more information, see [Deprecation notifications](compliance-dep-notif.md#hsm-dep-1 "compliance-dep-notif.md#hsm-dep-1") for details. | Available in AWS Regions that [CloudHSM is available.](https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html "https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html") |
| **Performance** | To see the performance of each HSM type, refer to [AWS CloudHSM performance information](performance.md "performance.md"). |
| **Certification** | FIPS 140-2, PCI DSS, PCI PIN, SOC2, and PCI-3DS compliant. | FIPS 140-3, PCI DSS, PCI PIN, and SOC2 compliant. |
