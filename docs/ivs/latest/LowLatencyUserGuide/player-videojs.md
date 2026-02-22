# IVS Player SDK: Video.js Integration

This document describes the most important functions available in the Amazon Interactive
Video Service (IVS) Video.js player.

**Latest version of Video.js player integration:** 1.49.0
([Release
Notes](release-notes.md#feb19-26-player-web-ll "release-notes.md#feb19-26-player-web-ll"))

## Getting Started

Amazon IVS support for Video.js is implemented through a Video.js [tech](https://videojs.com/guides/tech/ "https://videojs.com/guides/tech/"). We provide support through
script tags as well as through an npm module. Amazon IVS supports Video.js versions
7.6.6 and later 7\*, and 8\*.

Note that when instantiating the player, the Video.js [sources option](https://videojs.com/guides/options/#sources "https://videojs.com/guides/options/#sources")
is not supported. Instead, instantiate the player normally and call the Video.js
`src()` function. If autoplay is enabled, the stream will start playing;
otherwise, use `play()` to start playback.

### Demo

The following live demo shows how to use the Video.js integration with script tags
from our Content Delivery Network: [Amazon
IVS Player Video.js integration](https://codepen.io/amazon-ivs/pen/NWqewZo/bdc01e977102051eae5fb85482f88276 "https://codepen.io/amazon-ivs/pen/NWqewZo/bdc01e977102051eae5fb85482f88276").

### Setup With Script Tag

To set up the Amazon IVS tech using the `script` tag:

1. Include the following tag (for the latest version of the player
   integration).

```
<script src="https://player.live-video.net/1.49.0/amazon-ivs-videojs-tech.min.js"></script>
```

2. Register the tech using the `registerIVSTech` function:

```
registerIVSTech(videojs);
```

where `videojs` is the object provided by Video.js. 3. When creating an instance of the player, add `AmazonIVS` as
your first tech in the `techOrder` option.

When instantiating the player, the Video.js [sources
option](https://videojs.com/guides/options/#sources "https://videojs.com/guides/options/#sources") is not supported. Instead, to set the source, instantiate the
player normally, then call the Video.js `src()` function on it. If
autoplay is enabled, the stream will start playing; otherwise, use
`play()` to start playback.

### Sample Code

In this example, `PLAYBACK_URL` is the source stream you want to load.
The example uses the latest version of the Amazon IVS Player.

```
<!doctype html>
<html lang="en">
<head>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.14.3/video-js.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.14.3/video.min.js"></script>
    <script src="https://player.live-video.net/1.49.0/amazon-ivs-videojs-tech.min.js"></script>
</head>

<body>
    <div class="video-container">
        <video id="amazon-ivs-videojs" class="video-js vjs-4-3 vjs-big-play-centered" controls autoplay playsinline></video>
    </div>
    <style>
        body {
            margin: 0;
        }

        .video-container {
            width: 640px;
            height: 480px;
            margin: 15px;
        }
    </style>
    <script>
        (function play() {
            // Get playback URL from Amazon IVS API
            var PLAYBACK_URL = '';

            // Register Amazon IVS as playback technology for Video.js
            registerIVSTech(videojs);

            // Initialize player
            var player = videojs('amazon-ivs-videojs', {
               techOrder: ["AmazonIVS"]
            }, () => {
               console.log('Player is ready to use!');
               // Play stream
               player.src(PLAYBACK_URL);
            });
        })();
    </script>
</body>
</html>
```

### Setup With NPM

To use Amazon IVS player through npm:

1. Install the [video.js](https://www.npmjs.com/package/video.js/v/7.6.6 "https://www.npmjs.com/package/video.js/v/7.6.6") npm package or ensure that your project has some other
   access to the Video.js library.
2. Install the `amazon-ivs-player` npm package:

```
npm install amazon-ivs-player
```

3. When you’re ready to register the Amazon IVS tech, import the
   `registerIVSTech` function:

```
import { registerIVSTech } from 'amazon-ivs-player';
```

4. Register the tech using the `registerIVSTech` function:

```
registerIVSTech(videojs, options);
```

where:

    * `videojs` is the object provided by Video.js.
    * `options` is the options for the Amazon IVS tech layer.
     Supported options are:.




    	+ `wasmWorker`: URL where the
    	 `amazon-ivs-wasmworker.min.js` file is
    	 hosted.
    	+ `wasmBinary`: URL where the
    	 `amazon-ivs-wasmworker.min.wasm` file is
    	 hosted.
    The worker files are in your `node_modules/` folder
     under `amazon-ivs-player/dist/`. You need to host them,
     to use the IVS player.

5. When creating an instance of the player, add `AmazonIVS` as
   your first tech in the `techOrder` option:

```
const player = videojs('videojs-player', {
    techOrder: ["AmazonIVS"]
});
```

### TypeScript

If you’re using TypeScript, our npm package includes the following types you may
want to import and use.

- `VideoJSEvents`, which describes the returned structure from
  `getIVSEvents()`.
- `VideoJSIVSTech`, which describes the interface to a player
  instance that uses the `AmazonIVS` tech. This can be [intersected](https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types "https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types") with the `VideoJsPlayer` type exposed by
  the [@types/video.js](https://www.npmjs.com/package/@types/video.js "https://www.npmjs.com/package/@types/video.js") npm package.
- `TechOptions`, which describes the interface defining the
  configuration options you can send to `registerIVSTech()`.

For more information on these types, see the [Amazon IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/").

## Events

To listen to standard Video.js events, use the [on](https://docs.videojs.com/docs/api/player.html#Methodson "https://docs.videojs.com/docs/api/player.html#Methodson") function of
the Video.js player.

To listen to events that are specific to Amazon IVS, add and remove event listeners on
the Amazon IVS Web player:

```
player.getIVSPlayer().addEventListener(event, callback);
player.getIVSPlayer().removeEventListener(event, callback);
```

where `callback` is a callback you define, and `event` is one
of: `PlayerEventType` or `PlayerState`. For more information about
events, see the [Amazon IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/").

## Errors

For general Video.js errors, listen to the generic `error` event on the
player:

```
player.on("error", callback);
```

For errors specific to Amazon IVS, listen on the Amazon IVS player for its own
errors:

```
let playerEvent = player.getIVSEvents().PlayerEventType;
player.getIVSPlayer().addEventListener(playerEvent.ERROR, callback);
```

The callback will receive an object with the following fields:

| Field     | Description                                                                                                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`    | The error type. Corresponds to `ErrorType` events. For<br>more information, see [Amazon IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/"). |
| `code`    | The error code.                                                                                                                                                                                                                              |
| `source`  | Source of the error.                                                                                                                                                                                                                         |
| `message` | Human readable error message.                                                                                                                                                                                                                |

## Plugins

We provide a plugin that creates a UI toggle for available qualities. To use this
plugin, it must be loaded by including the `amazon-ivs-quality-plugin.min.js`
file if you are using our tech through the following `script` tag (for the
latest version of the IVS Player):

```
<script src="https://player.live-video.net/1.49.0/amazon-ivs-quality-plugin.min.js"></script>
```

If you are using npm, import the `registerIVSQualityPlugin` from the
`amazon-ivs-player` module:

```
import { registerIVSQualityPlugin } from 'amazon-ivs-player';
```

Then, once you create an instance of your Video.js player, the following calls are
required to register and enable it:

```
registerIVSQualityPlugin(videojs); // where videojs is the video.js variable
player.enableIVSQualityPlugin(); // where player is the instance of the videojs player
```

This will create a UI menu button which allows you to select a quality for the
stream.

### Plugins and TypeScript

If you’re using TypeScript, our npm package includes the
`VideoJSQualityPlugin` type that you may want to import and use with
our plugin. Plugins essentially are mixins, so this type interface is to be used as
an [intersection type](https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types "https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types") with the `VideoJSIVSTech` typescript
interface.

## Content Security Policy

The Amazon IVS Video.js API is configured to work on pages that use Content Security
Policy (CSP). See the section on “Working with Content Security Policy” in the [IVS Player SDK: Web Guide](web-content-security-policy.md "web-content-security-policy.md").

## Functions

### Playback

The Amazon IVS Video.js API supports the necessary interfaces for internal use by
the Video.js framework. The client application is not likely to need to use these
methods directly, since Video.js does the necessary integration and presents a
standard interface. However, if needed, one way to access internal Video.js and
Amazon IVS player methods is to use the Video.js player object to get the needed
object handle to the tech.

To access the API, retrieve the instance of your Video.js player as you would
normally:

```
let player = videojs("videoTagId"); //replace videoTagId with your <video> tag’s id
```

Then you can call functions on that instance.

The following are the subset of Video.js functions that the Amazon IVS tech layer
overrides. For the full list of Video.js functions, see the [video.js API
documentation](https://docs.videojs.com/player "https://docs.videojs.com/player").

| Function       | Description and Amazon IVS-Specific Information                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `currentTime`  | Gets or sets the time (in seconds from the beginning).<br>Amazon IVS: We do not recommend setting current time for live<br>streams.                                                                            |
| `dispose`      | Deletes the player instance<br>Amazon IVS: This also deletes the Amazon IVS tech<br>backend.                                                                                                                   |
| `duration`     | Returns the duration of the video, in seconds.<br>Amazon IVS: For live streams, this returns<br>`Infinity`.                                                                                                    |
| `load`         | Starts loading the `src()` data.<br>Amazon IVS: This is a no-op.                                                                                                                                               |
| `play`         | Plays the stream that was set up via the `src`<br>call.<br>Amazon IVS: If a live stream was paused, this plays the live<br>stream from the latest frames, instead of continuing from where<br>it was paused.   |
| `playbackRate` | Gets or sets the video-playback rate. 1.0 means normal<br>speed; 0.5, half normal speed; 2.0, two times normal speed; and<br>so on.<br>Amazon IVS: On a live stream, a get returns 1, and a set is<br>ignored. |
| `seekable`     | Returns the `TimeRanges` of the media that can<br>be seeked to.<br>Amazon IVS: For live streams, calling `end(0)` on<br>the return value (`TimeRange`) returns<br>Infinity.                                    |

### Amazon IVS Specific

The Amazon IVS Video.js tech has additional functions for accessing behaviors
specific to Amazon IVS features:

| Function       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `getIVSPlayer` | Returns the underlying Amazon IVS player instance. The full<br>Amazon IVS Player Web API is available through this instance. We<br>recommend using the basic Video.js playback API as much as<br>possible, and using this function only to access Amazon<br>IVS-specific features. The most common functions you are likely<br>to need to access on the Amazon IVS player instance are<br>`setQuality()` and<br>`addEventListener()` /<br>`removeEventListener()` . |
| `getIVSEvents` | Returns an object that holds Amazon IVS-specific enums.<br>This is used for listening to Amazon IVS-specific errors. For<br>more information, see [Events](#videojs-events "#videojs-events") and [Errors](#videojs-errors "#videojs-errors").                                                                                                                                                                                                                      |

## currentTime

Gets or sets the time (in seconds from the beginning).

Amazon IVS: We do not recommend setting current time for live streams.

### Signatures

```
currentTime
currentTime(time)
```

### Parameter

| Parameter | Type   | Description                                                                                               |
| --------- | ------ | --------------------------------------------------------------------------------------------------------- |
| `time`    | number | If `time` is absent, gets the current time. If<br>`time` is present, sets video playback to that<br>time. |

### Return Value

| Type   | Description                                      |
| ------ | ------------------------------------------------ |
| number | The current time, in seconds from the beginning. |

## dispose

Deletes the player instance.

Amazon IVS: This also deletes the Amazon IVS tech backend.

### Signature

```
dispose()
```

### Parameters

None

### Return Value

None

## duration

Returns the duration of the video, in seconds.

Amazon IVS: For live streams, this returns `Infinity`.

### Signature

```
duration()
```

### Parameters

None

### Return Value

| Type   | Description                                                                            |
| ------ | -------------------------------------------------------------------------------------- |
| number | The duration of the stream, in seconds. For live streams, this<br>value is `Infinity`. |

## getIVSEvents

Returns an object that holds Amazon IVS-specific enums. This is used for listening to
Amazon IVS-specific errors and events. For more information, see:

- [Events](#videojs-events "#videojs-events") and [Errors](#videojs-errors "#videojs-errors") in this
  document.
- [Amazon
  IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/") for more information about events,
  error types, and error sources.

### Signature

```
getIVSEvents()
```

### Parameters

None

### Return Value

| Type     | Description                                                                                                       |
| -------- | ----------------------------------------------------------------------------------------------------------------- |
| `object` | An object with `PlayerEventType`,<br>`PlayerState`, and `ErrorType` keys,<br>which map to their associated enums. |

## getIVSPlayer

Returns the underlying Amazon IVS player instance. The full Amazon IVS Player Web API
is available through this instance. We recommend using the basic Video.js playback API
as much as possible, and using this function only to access Amazon IVS-specific
features. The most common functions you are likely to need to access on the Amazon IVS
player instance are `setQuality()` and `addEventListener()` /
`removeEventListener()`.

### Signature

```
getIVSPlayer()
```

### Parameters

None

### Return Value

| Type          | Description                         |
| ------------- | ----------------------------------- |
| `MediaPlayer` | The created instance of the player. |

## load

Starts loading the `src()` data.

Amazon IVS: This is a no-op.

### Signature

```
load()
```

### Parameters

None

### Return Value

None

## play

Plays the stream that was set up via the `src` call.

Amazon IVS: If a live stream was paused, this plays the live stream from the latest
frames, instead of continuing from where it was paused.

### Signature

```
play()
```

### Parameters

None

### Return Value

None

## playbackRate

Gets or sets the video-playback rate. 1.0 means normal speed; 0.5, half normal speed;
2.0, two times normal speed; and so on.

Amazon IVS: On a live stream, a get returns 1, and a set is ignored.

### Signatures

```
playbackRate
playbackRate(rate)
```

### Parameter

| Parameter | Type   | Description                                                   |
| --------- | ------ | ------------------------------------------------------------- |
| `rate`    | number | The playback rate. Valid values: in the range [0.25,<br>2.0]. |

### Return Value

| Type   | Description        |
| ------ | ------------------ |
| number | The playback rate. |

## seekable

Returns the `TimeRanges` of the media that can be seeked to.

Amazon IVS: For live streams, calling `end(0)` on the return value
(`TimeRange`) returns Infinity.

### Signature

```
seekable()
```

### Parameter

None

### Return Value

| Type        | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| `TimeRange` | TimeRange of the media that is available for seeking<br>to. |
