# Infrastructure protection

| DSSEC05: How do you secure infrastructure access while enabling regional<br>operations? |
| --------------------------------------------------------------------------------------- |
|                                                                                         |

Access to data and environments must be limited to locations that are trusted and meet
local jurisdictional requirements. Organizations must implement comprehensive access controls,
continuous monitoring, and role-based access aligned with jurisdictional boundaries to
maintain sovereignty requirements.

**Considerations**:

Establish trust as a key component of your security posture and implement access control
policies to govern infrastructure and environments. Whilst least privileged is an essential
mechanism of control and only providing this when required, within a Sovereignty perspective,
access to data and environments also need to be limited to locations that are trusted and
meets local jurisdictional requirements.

First, identifying the authorized support staff is key, followed by the identifying or
restricting locational accesses from which the staff are located. Once the support staff has
been authenticated, it is then important to authorise that person for access to only the
systems they need access to for the activity they are authorized for. Various systems and
solutions can provide this authentication and authorisation.

Insider exploits are becoming more prevalent alongside cyber attacks through stolen
credentials. To combat this, organizations should implement comprehensive access review
processes and continuous monitoring of access patterns. This includes regular attestation of
access rights, monitoring for unusual behavior patterns, and implementing break-glass
procedures for emergency access that maintain sovereignty requirements.

Support staff access should be granted on a time-limited basis with clear documentation
of the business justification. Organizations should maintain detailed records of access grants
and revocations to demonstrate adherence to sovereignty requirements. Additionally, privileged
access sessions should be monitored and logged, with automated alerts for suspicious
activities or access attempts from unauthorized locations.

Consider implementing role-based access control (RBAC) aligned with support staff
responsibilities and jurisdictional boundaries. This verifies that access permissions are
consistently applied and can be quickly adjusted as staff roles or regulatory requirements
change. Regular training on security awareness and sovereignty requirements should be
mandatory for support staff to maintain access privileges.

###### Best practices

- [DSSEC05-BP01 Control unauthorized remote access to
  infrastructure](dssec05-bp01.md "dssec05-bp01.md")
- [DSSEC05-BP02 Record operator sessions and retain logs](dssec05-bp02.md "dssec05-bp02.md")
- [DSSEC05-BP03 Empower regional teams](dssec05-bp03.md "dssec05-bp03.md")
