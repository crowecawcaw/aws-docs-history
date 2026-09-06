

# Submission hooks
<a name="submission-hooks"></a>

Submission hooks allow you to run custom scripts during the Deadline Cloud job submission workflow. Hooks run locally on the workstation that is submitting the job, before the job reaches the Deadline Cloud service. Hooks do not run on workers or in the AWS Cloud. Because hooks execute on your machine, they have access to local files, environment variables, and network resources available to the submitting user.

You can use hooks to validate job configurations, discover additional assets, modify submission parameters, or integrate with external systems such as production-tracking software. For other integration points that run on workers or in the cloud, see [Hooks, events, and integration points for jobs](integration-points.md).

There are two ways to configure hooks:
+ **Bundle hooks** – Place a `hooks.yaml` (or `hooks.json`) file in your job bundle directory alongside `template.yaml`. Bundle hooks work well for CLI workflows where the bundle already exists before submission.
+ **Environment hooks** – Point the `DEADLINE_HOOKS_DIR` environment variable to a directory that contains `hooks.yaml`. Environment hooks are useful for studios that want to enforce hooks across all submissions without modifying job bundles.

Both sources can be active at the same time. When both are present, environment hooks run first, then bundle hooks.

**Note**  
In-application (DCC) submitters such as Maya, Nuke, or Blender run environment hooks for the pre-submission and post-submission phases only. The pre-GUI phase does not apply to DCC submitters. For more information, see [Pre-GUI hooks](#submission-hooks-pre-gui).

## Hook types
<a name="submission-hooks-types"></a>

Deadline Cloud supports three hook types that correspond to different points in the submission workflow.

### Pre-GUI hooks
<a name="submission-hooks-pre-gui"></a>

Pre-GUI hooks run before the submission dialog opens. You can use pre-GUI hooks for the following tasks:

**Important**  
Pre-GUI hooks run only with the standalone GUI submitter (`deadline bundle gui-submit`). They do not run in in-application (DCC) submitters such as Maya, Nuke, or Blender, because those applications build their submission dialog directly and do not invoke the pre-GUI phase. Pre-GUI hooks also do not apply to CLI submission (`deadline bundle submit`), which has no GUI phase. Pre-submission and post-submission hooks work across all submission methods.
+ Pre-populate job name, description, and priority
+ Set parameter defaults based on the current scene or pipeline context
+ Query a project management system for task metadata

Pre-GUI hooks block the dialog from opening if they fail (non-zero exit code or timeout).

Output JSON to stdout to modify the initial dialog state. The following example shows the output format:

```
import json

output = {
    "name": "My Render - v042",
    "description": "Submitted via pipeline",
    "parameters": {
        "SceneFile": "/resolved/path/to/scene.ma",
        "OutputPath": "/shots/sh010/renders/",
        "deadline:priority": 75,
        "deadline:maxFailedTasksCount": 5,
        "deadline:maxRetriesPerTask": 3,
        "deadline:maxWorkerCount": 10,
        "deadline:targetTaskRunStatus": "READY"
    }
}
print(json.dumps(output))
```

The following table describes the output fields for pre-GUI hooks.


| Field | Type | Description | 
| --- | --- | --- | 
| `name` | String | Pre-fills the job name field. | 
| `description` | String | Pre-fills the job description field. | 
| `parameters` | Object | Pre-fills parameter values by name. Job template parameters use their name directly. Shared job properties use the `deadline:` prefix. | 

The following table describes the shared job properties that you can set with the `deadline:` prefix in the `parameters` object.


| Key | Type | Description | 
| --- | --- | --- | 
| `deadline:priority` | Integer | Priority (0–100). | 
| `deadline:maxFailedTasksCount` | Integer | Maximum failed tasks before the job fails. | 
| `deadline:maxRetriesPerTask` | Integer | Maximum retries per failed task. | 
| `deadline:maxWorkerCount` | Integer | Maximum concurrent workers. | 
| `deadline:targetTaskRunStatus` | String | Initial task status: `READY` or `SUSPENDED`. | 

**Note**  
CLI-supplied `--parameter` values take precedence over hook-supplied `parameters`.

### Pre-submission hooks
<a name="submission-hooks-pre-submission"></a>

Pre-submission hooks run before job attachments are hashed and uploaded. You can use pre-submission hooks for the following tasks:
+ Validate job configuration
+ Discover and add additional input files
+ Modify job parameters such as priority
+ Enforce studio policies

Pre-submission hooks block submission if they fail (non-zero exit code or timeout).

Output JSON to stdout to modify the submission. The hook output replaces asset references at the nested key level. If your hook outputs `inputFilenames`, the hook output replaces the entire `inputFilenames` list. Deadline Cloud preserves keys that you don't include in your output.

The following example adds discovered texture files to the submission:

```
import json
import os
import sys

metadata = json.load(sys.stdin)
bundle_dir = metadata["jobBundleDir"]

textures = []
for root, _, files in os.walk(bundle_dir):
    for f in files:
        if f.endswith(('.exr', '.png', '.jpg', '.tx')):
            textures.append(os.path.join(root, f))

if textures:
    print(json.dumps({
        "attachments": {
            "assetReferences": {
                "inputFilenames": textures
            }
        }
    }))
```

Pre-submission hooks can also modify job template parameter values by emitting a `parameters` map on stdout:

```
print(json.dumps({"parameters": {"SceneFile": "/resolved/scene.ma", "Quality": "high"}}))
```

Parameter keys are job template parameter names. Values from a hook are applied on top of the bundle's parameter values, but CLI-supplied `--parameter` values still take precedence over hook-supplied ones.

**Important**  
`PATH` parameters emitted on stdout must be absolute. A hook does not run from the submitting shell's working directory, so a relative `PATH` value on stdout is ambiguous and is rejected with an error. Emit an absolute path (for example, join with `DEADLINE_JOB_BUNDLE_DIR`), or write the value to `parameter_values.yaml`/`parameter_values.json` on disk instead, where a relative `PATH` is resolved against the job bundle directory.

### Post-submission hooks
<a name="submission-hooks-post-submission"></a>

Post-submission hooks run after the `CreateJob` API call returns successfully. The job has been accepted by Deadline Cloud at this point. You can use post-submission hooks for the following tasks:
+ Send notifications (Slack, email)
+ Update tracking systems
+ Log submission details

Post-submission hook failures are logged as warnings but do not affect the submitted job.

## Configure submission hooks
<a name="submission-hooks-configuration"></a>

Define hooks in a `hooks.yaml` or `hooks.json` file. Place the file in your job bundle directory alongside `template.yaml`, or in the directory specified by `DEADLINE_HOOKS_DIR`. If both formats exist in the same directory, the submitter reports an error.

The `version` field is required and must be `"1.0"`.

The following example shows a `hooks.yaml` configuration:

```
version: "1.0"
preGUI:
  - command: python3
    args: [scripts/prefill_from_shotgrid.py]
    timeout: 10

preSubmission:
  - command: python3
    args: [scripts/validate_assets.py]
    timeout: 60
    env:
      VALIDATION_LEVEL: strict

  - command: python3
    args: [scripts/discover_textures.py]

postSubmission:
  - command: python3
    args: [scripts/notify_slack.py]
    timeout: 15
    env:
      SLACK_WEBHOOK: https://hooks.slack.com/...
```

### Hook definition fields
<a name="submission-hooks-definition-fields"></a>

Each hook entry accepts the following fields.


| Field | Required | Default | Description | 
| --- | --- | --- | --- | 
| `command` | Yes | – | Executable or interpreter (for example, `python3` or `bash`). | 
| `args` | No | `[]` | Command-line arguments. | 
| `timeout` | No | `60` | Maximum execution time in seconds. | 
| `env` | No | `{}` | Additional environment variables. Hooks inherit the submitter's full environment. The `DEADLINE_*` variables and any hook-specific `env` values are layered on top. | 

### Path resolution
<a name="submission-hooks-path-resolution"></a>

Hook scripts are resolved according to the following rules:
+ **Absolute paths** – Used as-is.
+ **Relative paths** – Resolved relative to the job bundle directory.
+ **Command names** – Searched in the system PATH.

## Hook input
<a name="submission-hooks-input"></a>

Hooks receive job metadata through JSON on stdin and through convenience environment variables.

### Environment variables
<a name="submission-hooks-env-vars"></a>

The following environment variables are available to all hooks.


| Variable | Description | 
| --- | --- | 
| `DEADLINE_JOB_NAME` | Job name. | 
| `DEADLINE_PRIORITY` | Job priority. | 
| `DEADLINE_FARM_ID` | Farm ID. | 
| `DEADLINE_QUEUE_ID` | Queue ID. | 
| `DEADLINE_JOB_BUNDLE_DIR` | Path to the job bundle directory. | 
| `DEADLINE_STORAGE_PROFILE_ID` | Storage profile ID (if set). | 
| `DEADLINE_JOB_ID` | Job ID (post-submission hooks only). | 

### JSON on stdin
<a name="submission-hooks-json-stdin"></a>

Complete metadata is provided as JSON on stdin. The following example shows the structure:

```
{
  "jobName": "My Render Job",
  "priority": 50,
  "farmId": "farm-abc123",
  "queueId": "queue-def456",
  "jobBundleDir": "/path/to/bundle",
  "parameters": {"SceneFile": "/path/to/scene.ma"},
  "submitterName": "Maya",
  "assetReferences": {
    "inputFilenames": ["/path/to/texture.exr"],
    "inputDirectories": [],
    "outputDirectories": ["/path/to/output"],
    "referencedPaths": []
  },
  "submissionPayload": {}
}
```

## Security
<a name="submission-hooks-security"></a>

Hooks are disabled by default. Each hook source has its own setting that you must enable.

### Enabling bundle hooks
<a name="submission-hooks-enable-bundle"></a>

To allow hooks defined in `hooks.yaml` within job bundles, enable the bundle hooks setting.

**To enable bundle hooks**
+ Run the following command:

  ```
  deadline config set settings.allow_bundle_hooks true
  ```

### Enabling environment hooks
<a name="submission-hooks-enable-environment"></a>

To allow hooks from a directory specified by `DEADLINE_HOOKS_DIR`, enable the environment hooks setting and set the directory path.

**To enable environment hooks**

1. Enable the setting:

   ```
   deadline config set settings.allow_environment_hooks true
   ```

1. Set the environment variable, typically in an application launcher script:

   ```
   export DEADLINE_HOOKS_DIR=/studio/pipeline/hooks/blender
   ```

### Confirmation prompt
<a name="submission-hooks-confirmation"></a>

When you enable hooks, the submitter prompts you to confirm before the hooks run. Pre-GUI hooks show the prompt before the dialog opens. Pre-submission and post-submission hooks show the prompt when you choose Submit.

The prompt shows which commands will run, allowing you to review before proceeding:

```
This job bundle contains submission hooks that will execute on your machine:

  Pre-GUI hooks:
    [1] python3 prefill_from_shotgrid.py

  Pre-submission hooks:
    [1] python3 validate_assets.py

  Post-submission hooks:
    [1] python3 notify.py

  Bundle: /path/to/bundle

Do you want to run these hooks? [Y/n]
```

To skip confirmation prompts for CI/automation workflows, run the following command:

```
deadline config set settings.auto_accept true
```

### Configuration settings summary
<a name="submission-hooks-config-summary"></a>


| Setting | Default | Description | 
| --- | --- | --- | 
| `settings.allow_bundle_hooks` | `false` | Specifies whether to allow hooks from the job bundle `hooks.yaml` file. | 
| `settings.allow_environment_hooks` | `false` | Specifies whether to allow hooks from the `DEADLINE_HOOKS_DIR` directory. | 
| `settings.auto_accept` | `false` | Specifies whether to skip confirmation prompts. Use with caution in CI/automation environments. | 

## Studio deployment
<a name="submission-hooks-studio-deployment"></a>

Pipeline technical directors can configure hooks to run automatically for all artists by deploying environment hooks across workstations. Use this procedure when your studio has a shared network location for hook scripts and you have administrative access to configure artist workstations.

**To deploy environment hooks for a studio**

1. Configure workstations to allow environment hooks:

   ```
   deadline config set settings.allow_environment_hooks true
   ```

1. Set `DEADLINE_HOOKS_DIR` in each application's launcher script:

   ```
   # blender_launcher.sh
   export DEADLINE_HOOKS_DIR=/studio/pipeline/hooks/blender
   exec blender "$@"
   ```

1. Create the hooks at the specified location:

   ```
   /studio/pipeline/hooks/blender/
   ├── hooks.yaml
   └── validate_scene.py
   ```

## Error handling
<a name="submission-hooks-error-handling"></a>

When a pre-submission or pre-GUI hook fails, the error output includes the following information:
+ Which hook failed
+ Exit code
+ stdout and stderr output
+ Timeout duration (if the hook timed out)

The submitter blocks submission until you resolve the issue. Post-submission hook failures are logged as warnings but do not affect the submitted job.

## Best practices
<a name="submission-hooks-best-practices"></a>
+ **Keep hooks fast.** Set appropriate timeouts and avoid long-running operations in hooks.
+ **Log to stderr.** Reserve stdout for JSON output in pre-GUI and pre-submission hooks.
+ **Handle errors gracefully.** Provide clear error messages on stderr so users can identify what went wrong.
+ **Test with the CLI first.** CLI submission is easier to debug than GUI submission.
+ **Use absolute paths in output.** When adding files to asset references, always use absolute paths.
+ **Use environment hooks for studio-wide policies.** Environment hooks are more secure than bundle hooks because they are controlled by the studio rather than the bundle author.
+ **Review bundle hooks before enabling.** Inspect `hooks.yaml` in bundles from untrusted sources before allowing bundle hooks to run.

## Submission methods
<a name="submission-hooks-cli-gui"></a>

Hooks work with the following submission methods:
+ `deadline bundle submit` (CLI) – Pre-submission and post-submission hooks run. The CLI has no GUI phase, so pre-GUI hooks do not apply.
+ `deadline bundle gui-submit` (standalone GUI) – All phases run, including pre-GUI hooks.
+ In-application (DCC) submitters – Pre-submission and post-submission hooks run. DCC submitters do not invoke the pre-GUI phase.

The standalone GUI copies `hooks.yaml` to the job history bundle and resolves script paths back to your original bundle directory.

## Additional resources
<a name="submission-hooks-related"></a>

For more information about integration points and related topics, see the following:
+ [Hooks, events, and integration points for jobs](integration-points.md)
+ [How to submit a job to Deadline Cloud](submit-jobs-how.md)
+ [Build jobs to submit to Deadline Cloud](building-jobs.md)
+ [deadline-cloud](https://github.com/aws-deadline/deadline-cloud) repository on the GitHub website