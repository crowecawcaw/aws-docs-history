

# Enforce fixed license limits with a Deadline Cloud submission hook
<a name="examples-license-limits-hook"></a>

The [license\_limits](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/submission_hooks/license_limits) sample on the GitHub website shows how to combine the Deadline Cloud [Limits](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-limits.html) feature with a submission hook to enforce a fixed number of concurrent licenses (for example, V-Ray licenses) across all job submissions, without requiring artists to configure anything manually. For more information about submission hooks, see [submission-hooks.md](https://github.com/aws-deadline/deadline-cloud/blob/mainline/docs/submission-hooks.md) on the GitHub website.

The Deadline Cloud Limits feature throttles task scheduling so that no more than N tasks requiring a license run concurrently. For the limit to take effect, each job must declare the license as a host requirement in its template. This sample provides a pre-submission hook that automatically injects the license host requirement into every job template at submission time. As a result:
+ Artists submit jobs normally with no extra steps.
+ The hook ensures every job declares its need for the license.
+ The Deadline Cloud scheduler enforces the concurrency limit.

**To set up the license limits hook**

1. Create a Limit on your farm with the AWS CLI:

   ```
   aws deadline create-limit \
       --farm-id {{farm-id}} \
       --display-name "VRay License" \
       --amount-requirement-name "amount.vray" \
       --max-count 5
   ```

1. Associate the Limit with your queue using `aws deadline create-queue-limit-association`.

1. Copy the `license_limits/` directory to a shared location accessible by all artist workstations.

1. On each artist workstation, enable environment hooks:

   ```
   deadline config set settings.allow_environment_hooks true
   ```

1. Set the `DEADLINE_HOOKS_DIR` environment variable in your application launcher scripts to point to the shared directory.

**Important**  
Don't add `amount.vray` as a `customAmounts` entry in your fleet's capabilities. If the fleet declares the amount as a capability, the fleet treats it as a per-worker resource and bypasses the queue-level limit. The limit association alone provides compatibility.

To extend the sample to other licenses (Houdini, Nuke, and so on), add entries to `license_limits.json` and create corresponding Limits and queue associations.