# Choosing a configuration in Amazon GameLift Streams

This guide can help you choose the optimal runtime environment and configuration settings for streaming your applications and games through
Amazon GameLift Streams. The configuration settings directly impact your content's performance and the costs associated with running it on Amazon GameLift Streams. There are
several options to support a wide variety of applications and graphical fidelity.

You can find the complete list of configuration options in [Configuration options](configuration-options.md "configuration-options.md").

The following key terms can help you understand how these configuration options work together:

- _Runtimes_ refer to the underlying operating system and software environment that will execute your application on
  Amazon GameLift Streams. The main runtime environment options are Windows, Linux, and Proton.
- _Stream classes_ represent the different resource configurations available within Amazon GameLift Streams, varying in operating
  system, CPU, GPU, RAM, and other specifications. The stream class is a configuration option of a stream group that defines both the
  hardware resources allocated to a stream session and the tenancy model (how many concurrent streams can run on a single virtual
  machine).
- _Multi-tenancy_ enables multiple users to share the same underlying hardware resources, which can be a
  cost-effective option for applications that don't require maximum hardware capabilities. A stream class with multi-tenancy can host
  multiple streams for the cost of one resource. "High" stream classes have 1:2 tenancy, while "Ultra" stream classes have 1 tenancy.
  When setting up your Amazon GameLift Streams configuration, the runtime environment you choose determines the specific stream class options that are
  compatible and available to you. Matching your application's requirements with the right runtime environment and stream class is key to
  optimizing performance and cost-efficiency in Amazon GameLift Streams.

The cost to stream depends on the stream class. For a detailed list of cost, refer to the Amazon GameLift Streams [Pricing page](https://aws.amazon.com/gamelift/streams/pricing/ "https://aws.amazon.com/gamelift/streams/pricing/").

## Starting point

Depending on your application, these are good starting points to get started streaming. Later, you can explore other configuration
options to optimize the cost.

### For Windows applications

We recommend using the Microsoft Windows Server 2022 Base runtime environment for Microsoft Windows applications. There are four hardware
configurations available for this runtime, the NVIDIA-based
`gen6n_pro_win2022`
,
`gen6n_ultra_win2022`
,
`gen5n_win2022`, and `gen4n_win2022` stream classes. In this environment, Amazon GameLift Streams supports games and other
3D applications using DirectX 11 or DirectX 12, and game engines including Unity 2022.3, Unreal Engine 4.27, and
Unreal Engine 5 up through . Streaming is supported over both IPv4 and IPv6.

This combination of runtime environment and stream classes provides a predictable, well-supported configuration with the highest
compatibility and best performance for your Windows-based content.

### For Linux applications

Use the Ubuntu 22.04 LTS runtime environment for applications built to run natively on Linux. To optimize for performance,
choose one of the Pro or Ultra stream classes (
`gen6n_pro`
,
`gen6n_ultra`
,

`gen5n_ultra`
, or
`gen4n_ultra`
). To optimize for cost, choose one of the Small,
Medium, or High stream classes (
`gen6n_high`
,
`gen6n_medium`
,
`gen6n_small`
,

`gen5n_high`
, or
`gen4n_high`
) that support _multi-tenancy_— a cost-effective
option where multiple concurrent stream sessions share the same compute resources.

###### Important

The Linux runtime in Amazon GameLift Streams does not support streaming over IPv6. Clients must stream applications over IPv4.

## Cost optimizations

While the starting point recommendations are a great place to begin, you might want to consider other configuration options to optimize
for cost while maintaining good performance.

### Use Proton runtime environment

Many Windows applications can run in the Proton runtime environment. Proton is a game-optimized compatibility layer that runs on
Linux. The stream class options for this runtime include powerful GPU resources running on NVIDIA hardware, with support for DirectX
11 and, beginning with Proton 8.0-5, DirectX 12. Visit the [Proton wiki](https://github.com/ValveSoftware/Proton/wiki "https://github.com/ValveSoftware/Proton/wiki") for more details about this option. If you choose to
explore running your application on Proton, we recommend that you start your testing using Proton 9.0-2.

###### Important

Proton runtimes in Amazon GameLift Streams do not support streaming over IPv6. Clients must stream applications over IPv4.

###### Important

The compatibility of your Windows application in a Proton runtime environment depends on your specific application requirements.
For example, Proton 9.0-2 has better support than Proton 8.0-2c for Unreal Engine 5. In general, the newer
your game, the newer version of Proton you will need. We strongly recommend thoroughly testing this runtime in your local
environment to ensure optimal performance. Use our [Proton troubleshooting
guide](troubleshoot-compatibility-wp.md "troubleshoot-compatibility-wp.md") to help you in this effort.

### Compile your application to Linux

Another cost-saving option is to target your application to run natively on Linux. Test the application on your end first to ensure
that the Linux version of your application performs as needed. If your application successfully runs on Linux, then you can follow the
Amazon GameLift Streams configuration options for Linux applications.

For information about cross-compiling Unreal Engine applications to Linux, refer to the [Cross-Compile Toolchain](https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine#cross-compiletoolchain "https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine#cross-compiletoolchain") section in Unreal Engine's developer guide.

## Deciding on a configuration

To determine the best runtime and stream class configuration, consider the following key questions.

1. **What platform is your application or game built for?** If you have a Windows application, the
   Windows runtime environment is the simplest to set up. If your application is built for Linux, the Linux runtime environment is
   the most straightforward. To save costs for streaming a Windows application, you can explore the Proton runtime environment or
   compile the application to Linux.
2. **How important is performance versus cost for your use case?** The Windows runtime environment may
   offer the best performance, but it can be more expensive to run. Comparitively, the Proton runtime environment is more
   cost-effective, though you might experience slightly lower performance or potential compatibility issues. This is because
   Windows-based applications might require certain functionality that is not yet fully supported in the available Proton runtimes.
   As a result, you could experience functional or graphical differences when running your application on the Proton environment. We
   recommend that you test your application on the different runtime environments and stream classes to evaluate the performance and
   cost trade-offs. For a full list of runtime environment options, see [Runtime environments](configuration-options.md#configuration-options-runtime "configuration-options.md#configuration-options-runtime").
3. **What are the graphical requirements of your application?** The graphical requirements of your
   application can help determine which stream class configuration is most appropriate. If your application demands high-performance
   GPUs, you should consider using stream classes with greater amounts of video memory (VRAM) and system memory (RAM). For example,
   the gen5n and gen6n stream classes deliver up to 3x better performance for graphics-intensive applications compared to the gen4n
   stream classes. If your application requires maximum GPU and CPU resources, you should consider the "pro" stream classes. Conversely,
   if your application can operate effectively at a lower graphical fidelity, you might save on costs by using stream classes that support
   multi-tenancy (any of the "small", "medium", or "high" stream classes). This allows multiple users to share the same underlying hardware
   resources. For a full description of stream class options, see [Stream classes](configuration-options.md#configuration-options-stream-classes "configuration-options.md#configuration-options-stream-classes").
4. **How much effort are you willing to invest in the setup?** The simplest way to set up your
   application is to run it natively using the Windows or Linux runtimes, since they are more likely to be compatible with your
   application out-of-the-box. In contrast, the Proton runtime environment will require more hands-on testing to identify the optimal
   Proton configuration for your needs. Consider the time and resources you can allocate to the setup and testing process when
   deciding between the runtime environment options.
5. **Have you tested your application on the various runtime environments and stream classes?** We
   recommend testing your content on different runtime environments and stream classes to see how it performs. This helps you
   determine the best fit based on factors like stability, graphics quality, feature functionality, and input responsiveness.

## How your configuration choices impact next steps

The configuration you select directly impacts the next phases of setting up your streaming environment. Specifically:

- **Creating an Amazon GameLift Streams application**: When you upload your game or application to Amazon GameLift Streams, you'll need
  to specify the runtime environment you want to use. This choice will determine the type of stream group you can use.
- **Linking to a stream group**: If you already have an existing stream group, your runtime environment
  choice will need to match the configuration of that group. For example, if you select the Windows runtime, you can only link your
  application to a stream group that's set up for Windows applications.
- **Creating a stream group**: When you create a new stream group, you must choose a stream class
  that's compatible with your chosen runtime. The stream class you choose should match the graphics requirements and compute power
  that your application requires.

By understanding how the configuration settings you choose influences these subsequent steps, you can better plan your overall
streaming implementation and ensure a smooth integration process.

## Next steps

Depending on the configuration you've chosen, there are a few different approaches you can take to set up your application for
streaming.

### If you've selected the Windows or Linux runtime

For Windows or Linux runtimes, the next steps are to set up streaming in Amazon GameLift Streams and then test the stream. For more information,
proceed to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md").

### If you're considering using Proton

An application's compatibility with Proton depends on the application's specific requirements. Therefore, we recommend that you
test your application on different Proton versions before bringing it to Amazon GameLift Streams. This helps you identify the Proton setup that
provides the best performance and compatibility for your needs. By testing outside of Amazon GameLift Streams, you can validate the application's
performance and functionality, and debug issues that are specific to the runtime. For information, see [Testing and troubleshooting compatibility with Proton for Amazon GameLift Streams](troubleshoot-compatibility-wp.md "troubleshoot-compatibility-wp.md").

When you've selected a specific Proton configuration, you're ready to set up streaming in Amazon GameLift Streams. For
more information, proceed to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md").
