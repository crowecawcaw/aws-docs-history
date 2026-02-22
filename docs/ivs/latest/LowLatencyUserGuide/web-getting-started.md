# Getting Started with the IVS Web Player

SDK

This document takes you through the steps involved in getting started with the Amazon
IVS Web player SDK.

We provide support through a `script` tag as well as through an npm module.

## Demos

The following live demo shows how to use the Web player with a `script`
tag from our Content Delivery Network: [Amazon IVS Player Sample](https://codepen.io/amazon-ivs/pen/QWbzORP/c3b13a2df34b60ada7756f3a2af8d2f0 "https://codepen.io/amazon-ivs/pen/QWbzORP/c3b13a2df34b60ada7756f3a2af8d2f0"). The demo includes setting up event
listeners.

Also see [https://github.com/aws-samples/amazon-ivs-player-web-sample](https://github.com/aws-samples/amazon-ivs-player-web-sample "https://github.com/aws-samples/amazon-ivs-player-web-sample") for a
selection of additional Web player demos.

## Setup With Script Tag

To set up the Amazon IVS player using the `script` tag:

1. Include the following tag (for the latest version of the player).

```
<script src="https://player.live-video.net/1.49.0/amazon-ivs-player.min.js"></script>
```

2. Once `amazon-ivs-player.min.js` is loaded, it adds an
   `IVSPlayer` variable to the global context. This is the
   library you will use to create a player instance. First, check
   `isPlayerSupported` to determine if the browser supports the
   IVS player:

```
if (IVSPlayer.isPlayerSupported) { ... }
```

Then, to create a player instance, call the `create` function
on the `IVSPlayer` object.

```
const player = IVSPlayer.create();
```

The Amazon IVS Web player SDK uses web workers to optimize video
playback. 3. Load and play a stream using the `load` and `play`
functions on the player instance:

```
player.load("PLAYBACK_URL");
player.play();
```

where `PLAYBACK_URL` is the URL returned from the Amazon IVS
API when a stream key is requested.

## Sample Code

In this example, replace `PLAYBACK_URL` with the URL of the
source stream you want to load. The example uses the latest version of the Amazon
IVS player.

```
<script src="https://player.live-video.net/1.49.0/amazon-ivs-player.min.js"></script>
<video id="video-player" playsinline></video>
<script>
  if (IVSPlayer.isPlayerSupported) {
    const player = IVSPlayer.create();
    player.attachHTMLVideoElement(document.getElementById('video-player'));
    player.load("PLAYBACK_URL");
    player.play();
  }
</script>
```

In the `<video>` tag, `playsinline` is required for
inline playback on iOS Safari. See [https://webkit.org/blog/6784/new-video-policies-for-ios/](https://webkit.org/blog/6784/new-video-policies-for-ios/ "https://webkit.org/blog/6784/new-video-policies-for-ios/").

## Setup With NPM

For guidance, including an example Webpack configuration file, see the following
repository: [https://github.com/aws-samples/amazon-ivs-player-web-sample](https://github.com/aws-samples/amazon-ivs-player-web-sample "https://github.com/aws-samples/amazon-ivs-player-web-sample").

**Note:** When hosting player static assets from your
own domain, you must set the "Content-Type" response header for the WebAssembly
binary (`amazon-ivs-wasmworker.min.wasm`) to "application/wasm." You also
should gzip your assets to reduce bytes downloaded over the wire and improve the
player’s time to start playback.

## TypeScript

If you’re using TypeScript, the npm package includes types you may want to import
and use. For information on these types, see the [Amazon IVS Player
SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.49.0/web/").

## Set Up Service Worker

To lower latency further when playing via browsers that only support native
playback (primarily iOS Safari), a service worker can be set up and configured. For
more context, see [Reducing Latency in
Third-Party Players](player.md#player-reducing-latency "player.md#player-reducing-latency").

To set up the Amazon IVS player to use a service worker:

1. Create a file to load the IVS service worker off the CDN. This is required
   as service workers must be hosted on the same domain as the page that pulls
   them in.

Create a file named `amazon-ivs-service-worker-loader.js` or
similar and add the following line:

```
importScripts('https://player.live-video.net/1.49.0/amazon-ivs-service-worker.min.js');
```

2. When creating a player instance, pass in the following
   `serviceWorker` config referencing the
   `amazon-ivs-service-worker-loader.js` file:

```
const player = IVSPlayerPackage.create({
   serviceWorker: {
      url: 'amazon-ivs-service-worker-loader.js'
   }
});
```

3. On the video element, set the `crossOrigin` attribute to
   `anonymous`. This is required to allow the service worker to
   make changes to the manifest.

**Note**: To test the service worker locally, the
page either needs to be served off _localhost_ or
_https_.

For a live demo, see the service worker example in the following
repository:

[https://github.com/aws-samples/amazon-ivs-player-web-sample](https://github.com/aws-samples/amazon-ivs-player-web-sample "https://github.com/aws-samples/amazon-ivs-player-web-sample")

## Audio-Only Playback

Audio-only quality must be manually selected with the `setQuality()`
method. Note that the player does not support a `true` value for the
second argument, `adaptive`, so by default, this argument is
`false`.

To set the quality to audio-only before playback begins, call
`setQuality()` inside the `READY` event:

```
player.addEventListener(PlayerState.READY, () => {
   const qualities = player.getQualities();
   const audioOnly = qualities.find(q => q.name === 'audio_only');
   if (audioOnly) {
      player.setQuality(audioOnly);
   }
});
```

Setting the quality within `READY` works for both autoplay and
non-autoplay modes.

## Optimizing Background

Playback

Starting with SDK version 1.45.0, the client can be configured to optimize data usage while playing in a background tab. When this feature is enabled, then after the duration specified, the player selects the highest available SD video quality, with a maximum of 480p. The player always selects video; audio_only is not selected. This applies to both manual and auto modes. When the tab is foregrounded, the player automatically switches back to its prior setting.

To enable this feature:

```
const player = IVSPlayer.create({
   optimizeBackgroundPlayback: {
      enabled: true,
      switchDelayMs: 60 * 1000,   // Optional, defaults to 60s
   }
});
```
