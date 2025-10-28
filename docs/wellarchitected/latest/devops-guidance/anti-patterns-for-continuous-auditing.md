# Anti-patterns for continuous

auditing

- **Inadequate audit trails**: Not keeping comprehensive
  audit trails makes it difficult to track actions performed in your environment. This
  makes it harder to detect suspicious activity or understand the cause of issues when
  they occur. Use services like AWS CloudTrail to create a record of actions taken in your AWS
  environment.
- **Manual evidence review**: Relying on manual processes to
  collect, aggregate, and review audit data can be error prone and can lead to
  inconsistencies. Manual review can be time-consuming and often cannot keep pace with the
  pace of development which leads to reduced ability to quickly respond to compliance
  issues. Instead, implement automated tools to continuously gather and analyze audit
  data. Use dashboards and alerts to give a real-time view of system compliance.
- **Viewing audits as a one-time event**: Treating audits as
  periodic, isolated checks instead of a continuous process can result in significant gaps
  between audits. During this time, many compliance issues might go undetected. Embed
  continuous auditing practices into the development lifecycle, including regular,
  automated checks in pipelines and taking an event-driven approach to auditing. Internal
  auditors can be embedded within teams, or act as enabling teams, to provide just-in-time
  audit expertise during planning and development cycles.
- **Expecting auditors to track every feature**: Anticipating
  that auditing teams will be able to keep up with the rapid pace of feature development
  and deployments while understanding the nuances of each change is an impractical
  expectation when practicing DevOps. The primary focus of the auditor should be on
  processes, controls, and patterns, rather than granular features. Shift the compliance
  responsibility closer to the source. Educate development teams on auditing requirements
  and best practices, empowering them to incorporate compliance into their development
  processes. Put detective, responsive, and preventive controls in place to enforce
  compliance where possible. This way, developers can produce features with built-in
  compliance, reducing the load on auditors and ensuring tighter compliance integration.
- **Overlooking developer training**: Assuming that
  development teams automatically know compliance and auditing best practices without
  proper training might result in them unknowingly introducing vulnerabilities or
  non-compliant features. Regularly update training materials and hold sessions, ensuring
  development teams are well-versed in compliance requirements.
