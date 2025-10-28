# DRHCSEC10-BP01 Update your threat models to cover the accidental or malicious storage of data in unauthorized locations

Threat models should include specific
scenarios where the threat is data stored in unauthorized
locations due to accidental storage as well as maliciously
intent.

**Desired outcome:** Threat models
cover all risks to data residency compliance.

**Common anti-patterns:**

- Threat models do not include specific location of data as a
  risk

**Benefits of establishing this best
practice:** Up to date threat models help prepare people
to respond to incidents.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Review existing threat models, and remediate if they don't
  already address exfiltration to unauthorized internal
  accounts, unauthorized external accounts, or locations
  outside of AWS.
- Add threat scenarios where data is stored in an unauthorized
  location, such as in any or specific Regions, due to data
  residency policies within the same account.

## Resources

**Related documentation:**

- [How
  to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/ "https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/")
