

# Queue environment examples for Deadline Cloud
<a name="examples-queue-environments"></a>

The [queue\_environments](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments) directory on the GitHub website includes queue environments that you can attach to a Deadline Cloud queue. Conda and Rez queue environments provide software to jobs so that each job only needs a parameter value for `CondaPackages` or `RezPackages` to specify the list of packages to use.

Queue environments follow the [Open Job Description environment template specification](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas) on the GitHub website. To attach a queue environment to your queue, see [Configure jobs using queue environments](configure-jobs.md). For background on environments and how they affect your jobs, see [Control the job environment with OpenJD queue environments](control-the-job-environment.md).

To create a queue environment with the AWS CLI:

```
aws deadline create-queue-environment \
    --farm-id {{FARM_ID}} \
    --queue-id {{QUEUE_ID}} \
    --priority 1 \
    --template-type YAML \
    --template file://conda_queue_env_improved_caching.yaml
```

**Topics**
+ [Console-equivalent and improved-caching conda queue environments](examples-queue-env-conda-console.md)
+ [Inline conda queue environments for Deadline Cloud customer-managed fleets](examples-queue-env-conda-inline.md)
+ [py-rattler conda queue environment for Deadline Cloud](examples-queue-env-conda-pyrattler.md)
+ [Rez queue environment for Deadline Cloud customer-managed fleets](examples-queue-env-rez.md)
+ [Pip queue environment for Deadline Cloud](examples-queue-env-pip.md)
+ [Disconnect Deadline Cloud usage-based licensing with a queue environment](examples-queue-env-disconnect-ubl.md)