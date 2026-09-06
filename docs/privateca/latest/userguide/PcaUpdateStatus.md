

# Understand AWS Private CA CA status
<a name="PcaUpdateStatus"></a>

The status of a CA that is managed by AWS Private CA results from a user action or, in some cases, from a service action. For example, a CA status changes when it expires. The status options available to CA administrators vary depending on the current status of the CA.

AWS Private CA can report the following status values. The table shows the CA capabilities available in each state.

**Note**  
For all status values except `DELETED` and `FAILED`, you are billed for the CA.



<table>
<thead>
  <tr><th>Status</th><th>Issue certificates</th><th>Validate certs with OCSP</th><th>Generate CRLs</th><th>Generate audits</th><th>You can update the CA cert</th><th>Certificates can be revoked</th><th>You are billed for the CA</th></tr>
</thead>
<tbody>
  <tr><td><code>CREATING</code> – The CA is being created.</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td><code>PENDING_CERTIFICATE</code> – The CA has been created and needs a certificate to be operational.*</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td><code>ACTIVE</code></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><code>DISABLED</code> – You have manually disabled the CA.</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><code>EXPIRED</code> – The CA certificate has expired.**</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td><code>FAILED</code></td><td colspan="6">The <code>CreateCertificateAuthority</code> action failed. This can occur because of a network outage, backend AWS failure, or other errors. A failed CA cannot be recovered. Delete the CA and create a new one.</td><td>No</td></tr>
  <tr><td><code>DELETED</code></td><td colspan="6">Your CA is within the restoration period, which can have a length of 7-30 days. After this period, it is permanently deleted. <ul><li> If you call the <code>RestoreCertificateAuthority</code> API on a CA with <code>DELETED</code> status and an expired certificate, the CA will be set to <code>EXPIRED</code>. </li><li> For more information about deleting a CA, see <a href="PCADeleteCA.md">Delete your private CA</a>. </li></ul></td><td>No</td></tr>
</tbody>
</table>


To complete activation, you need to generate a CSR, get a signed CA certificate from a CA, and import the certificate into AWS Private CA. The CSR can be submitted either to your new CA (for self-signing), or to an on-premises root or subordinate CA. For more information, see [Installing the CA certificate](PCACertInstall.md).

You cannot directly change the status of an expired CA. If you import a new certificate for the CA, AWS Private CA resets the status to `ACTIVE` unless it was set to `DISABLED` before the certificate expired.

**Additional considerations about expired CA certificates:**
+ CA certificates are not automatically renewed. For information about automating renewal through AWS Certificate Manager, see [Assign certificate renewal permissions to ACM](assign-permissions.md#PcaPermissions). 
+ If you attempt to issue a new certificate with an expired CA, the `IssueCertificate` API returns `InvalidStateException`. An expired root CA must self-sign a new root CA certificate before it can issue new subordinate certificates.
+ `The ListCertificateAuthorities` and `DescribeCertificateAuthority` APIs return a status of `EXPIRED` if the CA certificate is expired, regardless of whether the CA status is set to `ACTIVE` or `DISABLED`. However, if the expired CA has been set to `DELETED`, the status returned is `DELETED`.
+ The `UpdateCertificateAuthority` API cannot update the status of an expired CA.
+ The `RevokeCertificate` API cannot be used to revoke any expired certificate, including a CA certificate.

## Relation between CA status and CA lifecycle
<a name="status-and-lifecycle"></a>

The following diagram illustrates the CA lifecycle as an interaction of management actions with CA status.



![Interaction of CA management actions and status.](http://docs.aws.amazon.com/privateca/latest/userguide/images/status.png)



**Diagram key**  

|  |  |  |  | 
| --- |--- |--- |--- |
| ![Blue rectangle shape representing a management action in the diagram.](http://docs.aws.amazon.com/privateca/latest/userguide/images/rectangle.png)Management action | ![Blue parallelogram shape with angled sides and sharp corners.](http://docs.aws.amazon.com/privateca/latest/userguide/images/parallelogram.png)CA status | ![Blue arrow pointing to the right, indicating direction or progression.](http://docs.aws.amazon.com/privateca/latest/userguide/images/arrow-solid.png)Action results in a state change | ![Four dots followed by a right-pointing arrow indicating progression or continuation.](http://docs.aws.amazon.com/privateca/latest/userguide/images/arrow-dotted.png)New state enables new action | 

At the top of the diagram, management actions are applied through the AWS Private CA console, CLI, or API. The actions take the CA through creation, activation, expiration and renewal. The CA status changes in response (as shown by the solid lines) to manual actions or automated updates. In most cases, a new status leads to a new possible action (shown by a dotted line) that the CA administrator can apply. The lower-right inset shows the possible status values permitting delete and restore actions.

**Topics**
+ [Relation between CA status and CA lifecycle](#status-and-lifecycle)