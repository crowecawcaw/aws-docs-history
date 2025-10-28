# Anti-patterns for cryptographic signing

- **Ignoring key compromise**: Key compromise can severely
  affect the integrity of the software. When cryptographic signing keys are suspected to
  be compromised, immediate steps should be taken to revoke and replace them to maintain
  the security and trust in the code base. Regular key rotation prevents prolonged
  unauthorized access from a compromised key and strengthens overall security.
- **Reuse of signing keys across projects**: Sharing the same
  signing keys across multiple projects also can affect the integrity of the software. If
  a key is compromised, all projects signed with that key become potential targets. To
  mitigate the risk, the best practice is to use distinct keys for different projects or
  workloads.
- **Incomplete signature verification**: Trusting incorrectly
  signed code can introduce vulnerabilities. Skipping the validation of cryptographic
  signatures for third-party libraries or dependencies jeopardizes application security.
  You should consistently validate signatures to maintain code integrity and authenticity.
  It is equally important to assess certificate attributes such as validity periods and
  key usage. Avoid relying exclusively on manual checks for signature validation; human
  oversight in this process is a risk. Using automation in the verification process
  upholds consistent security checks and minimizes errors.
- **Overlooking timestamp
  validation:** Ignoring timestamp validation can
  lead to situations where code is deemed untrustworthy due
  to an expired certificate, even if the code itself is
  legitimate and unaltered. This may result in unintentional
  outages or service disruptions, as systems might refuse to
  run or integrate with the signed artifact. Proper
  timestamp validation ensures that certificates were valid
  at the time the code was signed, preventing unnecessary
  disruptions due to expired certificates while still
  maintaining trust in the code's integrity.
- **Avoid certificate pinning**: Hard-coding certificate
  information within your software, often called [certificate
  pinning](../../../acm/latest/userguide/acm-bestpractices.md#best-practices-pinning "../../../acm/latest/userguide/acm-bestpractices.md#best-practices-pinning"), might initially seem like an extra layer of security by tightly
  coupling your code to a certificate. However, it is an anti-pattern as it makes your
  software inflexible and brittle. If the pinned certificate needs to be replaced or
  updated, it will require a software update, which might not be feasible, especially for
  critical systems or widely distributed applications. Instead, rely on proper certificate
  validation processes and maintain a flexible and agile certificate management system.
