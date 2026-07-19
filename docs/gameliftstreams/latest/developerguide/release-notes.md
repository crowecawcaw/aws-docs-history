# Amazon GameLift Streams release notes

The following release notes are in reverse chronological order, with the latest updates listed first. Amazon GameLift Streams was first released in 2025.

With IAM role support for stream sessions, your application can now access AWS
resources in your account, such as Amazon S3 buckets and DynamoDB tables. When you pass a
role ARN on `StartStreamSession`, Amazon GameLift Streams assumes the role on your behalf
and makes credentials available to your application automatically. You do not need
to change your application code.

###### Learn more:

- [Provide AWS credentials to your streaming application](session-credentials.md "session-credentials.md"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers Stream Session Admin Shell, a secure terminal connection to
the live runtime environment of a stream session. Inspect logs, query running
processes, check GPU utilization, and examine application state in real time.
Available at no additional cost in all AWS Regions where Amazon GameLift Streams is offered.

###### Learn more:

- [Stream Session Admin Shell](troubleshoot-admin-shell-guide.md "troubleshoot-admin-shell-guide.md"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers Generation 6e stream classes, powered by the EC2 G6e instance
family. Generation 6e features NVIDIA L40S Tensor Core GPUs and 3rd generation AMD
EPYC processors, delivering 2x the GPU memory and up to 2.9x faster GPU memory
bandwidth compared to standard Generation 6 stream classes. These classes are
designed for streaming high-fidelity, graphically demanding games and applications
that benefit from additional GPU memory and performance. Generation 6e stream
classes are available in select AWS Regions.

###### Learn more:

- [Stream classes](configuration-options.md#configuration-options-stream-classes "configuration-options.md#configuration-options-stream-classes"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers Proton 10 as a managed runtime environment for improved
compatibility with newer Windows-based applications running on Linux. You must
create new Amazon GameLift Streams applications and stream groups to use this new runtime.

###### Learn more:

- [Runtime environments](configuration-options.md#configuration-options-runtime "configuration-options.md#configuration-options-runtime"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers two additional Generation 6 stream
classes — gen6n\_small\_win2022 and gen6n\_medium\_win2022. These Microsoft
Windows Server 2022 Base classes use NVIDIA L4 Tensor Core GPUs and 3rd
generation AMD EPYC processors, providing cost-optimized options for streaming
well-optimized or lower-fidelity games on Windows environments.

###### Learn more:

- [Stream classes](configuration-options.md#configuration-options-stream-classes "configuration-options.md#configuration-options-stream-classes"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers six new locations — ap-northeast-2 (Seoul), ap-south-1
(Mumbai), ap-southeast-2 (Sydney), eu-north-1 (Stockholm), eu-west-2 (London),
and sa-east-1 (São Paulo). These new locations help reduce latency and improve
gameplay experience for players in those areas.

###### Learn more:

- [AWS Regions and streaming locations supported by Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md"), _Amazon GameLift Streams Developer Guide_

### Maximum capacity and target-idle capacity

Amazon GameLift Streams now configures stream group capacity using two new parameters: maximum
capacity and target-idle capacity. Target-idle capacity keeps capacity ready
before players create sessions to reduce wait time and improve player experience.
Maximum capacity limits the number of sessions that can run at once to help you
control costs. These parameters offer improved capacity management for on-demand
streaming.

###### Learn more:

- [Manage streaming with an Amazon GameLift Streams stream group](stream-groups.md "stream-groups.md"), _Amazon GameLift Streams Developer Guide_

### Generation 6 stream classes

Amazon GameLift Streams now offers Generation 6 stream classes, powered by the EC2 G6 instance
family. Generation 6 improves price-performance across a wide range of
configurations, making it the best option for both performance-focused and
cost-focused use cases.

###### Learn more:

- [Stream classes](configuration-options.md#configuration-options-stream-classes "configuration-options.md#configuration-options-stream-classes"), _Amazon GameLift Streams Developer Guide_

### Performance stats overlay

Amazon GameLift Streams now provides performance stats for stream sessions. You can receive a
live stream of performance data on the client during active sessions, and view a
real-time overlay of performance stats alongside your stream on the "Test stream"
page in the AWS Management Console. Additionally, the Export stream session files feature now
includes a CSV of performance stats for post-session analysis. Stats include
application-level data (CPU and memory usage) and shared system-level data (CPU,
memory, GPU, and VRAM utilization).

###### Learn more:

- [Monitoring Amazon GameLift Streams](monitoring-overview.md "monitoring-overview.md"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers enhanced flexibility for managing default applications in stream
groups. You can now create new stream groups without specifying a default
application, and modify or remove default applications in existing stream groups.

###### Note

Linking a default application is still required before streaming from a stream group.

###### Learn more:

- [About default applications](multi-apps.md#multi-apps-about-linking "multi-apps.md#multi-apps-about-linking"), _Amazon GameLift Streams Developer Guide_

Amazon GameLift Streams now offers Proton 9 as a managed runtime environment for improved
compatibility with newer Windows-based applications running on Linux. You must
create new Amazon GameLift Streams applications and stream groups to use this new runtime.

###### Learn more:

- [Runtime environments](configuration-options.md#configuration-options-runtime "configuration-options.md#configuration-options-runtime"), _Amazon GameLift Streams Developer Guide_
