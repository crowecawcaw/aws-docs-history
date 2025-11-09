# Apply the CodeGuru Profiler function decorator to your

handler function

Pull your `codeguru_profiler_agent` dependency to your local environment
through `pip` and include it in the .zip file for Lambda.

The only required configuration option to start the agent is the profiling group name.
You can find this in the **Settings** section of your profiling group on
the CodeGuru Profiler console. You can also provide the Region if you want to use a profiling group
that was created in a different region than the one where Lambda is running. You can also
provide the profiling group ARN directly, which contains both the name and Region. Either
the profiling group name or ARN must be provided.

| Option               | Environment variable key              | Environment variable value                                                    | Decorator argument example                                  |
| -------------------- | ------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Profiling group name | `AWS_CODEGURU_PROFILER_GROUP_NAME`    | `MyGroupName`                                                                 | `@with_lambda_profiler(profiling_group_name="MyGroupName")` |
| Profiling group ARN  | `AWS_CODEGURU_PROFILER_GROUP_ARN`     | `arn:aws:codeguru-profiler:us-east-1:123456789123:profilingGroup/MyGroupName` | An ARN cannot be passed as a decorator argument             |
| Region               | `AWS_CODEGURU_PROFILER_TARGET_REGION` | `us-east-1`                                                                   | `@with_lambda_profiler(region_name="us-east-1")`            |

Decorate your handler function with `@with_lambda_profiler()`. The following
example shows what your handler function code looks like with CodeGuru Profiler turned on.

```
from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler(profiling_group_name="MyGroupName")
def handler_name(event, context):
    return "Hello World"
```

Only decorate your handler function. You do not have to decorate other internal
functions. You can pass the profiling group name directly in the decorator, or with
environment variables.
