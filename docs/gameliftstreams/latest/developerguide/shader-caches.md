

# Shader cache
<a name="shader-caches"></a>

With shader caching, your application can skip costly shader recompilation in future stream sessions. If your application suffers from stuttering or slow load times, capturing a shader cache can significantly improve the experience for your end users.

With Amazon GameLift Streams, you can capture a shader cache from a specially designated stream session. Subsequent stream sessions of the application in all compatible stream groups automatically use the captured shader cache. Using the shader caching feature requires no code or other changes to your application.

## Prerequisites
<a name="shader-caches-prerequisites"></a>

To use shader caching, you must meet the following requirements:
+ The stream group must have been created on or after July 31, 2026. Stream groups created before this date do not support shader caching.

## How shader caching works
<a name="shader-caches-how-it-works"></a>

Graphics applications such as games benefit from shader caches. Caches avoid repeated graphics-related processing and compilation work. To capture a shader cache from designated stream sessions, Amazon GameLift Streams collects system shader cache files automatically generated for your application. The service stores this cache and automatically applies it to future sessions on compatible stream groups. This reduces the time spent on processing shaders during future sessions. Generating or consuming a shader cache requires no changes to your application.

The shader caching lifecycle has three stages:

1. **Capture** – You run a stream session with shader cache capture enabled. During this session, the system compiles shader programs used by your application automatically into a local filesystem cache. When you gracefully exit your application, Amazon GameLift Streams packages and uploads this local cache.

1. **Replication** – Amazon GameLift Streams replicates the shader cache to all streaming locations of the stream group. You can monitor the replication status using the [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html) API operation.

1. **Consumption** – Amazon GameLift Streams automatically downloads and applies the shader cache to all subsequent stream sessions for the same application. The shader cache is used across all compatible associated stream groups and streaming locations. This behavior is on by default.

## Capturing a shader cache
<a name="shader-caches-capturing"></a>

To capture a shader cache, follow these steps:

1. Start a stream session using the [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html) API operation. In the request, include the `GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_CAPTURE` set to `1` as additional environment variable when calling [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html):

   ```
   {
     "AdditionalEnvironmentVariables": {
       "GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_CAPTURE": "1"
     }
   }
   ```

1. Use your application as you normally would during the session.

1. When complete, exit your application gracefully from its built-in menu or by using other built-in exit commands. This ensures that the shader cache is ready to be collected.

1. After termination, Amazon GameLift Streams packages the compiled shader cache and begins replication to all streaming locations across all compatible associated stream groups.

**Tip**  
In gaming applications, navigating through different environments, content, and levels generates additional shader data. The more of your application you cover during the capture, the more comprehensive the shader cache coverage becomes. Improved coverage can further reduce shader processing times in future sessions.

**Important**  
Avoid terminating the session using the [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html) API operation. If your application does not have a built-in exit, use the [Stream session admin shell](troubleshoot-admin-shell-guide.md) feature to remotely log in. Then stop the application process after ensuring that the application is in idle state and not rendering new content.

After generating a shader cache, you can improve it by starting further sessions with `GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_CAPTURE` set to `1`. These sessions start with the existing shader cache and produce an updated version.

### Shader cache size limits
<a name="shader-caches-size-limits"></a>

Shader caches smaller than 10 KB or larger than 4 GB (uncompressed) are rejected.

### Shader cache workflow
<a name="shader-caches-workflow"></a>

When you generate a shader cache for an existing Amazon GameLift Streams application, all compatible associated stream groups automatically start using it.

To test a shader cache before it affects production sessions, we recommend this approach:

1. Create a separate application.

1. Collect the shader cache for that application.

1. Verify the results using a new stream session.

1. Use the application in your production setup.

## Shader cache replication
<a name="shader-caches-replication"></a>

After a successful capture, Amazon GameLift Streams automatically makes the shader cache available in every active streaming location in the application's compatible associated stream groups. This replication process typically completes within a few minutes.

You can monitor replication progress using the [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html) API operation. The shader cache `Status` field indicates the aggregated status across all locations of the stream group. Possible statuses include the following.


| Status | Description | 
| --- | --- | 
| INITIALIZED | Amazon GameLift Streams received the request and is preparing the shader cache. | 
| PROCESSING | Amazon GameLift Streams is replicating the shader cache to the streaming locations in the associated stream groups. | 
| READY | The shader cache is replicated and available for use in stream sessions. | 
| ERROR | An error occurred during shader cache processing. Create a new shader cache to try again. | 
| DELETING | Amazon GameLift Streams is deleting the shader cache. | 

When the status is `READY`, the shader cache is automatically applied to all new stream sessions for the application.

Newly provisioned stream capacity receives the shader cache immediately. Existing stream group capacity can take up to one hour to obtain the new shader cache.

## Disabling shader cache consumption
<a name="shader-caches-disabling"></a>

By default, Amazon GameLift Streams downloads and applies the shader cache before launching the application. To disable this behavior for a specific session, set the following environment variable:

```
{
  "AdditionalEnvironmentVariables": {
    "GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_IGNORE": "1"
  }
}
```

To improve upon an existing shader cache, provide only `GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_CAPTURE`. To discard the existing cache and collect a completely new one, provide both `GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_IGNORE` and `GAMELIFT_STREAMS_PACKAGED_SHADER_CACHE_CAPTURE`.

## Shader cache compatibility
<a name="shader-caches-compatibility"></a>

You can associate an application with multiple stream groups. To find out which stream groups your application is currently associated with, use the [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html) API operation and review the `AssociatedStreamGroups` field.

Not all associated stream groups are necessarily compatible with a collected shader cache. You can determine which associated stream groups are compatible by using the [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html) API operation. In its response, the `AssociatedStreamGroups` field contains only those associated stream groups that are compatible with the shader cache.

Graphics hardware and drivers determine how the system compiles shader programs. Because of this, caches are not transferable across different hardware and software configurations. With Amazon GameLift Streams, shader cache compatibility is determined by the properties of the stream group used during capture:
+ Exact model of underlying graphics hardware (GPU)
+ Installed GPU driver version

In practice, this means that a Amazon GameLift Streams shader cache has the following compatibility restrictions.
+ A shader cache is not compatible across stream classes that use different GPU hardware, meaning different generation stream classes. For example, `gen5n_high` and `gen6n_high` stream classes are not compatible, but `gen6n_high` and `gen6n_ultra` are. Similarly, `gen6n_pro` and `gen6e_pro` are also not compatible.
+ A shader cache is not compatible between stream groups that have a different GPU driver version installed. A stream group uses the same GPU driver version for its lifetime, but a newly created one might receive an updated version. For more information about the GPU driver versions currently available on Amazon GameLift Streams for new stream groups, see [GPU driver versions](configuration-options.md#configuration-options-gpu-driver-versions).
+ A shader cache is not compatible between Windows, Linux, and Proton runtimes.

Amazon GameLift Streams automatically determines this compatibility and uses the collected shader cache only with compatible sessions.

### Example: Different generation stream classes
<a name="shader-caches-compatibility-example1"></a>

Your application is associated with two stream groups:
+ First stream group uses the stream class `gen5n_high`
+ Second stream group uses the stream class `gen6n_high`

The same shader cache is not compatible across these two different generation stream groups. To support both stream groups, generate a separate shader cache for each stream class.

### Example: Different GPU driver versions
<a name="shader-caches-compatibility-example2"></a>

You have a stream group that uses the `gen6n_high` stream class, and have generated a shader cache for it. Later you create another stream group, still using the same stream class `gen6n_high`.

This new stream group now uses a different, more recent GPU driver version. By using [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html), you find out that your new stream group is not listed under `AssociatedStreamGroups`. The existing shader cache is therefore not compatible with the new stream group. Generate a new shader cache by using the new stream group.

## Troubleshooting shader cache issues
<a name="shader-caches-troubleshooting"></a>
+ **ListApplicationShaderCaches shows status ERROR** – An error occurred during shader cache processing. Create a new shader cache to try again.
+ **ListApplicationShaderCaches does not list the new shader cache**
  + The shader cache was too small or too large to be collected.
  + The application did not exit gracefully.
  + An error occurred during collection.

  Create a new shader cache to try again.