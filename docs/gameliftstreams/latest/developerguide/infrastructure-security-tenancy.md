# Reuse and multi-tenancy in Amazon GameLift Streams

Amazon GameLift Streams doesn't share any compute resources across stream groups or with other AWS customers. Some Amazon GameLift Streams stream groups rely
on internal resource sharing.

## Reuse of compute resources

Within a stream group, resources are reused over time to serve multiple sessions with minimal downtime. The specific details of reuse
are different between Windows and non-Windows stream groups.

Non-Windows stream groups with stream classes such as `gen4n_high`, `gen5n_ultra`, `gen6n_ultra` or
`gen6n_pro` execute your applications inside of dedicated per-session containers. Each stream session begins with a copy of
the application files and an empty user profile folder. When a session terminates, all file system modifications are discarded and all
processes launched by your application are terminated as part of container cleanup.

Windows-based stream groups with stream classes such as `gen4n_win2022`, `gen5n_win2022`, `gen6n_ultra_win2022`,
or `gen6n_pro_win2022` execute your applications directly on the host operating system. Each stream session begins with a copy of
the application files and an empty user profile folder. When a session terminates, the user profile folder and application folder are fully reset.
Sub-processes launched by your application are terminated. If your application modifies files outside of the user profile folder and the application
folder, or modifies the system registry, then those changes might persist across multiple sessions.

For any stream group configuration, the underlying compute resources and operating system environment will be reused over time to
launch new stream sessions. Under the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), it is your responsibility to maintain the security of
your applications and avoid executing untrusted code or modifying critical operating system files.

## Multi-tenant stream groups

Stream groups are either single-tenant or multi-tenant, depending on your selection of stream class. Multi-tenant stream classes such as
`gen4n_high` or `gen5n_high` share one GPU across multiple simultaneous sessions. In this context, multi-tenancy
refers to running more than one session at a time on the underlying hardware. The hardware is still dedicated to your stream group and is
not shared across stream groups or with other AWS customers.

This multi-tenant stream group model is unique to Amazon GameLift Streams and comes with important security and performance implications. The security
posture of a multi-tenant stream group is equivalent to hosting multiple application containers on a single physical server. This posture
isn't inherently insecure, but it might amplify the impact of existing security vulnerabilities in your applications. Under the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), it is your responsibility to
maintain the security of your applications.

Amazon GameLift Streams makes efforts to ensure that multi-tenant sessions do not interfere with each other. However, if an application
consumes CPU or GPU resources without regard for the defined limits of the stream class, this can have an impact on other streams that are
trying to use the same shared resources. For example, in a "high" stream group with two tenants per GPU, a greedy application can
negatively impact up to one other stream. Your application should regulate its own resource consumption. If your application cannot
self-regulate and your use case has no tolerance for potential "noisy neighbor" performance variations, a single-tenant stream class, such
as `gen5n_win2022`, `gen6n_pro_win2022`, `gen5n_ultra`, or `gen6n_ultra`, is recommended.
