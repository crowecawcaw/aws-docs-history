# JRuby

You can add support for the CodeGuru Profiler agent into your JRuby application by adding the
following lines into your startup or `main` function.

```
Java::SoftwareAmazonCodeguruprofilerjavaagent::Profiler
    .builder
    .profiling_group_name("MyProfilingGroup")
    .aws_credentials_provider(myAwsCredentialsProvider) # optional
    .build
    .start
...
```

You need to [add a dependency](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md") to the
agent .jar file.
