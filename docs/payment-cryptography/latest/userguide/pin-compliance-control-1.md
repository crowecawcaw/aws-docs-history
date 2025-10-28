# Control Objective 1: PINs used in transactions governed by these requirements are processed using equipment

and methodologies that ensure they are kept secure.

_Requirement 1:_ HSMs used by AWS Payment Cryptography were assessed as part of our PCI PIN assessment. For customers
using the service, Requirement 1-3 and 1-4 are “In Place” relative to the HSM managed by the service. The findings for
HSM will state that testing was attested to by the AWS QPA. The PIN Attestation of Compliance is available to be
referenced on AWS Artifact. Other SCD, like POI, in your solution will need to be inventoried and referenced.

_Requirement 2:_ Documentation of your procedures must specify how cardholder PINs are protected
with regards to divulging to your personnel, the PIN translation protocol(s) implemented, and protection during on-line and
off-line processing. In addition, your documentation should contain summary of cryptographic key management methods used within each zone.

_Requirement 3:_ POI must be configured for secure PIN encryption and transmission. AWS Payment Cryptography supports
only PIN block translations specified in Requirement 3-3.

_Requirement 4:_ The application must not store PIN blocks. The PIN blocks, even encrypted, must not be retained in
transaction journals or logs. The service does not store PIN blocks and the PIN assessment verifies that they are not in logs.

Note that the PCI PIN Security standard is applies to acquiring “the secure management, processing, and transmission of personal
identification number (PIN) data during online and offline payment card transaction processing at ATMs and point-of-sale (POS) terminals”,
as stated in the standard. However, the standard is often used for assessing cryptographic key management for payments outside of that
intended scope. This may include issuer use cases where PINs are stored. Exceptions to requirements for these cases should be agreed
with intended audience for the assessment.
