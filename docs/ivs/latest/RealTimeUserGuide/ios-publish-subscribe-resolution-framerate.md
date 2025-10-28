# How iOS Chooses Camera

Resolution and Frame Rate

The camera managed by the broadcast SDK optimizes its resolution and frame rate
(frames-per-second, or FPS) to minimize heat production and energy consumption. This
section explains how the resolution and frame rate are selected to help host
applications optimize for their use cases.

When creating an `IVSLocalStageStream` with an `IVSCamera`, the
camera is optimized for a frame rate of
`IVSLocalStageStreamVideoConfiguration.targetFramerate` and a resolution
of `IVSLocalStageStreamVideoConfiguration.size`. Calling
`IVSLocalStageStream.setConfiguration` updates the camera with newer
values.

## Camera Preview

If you create a preview of an `IVSCamera` without attaching it to a
`IVSBroadcastSession` or `IVSStage`, it defaults to a
resolution of 1080p and a frame rate of 60 fps.

## Broadcasting a Stage

When using an `IVSBroadcastSession` to broadcast an
`IVSStage`, the SDK tries to optimize the camera with a resolution
and frame rate that meet the criteria of both sessions.

For example, if the broadcast configuration is set to have a frame rate of 15 FPS
and a resolution of 1080p, while the Stage has a frame rate of 30 FPS and a
resolution of 720p, the SDK will select a camera configuration with a frame rate of
30 FPS and a resolution of 1080p. The `IVSBroadcastSession` will drop
every other frame from the camera, and the `IVSStage` will scale the
1080p image down to 720p.

If a host application plans on using both `IVSBroadcastSession` and
`IVSStage` together, with a camera, we recommend that the
`targetFramerate` and `size` properties of the respective
configurations match. A mismatch could cause the camera to reconfigure itself while
capturing video, which will cause a brief delay in video-sample delivery.

If having identical values does not meet the host application’s use case, creating
the higher quality camera first will prevent the camera from reconfiguring itself
when the lower quality session is added. For example, if you broadcast at 1080p and
30 FPS and then later join a Stage set to 720p and 30 FPS, the camera will not
reconfigure itself and video will continue uninterrupted. This is because 720p is
less than or equal to 1080p and 30 FPS is less than or equal to 30 FPS.

## Arbitrary Frame Rates, Resolutions,

and Aspect Ratios

Most camera hardware can exactly match common formats, such as 720p at 30 FPS or
1080p at 60 FPS. However, it is not possible to exactly match all formats. The
broadcast SDK chooses the camera configuration based on the following rules (in
priority order):

1. The width and height of the resolution are greater than or equal to the
   desired resolution, but within this constraint, width and height are as
   small as possible.
2. The frame rate is greater than or equal to the desired frame rate, but
   within this constraint, frame rate is as low as possible.
3. The aspect ratio matches the desired aspect ratio.
4. If there are multiple matching formats, the format with the greatest field
   of view is used.

Here are two examples:

- The host application is trying to broadcast in 4k at 120 FPS. The selected
  camera supports only 4k at 60 FPS or 1080p at 120 FPS. The selected format
  will be 4k at 60 FPS, because the resolution rule is higher priority than
  the frame-rate rule.
- An irregular resolution is requested, 1910x1070. The camera will use
  1920x1080. _Be careful: choosing a resolution like
  1921x1080 will cause the camera to scale up to the next available
  resolution (such as 2592x1944), which incurs a CPU and memory-bandwidth
  penalty_.

## What about Android?

Android does not adjust its resolution or frame rate on the fly like iOS does, so
this does not impact the Android broadcast SDK.
