# 12 – Plan for data recovery

**How do you plan for logical, data-related recovery for your SAP
workload?** Work backwards from the business requirements to define an approach
to recover or reconstruct your business data. Depending on how you have architected for
resilience, different scenarios might fit in this category. At a minimum, your backup or
disaster recovery (DR) posture should protect you from accidental deletion, logical data
corruption, and malware. Be deliberate about the decision to restore, taking into account
the time to return to service and the dependencies between systems.

| ID        | Priority           | Best Practice                                                  |
| --------- | ------------------ | -------------------------------------------------------------- |
| ☐ BP 12.1 | Required           | Establish a method for consistent recovery of business<br>data |
| ☐ BP 12.2 | Highly Recommended | Establish a method for recovering configuration data           |
| ☐ BP 12.3 | Highly Recommended | Define a recovery approach for your complete SAP<br>estate     |
| ☐ BP 12.4 | Recommended        | Conduct periodic tests to validate your recovery<br>procedure  |
