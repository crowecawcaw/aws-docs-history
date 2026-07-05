End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Automated instance configuration in AMS Advanced

The AMS Advanced automated instance configuration service runs daily and automatically scans and updates
the SSM and CloudWatch agents and configuration files on your managed EC2 instances.
The updates apply, as needed to:

- SSM and CloudWatch agents
- CloudWatch configuration files

These updates allow AMS to access your AMS-managed EC2 instances, and to configure your instances
to emit appropriate
[logs](auto-config-logs-cw.md "auto-config-logs-cw.md") and metrics.

###### Topics

- [Prerequisites for automated instance configuration](auto-config-pre-reqs.md "auto-config-pre-reqs.md")
- [SSM Agent automatic installation](ssm-agent-auto-install.md "ssm-agent-auto-install.md")
- [Automated changes](auto-config-changes-made.md "auto-config-changes-made.md")
