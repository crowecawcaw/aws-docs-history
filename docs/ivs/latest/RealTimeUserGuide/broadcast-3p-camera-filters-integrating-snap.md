# Using Snap with the IVS Broadcast SDK

This document explains how to use Snap’s Camera Kit SDK with the IVS broadcast SDK.

## Web

This section assumes you are already familiar with [publishing and subscribing to video using
the Web Broadcast SDK](getting-started-pub-sub-web.md "getting-started-pub-sub-web.md").

To integrate Snap’s Camera Kit SDK with the IVS real-time streaming Web broadcast
SDK, you need to:

1. Install the Camera Kit SDK and Webpack. (Our example uses Webpack as the
   bundler, but you can use any bundler of your choice.)
2. Create `index.html`.
3. Add setup elements.
4. Create `index.css`.
5. Display and set up participants.
6. Display connected cameras and microphones.
7. Create a Camera Kit session.
8. Fetch lenses and populate lens selector.
9. Render the output from a Camera Kit session to a canvas.
10. Create a function to populate the Lens dropdown.
11. Provide Camera Kit with a media source for rendering and publish a
    `LocalStageStream`.
12. Create `package.json`.
13. Create a Webpack config file.
14. Set up an HTTPS server and test.

Each of these steps is described below.

### Install the Camera Kit

SDK and Webpack

In this example we use Webpack as our bundler; however, you can use any bundler.

```
npm i @snap/camera-kit webpack webpack-cli
```

### Create index.html

Next, create the HTML boilerplate and import the Web broadcast SDK as a script
tag. In the following code, be sure to replace `<SDK version>`
with the broadcast SDK version that you are using.

```
<!--
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */
-->
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Amazon IVS Real-Time Streaming Web Sample (HTML and JavaScript)</title>

  <!-- Fonts and Styling -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css" />
  <link rel="stylesheet" href="./index.css" />

  <!-- Stages in Broadcast SDK -->
  <script src="https://web-broadcast.live-video.net/<SDK version>/amazon-ivs-web-broadcast.js"></script>
</head>

<body>
  <!-- Introduction -->
  <header>
    <h1>Amazon IVS Real-Time Streaming Web Sample (HTML and JavaScript)</h1>

    <p>This sample is used to demonstrate basic HTML / JS usage. <b><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html">Use the AWS CLI</a></b> to create a <b>Stage</b> and a corresponding <b>ParticipantToken</b>. Multiple participants can load this page and put in their own tokens. You can <b><a href="https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-guides/stages#glossary" target="_blank">read more about stages in our public docs.</a></b></p>
  </header>
  <hr />

  <!-- Setup Controls -->

  <!-- Display Local Participants -->

  <!-- Lens Selector -->

  <!-- Display Remote Participants -->

  <!-- Load All Desired Scripts -->


```

### Add Setup

Elements

Create the HTML for selecting a camera, microphone, and lens and specifying a participant token:

```
<!-- Setup Controls -->
  <div class="row">
    <div class="column">
      <label for="video-devices">Select Camera</label>
      <select disabled id="video-devices">
        <option selected disabled>Choose Option</option>
      </select>
    </div>
    <div class="column">
      <label for="audio-devices">Select Microphone</label>
      <select disabled id="audio-devices">
        <option selected disabled>Choose Option</option>
      </select>
    </div>
    <div class="column">
      <label for="token">Participant Token</label>
      <input type="text" id="token" name="token" />
    </div>
    <div class="column" style="display: flex; margin-top: 1.5rem">
      <button class="button" style="margin: auto; width: 100%" id="join-button">Join Stage</button>
    </div>
    <div class="column" style="display: flex; margin-top: 1.5rem">
      <button class="button" style="margin: auto; width: 100%" id="leave-button">Leave Stage</button>
    </div>
  </div>
```

Add additional HTML beneath that to display camera feeds from local and remote
participants:

```
 <!-- Local Participant -->
<div class="row local-container">
    <canvas id="canvas"></canvas>

    <div class="column" id="local-media"></div>
    <div class="static-controls hidden" id="local-controls">
      <button class="button" id="mic-control">Mute Mic</button>
      <button class="button" id="camera-control">Mute Camera</button>
    </div>
  </div>


  <hr style="margin-top: 5rem"/>

  <!-- Remote Participants -->
  <div class="row">
    <div id="remote-media"></div>
  </div>
```

Load additional logic, including helper methods for setting up the camera and
the bundled JavaScript file. (Later in this section, you will create these
JavaScript files and bundle them into a single file, so you can import Camera
Kit as a module. The bundled JavaScript file will contain the logic for setting
up Camera Kit, applying a Lens, and publishing the camera feed with a Lens
applied to a stage.) Add closing tags for the `body` and `html` elements to complete the creation of `index.html`.

```
<!-- Load all Desired Scripts -->
  <script src="./helpers.js"></script>
  <script src="./media-devices.js"></script>
  <!-- <script type="module" src="./stages-simple.js"></script> -->
  <script src="./dist/bundle.js"></script>
</body>
</html>

```

### Create index.css

Create a CSS source file to style the page. We will not be going over this code so as to focus on the logic for managing a Stage and integrating with Snap’s Camera Kit SDK.

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

html,
body {
  margin: 2rem;
  box-sizing: border-box;
  height: 100vh;
  max-height: 100vh;
  display: flex;
  flex-direction: column;
}

hr {
  margin: 1rem 0;
}

table {
  display: table;
}

canvas {
  margin-bottom: 1rem;
  background: green;
}

video {
  margin-bottom: 1rem;
  background: black;
  max-width: 100%;
  max-height: 150px;
}

.log {
  flex: none;
  height: 300px;
}

.content {
  flex: 1 0 auto;
}

.button {
  display: block;
  margin: 0 auto;
}

.local-container {
  position: relative;
}

.static-controls {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  bottom: -4rem;
  text-align: center;
}

.static-controls button {
  display: inline-block;
}

.hidden {
  display: none;
}

.participant-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin: 1rem;
}

video {
  border: 0.5rem solid #555;
  border-radius: 0.5rem;
}
.placeholder {
  background-color: #333333;
  display: flex;
  text-align: center;
  margin-bottom: 1rem;
}
.placeholder span {
  margin: auto;
  color: white;
}
#local-media {
  display: inline-block;
  width: 100vw;
}

#local-media video {
  max-height: 300px;
}

#remote-media {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  width: 100%;
}

#lens-selector {
  width: 100%;
  margin-bottom: 1rem;
}
```

### Display and Set Up

Participants

Next, create `helpers.js`, which contains helper methods that you
will use to display and set up participants:

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

function setupParticipant({ isLocal, id }) {
  const groupId = isLocal ? 'local-media' : 'remote-media';
  const groupContainer = document.getElementById(groupId);

  const participantContainerId = isLocal ? 'local' : id;
  const participantContainer = createContainer(participantContainerId);
  const videoEl = createVideoEl(participantContainerId);

  participantContainer.appendChild(videoEl);
  groupContainer.appendChild(participantContainer);

  return videoEl;
}

function teardownParticipant({ isLocal, id }) {
  const groupId = isLocal ? 'local-media' : 'remote-media';
  const groupContainer = document.getElementById(groupId);
  const participantContainerId = isLocal ? 'local' : id;

  const participantDiv = document.getElementById(
    participantContainerId + '-container'
  );
  if (!participantDiv) {
    return;
  }
  groupContainer.removeChild(participantDiv);
}

function createVideoEl(id) {
  const videoEl = document.createElement('video');
  videoEl.id = id;
  videoEl.autoplay = true;
  videoEl.playsInline = true;
  videoEl.srcObject = new MediaStream();
  return videoEl;
}

function createContainer(id) {
  const participantContainer = document.createElement('div');
  participantContainer.classList = 'participant-container';
  participantContainer.id = id + '-container';

  return participantContainer;
}
```

### Display

Connected Cameras and Microphones

Next, create `media-devices.js`, which contains helper methods for
displaying cameras and microphones connected to your device:

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

/**
 * Returns an initial list of devices populated on the page selects
 */
async function initializeDeviceSelect() {
  const videoSelectEl = document.getElementById('video-devices');
  videoSelectEl.disabled = false;

  const { videoDevices, audioDevices } = await getDevices();
  videoDevices.forEach((device, index) => {
    videoSelectEl.options[index] = new Option(device.label, device.deviceId);
  });

  const audioSelectEl = document.getElementById('audio-devices');

  audioSelectEl.disabled = false;
  audioDevices.forEach((device, index) => {
    audioSelectEl.options[index] = new Option(device.label, device.deviceId);
  });
}

/**
 * Returns all devices available on the current device
 */
async function getDevices() {
  // Prevents issues on Safari/FF so devices are not blank
  await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

  const devices = await navigator.mediaDevices.enumerateDevices();
  // Get all video devices
  const videoDevices = devices.filter((d) => d.kind === 'videoinput');
  if (!videoDevices.length) {
    console.error('No video devices found.');
  }

  // Get all audio devices
  const audioDevices = devices.filter((d) => d.kind === 'audioinput');
  if (!audioDevices.length) {
    console.error('No audio devices found.');
  }

  return { videoDevices, audioDevices };
}

async function getCamera(deviceId) {
  // Use Max Width and Height
  return navigator.mediaDevices.getUserMedia({
    video: {
      deviceId: deviceId ? { exact: deviceId } : null,
    },
    audio: false,
  });
}

async function getMic(deviceId) {
  return navigator.mediaDevices.getUserMedia({
    video: false,
    audio: {
      deviceId: deviceId ? { exact: deviceId } : null,
    },
  });
}
```

### Create a Camera Kit

Session

Create `stages.js`, which contains the logic for applying a Lens to
the camera feed and publishing the feed to a stage. We recommend copying and pasting the following code block into `stages.js`. You can then review the code piece by piece to understand what’s going on in the following sections.

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

const {
  Stage,
  LocalStageStream,
  SubscribeType,
  StageEvents,
  ConnectionState,
  StreamType,
} = IVSBroadcastClient;

import {
  bootstrapCameraKit,
  createMediaStreamSource,
  Transform2D,
} from '@snap/camera-kit';

let cameraButton = document.getElementById('camera-control');
let micButton = document.getElementById('mic-control');
let joinButton = document.getElementById('join-button');
let leaveButton = document.getElementById('leave-button');

let controls = document.getElementById('local-controls');
let videoDevicesList = document.getElementById('video-devices');
let audioDevicesList = document.getElementById('audio-devices');

let lensSelector = document.getElementById('lens-selector');
let session;
let availableLenses = [];

// Stage management
let stage;
let joining = false;
let connected = false;
let localCamera;
let localMic;
let cameraStageStream;
let micStageStream;

const liveRenderTarget = document.getElementById('canvas');

const init = async () => {
  await initializeDeviceSelect();

  const cameraKit = await bootstrapCameraKit({
    apiToken: 'INSERT_YOUR_API_TOKEN_HERE',
  });

  session = await cameraKit.createSession({ liveRenderTarget });
  const { lenses } = await cameraKit.lensRepository.loadLensGroups([
    'INSERT_YOUR_LENS_GROUP_ID_HERE',
  ]);

  availableLenses = lenses;
  populateLensSelector(lenses);

  const snapStream = liveRenderTarget.captureStream();

  lensSelector.addEventListener('change', handleLensChange);
  lensSelector.disabled = true;
  cameraButton.addEventListener('click', () => {
    const isMuted = !cameraStageStream.isMuted;
    cameraStageStream.setMuted(isMuted);
    cameraButton.innerText = isMuted ? 'Show Camera' : 'Hide Camera';
  });

  micButton.addEventListener('click', () => {
    const isMuted = !micStageStream.isMuted;
    micStageStream.setMuted(isMuted);
    micButton.innerText = isMuted ? 'Unmute Mic' : 'Mute Mic';
  });

  joinButton.addEventListener('click', () => {
    joinStage(session, snapStream);
  });

  leaveButton.addEventListener('click', () => {
    leaveStage();
  });
};

async function setCameraKitSource(session, mediaStream) {
  const source = createMediaStreamSource(mediaStream);
  await session.setSource(source);
  source.setTransform(Transform2D.MirrorX);
  session.play();
}

const populateLensSelector = (lenses) => {
  lensSelector.innerHTML = '<option selected disabled>Choose Lens</option>';

  lenses.forEach((lens, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.text = lens.name || `Lens ${index + 1}`;
    lensSelector.appendChild(option);
  });
};

const handleLensChange = (event) => {
  const selectedIndex = parseInt(event.target.value);
  if (session && availableLenses[selectedIndex]) {
    session.applyLens(availableLenses[selectedIndex]);
  }
};

const joinStage = async (session, snapStream) => {
  if (connected || joining) {
    return;
  }
  joining = true;

  const token = document.getElementById('token').value;

  if (!token) {
    window.alert('Please enter a participant token');
    joining = false;
    return;
  }

  // Retrieve the User Media currently set on the page
  localCamera = await getCamera(videoDevicesList.value);
  localMic = await getMic(audioDevicesList.value);
  await setCameraKitSource(session, localCamera);

  // Create StageStreams for Audio and Video
  cameraStageStream = new LocalStageStream(snapStream.getVideoTracks()[0]);
  micStageStream = new LocalStageStream(localMic.getAudioTracks()[0]);

  const strategy = {
    stageStreamsToPublish() {
      return [cameraStageStream, micStageStream];
    },
    shouldPublishParticipant() {
      return true;
    },
    shouldSubscribeToParticipant() {
      return SubscribeType.AUDIO_VIDEO;
    },
  };

  stage = new Stage(token, strategy);

  // Other available events:
  // https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-guides/stages#events
  stage.on(StageEvents.STAGE_CONNECTION_STATE_CHANGED, (state) => {
    connected = state === ConnectionState.CONNECTED;

    if (connected) {
      joining = false;
      controls.classList.remove('hidden');
      lensSelector.disabled = false;
    } else {
      controls.classList.add('hidden');
      lensSelector.disabled = true;
    }
  });

  stage.on(StageEvents.STAGE_PARTICIPANT_JOINED, (participant) => {
    console.log('Participant Joined:', participant);
  });

  stage.on(
    StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED,
    (participant, streams) => {
      console.log('Participant Media Added: ', participant, streams);

      let streamsToDisplay = streams;

      if (participant.isLocal) {
        // Ensure to exclude local audio streams, otherwise echo will occur
        streamsToDisplay = streams.filter(
          (stream) => stream.streamType === StreamType.VIDEO
        );
      }

      const videoEl = setupParticipant(participant);
      streamsToDisplay.forEach((stream) =>
        videoEl.srcObject.addTrack(stream.mediaStreamTrack)
      );
    }
  );

  stage.on(StageEvents.STAGE_PARTICIPANT_LEFT, (participant) => {
    console.log('Participant Left: ', participant);
    teardownParticipant(participant);
  });

  try {
    await stage.join();
  } catch (err) {
    joining = false;
    connected = false;
    console.error(err.message);
  }
};

const leaveStage = async () => {
  stage.leave();

  joining = false;
  connected = false;

  cameraButton.innerText = 'Hide Camera';
  micButton.innerText = 'Mute Mic';
  controls.classList.add('hidden');
};

init();
```

In the first part of this file, we import the broadcast SDK and Camera Kit Web SDK and initialize the variables we will use with each SDK. We create a Camera Kit session by calling `createSession` after [bootstrapping the Camera Kit Web SDK](https://kit.snapchat.com/reference/CameraKit/web/0.7.0/index.html#bootstrapping-the-sdk "https://kit.snapchat.com/reference/CameraKit/web/0.7.0/index.html#bootstrapping-the-sdk"). Note that a canvas element object is passed to a session; this tells Camera Kit to render into that canvas.

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

const {
  Stage,
  LocalStageStream,
  SubscribeType,
  StageEvents,
  ConnectionState,
  StreamType,
} = IVSBroadcastClient;

import {
  bootstrapCameraKit,
  createMediaStreamSource,
  Transform2D,
} from '@snap/camera-kit';

let cameraButton = document.getElementById('camera-control');
let micButton = document.getElementById('mic-control');
let joinButton = document.getElementById('join-button');
let leaveButton = document.getElementById('leave-button');

let controls = document.getElementById('local-controls');
let videoDevicesList = document.getElementById('video-devices');
let audioDevicesList = document.getElementById('audio-devices');

let lensSelector = document.getElementById('lens-selector');
let session;
let availableLenses = [];

// Stage management
let stage;
let joining = false;
let connected = false;
let localCamera;
let localMic;
let cameraStageStream;
let micStageStream;

const liveRenderTarget = document.getElementById('canvas');

const init = async () => {
  await initializeDeviceSelect();

  const cameraKit = await bootstrapCameraKit({
    apiToken: 'INSERT_YOUR_API_TOKEN_HERE',
  });

  session = await cameraKit.createSession({ liveRenderTarget });
```

### Fetch Lenses and Populate Lens Selector

To fetch your Lenses, replace the placeholder for the Lens Group ID with your
own, which can be found in the [Camera Kit Developer Portal](https://camera-kit.snapchat.com/ "https://camera-kit.snapchat.com/"). Populate the Lens selection dropdown
using the `populateLensSelector()` function which we will create
later.

```
session = await cameraKit.createSession({ liveRenderTarget });
  const { lenses } = await cameraKit.lensRepository.loadLensGroups([
    'INSERT_YOUR_LENS_GROUP_ID_HERE',
  ]);

  availableLenses = lenses;
  populateLensSelector(lenses);
```

### Render the Output

from a Camera Kit Session to a Canvas

Use the [captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream "https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream") method to return a `MediaStream` of the
canvas’s contents. The canvas will contain a video stream of the camera feed
with a Lens applied. Also, add event listeners for buttons to mute the camera
and microphone as well as event listeners for joining and leaving a stage. In
the event listener for joining a stage, we pass in a Camera Kit session and the
`MediaStream` from the canvas so it can be published to a
stage.

```
const snapStream = liveRenderTarget.captureStream();

  lensSelector.addEventListener('change', handleLensChange);
  lensSelector.disabled = true;
  cameraButton.addEventListener('click', () => {
    const isMuted = !cameraStageStream.isMuted;
    cameraStageStream.setMuted(isMuted);
    cameraButton.innerText = isMuted ? 'Show Camera' : 'Hide Camera';
  });

  micButton.addEventListener('click', () => {
    const isMuted = !micStageStream.isMuted;
    micStageStream.setMuted(isMuted);
    micButton.innerText = isMuted ? 'Unmute Mic' : 'Mute Mic';
  });

  joinButton.addEventListener('click', () => {
    joinStage(session, snapStream);
  });

  leaveButton.addEventListener('click', () => {
    leaveStage();
  });
};
```

### Create a Function to Populate the Lens Dropdown

Create the following function to populate the **Lens** selector with the lenses fetched earlier. The **Lens** selector is a UI element on the page that lets you select from a list of lenses to apply to the camera feed. Also, create the `handleLensChange` callback function to apply the specified lens when it is selected from the **Lens** dropdown.

```
const populateLensSelector = (lenses) => {
  lensSelector.innerHTML = '<option selected disabled>Choose Lens</option>';

  lenses.forEach((lens, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.text = lens.name || `Lens ${index + 1}`;
    lensSelector.appendChild(option);
  });
};

const handleLensChange = (event) => {
  const selectedIndex = parseInt(event.target.value);
  if (session && availableLenses[selectedIndex]) {
    session.applyLens(availableLenses[selectedIndex]);
  }
};
```

### Provide Camera

Kit with a Media Source for Rendering and Publish a LocalStageStream

To publish a video stream with a Lens applied, create a function called
`setCameraKitSource` to pass in the `MediaStream`
captured from the canvas earlier. The `MediaStream` from the canvas
isn’t doing anything at the moment because we have not incorporated our local
camera feed yet. We can incorporate our local camera feed by calling the
`getCamera` helper method and assigning it to
`localCamera` . We can then pass in our local camera feed (via
`localCamera`) and the session object to
`setCameraKitSource`. The `setCameraKitSource`
function converts our local camera feed to a [source of media for CameraKit](https://docs.snap.com/camera-kit/integrate-sdk/web/web-configuration#creating-a-camerakitsource "https://docs.snap.com/camera-kit/integrate-sdk/web/web-configuration#creating-a-camerakitsource") by calling
`createMediaStreamSource`. The media source for
`CameraKit` is then [transformed](https://docs.snap.com/camera-kit/integrate-sdk/web/web-configuration#2d-transforms "https://docs.snap.com/camera-kit/integrate-sdk/web/web-configuration#2d-transforms") to mirror the front-facing camera. The Lens effect is
then applied to the media source and rendered to the output canvas by calling
`session.play()`.

With Lens now applied to the `MediaStream` captured from the
canvas, we can then proceed to publishing it to a stage. We do that by creating
a `LocalStageStream` with the video tracks from the
`MediaStream`. An instance of `LocalStageStream` can
then be passed in to a `StageStrategy` to be published.

```
async function setCameraKitSource(session, mediaStream) {
  const source = createMediaStreamSource(mediaStream);
  await session.setSource(source);
  source.setTransform(Transform2D.MirrorX);
  session.play();
}

const joinStage = async (session, snapStream) => {
  if (connected || joining) {
    return;
  }
  joining = true;

  const token = document.getElementById('token').value;

  if (!token) {
    window.alert('Please enter a participant token');
    joining = false;
    return;
  }

  // Retrieve the User Media currently set on the page
  localCamera = await getCamera(videoDevicesList.value);
  localMic = await getMic(audioDevicesList.value);
  await setCameraKitSource(session, localCamera);
  // Create StageStreams for Audio and Video
  // cameraStageStream = new LocalStageStream(localCamera.getVideoTracks()[0]);
  cameraStageStream = new LocalStageStream(snapStream.getVideoTracks()[0]);
  micStageStream = new LocalStageStream(localMic.getAudioTracks()[0]);

  const strategy = {
    stageStreamsToPublish() {
      return [cameraStageStream, micStageStream];
    },
    shouldPublishParticipant() {
      return true;
    },
    shouldSubscribeToParticipant() {
      return SubscribeType.AUDIO_VIDEO;
    },
  };
```

The remaining code below is for creating and managing our stage:

```
stage = new Stage(token, strategy);

  // Other available events:
  // https://aws.github.io/amazon-ivs-web-broadcast/docs/sdk-guides/stages#events

  stage.on(StageEvents.STAGE_CONNECTION_STATE_CHANGED, (state) => {
    connected = state === ConnectionState.CONNECTED;

    if (connected) {
      joining = false;
      controls.classList.remove('hidden');
    } else {
      controls.classList.add('hidden');
    }
  });

  stage.on(StageEvents.STAGE_PARTICIPANT_JOINED, (participant) => {
    console.log('Participant Joined:', participant);
  });

  stage.on(
    StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED,
    (participant, streams) => {
      console.log('Participant Media Added: ', participant, streams);

      let streamsToDisplay = streams;

      if (participant.isLocal) {
        // Ensure to exclude local audio streams, otherwise echo will occur
        streamsToDisplay = streams.filter(
          (stream) => stream.streamType === StreamType.VIDEO
        );
      }

      const videoEl = setupParticipant(participant);
      streamsToDisplay.forEach((stream) =>
        videoEl.srcObject.addTrack(stream.mediaStreamTrack)
      );
    }
  );

  stage.on(StageEvents.STAGE_PARTICIPANT_LEFT, (participant) => {
    console.log('Participant Left: ', participant);
    teardownParticipant(participant);
  });

  try {
    await stage.join();
  } catch (err) {
    joining = false;
    connected = false;
    console.error(err.message);
  }
};

const leaveStage = async () => {
  stage.leave();

  joining = false;
  connected = false;

  cameraButton.innerText = 'Hide Camera';
  micButton.innerText = 'Mute Mic';
  controls.classList.add('hidden');
};

init();
```

### Create package.json

Create `package.json` and add the following JSON configuration.
This file defines our dependencies and includes a script command for bundling
our code.

```
{
  "dependencies": {
    "@snap/camera-kit": "^0.10.0"
  },
  "name": "ivs-stages-with-snap-camerakit",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "build": "webpack"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "webpack": "^5.95.0",
    "webpack-cli": "^5.1.4"
  }
}
```

### Create a Webpack Config

File

Create `webpack.config.js` and add the following code. This bundles
the code we created thus far so that we can use the import statement to use
Camera Kit.

```
const path = require('path');
module.exports = {
  entry: ['./stage.js'],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

Finally, run `npm run build` to bundle your JavaScript as
defined in the Webpack config file. For testing purposes, you can then serve HTML and JavaScript from your local computer. In this example, we use Python’s `http.server` module.

### Set Up an HTTPS Server and Test

To test our code, we need to set up an HTTPS server. Using an HTTPS server for local development and testing of your web app's integration with the Snap Camera Kit SDK will help avoid CORS (Cross-Origin Resource Sharing) issues.

Open a terminal and navigate to the directory where you created all the code
up to this point. Run the following command to generate a self-signed SSL/TLS
certificate and private key:

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

This creates two files: `key.pem` (the private key) and
`cert.pem` (the self-signed certificate). Create a new Python
file named `https_server.py` and add the following code:

```
import http.server
import ssl

# Set the directory to serve files from
DIRECTORY = '.'

# Create the HTTPS server
server_address = ('', 4443)
httpd = http.server.HTTPServer(
    server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the socket with SSL/TLS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f'Starting HTTPS server on https://localhost:4443, serving {DIRECTORY}')
httpd.serve_forever()

```

Open a terminal, navigate to the directory where you created the
`https_server.py` file, and run the following command:

```
python3 https_server.py
```

This starts the HTTPS server on https://localhost:4443, serving files from the
current directory. Make sure that the `cert.pem` and
`key.pem` files are in the same directory as the
`https_server.py` file.

Open your browser and navigate to https://localhost:4443. Since this is a
self-signed SSL/TLS certificate, it will not be trusted by your web browser, so
you will get a warning. Since this is only for testing purposes, you can bypass
the warning. You should then see the AR effect for the Snap Lens you specified
earlier applied to your camera feed on screen.

Note that this setup using Python's built-in `http.server` and `ssl` modules is
suitable for local development and testing purposes, but it is not recommended
for a production environment. The self-signed SSL/TLS certificate used in this
setup is not trusted by web browsers and other clients, which means users will
encounter security warnings when accessing the server. Also, although we use
Python’s built-in http.server and ssl modules in this example, you may choose to
use another HTTPS server solution.

## Android

To integrate Snap’s Camera Kit SDK with the IVS Android broadcast SDK, you must
install the Camera Kit SDK, initialize a Camera Kit session, apply a Lens and feed
the Camera Kit session’s output to the custom-image input source.

To install the Camera Kit SDK, add the following to your module’s
`build.gradle` file. Replace `$cameraKitVersion` with the
[latest Camera Kit SDK version](https://docs.snap.com/camera-kit/integrate-sdk/mobile/changelog-mobile "https://docs.snap.com/camera-kit/integrate-sdk/mobile/changelog-mobile").

```
implementation "com.snap.camerakit:camerakit:$cameraKitVersion"
```

Initialize and obtain a `cameraKitSession`. Camera Kit also provides a
convenient wrapper for Android’s [CameraX](https://developer.android.com/media/camera/camerax "https://developer.android.com/media/camera/camerax") APIs, so
you don’t have to write complicated logic to use CameraX with Camera Kit. You can
use the `CameraXImageProcessorSource` object as a [Source](https://snapchat.github.io/camera-kit-reference/api/android/latest/-camera-kit/com.snap.camerakit/-source/index.html "https://snapchat.github.io/camera-kit-reference/api/android/latest/-camera-kit/com.snap.camerakit/-source/index.html") for [ImageProcessor](https://snapchat.github.io/camera-kit-reference/api/android/latest/-camera-kit/com.snap.camerakit/-image-processor/index.html "https://snapchat.github.io/camera-kit-reference/api/android/latest/-camera-kit/com.snap.camerakit/-image-processor/index.html"), which allows you to start camera-preview streaming
frames.

```
 protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Camera Kit support implementation of ImageProcessor that is backed by CameraX library:
        // https://developer.android.com/training/camerax
        CameraXImageProcessorSource imageProcessorSource = new CameraXImageProcessorSource(
            this /*context*/, this /*lifecycleOwner*/
        );
        imageProcessorSource.startPreview(true /*cameraFacingFront*/);

        cameraKitSession = Sessions.newBuilder(this)
                .imageProcessorSource(imageProcessorSource)
                .attachTo(findViewById(R.id.camerakit_stub))
                .build();
    }
```

### Fetch and Apply Lenses

You can
configure Lenses and their ordering in the carousel on the [Camera Kit Developer
Portal](https://camera-kit.snapchat.com/ "https://camera-kit.snapchat.com/"):

```
// Fetch lenses from repository and apply them
 // Replace LENS_GROUP_ID with Lens Group ID from https://camera-kit.snapchat.com
cameraKitSession.getLenses().getRepository().get(new Available(LENS_GROUP_ID), available -> {
     Log.d(TAG, "Available lenses: " + available);
     Lenses.whenHasFirst(available, lens -> cameraKitSession.getLenses().getProcessor().apply(lens, result -> {
          Log.d(TAG,  "Apply lens [" + lens + "] success: " + result);
      }));
});
```

To broadcast, send processed frames to the underlying `Surface` of
a custom image source. Use a `DeviceDiscovery` object and create a
`CustomImageSource` to return a `SurfaceSource`. You
can then render the output from a `CameraKit` session to the
underlying `Surface` provided by the
`SurfaceSource`.

```
val publishStreams = ArrayList<LocalStageStream>()

val deviceDiscovery = DeviceDiscovery(applicationContext)
val customSource = deviceDiscovery.createImageInputSource(BroadcastConfiguration.Vec2(720f, 1280f))

cameraKitSession.processor.connectOutput(outputFrom(customSource.inputSurface))
val customStream = ImageLocalStageStream(customSource)

// After rendering the output from a Camera Kit session to the Surface, you can
// then return it as a LocalStageStream to be published by the Broadcast SDK
val customStream: ImageLocalStageStream = ImageLocalStageStream(surfaceSource)
publishStreams.add(customStream)

@Override
fun stageStreamsToPublishForParticipant(stage: Stage, participantInfo: ParticipantInfo): List<LocalStageStream> = publishStreams
```
