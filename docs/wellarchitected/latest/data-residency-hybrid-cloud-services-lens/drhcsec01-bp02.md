# DRHCSEC01-BP02 Document any differences in the treatment of log data into the control objectives

As data residency requirements have the potential to apply to Log
data, control objectives should explicitly state which data
elements are subject to data residency requirements and if there
is differences is requirements when stored in the form of logs.

**Desired outcome:** Control
objectives address the allowed location of specific data elements
present in log data.

**Common anti-patterns:**

- Enabling logging without awareness or control of where the
  logs are stored and what data is stored
- Only reviewing log data attributes and location during the
  testing phase of project

**Benefits of establishing this best
practice:** Addressing requirements for log data up front
can lower cost and risk of non-compliance by avoiding rework later
in the initiative cycle.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

1. For each AWS service your architecture will use to store or
   transmit data, review the logging section of the service's
   user guide.
2. Identify what data elements are always logged if logging is
   enabled, which data elements are optionally logged, and if
   the location of storage of the logs is configurable. Many
   services can be configured to use Amazon CloudWatch Logs,
   and some also store logs in files. Include all forms of
   logs, including AWS service logs, application logs generated
   by the workload, operating system, agent, and other system
   level logs.
3. Update control objectives if they do not clearly address log
   data elements.
4. If compliance requirements prohibit any of those data
   elements from being stored in the Region, then implement
   controls which prevent or detect enablement of that specific
   logging. Examples where logs can only be configured to be
   stored in the Region are ALB access logs, VPC Flow Logs, any
   CloudWatch Logs, and AWS X-Ray logs. Example of potentially
   sensitive data element in logs is source (client) IP
   address.
5. If any logs are replicated to other locations, then
   explicitly define controls for the location of those servers
   or services.

## Resources

- [SEC04-BP01
  Configure service and application logging](../security-pillar/sec_detect_investigate_events_app_service_logging.md "../security-pillar/sec_detect_investigate_events_app_service_logging.md")
