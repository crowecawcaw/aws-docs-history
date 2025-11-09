# Integrating with your JVM-based application

To start profiling your application, enable the CodeGuru Profiler agent to be loaded and started when
your JVM-based application starts. After the agent starts, it automatically sends profiles to
CodeGuru Profiler service. You’ll see continuous updates and recommendations.

The following sections explain which environments and languages are supported by
CodeGuru Profiler.

###### Topics

- [Choosing the right integration
  option](#choosing-the-right-integration-option "#choosing-the-right-integration-option")
- [Profiling your applications that run on AWS Lambda](setting-up-lambda.md "setting-up-lambda.md")
- [Enabling the agent from the command
  line](enabling-the-agent-with-command-line.md "enabling-the-agent-with-command-line.md")
- [Enabling the agent with code](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md")

## Choosing the right integration

option

You can load the CodeGuru Profiler agent into your JVM-based application in two ways:

1. **Command line** – Use the `-javaagent`
   command line option when starting your application.
2. **Code** – Add the CodeGuru Profiler agent into your
   application code.

The same functionality is available in either option. Choosing the right option for your
situation depends on the following:

To quickly start profiling your existing JVM-based application, the command line option
might be best because it doesn't require recompiling your application.

For more control over when to start profiling, or in rare cases where you need to provide
a custom authentication provider, you might want to choose the code option.

The following table helps summarize these options.

| Option                         | Command line                     | Code                     |
| ------------------------------ | -------------------------------- | ------------------------ |
| Profile existing application   | Yes                              | No (requires re-compile) |
| Custom authentication provider | No                               | Yes                      |
| Control when profiling starts  | No (profiling begins at startup) | Yes                      |

You can always choose a different option later. All of the profiling data is stored in the
CodeGuru Profiler service, and is available even when switching the CodeGuru Profiler agent.
