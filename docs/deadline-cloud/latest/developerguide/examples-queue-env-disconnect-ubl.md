# Disconnect Deadline Cloud usage-based licensing with a queue environment

The
[disconnect\_ubl\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/disconnect_ubl_queue_env.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/disconnect_ubl_queue_env.yaml")
queue environment unsets Deadline Cloud usage-based license (UBL) environment
variables. Use this queue environment when you want to turn off all
connections to Deadline Cloud UBL for your queue and force the use of a custom
license server. For more information about bring your own license, see
[Connect service-managed fleets to a custom license server](smf-byol.md "smf-byol.md").

Set the priority of this queue environment to `0` so that
it runs before any other queue environments. Otherwise, connections to
your custom floating licenses (such as RLM) in other queue environments
can be unset accidentally.

###### Note

This queue environment is a sample. Additional UBL environment variables can be added
in the future.
