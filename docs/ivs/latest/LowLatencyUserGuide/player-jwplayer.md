# IVS Player SDK: JW Player Integration

This document describes the most important functions available in the Amazon Interactive
Video Service (IVS) JW Player integration.

**Latest version of JW Player integration:** 1.47.0 ([Release Notes](release-notes.md#nov20-25-player-web-ll "release-notes.md#nov20-25-player-web-ll"))

## Getting Started

Amazon IVS support for JW Player is implemented through a Provider. Amazon IVS
Provider is supported only on JW Player’s web player. The Provider is loaded through a
script tag, and any streams requiring Amazon IVS Provider playback must be tagged with
`type: 'ivs'` in the playlist. Amazon IVS supports JW Player version
8.18.4 and later.

### Setup

In these instructions, `JW_PLAYER_DIV` is the name of the
`<div>` of your JW Player instance and `IVS_STREAM` is
your IVS playback URL. To set up the Amazon IVS Provider and enable playback:

1. Include the following `script` tag (for the latest version of
   the player integration; in this case, 1.47.0):

```
<script src="https://player.live-video.net/1.47.0/amazon-ivs-jw-provider.min.js"></script>
```

2. Use the `ivs` type to mark your IVS playlist items. Set the
   `cast` value in your `setup()` to
   `null` (since Chromecast is not supported).

```
jwplayer(JW_PLAYER_DIV).setup({
   playlist: [{
      file:IVS_STREAM,
      type: 'ivs',
   }]
});
```

3. If you want a reference to the underlying Amazon IVS Player to make Amazon
   IVS Player API calls or you want references to Amazon IVS-specific enums for
   callback handling, add a listener to the `'providerPlayer'`
   event:

```
jwplayer(JW_PLAYER_DIV).on('providerPlayer', function (player) {
   // player object has 'ivsPlayer' and 'ivsEvents' properties
   // ...callback code...
});
```

### Sample Code

In this example, `JW_PLAYER_LIB` is the URL to your JW Player library
script and `IVS_STREAM` is your IVS playback URL.

```
<!DOCTYPE html>
<html lang="en">
<head>
   <script src=JW_PLAYER_LIB></script>
   <script src="https://player.live-video.net/1.47.0/amazon-ivs-jw-provider.min.js"></script>
</head>
<body>
   <div id='player'></div>
   <script>
      // set default values for ivsPlayer and ivsEvents
      var ivsPlayer = {};
      var ivsEvents = {};

      // define our player setup
      const ivsConfig = {
         playlist: [{
            file: IVS_STREAM,
            type: 'ivs',
         }]
      };

      jwplayer('player')
         .setup(ivsConfig)
         .on('providerPlayer', function (player) {
            console.log('Amazon IVS Player: ', player.ivsPlayer);
            console.log('Amazon IVS Player Events: ', player.ivsEvents);

            // store the reference to the Amazon IVS Player
            ivsPlayer = player.ivsPlayer;
            // store the reference to the Amazon IVS Player Events
            ivsEvents = player.ivsEvents;
         });
   </script>
</body>
</html>
```

## Events

To listen to standard JW Player events, use the [on](https://developer.jwplayer.com/jwplayer/docs/jw8-javascript-api-reference "https://developer.jwplayer.com/jwplayer/docs/jw8-javascript-api-reference") function of the JW Player.

To listen to events that are specific to Amazon IVS, or to add and remove event
listeners on the Amazon IVS Web player, you must listen to the
`'providerPlayer'` event to get a reference to the Amazon IVS Player and
then add event listening onto it. For example:

```
// store a default value for ivsPlayer
var ivsPlayer = {};

// store references to the Amazon IVS Player and Amazon IVS Events:
jwplayer(JW_PLAYER_DIV).on('providerPlayer', function (player) {
   ivsPlayer = player.ivsPlayer;
});

// set up event listening
ivsPlayer.addEventListener(event, callback);
ivsPlayer.removeEventListener(event, callback);
```

where `callback` is a callback that you define, and `event` is
one of: `PlayerEventType`, `PlayerState`, or
`ErrorType`. For more information about events, see the [Amazon IVS Player SDK:
Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/").

The `'providerPlayer'` event is emitted by JW Player, and the callback you
register with it will receive an object with the following fields:

| Field       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ivsPlayer` | Returns the underlying Amazon IVS player instance. The full Amazon<br>IVS Player Web API is available through this instance. We recommend<br>using the basic JW Player playback API as much as possible, and<br>using this function only to access Amazon IVS-specific features. The<br>most common functions you are likely to need to access on the Amazon<br>IVS player instance are `addEventListener()` and<br>`removeEventListener()`. |
| `ivsEvents` | Returns an object with `PlayerEventType`,<br>`PlayerState`, and `ErrorType` fields,<br>which map to their associated Amazon IVS-specific enums. For more<br>information, see [Amazon IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/").                                                                                                    |

## Errors

For general JW Player errors, use the [on](https://developer.jwplayer.com/jwplayer/docs/jw8-javascript-api-reference "https://developer.jwplayer.com/jwplayer/docs/jw8-javascript-api-reference") function of the JW Player to listen to error events.

For errors specific to Amazon IVS, listen on the Amazon IVS player for its own
errors:

```
// set default values for ivsPlayer and ivsEvents
var ivsPlayer = {};
var ivsEvents = {};

// store references to the Amazon IVS Player and Amazon IVS Events
jwplayer(JW_PLAYER_DIV).on('providerPlayer', function (player) {
   ivsPlayer = player.ivsPlayer;
   ivsEvents = player.ivsEvents;
});

// set up event listening:
let playerEvent = ivsEvents.PlayerEventType;
ivsPlayer.addEventListener(playerEvent.ERROR, callback);
```

The callback will receive an object with the following fields:

| Field     | Description                                                                                                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`    | The error type. Corresponds to `ErrorType` events. For<br>more information, see [Amazon IVS Player SDK: Web Reference](https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.47.0/web/"). |
| `code`    | The error code.                                                                                                                                                                                                                              |
| `source`  | Source of the error.                                                                                                                                                                                                                         |
| `message` | Human readable error message.                                                                                                                                                                                                                |

## Content Security Policy

The Amazon IVS Provider API is configured to work on pages that use Content Security
Policy (CSP). See the section on “Working with Content Security Policy” in the [IVS Player SDK: Web Guide](web-content-security-policy.md "web-content-security-policy.md").

## Limitations

The Provider does not support casting. If you enabled casting in the JW Player
dashboard, you can disable it by setting `cast` to `null` when
calling `setup()`. This hides the casting button.
