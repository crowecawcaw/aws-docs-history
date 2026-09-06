

# Console-equivalent and improved-caching conda queue environments
<a name="examples-queue-env-conda-console"></a>

The samples repository on the GitHub website includes the following conda queue environments that match the Deadline Cloud console onboarding flow:

[conda\_queue\_env\_from\_console.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml)  
A copy of the queue environment that the Deadline Cloud console onboarding flow adds. The `onEnter` and `onExit` actions run the `conda-queue-env-enter` and `conda-queue-env-exit` commands, which are provided on service-managed fleet workers and use [Rattler](https://github.com/conda/rattler) on the GitHub website. These commands typically run faster than equivalent operations with conda.

[conda\_queue\_env\_improved\_caching.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml)  
A version of the console-equivalent queue environment that reuses virtual environments across multiple jobs. This setting can significantly improve performance when running many jobs with the same package requirements. By default, persistent environments are stored under `~/.persistent_envs`; modify the `onEnter` and `onExit` actions to reference a different path.

To get equivalent functionality on customer-managed fleets, see [Inline conda queue environments for Deadline Cloud customer-managed fleets](examples-queue-env-conda-inline.md).