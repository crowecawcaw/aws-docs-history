# Responding to events

You should anticipate operational events, both planned (for
example, sales promotions, deployments, and failure tests) and
unplanned (for example, surges in utilization and component
failures). You should use your existing runbooks and playbooks to
deliver consistent results when you respond to alerts. Defined
alerts should be owned by a role or a team that is accountable for
the response and escalations. You will also want to know the
business impact of your system components and use this to target
efforts when needed. You should perform a root cause analysis
(RCA) after events, and then prevent recurrence of failures or
document workarounds.

AWS simplifies your event response by providing tools supporting
all aspects of your workload and operations as code. These tools
allow you to script responses to operations events and start
their initiation in response to monitoring data.

In AWS, you can improve recovery time by replacing failed
components with known good versions, rather than trying to repair
them. You can then carry out analysis on the failed resource out
of band.

###### Best practices

- [OPS10-BP01 Use a process for event, incident, and problem
  management](ops_event_response_event_incident_problem_process.md "ops_event_response_event_incident_problem_process.md")
- [OPS10-BP02 Have a process per alert](ops_event_response_process_per_alert.md "ops_event_response_process_per_alert.md")
- [OPS10-BP03 Prioritize operational events based on business
  impact](ops_event_response_prioritize_events.md "ops_event_response_prioritize_events.md")
- [OPS10-BP04 Define escalation paths](ops_event_response_define_escalation_paths.md "ops_event_response_define_escalation_paths.md")
- [OPS10-BP05 Define a customer communication plan for service-impacting events](ops_event_response_push_notify.md "ops_event_response_push_notify.md")
- [OPS10-BP06 Communicate status through dashboards](ops_event_response_dashboards.md "ops_event_response_dashboards.md")
- [OPS10-BP07 Automate responses to events](ops_event_response_auto_event_response.md "ops_event_response_auto_event_response.md")
