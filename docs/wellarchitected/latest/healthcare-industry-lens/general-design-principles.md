# General design principles

The Well-Architected Framework identifies a set of general design
principles to facilitate good design in the cloud. In addition, the
following design principles should also be considered for designing
and operating healthcare workloads:

- **Align with applicable regulatory and
  quality frameworks:** Identify relevant regulations
  early, and architect solutions from the start to meet regulatory
  requirements.
- **Automation reduces operational
  risk:** Modern software practices, such as continuous
  integration and continuous delivery, allow for automated checks,
  like aligning to specific controls frameworks.
- **Encrypt all sensitive data:**
  Protecting data with encryption, at rest and in transit, is a
  best practice of the Well-Architected Framework.  Further, many
  regulatory frameworks applicable to healthcare workloads
  specifically call out encryption of health data, and it is
  required by the AWS Business Associate Addendum. Implement
  encryption of all health data in your environments.
- **Log everything:** Logging
  allows you to monitor system and data access, and to verify that
  only authorized individuals are accessing the appropriate data.
  Implement immutability for logs for long term retention.
- **Implement least privilege for all data,
  not just health data:** Granting access to only the
  systems and data required for someone, or something, to do a job
  is a best practice in the Well-Architected Framework.  Similar
  to the encryption design principle above, healthcare regulatory
  frameworks may require enforcing restrictions on access to
  health data. Restrict access to production systems and health
  data to only those who need it. Implement reviews to maintain
  least privilege over time.
- **Adopt modern software communication
  protocols:** Healthcare has many standards, some of
  which do not embrace modern software practices, such as APIs.
  Where possible, use data standards and communication protocols
  in-line with best practices to align with both current standards
  and potential future standards.
- **Promote interoperability:**
  Unlock new product development opportunities and improve patient
  outcomes with architectures that facilitate secure, governed
  access to health data across silos.
- **Plan to recover from failures
  automatically:** Healthcare workloads enable the
  delivery of care to patients. Consequently, failures may
  negatively impact patients. Identify critical workloads and the
  key performance indicators (KPIs) that describe workload health.
  Design architectures with monitoring and automated recovery
  processes to ensure that systems meet availability requirements.
