# Troubleshoot Amazon SageMaker AI model deployments

If you encounter an issue when deploying machine learning models in Amazon SageMaker AI, see the
following guidance.

###### Topics

- [Detection Errors in the Active CPU
  Count](#deploy-model-troubleshoot-jvms "#deploy-model-troubleshoot-jvms")
- [Issues with deploying a model.tar.gz file](#deploy-model-troubleshoot-tarballs "#deploy-model-troubleshoot-tarballs")
- [Primary container did not pass ping health checks](#deploy-model-troubleshoot-ping "#deploy-model-troubleshoot-ping")

## Detection Errors in the Active CPU

Count

If you deploy a SageMaker AI model with a Linux Java Virtual Machine (JVM), you might
encounter detection errors that prevent using available CPU resources. This issue
affects some JVMs that support Java 8 and Java 9, and most that support Java 10 and Java 11. These JVMs implement a mechanism that detects and handles the CPU count and the
maximum memory available when running a model in a Docker container, and, more
generally, within Linux `taskset` commands or control groups (cgroups). SageMaker AI
deployments take advantage of some of the settings that the JVM uses for managing these
resources. Currently, this causes the container to incorrectly detect the number of
available CPUs.

SageMaker AI doesn't limit access to CPUs on an instance. However, the JVM might detect the
CPU count as `1` when more CPUs are available for the container. As a result,
the JVM adjusts all of its internal settings to run as if only `1` CPU core
is available. These settings affect garbage collection, locks, compiler threads, and
other JVM internals that negatively affect the concurrency, throughput, and latency of
the container.

For an example of the misdetection, in a container configured for SageMaker AI that is
deployed with a JVM that is based on Java8_191 and that has four available CPUs on the
instance, run the following command to start your JVM:

```
java -XX:+UnlockDiagnosticVMOptions -XX:+PrintActiveCpus -version
```

This generates the following output:

```
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: determined by OSContainer: 1
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: determined by OSContainer: 1
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: determined by OSContainer: 1
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: determined by OSContainer: 1
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-2ubuntu0.16.04.1-b12)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

Many of the JVMs affected by this issue have an option to disable this behavior and
reestablish full access to all of the CPUs on the instance. Disable the unwanted
behavior and establish full access to all instance CPUs by including the
`-XX:-UseContainerSupport` parameter when starting Java applications. For
example, run the `java` command to start your JVM as follows:

```
java -XX:-UseContainerSupport -XX:+UnlockDiagnosticVMOptions -XX:+PrintActiveCpus -version
```

This generates the following output:

```
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: sched_getaffinity processor count: 4
active_processor_count: sched_getaffinity processor count: 4
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-2ubuntu0.16.04.1-b12)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

Check whether the JVM used in your container supports the
`-XX:-UseContainerSupport` parameter. If it does, always pass the
parameter when you start your JVM. This provides access to all of the CPUs in your
instances.

You might also encounter this issue when indirectly using a JVM in SageMaker AI containers.
For example, when using a JVM to support SparkML Scala. The
`-XX:-UseContainerSupport` parameter also affects the output returned by
the Java `Runtime.getRuntime().availableProcessors()` API .

## Issues with deploying a model.tar.gz file

When you deploy a model using a `model.tar.gz` file, the model tarball should not include any symlinks. Symlinks cause
the model creation to fail. Also, we recommend that you do not include any unnecessary files in the tarball.

## Primary container did not pass ping health checks

If your primary container fails ping health checks with the following error message, it indicates that there
is an issue with your container or script:

```
The primary container for production variant beta did not pass the ping health check. Please check CloudWatch Logs logs for this endpoint.
```

To troubleshoot this issue, you should check the CloudWatch Logs logs for the endpoint in question to see if there are
any errors or issues that are preventing the container from responding to `/ping` or
`/invocations`. The logs may provide an error message that could point to the issue. Once you
have identified the error and failure reason you should resolve the error.

It is also good practice to test the model deployment locally before creating an endpoint.

- Use local mode in the SageMaker SDK to imitate the hosted environment by deploying the model
  to a local endpoint. For more information, see [Local Mode](https://sagemaker.readthedocs.io/en/stable/overview.html#local-mode "https://sagemaker.readthedocs.io/en/stable/overview.html#local-mode").
- Use vanilla docker commands to test the container responds to /ping and /invocations. For more
  information, see [local_test](https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/scikit_bring_your_own/container/local_test "https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/scikit_bring_your_own/container/local_test").
