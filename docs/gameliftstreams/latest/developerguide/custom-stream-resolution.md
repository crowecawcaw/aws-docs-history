# Custom stream resolution in Amazon GameLift Streams

By default, Amazon GameLift Streams delivers interactive streams at the industry-standard full
HD resolution of 1920 × 1080 pixels, in a standard 16-by-9 aspect ratio.
You can set a custom resolution for each session to match the
screen shape or aspect ratio of the player's device. Custom resolutions support landscape,
portrait, and square aspect ratios.

Use custom resolutions to:

- Stream full-screen experiences to phones and tablets in their native device aspect
  ratio, without padding or cropping.
- Match ultrawide monitor aspect ratios for a native widescreen experience.
- Support game streams with arbitrary dimensions for embedding in non-full-screen
  web experiences.
  You can use custom resolution with all Amazon GameLift Streams service configurations, regardless of stream
  class or runtime environment.

## How resolution works

When you set a custom resolution, Amazon GameLift Streams configures the session's virtual monitor to
the desired resolution. This becomes the **monitor
resolution** for the session. For best visual quality, the application must
render to the configured monitor resolution.

The monitor resolution determines the dimensions of the virtual monitor and the
resolution at which frames are captured. Two additional Web SDK settings affect the
resolution of the stream delivered to the player:

- **Maximum resolution:** A Web SDK setting
  that caps the stream resolution. When unspecified, no cap is applied and the full
  monitor resolution is streamed. See [Interaction with maximum resolution](#custom-stream-resolution-max-resolution "#custom-stream-resolution-max-resolution").
- **Dynamic resolution:** Automatically
  adjusts the stream resolution to deliver the best visual quality the viewer's
  network connection can sustain. See [Interaction with dynamic resolution](#custom-stream-resolution-dynamic-resolution "#custom-stream-resolution-dynamic-resolution").

Neither setting changes the monitor resolution for the session.

## Custom resolution constraints

The resolution you specify must meet these requirements:

| Constraint             | Value                                      |
| ---------------------- | ------------------------------------------ |
| Maximum total pixels   | 2,073,600 (1920 × 1080)                    |
| Width and height range | 320 – 4096 pixels                          |
| Dimension parity       | Both width and height must be even numbers |

The service validates these constraints when you start a session. If the resolution
does not meet the requirements, the request fails with a validation error.

## Set a custom resolution

You can set a custom resolution when you start a stream session using the console,
the AWS CLI, or the API.

### Using the Amazon GameLift Streams console

To test a stream with a custom resolution:

1. Open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/") and navigate to your stream group.
2. Choose **Test stream**.
3. In the **Resolution** dropdown, select a resolution for
   desktop, tablet, or mobile devices.
4. Choose **Test stream** to start the session.

After the stream is active, you can view the current resolution in the real-time
stats overlay.

### Using the AWS CLI

Use the `start-stream-session` command with the
`--display-configuration` parameter:

```
aws gameliftstreams start-stream-session \
  --identifier sg-ExampleStreamGroup \
  --application-identifier a-ExampleApp \
  --protocol WebRTC \
  --signal-request "your-signal-request" \
  --display-configuration '{"Resolution":{"Width":1920,"Height":1080}}'
```

### Using the API

In the [StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md") API
request, include the `DisplayConfiguration` parameter:

```
{
  "ApplicationIdentifier": "a-ExampleApp",
  "Protocol": "WebRTC",
  "SignalRequest": "your-signal-request",
  "DisplayConfiguration": {
    "Resolution": {
      "Width": 1920,
      "Height": 1080
    }
  }
}
```

## Calculate the optimal resolution for a device

You can use any resolution that meets the resolution constraints. The following formula is
one recommended approach to find the largest resolution for a specific aspect ratio. It
maximizes the available pixels for the best visual quality:

```
height = floor_to_even( sqrt(2,073,600 * H / W) )
width  = floor_to_even( height * W / H )
```

In this formula, `W:H` is the target aspect ratio and `2,073,600`
is the maximum total pixel count (1920 × 1080). The function
`floor_to_even(x)` rounds down to the nearest even integer.

###### Example 19.5:9 (mobile phone)

```
height = floor_to_even( sqrt(2,073,600 * 9 / 19.5) ) = floor_to_even(978.2) = 978
width  = floor_to_even( 978 * 19.5 / 9 )             = floor_to_even(2118.3) = 2118
→  Resolution: 2118 × 978  (2,071,404 pixels, 99.9% utilization)
```

For portrait resolutions, calculate the landscape resolution and swap the width and
height values.

## Common resolution values for devices

The following values use generic standard ratios that cover common device categories.
Individual devices might have slightly different native aspect ratios, which results in
visually negligible black bars. For pixel-perfect fill, use the device's exact native
aspect ratio with the formula above.

| Category | Aspect ratio | Landscape   | Portrait       | Matching devices                         |
| -------- | ------------ | ----------- | -------------- | ---------------------------------------- |
| Desktop  | 16:9         | 1920 × 1080 | 1080 × 1920    | Desktop monitors, TVs, HD mobile         |
| Desktop  | 16:10        | 1820 × 1138 | 1138 × 1820    | Widescreen monitors, Amazon Fire tablets |
| Desktop  | 21:9         | 2198 × 942  | Not applicable | Ultrawide monitors                       |
| Tablet   | 3:2          | 1760 × 1174 | 1174 × 1760    | Various iPads                            |
| Tablet   | 4:3          | 1660 × 1246 | 1246 × 1660    | iPads, Android tablets                   |
| Mobile   | 20:9         | 2142 × 964  | 964 × 2142     | Google Pixel, Samsung Galaxy             |
| Mobile   | 19.5:9       | 2118 × 978  | 978 × 2118     | iPhones, Samsung Galaxy                  |
| Mobile   | 18:9         | 2036 × 1018 | 1018 × 2036    | Other Android phones                     |
| Other    | 1:1          | 1440 × 1440 | Not applicable | Square monitors                          |

## Interaction with maximum resolution

Custom resolution and maximum resolution serve different purposes:

- **Custom resolution:** When you set a
  custom resolution, it becomes the monitor resolution for the session. This is
  what the server renders, including the aspect ratio and pixel dimensions of
  captured frames.
- **Maximum resolution:** A Web SDK setting
  that caps the stream resolution. The cap fits within the oriented bounding
  box of the selected tier (for example, 1280 × 720 for 720p). Use this
  setting to target lower-end devices that cannot decode a full-resolution
  image.

For more information about the maximum resolution parameter, see the
Amazon GameLift Streams Web SDK API Reference on the [Amazon GameLift Streams documentation page](../../../gameliftstreams.md "../../../gameliftstreams.md").

## Interaction with dynamic resolution

Dynamic resolution automatically adjusts the stream resolution to deliver the best
visual quality the viewer's network connection can sustain. This feature is available
with Amazon GameLift Streams Web SDK version 1.3.0 and later.

Dynamic resolution does not affect the monitor resolution for the session. Amazon GameLift Streams
adjusts only the stream resolution delivered to the player. When bandwidth is limited,
the stream resolution scales down while preserving the aspect ratio. When bandwidth
recovers, it scales back up to the full monitor resolution or the maximum resolution
cap.

For example, if you set a custom resolution of 1080 × 1920 (mobile portrait,
9:16), the player receives the full 1080 × 1920 stream under normal bandwidth.
If the player's network becomes constrained, dynamic resolution might scale the stream
down to a lower resolution (for example, 720 × 1280) while maintaining the 9:16
aspect ratio. The monitor resolution on the server remains 1080 × 1920
throughout.

For more information about the dynamic resolution parameter, see the
Amazon GameLift Streams Web SDK API Reference on the [Amazon GameLift Streams documentation page](../../../gameliftstreams.md "../../../gameliftstreams.md").

## Best practices

Follow these best practices when using custom resolutions with Amazon GameLift Streams:

- **Match the player's device aspect ratio to fill
  the screen without letterboxing or pillarboxing.** Use the common resolution values
  or calculation formula to find the optimal resolution for a given aspect ratio. For
  portrait-oriented mobile games, use a portrait resolution to provide a native
  vertical experience.
- **Optimize your frontend for the streaming
  experience.** Make sure your web client handles the stream's aspect
  ratio correctly when streaming to mobile devices or tablets.
- **Test your application with custom resolutions before deploying to players.**
  Most applications adapt to the monitor resolution automatically when running in
  fullscreen. However, some applications might not handle
  non-16:9 resolutions gracefully.
- **Make sure your in-game camera and UI adapt to the aspect
  ratio.** Adjust the game camera's field of view to show the
  appropriate amount of the scene rather than cropping the viewport. Reflow or
  reposition UI elements to fit the new aspect ratio.
- **Avoid changing the virtual monitor resolution at
  runtime within your application.** Amazon GameLift Streams sets the monitor resolution when the session
  starts. Applications that modify it during gameplay might produce unexpected
  results.
- **Handle device rotation in your application and frontend.** The
  monitor resolution is fixed for the duration of the session. To support
  mid-stream device rotation, we recommend sending the rotation signal through
  [Data channel communication between an application and web client](data-channels.md "data-channels.md") to the
  application. Have the application rotate its rendering, and update your frontend
  accordingly.

## Troubleshooting

The following table describes common issues, their causes, and suggested
solutions.

| Issue                                                                        | Cause                                                                                                 | Solution                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Session fails to start with validation error                                 | Resolution does not meet constraints                                                                  | Verify that your resolution meets all constraints listed in [Custom resolution constraints](#custom-stream-resolution-constraints "#custom-stream-resolution-constraints").                                                                                                                                                                                               |
| Application renders at wrong resolution                                      | Application is not running in fullscreen, or renders at a different<br>resolution in windowed mode    | Configure the application to run in fullscreen. The application can query the system for the configured<br>resolution.                                                                                                                                                                                                                                                    |
| Stream resolution is lower than expected (same aspect<br>ratio)              | Maximum resolution cap or dynamic resolution is active                                                | This is expected behavior when maximum resolution or dynamic<br>resolution is active. Both features scale the stream resolution down<br>while preserving the aspect ratio. Check the maximum resolution or<br>dynamic resolution setting in the Web SDK.                                                                                                                  |
| Stream resolution differs from custom resolution (different aspect<br>ratio) | Application changes the monitor resolution during startup or<br>mid-stream                            | Maximum resolution and dynamic resolution do not cause this issue.<br>This is a known behavior<br>for some applications that override the monitor resolution.<br>Consider using an application that does not override the monitor<br>resolution, or configure the application to render at the monitor<br>resolution in fullscreen.                                       |
| Black bars appear on the player's screen                                     | Aspect ratio mismatch between stream and device, or application<br>renders with black bars internally | Check if the black bars are from the client (aspect ratio mismatch)<br>or within the application itself. Use a resolution value that matches<br>the player's device aspect ratio, or calculate the optimal resolution<br>using the formula in [Calculate the optimal resolution for a device](#custom-stream-resolution-calculate "#custom-stream-resolution-calculate"). |
