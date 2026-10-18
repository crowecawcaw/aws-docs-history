

# Best practices for container images
<a name="containers-best-practices"></a>

Follow these best practices when you build container images for HealthOmics workflows.

## Using Java in Amazon ECR container images
<a name="ecr-java-considerations"></a>

If a workflow task uses a Java application such as GATK, consider the following memory requirements for the container:
+ Java applications use stack memory and heap memory. By default, the maximum heap memory is a percentage of the total available memory in the container. This default depends on the specific JVM distribution and JVM version, so consult the relevant documentation for your JVM or explicitly set the heap memory maximum using Java command line options (such as `-Xmx`). 
+ Don't set the maximum heap memory to be 100% of the container's memory allocation, because the JVM stack also requires memory. Memory is also required for the JVM garbage collector and any other operating system processes running in the container.
+ Some Java applications, such as GATK, can use native method invocations or other optimizations such as memory mapping files. These techniques require memory allocations that are performed "off-heap", which the JVM maximum heap parameter doesn't control. 

  If you know (or suspect) that your Java application allocates off-heap memory, make sure your task memory allocation includes the off-heap memory requirements.

  If these off-heap allocations cause the container to run out of memory, you typically don't see a Java `OutOfMemory` error, because the JVM doesn't control this memory. 

## Add task inputs to an Amazon ECR container image
<a name="ecr-tasks"></a>

Add all executables, libraries, and scripts needed to run a workflow task into the Amazon ECR image that's used to run the task. 

It's best practice to avoid using scripts, binaries, and libraries that are external to a task's container image. This is especially important when using `nf-core` workflows that use a `bin` directory as part of the workflow package. Although this directory is available to the workflow task, it's mounted as a read-only directory. Required resources in this directory should be copied into the task image and made available at runtime or when building the container image used for the task. 

See [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows) for the maximum size of container image that HealthOmics supports.

## Use a digest or version instead of a tag for non-PTC images
<a name="containers-best-practices-non-ptc-pin"></a>

For container images from registries that pull through cache doesn't support, such as Seqera, NVIDIA NGC, and Google Artifact Registry, reference a digest or a version instead of a tag such as `latest`. HealthOmics copies an image the first time a task needs it and doesn't refresh the copy, so a tag that changes upstream keeps resolving to the earlier copy. For more information, see [Using third-party registries not supported by pull through cache](containers-non-ptc-registries.md).

The following example references a Seqera Containers image by version and digest:

```
community.wave.seqera.io/library/htslib_samtools:1.24--d697cfb9dce007cd@sha256:a55ddea590e567a91df592300a960aa534cfc1bd16e7623e3938ec21f4f3df15
```