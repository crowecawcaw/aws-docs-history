# Recommended alarm templates for monitoring your AWS media workflow

Workflow monitor's recommended templates are a curated selection of AWS Elemental
service metrics with predefined alarm settings appropriate for the
metric. If you do not want to create customized alarm templates,
recommended templates provide you with best-practice monitoring
templates that are created by AWS.

Workflow monitor contains recommended template groups for each supported
service. These groups are designed to apply best-practice monitoring to
specific types of workflows. Each template group contains a curated
selection of alarms configured from service-specific metrics. For
example, a recommended template group for a MediaLive multiplex workflow
will have a different set of preconfigured metrics than a MediaConnect CDI
workflow.

###### To use recommended alarm templates

1. Follow the steps to [create an alarm template group](monitor-with-workflow-monitor-configure-alarms.md#monitor-with-workflow-monitor-alarms-groups-create "monitor-with-workflow-monitor-configure-alarms.md#monitor-with-workflow-monitor-alarms-groups-create"), or select an existing one.
2. In the **Alarm templates** section, select
   **Import**. You will need to import the
   AWS recommended templates into your template group.
3. Use the **CloudWatch alarm template groups**
   dropdown to select an AWS recommended group. These groups
   contain curated alarms for specific services.
4. Select the templates to import using the check boxes. Each
   template will list its metrics, preconfigured monitoring values,
   and provide a description of the metric. When you are done
   selecting templates, select the **Add** button.
5. The selected templates will move to the **Alarm
   template(s) to import** section. Review your
   choices and select **Import**.
6. After the import is complete, the selected templates will be
   added to the template group. If you want to add more templates,
   repeat the import process.
7. Imported templates can be customized after import. Alarm
   settings can be modified to fit your alarming needs.
