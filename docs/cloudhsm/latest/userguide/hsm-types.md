

# HSM types in AWS CloudHSM
<a name="hsm-types"></a>

AWS CloudHSM also offers two hardware security module (HSM) types: *hsm1.medium* and *hsm2m.medium*. Review the details on this page before deciding which HSM type is right for your needs. 

In addition to cluster modes, AWS CloudHSM offers two HSM types: *hsm1.medium* and *hsm2m.medium*. Each HSM type uses different hardware, and each cluster can only contain one type of HSM. The following table lists the major differences between the two:


<table>
<thead>
  <tr><th>Differentiating feature</th><th>hsm1.medium</th><th>hsm2m.medium</th></tr>
</thead>
<tbody>
  <tr><td><b>Cluster mode compatibility</b></td><td>Available for clusters in FIPS mode.</td><td>Available for clusters in FIPS or non-FIPS mode.</td></tr>
  <tr><td><b>Network type compatibility</b></td><td>Not available</td><td>Available for clusters in FIPS or non-FIPS mode.</td></tr>
  <tr><td><b>Backup compatibility</b></td><td>Can be used to backup and restore to <b>hsm1.medium</b> and <b>hsm2m.medium</b> clusters in FIPS mode.</td><td>Can only be used to backup and restore <b>hsm2m.medium</b> clusters.</td></tr>
  <tr><td><b>Key capacity</b></td><td>3,300 per cluster.</td><td>16,666 total keys, with asymmetric keys having a maximum of 3,333 per cluster.</td></tr>
  <tr><td><b><a href="use-hsm.md">Client SDKs</a></b></td><td>Supports all Client SDKs.</td><td>Supports all Client SDKs.</td></tr>
  <tr><td><b><a href="client-history.md">Client SDK versions</a></b></td><td>Compatible with SDK version 3.1.0 and later.</td><td>Compatible with Client SDK version 5.9.0 and later.</td></tr>
  <tr><td><b>Region availability </b></td><td>CloudHSM no longer supports creating new clusters in any AWS Region. For more information, see <a href="compliance-dep-notif.md#hsm-dep-1">Deprecation notifications</a> for details.</td><td>Available in AWS Regions that <a href="https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html">CloudHSM is available.</a></td></tr>
  <tr><td><b>Performance</b></td><td colspan="2">To see the performance of each HSM type, refer to <a href="performance.md">AWS CloudHSM performance information</a>.</td></tr>
  <tr><td><b>Certification</b></td><td>FIPS 140-2, PCI DSS, PCI PIN, SOC2, and PCI-3DS compliant.</td><td>FIPS 140-3, PCI DSS, PCI PIN, SOC2 and PCI-3DS compliant.</td></tr>
</tbody>
</table>
