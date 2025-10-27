# Opt out

AWS Deadline Cloud collects certain operational information to help us develop and improve Deadline Cloud.
The collected data includes things such as your AWS account ID and user ID, so that we can
correctly identify you if you have an issue with the Deadline Cloud. We also collect Deadline Cloud specific
information, such as Resource IDs (a FarmID or QueueID when applicable), the product name (for
example, JobAttachments, WorkerAgent, and more) and the product version.

You can choose to opt out from this data collection using application configuration. Each
computer interacting with Deadline Cloud, both client workstations and fleet workers, needs to opt out
separately.

## Deadline Cloud monitor - desktop

Deadline Cloud monitor - desktop collects operational information, such as when crashes occur and when
the application is opened, to help us know when you are having problems with the
application. To opt out from the collection of this operational information, go to the
settings page and clear **Turn on data collection to measure Deadline Cloud
Monitor's performance**.

After you opt out, the desktop monitor no longer sends the operational data. Any
previously collected data is retained and may still be used to improve the service. For more
information, see [Data
Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

## AWS Deadline Cloud CLI and Tools

The AWS Deadline Cloud CLI, submitters, and worker agent all collect operational information such
as when crashes occur and when jobs are submitted to help us know when you are having
problems with these applications. To opt out from the collection of this operational
information, use any of the following methods:

- In the terminal, enter `deadline config set telemetry.opt_out
true`.

This will opt out the CLI, submitters, and worker agent when running as the current
user.

- When installing the Deadline Cloud worker agent, add the
  `--telemetry-opt-out` command line argument. For example,
  `./install.sh --farm-id $FARM_ID --fleet-id $FLEET_ID
--telemetry-opt-out`.
- Before running the worker agent, CLI, or submitter, set an environment variable:
  `DEADLINE_CLOUD_TELEMETRY_OPT_OUT=true`

After you opt out, the Deadline Cloud tools no longer send the operational data. Any previously
collected data is retained and may still be used to improve the service. For more
information, see [Data
Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").
