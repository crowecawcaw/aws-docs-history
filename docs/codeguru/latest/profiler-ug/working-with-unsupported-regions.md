# Working with unsupported AWS

Regions

To use Amazon CodeGuru Profiler in an AWS Region it doesn't support, you can configure your agent to
submit profiles to one of the supported Regions instead. You can specify which AWS Region to
submit profiles to by adding a specified region name to your code or adding an environment variable.
For example, using CodeGuru Profiler in `eu-west-1` would mean that profiled data would be
stored in that Region, even while your application is running in an unsupported region.

You should create the profiling group in the target AWS Region, which might differ from
the Region that the application is running in. The application role should have permissions set
up to allow profiles to be submitted to the target Region.

The following code examples demonstrate how to configure your agent to get access to the
CodeGuru Profiler console from `eu-west-1` when enabling the agent with code or integrating with
Lambda. You can do this for [any
of the supported Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"), by replacing `EU_WEST_1` with the Region name you
want.

To submit any profiles to the CodeGuru Profiler API, your host must have internet access.

## Enabling the agent with code

The following sections show how to use Amazon CodeGuru Profiler in an unsupported region when enabling the
agent with Java or Python code.

### Java

If you are enabling the agent with code in Java, add the following lines to your code.

You first import the region package from the AWS SDK by adding this line to the top of your code.

```
import software.amazon.awssdk.regions.Region; // Uses AWK SDK for Java v2

```

Then add
`.awsRegionToReportTo(<AWS Region>)` to the code that enables the
agent.

Below is a complete example of what your code should look like if you want to configure your
agent to get access to the CodeGuru Profiler console from `eu-west-1`.

```
import software.amazon.awssdk.regions.Region; // Uses AWK SDK for Java v2`
import software.amazon.codeguruprofilerjavaagent.Profiler;

Profiler.builder()
        .profilingGroupName("ExampleAppConsumingCodeGuruProfilerJavaAgent")
        .awsRegionToReportTo(Region.EU_WEST_1)
        .build()
        .start();

```

For more information on enabling the agent with Java code, see [Enabling the agent with code (Java)](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md").

### Python

If you are enabling the agent with code in Python, set the following parameter to the line
where you start the agent.

```
region_name='<AWS Region>'

```

Below is an example of what your code should look like if you want to configure your
agent to get access to the CodeGuru Profiler console from `eu-west-1`.

```
from codeguru_profiler_agent import Profiler

if __name__ == '__main__':
    Profiler(profiling_group_name='MyProfilingGroup', region_name='eu-west-1').start()
    start_application()

```

For more information on enabling the agent with Python code, see [Enabling the agent with
code (Python)](python-code-change.md "python-code-change.md").

## Profiling applications that run on

AWS Lambda

The following sections show how to use Amazon CodeGuru Profiler in an unsupported region when integrating with
AWS Lambda.

### Java

If you're using Java 8 on Amazon Linux 2 or Java 11 (Corretto) to profile your
application on AWS Lambda, you can set the environment variable
`AWS_CODEGURU_PROFILER_TARGET_REGION` to your target region, see below.

```
AWS_CODEGURU_PROFILER_TARGET_REGION='eu-west-1'
```

For more information on using integrating with Java and AWS Lambda, see [Profiling your Java applications that run on AWS
Lambda](setting-up-lambda.md "setting-up-lambda.md").

### Python

#### Using the Amazon CodeGuru Profiler function decorator

If you're applying the Amazon CodeGuru Profiler function decorator to your AWS Lambda handler
function, set the following parameter in the function decorator.

```
region_name='<AWS Region>'

```

Below is an example of what your code should look like if you're applying the
Amazon CodeGuru Profiler function decorator to your AWS Lambda handler function from
`eu-west-1`.

```
from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler(profiling_group_name='MyProfilingGroup', region_name='eu-west-1')
def handler_name(event, context):
    return "Hello World"

```

For more information on the Amazon CodeGuru Profiler function decorator, see
[Apply the CodeGuru Profiler function decorator to your
handler function](python-lambda-command-line.md "python-lambda-command-line.md").

#### Using AWS Lambda layers

If you're using AWS Lambda layers to profile your Python application, you can set the
environment variable `AWS_CODEGURU_PROFILER_TARGET_REGION` to your target
region, see below.

```
AWS_CODEGURU_PROFILER_TARGET_REGION='eu-west-1'
```

For more information on using layers, see
[Use AWS Lambda layers](python-lambda-layers.md "python-lambda-layers.md").
