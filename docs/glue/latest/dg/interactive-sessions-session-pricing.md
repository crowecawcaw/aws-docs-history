# AWS Glue interactive session pricing

AWS charges for AWS Glue interactive sessions based on how long the session is active and
the number of Data Processing Units (DPU) used. You are charged an hourly rate for the number
of DPUs used to run your workloads, billed in increments of one second. AWS Glue interactive
sessions assigns a default of 5 DPUs and requires a minimum of 2 DPUs. There is also
a 1-minute minimum billing duration for each interactive session. To see the AWS Glue
rates and pricing examples, or to estimate your costs using the AWS Pricing Calculator,
see [AWS Glue pricing](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

## Configure your AWS Glue interactive sessions

You can use Jupyter magics in your AWS interactive session to modify your session
and configuration parameters. Magics are short commands prefixed with `%` at the start of
Jupyter cells that provide a quick and easy way to help you control your environment.
For example, if you want to change the number of workers allocated to your job from the
default 5 to 10, you can specify `%number_of_workers 10`. If you want to configure your
session to stop after 10 minutes of idle time instead of the default 2880, you can specify `%idle_timeout 10`.

For the complete list of AWS magics available, see [Configuring AWS interactive sessions for Jupyter and AWS Glue Studio notebooks](interactive-sessions-magics.md "interactive-sessions-magics.md").
