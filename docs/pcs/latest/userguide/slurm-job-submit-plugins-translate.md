

# Translate a Lua Job Submit Plugin script to Starlark for AWS PCS

If you use a Lua Job Submit Plugin (`job_submit/lua`) in another Slurm environment, translate it to Starlark to use it in AWS PCS. The function names, arguments, and most field names stay the same.

## Prerequisites
<a name="slurm-job-submit-plugins-translate-prerequisites"></a>

Before you translate your script, make sure that you have the following:
+ Your existing `job_submit.lua` script
+ A non-production AWS PCS cluster that uses Slurm 25.11 or later, for testing

## Translate the script
<a name="slurm-job-submit-plugins-translate-steps"></a>

**To translate a Lua script to Starlark**

1. List each rule in your Lua script, and the job fields that it reads or changes.

1. Rewrite the script in Starlark, using the tables in this topic. For the Starlark language, see the [Starlark specification](https://github.com/bazelbuild/starlark/blob/master/spec.md) on the GitHub website.

1. Check your script for the problems in [Common problems](#slurm-job-submit-plugins-translate-pitfalls).

## Lua to Starlark mapping
<a name="slurm-job-submit-plugins-translate-map"></a>

The function names and arguments are the same in Lua and Starlark. The following table lists the other changes that you make. Fields that aren't in this table keep the same name, for example `job_desc.qos` becomes `job_desc["qos"]`.


**Lua and Starlark equivalents**  

| Lua (`job_submit/lua`) | Starlark (AWS PCS) | Notes | 
| --- | --- | --- | 
| return slurm.SUCCESS | return slurm.ACCEPT\_JOB | Accepts the job. | 
| return slurm.ERROR, or a Slurm error code such as return slurm.ESLURM\_INVALID\_ACCOUNT | return slurm.REJECT\_JOB | Only slurm.REJECT\_JOB rejects a job. A plain number, such as return 2017, accepts it. slurm.ERROR and slurm.ESLURM\_{{\*}} names don't exist in AWS PCS, so a script that uses them fails, and Slurm rejects the job with no message. Use log.user() to give the reason. | 
| slurm.log\_user("Invalid account %s", acct) | log.user("Invalid account %s" % acct) | The log functions take one string, so format the message first. | 
| slurm.log\_info, slurm.log\_verbose, slurm.log\_error | log.info, log.verbose, log.error | Writes to the Slurm controller log. | 
| slurm.log\_debug to slurm.log\_debug4 | log.debug | Debug messages appear in the controller log, marked [debug]. | 
| job\_desc.account | job\_desc["account"] | Job fields are dictionary keys. | 
| job\_desc.account == nil | job\_desc["account"] == None | Unset string fields, min\_mem\_per\_cpu, min\_mem\_per\_node, and site\_factor are None. Other unset numeric fields use values such as slurm.NO\_VAL. | 
| job\_rec.min\_nodes | job\_rec["details"]["min\_nodes"] | Details of an existing job, such as min\_nodes, min\_cpus, and nice, are in job\_rec["details"]. | 
| for name, part in pairs(part\_list) | for part in part\_list | Use part["name"] for the partition name. part\_list includes every partition, not only the ones the user can use. | 
| job\_desc.oversubscribe | job\_desc["shared"] | Renamed field. | 
| job\_desc.pack\_job\_offset, job\_rec.pack\_job\_offset | job\_desc["het\_job\_offset"], job\_rec["het\_job\_offset"] | Renamed field. | 
| job\_rec.pack\_job\_id | job\_rec["het\_job\_id"] | Renamed field. | 
| job\_rec.curr\_dependency | job\_rec["details"]["dependency"] | Renamed field, in the nested dictionary. | 
| job\_rec.pn\_min\_memory | job\_rec["details"]["min\_mem\_per\_cpu"] or job\_rec["details"]["min\_mem\_per\_node"] | Read the per-CPU or per-node field instead of the raw value. | 
| job\_desc.gres | job\_desc["tres\_per\_node"] | job\_desc["gres"] isn't available. In job\_rec, gres is available. | 
| job\_desc.segment\_size and the job\_rec fields array\_task\_cnt, gres\_req, resizing, script, and segment\_size | Not available | Remove these fields from your script. | 
| job\_desc.site\_factor == slurm.NO\_VAL | job\_desc["site\_factor"] == None | Unlike most numeric fields, an unset site\_factor is None, not slurm.NO\_VAL. | 
| job\_rec.site\_factor | job\_rec["site\_factor\_adjusted"] | job\_rec["site\_factor"] is the raw stored value. An unset site\_factor\_adjusted is None. | 
| part.max\_oversubscribe | part["max\_share"] | Renamed field. | 
| "Invalid account " .. acct | "Invalid account " \+ acct or "Invalid account %s" % acct | Starlark has no .. operator. | 
| \~= | \!= | Not equal. | 
| tonumber(value) | int(value) or float(value) | Unlike tonumber(), these functions stop the script with an error if the value isn't a number. | 
| while loop | for i in range({{n}}) | Starlark has no while loop. A script that uses one fails to load, and Slurm rejects every job. | 
| pcall() | No equivalent | Starlark can't catch errors. Check a value before you use it, for example with value \!= None and value.isdigit() before int(value). | 
| elseif, local, end | elif, no keyword, indentation | For other syntax, see the [Starlark specification](https://github.com/bazelbuild/starlark/blob/master/spec.md) on the GitHub website. | 

## Common problems
<a name="slurm-job-submit-plugins-translate-pitfalls"></a>

The following problems can make a translated script accept or reject the wrong jobs.


**Common translation problems**  

| Problem | Result | Fix | 
| --- | --- | --- | 
| Comparing a field with slurm.NO\_VAL64 or slurm.INFINITE64 | The comparison is never true, so the script takes the wrong branch. | For min\_mem\_per\_cpu and min\_mem\_per\_node, compare with None. Don't set a field to these values. | 
| Changing a read-only field, such as user\_id | Slurm rejects jobs that the script accepts. | Change only fields that you can set, such as partition. | 
| Testing only rejected jobs | Errors in accepted jobs aren't found. | For each rule, test a job that the script must accept and a job that it must reject. | 
| Keeping values between jobs in global variables | Global variables can't change after the script loads. | Keep all state inside your functions. | 
| Setting more than one memory field | The job can lose its memory request. | Set only the memory field that you want. | 
| The script doesn't define slurm\_job\_modify | Slurm rejects every job modification, such as scontrol update job. | Define slurm\_job\_modify. To allow all modifications, return slurm.ACCEPT\_JOB. | 
| The Lua script loads other files, for example with require | AWS PCS loads only one script file, so the script fails. | Combine the code into one .star file. | 
| Setting an integer field to a fractional number, such as 60.5 | Slurm rejects the job. This can happen when your rule divides, because the / operator can return a fractional number. | Set whole numbers, for example with // or int(). | 
| Using print() for messages | AWS PCS discards the output, so it doesn't reach the user or the controller log. | Use the log module. | 
| Returning a Slurm error code, such as slurm.ESLURM\_INVALID\_ACCOUNT | In Lua, Slurm shows the error message for the code. In AWS PCS, the name doesn't exist, so the script fails. Slurm rejects the job, and the user sees only Unspecified error, even if the script called log.user(). | Call log.user() with the reason, and then return slurm.REJECT\_JOB. | 
| Lua syntax left in the script, such as .. for string concatenation | The script fails to load, and Slurm rejects every job. | Rewrite the syntax in Starlark. For example, join strings with \+ or %. | 
| Converting a value with int() that might not be a number, as Lua code does inside pcall() | The script stops with an error, and Slurm rejects the job. | Check the value before you convert it, for example with value \!= None and value.isdigit(). | 

## Test the translated script
<a name="slurm-job-submit-plugins-translate-test"></a>

**To test a translated script**

1. Configure the script on a non-production cluster. For instructions on configuring a Job Submit Plugin, see [Configure a Slurm Job Submit Plugin on an AWS PCS cluster](slurm-job-submit-plugins-configure.md).

1. For each rule in your script, submit a job that the script must accept and a job that it must reject.

1. Modify a job with `scontrol update job` to test `slurm_job_modify`.

1. Check the results in the Slurm controller log.

## Expected results
<a name="slurm-job-submit-plugins-translate-results"></a>

After you complete the translation:
+ Your translated script enforces the same job policies as your Lua script
+ Users see your `log.user()` messages when the script rejects a job
+ Job submission policies are maintained during migration to AWS PCS

## Troubleshooting
<a name="slurm-job-submit-plugins-translate-troubleshooting"></a>

**Translated script rejects every job**  
**Symptoms:** All job submissions fail with `Unspecified error`.  
**Likely cause:** Lua code left in the script, such as `end`, `..`, a top-level `return` statement, or `slurm.SUCCESS` or `slurm.ERROR`, which don't exist in AWS PCS.  
**Resolution:** Check the `job_submit/json` entries in the Slurm controller log for the error, and fix the syntax.

**Translated script accepts jobs that the Lua script rejected**  
**Symptoms:** Jobs that don't follow your policies are accepted.  
**Likely cause:** The script returns a plain number other than `slurm.REJECT_JOB` to reject a job, such as `return 2017`. Only `slurm.REJECT_JOB` rejects a job.  
**Resolution:** Replace every error return with `slurm.REJECT_JOB`.

**Some jobs are rejected after translation**  
**Symptoms:** Jobs that the Lua script accepted are rejected.  
**Likely cause:** Lua field access left in the script, such as `job_desc.account` instead of `job_desc["account"]`, or a change to a read-only field.  
**Resolution:** Use the field names in [Lua to Starlark mapping](#slurm-job-submit-plugins-translate-map), and change only fields that you can set. For more information about job fields, see [Write the script](slurm-job-submit-plugins-scripts.md#slurm-job-submit-plugins-scripts-write).