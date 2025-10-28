# Model Monitor schedules and alerts

Using the Python SDK, you can create a model monitor for data quality, model quality, bias
drift, or feature attribution drift. For more information about using SageMaker Model Monitor, see [Data and model quality monitoring with Amazon SageMaker Model Monitor](model-monitor.md "model-monitor.md"). The Model Dashboard populates information from all
the monitors you create on all your models in your account. You can track the status of each
monitor, which indicates whether your monitor is running as expected or failed due to an
internal error. You can also activate or deactivate any monitor in the model details page
itself. For instructions about how to view scheduled monitors for a model, see [View scheduled monitors](model-dashboard-schedule-view.md "model-dashboard-schedule-view.md"). For
instructions about how to activate or deactivate model monitors, see [Activate or deactivate a model
monitor](model-dashboard-schedule-activate.md "model-dashboard-schedule-activate.md").

A properly-configured and actively-running model monitor might raise alerts, in which case
the monitoring executions produce violation reports. For details about how alerts work and how
to view alert results, history, and links to job reports for debug, see [View and edit alerts](model-dashboard-alerts.md "model-dashboard-alerts.md").
