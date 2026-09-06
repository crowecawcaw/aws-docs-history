

# Translate a Slurm Job Submit plugin script to use CLI Filter Plugin in AWS PCS
<a name="slurm-cli-filter-plugins-translate"></a>

Translate your existing Job Submit Plugin Lua script to CLI Filter Plugin when you migrate from other Slurm environments. The translation process involves updating function names and field access patterns to work with the CLI Filter Plugin API.

## Prerequisites
<a name="slurm-cli-filter-plugin-translate-prerequisites"></a>

Before you translate your script, complete these tasks:
+ Review your existing Job Submit Plugin Lua script
+ Understand differences between Job Submit and CLI Filter Plugin APIs
+ Access Slurm CLI Filter Plugin documentation

**To translate Job Submit Plugin script to CLI Filter Plugin**

1. Review your existing Job Submit Plugin script functions (`slurm_job_submit`, `slurm_job_modify`).

1. Identify equivalent CLI Filter Plugin functions:
   + `slurm_job_submit` becomes `slurm_cli_pre_submit`
   + Add `slurm_cli_setup_defaults` for default parameter setting
   + Add `slurm_cli_post_submit` for post-submission actions

1. Translate job validation logic from `job_desc` fields to `options` array access:
   + `job_desc.account` becomes `options["account"]`
   + `job_desc.partition` becomes `options["partition"]`
   + `job_desc.features` becomes `options["constraint"]`

1. Update logging calls from `slurm.log_user()` to `slurm.log_error()`.

1. Test your translated script on a development cluster.

1. Deploy to your production cluster following the standard CLI Filter Plugin deployment process.

## Expected results
<a name="slurm-cli-filter-plugin-translate-results"></a>

After you complete the translation:
+ Your translated script provides equivalent job submission validation
+ Users see similar error messages and prompts as with your original Job Submit Plugin
+ Job submission policies are maintained during migration to AWS PCS

## Troubleshooting
<a name="slurm-cli-filter-plugin-translate-troubleshooting"></a>

**Script translation errors**  
**Symptoms:** Job submissions fail with Lua execution errors.  
**Likely cause:** Incorrect field access or function calls in translated script.  
**Resolution:** Review CLI Filter Plugin API documentation and compare field mappings between Job Submit and CLI Filter interfaces.