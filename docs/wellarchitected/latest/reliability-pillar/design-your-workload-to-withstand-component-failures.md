# Design your workload to withstand component failures

Workloads with a requirement for high availability and low mean
time to recovery (MTTR) must be architected for resiliency.

###### Best practices

- [REL11-BP01 Monitor all components of the workload to detect
  failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md")
- [REL11-BP02 Fail over to healthy resources](rel_withstand_component_failures_failover2good.md "rel_withstand_component_failures_failover2good.md")
- [REL11-BP03 Automate healing on all layers](rel_withstand_component_failures_auto_healing_system.md "rel_withstand_component_failures_auto_healing_system.md")
- [REL11-BP04 Rely on the data plane and not the control plane
  during recovery](rel_withstand_component_failures_avoid_control_plane.md "rel_withstand_component_failures_avoid_control_plane.md")
- [REL11-BP05 Use static stability to prevent bimodal
  behavior](rel_withstand_component_failures_static_stability.md "rel_withstand_component_failures_static_stability.md")
- [REL11-BP06 Send notifications when events impact
  availability](rel_withstand_component_failures_notifications_sent_system.md "rel_withstand_component_failures_notifications_sent_system.md")
- [REL11-BP07 Architect your product to meet availability targets and uptime service level agreements (SLAs)](rel_withstand_component_failures_service_level_agreements.md "rel_withstand_component_failures_service_level_agreements.md")
