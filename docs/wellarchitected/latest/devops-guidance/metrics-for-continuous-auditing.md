# Metrics for continuous auditing

- **Audit lead time**: The
  total duration taken to complete a single audit cycle,
  from the initiation of the audit to its completion. This
  metrics can help in optimizing the audit process and
  allocating resources efficiently. Long audit times might
  suggest inefficiencies, bottlenecks, or a lack of
  automation. Streamline the audit process by incorporating
  automated tools, refining audit scopes, and ensuring clear
  communication among involved teams. Measure this metric by
  logging the start and end time of each audit cycle.
  Calculate the difference to get the total time spent per
  audit.
- **Mean time between audits
  (MTBA)**: The average time interval between
  consecutive audits. This metric can help organizations
  determine if they are auditing frequently enough to catch
  potential vulnerabilities or compliance issues in a timely
  manner. If the time between audits is too long,
  vulnerabilities may go undetected for extended periods,
  increasing risk and reducing the ability to adhere to
  regulatory changes or major incidents. As processes become
  more streamlined and as automation is integrated, this
  metric should naturally improve. The ideal MTBA will vary
  based on risk assessments, compliance needs, and system
  changes. Measure this metric by logging the date of each
  completed audit. Calculate the difference in dates between
  consecutive audits and then find the average over a given
  period, such as quarterly or yearly.
- **Known vulnerability
  age**: The duration that known vulnerabilities
  have remained unresolved in the system. This metric helps
  keep track of the age of vulnerabilities and can provide
  insights that drive the effectiveness and agility of the
  remediation process. High severity vulnerabilities that
  remain open for long periods indicate potential risks.
  Calculate for each open vulnerability by subtracting the
  date it was identified from the current date to determine
  its age. Categorize the results by severity, such as
  critical, high, medium, and low, as an additional facet to
  consider.
- **Security control
  risk**: The potential risk posed by each system
  based on the effectiveness and health of its implemented
  security controls. This metric enables pinpointing which
  systems might be at higher risk due to insufficient or
  ineffective security controls. Improve this metric by
  regularly reviewing and updating security controls based
  on threat modeling, attack vectors, audit findings, and
  system-specific risks. Evaluate each system's security
  controls against a standardized framework or criteria.
  Weight scores based on the importance of the control to
  the overall system security, and aggregate to get an
  overall risk level for the system.
- **Exception rate**: The number of compliance exceptions,
  such as elevated permissions or bypassed controls, relative to the number of changes
  being made. This metric serves as an early warning system for potential vulnerabilities,
  emerging anti-patterns, or the need to update controls. Monitoring the nature and
  severity of exceptions can offer insights into both the quantity and quality of
  compliance deviations. Improve this metric by regularly reviewing compliance
  requirements and procedures for granting exceptions. Exceptions should be
  well-documented, searchable, and only granted when absolutely necessary. Conduct regular
  exception reviews, especially for major exceptions, to understand the root cause and
  implement corrective measures. Calculate by dividing the number of exceptions made for a
  given system by the number of changes made over a specific time frame. Regularly review
  the nature and severity of these exceptions to differentiate between minor deviations
  and major compliance breaches.
