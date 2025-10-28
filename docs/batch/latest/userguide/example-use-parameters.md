# Parameter substitution

The following example job definition illustrates how to allow for parameter substitution and to set default
values.

The `Ref::` declarations in the `command` section are used to set placeholders for
parameter substitution. When you submit a job with this job definition, you specify the parameter overrides to fill
in those values, such as the `inputfile` and `outputfile`. The `parameters` section
that follows sets a default for `codec`, but you can override that parameter as needed.

For more information, see [Parameters](job_definition_parameters.md#parameters "job_definition_parameters.md#parameters").

```
{
    "jobDefinitionName": "ffmpeg_parameters",
    "type": "container",
    "parameters": {"codec": "mp4"},
    "containerProperties": {
        "image": "my_repo/ffmpeg",
        "resourceRequirements": [
            {
                "type": "MEMORY",
                "value": "2000"
            },
            {
                "type": "VCPU",
                "value": "2"
            }
        ],
        "command": [
            "ffmpeg",
            "-i",
            "Ref::inputfile",
            "-c",
            "Ref::codec",
            "-o",
            "Ref::outputfile"
        ],
        "jobRoleArn": "arn:aws:iam::`123456789012`:role/ECSTask-S3FullAccess",
        "user": "nobody"
    }
}
```
