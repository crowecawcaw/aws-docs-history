# DRHCSEC09-BP01 Train and test incident responders on policies specific to data residency

Train and test incident responders on regulations on storage
location based on data
classification. 

**Desired outcome:** Incident
responders have passed tests of their ability to respond to data
being stored in noncompliant locations.

**Common anti-patterns:**

- Playbooks not being tested by people responsible for using
  them

**Benefits of establishing this best
practice:** You can prepare for a data residency incident
by having incident management and investigation policy and
processes that align to your data residency requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Update your incident response playbooks with the impact of
  policies specific to data residency, such as authorized and
  unauthorized locations for data.
- Update expected incidents and known security findings or
  alerts with the findings for each data residency-related
  detective control.
- For each preventative control, create at least one test hat
  proves that the attempted action is denied.
- For each detective control, create at least one test,
  perform the test, then assess if the detection occurred and
  was visible where expected for responders.
- If you use Outposts or Local Zones and have policies that
  prohibit data from being stored within Region locations,
  create a test for each service you use in the workload, and
  configure iterations of the test for all Regions that aren't
  covered by the organization-wide Region deny SCP.
- Evaluate
  [AWS Security Incident Response](../../../security-ir/latest/userguide/what-is.md "../../../security-ir/latest/userguide/what-is.md") to determine if it's an
  appropriate option for your organization.

## Resources

**Related best practices:**

- [SEC10-BP03
  Prepare forensic capabilities](../security-pillar/sec_incident_response_prepare_forensic.md "../security-pillar/sec_incident_response_prepare_forensic.md")
- [SEC11-BP01
  Train for application security](../security-pillar/sec_appsec_train_for_application_security.md "../security-pillar/sec_appsec_train_for_application_security.md")
- [SEC10-BP04
  Develop and test security incident response
  playbooks](../security-pillar/sec_incident_response_playbooks.md "../security-pillar/sec_incident_response_playbooks.md")

**Related documentation:**

- [Application
  security](../security-pillar/application-security.md "../security-pillar/application-security.md")

**Related videos:**

- [re:Invent
  2024 SEC360: Respond and recovery faster with AWS Security
  Incident Response](https://www.youtube.com/watch?v=5Bx7f_e4dDM "https://www.youtube.com/watch?v=5Bx7f_e4dDM")
