# Using Background Replacement with the IVS Broadcast SDK

Background replacement is a type of camera filter that enables live-stream creators to
change their backgrounds. As shown in the following diagram, replacing your background
involves:

1. Getting a camera image from the live camera feed.
2. Segmenting it into foreground and background components using Google ML
   Kit.
3. Combining the resulting segmentation mask with a custom background
   image.
4. Passing it to a Custom Image Source for broadcast.

![Workflow for implementing background replacement.](images/3P_Camera_Filters_Background_Replacement.png)

## Web

This section assumes you are already familiar with [publishing and subscribing to video using the Web Broadcast
SDK](getting-started-pub-sub-web.md "getting-started-pub-sub-web.md").

To replace the background of a live stream with a custom image, use the [selfie segmentation model](https://developers.google.com/mediapipe/solutions/vision/image_segmenter#selfie-model "https://developers.google.com/mediapipe/solutions/vision/image_segmenter#selfie-model") with [MediaPipe Image Segmenter](https://developers.google.com/mediapipe/solutions/vision/image_segmenter "https://developers.google.com/mediapipe/solutions/vision/image_segmenter"). This is a machine-learning model that
identifies which pixels in the video frame are in the foreground or background.
You can then use the results from the model to replace the background of a live
stream, by copying foreground pixels from the video feed to a custom image
representing the new background.

To integrate background replacement with the IVS real-time streaming Web broadcast
SDK, you need to:

1. Install MediaPipe and Webpack. (Our example uses Webpack as the bundler,
   but you can use any bundler of your choice.)
2. Create `index.html`.
3. Add media elements.
4. Add a script tag.
5. Create `app.js`.
6. Load a custom background image.
7. Create an instance of `ImageSegmenter`.
8. Render the video feed to a canvas.
9. Create background replacement logic.
10. Create Webpack config File.
11. Bundle Your JavaScript file.

### Install MediaPipe and Webpack

To start, install the `@mediapipe/tasks-vision` and
`webpack` npm packages. The example below uses Webpack as a
JavaScript bundler; you can use a different bundler if preferred.

```
npm i @mediapipe/tasks-vision webpack webpack-cli
```

Make sure to also update your `package.json` to specify
`webpack` as your build script:

```
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
```

### Create index.html

Next, create the HTML boilerplate and import the Web broadcast SDK as a script
tag. In the following code, be sure to replace `<SDK version>`
with the broadcast SDK version that you are using.

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Import the SDK -->
  <script src="https://web-broadcast.live-video.net/<SDK version>/amazon-ivs-web-broadcast.js"></script>
</head>

<body>

</body>
</html>
```

### Add Media Elements

Next, add a video element and two canvas elements within the body tag. The
video element will contain your live camera feed and will be used as input to
the MediaPipe Image Segmenter. The first canvas element will be used to render a
preview of the feed that will be broadcast. The second canvas element will be
used to render the custom image that will be used as a background. Since the
second canvas with the custom image is used only as a source to programmatically
copy pixels from it to the final canvas, it is hidden from view.

```
<div class="row local-container">
      <video id="webcam" autoplay style="display: none"></video>
    </div>
    <div class="row local-container">
      <canvas id="canvas" width="640px" height="480px"></canvas>

      <div class="column" id="local-media"></div>
      <div class="static-controls hidden" id="local-controls">
        <button class="button" id="mic-control">Mute Mic</button>
        <button class="button" id="camera-control">Mute Camera</button>
      </div>
    </div>
    <div class="row local-container">
      <canvas id="background" width="640px" height="480px" style="display: none"></canvas>
    </div>
```

### Add a Script Tag

Add a script tag to load a bundled JavaScript file that will contain the code
to do the background replacement and publish it to a stage:

```
<script src="./dist/bundle.js"></script>
```

### Create app.js

Next, create a JavaScript file to get the element objects for the canvas and
video elements that were created in the HTML page. Import the
`ImageSegmenter` and `FilesetResolver` modules. The
`ImageSegmenter` module will be used to perform the segmentation
task.

```
const canvasElement = document.getElementById("canvas");
const background = document.getElementById("background");
const canvasCtx = canvasElement.getContext("2d");
const backgroundCtx = background.getContext("2d");
const video = document.getElementById("webcam");

import { ImageSegmenter, FilesetResolver } from "@mediapipe/tasks-vision";
```

Next, create a function called `init()` to retrieve the MediaStream
from the user’s camera and invoke a callback function each time a camera frame
finishes loading. Add event listeners for the buttons to join and leave a
stage.

Note that when joining a stage, we pass in a variable named
`segmentationStream`. This is a video stream that is captured
from a canvas element, containing a foreground image overlaid on the custom
image representing the background. Later, this custom stream will be used to
create an instance of a `LocalStageStream`, which can be published to
a stage.

```
const init = async () => {
  await initializeDeviceSelect();

  cameraButton.addEventListener("click", () => {
    const isMuted = !cameraStageStream.isMuted;
    cameraStageStream.setMuted(isMuted);
    cameraButton.innerText = isMuted ? "Show Camera" : "Hide Camera";
  });

  micButton.addEventListener("click", () => {
    const isMuted = !micStageStream.isMuted;
    micStageStream.setMuted(isMuted);
    micButton.innerText = isMuted ? "Unmute Mic" : "Mute Mic";
  });

  localCamera = await getCamera(videoDevicesList.value);
  const segmentationStream = canvasElement.captureStream();

  joinButton.addEventListener("click", () => {
    joinStage(segmentationStream);
  });

  leaveButton.addEventListener("click", () => {
    leaveStage();
  });
};
```

### Load a Custom Background Image

At the bottom of the `init` function, add code to call a function
named `initBackgroundCanvas`, which loads a custom image from a local
file and renders it onto a canvas. We will define this function in the next
step. Assign the `MediaStream` retrieved from the user’s camera to
the video object. Later, this video object will be passed to the Image
Segmenter. Also, set a function named `renderVideoToCanvas` as the
callback function to invoke whenever a video frame has finished loading. We will
define this function in a later step.

```
initBackgroundCanvas();

  video.srcObject = localCamera;
  video.addEventListener("loadeddata", renderVideoToCanvas);
```

Let’s implement the `initBackgroundCanvas` function, which loads an
image from a local file. In this example, we use an image of a beach as the
custom background. The canvas containing the custom image will be hidden from
display, as you will merge it with the foreground pixels from the canvas element
containing the camera feed.

```
const initBackgroundCanvas = () => {
  let img = new Image();
  img.src = "beach.jpg";

  img.onload = () => {
    backgroundCtx.clearRect(0, 0, canvas.width, canvas.height);
    backgroundCtx.drawImage(img, 0, 0);
  };
};
```

### Create an Instance of ImageSegmenter

Next, create an
instance of `ImageSegmenter`, which will segment the image and return the
result as a mask. When creating an instance of an `ImageSegmenter`, you will
use the [selfie segmentation model](https://developers.google.com/mediapipe/solutions/vision/image_segmenter#selfie-model "https://developers.google.com/mediapipe/solutions/vision/image_segmenter#selfie-model").

```
const createImageSegmenter = async () => {
  const audio = await FilesetResolver.forVisionTasks("https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.2/wasm");

  imageSegmenter = await ImageSegmenter.createFromOptions(audio, {
    baseOptions: {
      modelAssetPath: "https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/latest/selfie_segmenter.tflite",
      delegate: "GPU",
    },
    runningMode: "VIDEO",
    outputCategoryMask: true,
  });
};
```

### Render the Video Feed to a Canvas

Next, create the function that renders the video feed to the other canvas
element. We need to render the video feed to a canvas so we can extract the
foreground pixels from it using the Canvas 2D API. While doing this, we also
will pass a video frame to our instance of `ImageSegmenter`, using
the [segmentforVideo](https://developers.google.com/mediapipe/api/solutions/js/tasks-vision.imagesegmenter#imagesegmentersegmentforvideo "https://developers.google.com/mediapipe/api/solutions/js/tasks-vision.imagesegmenter#imagesegmentersegmentforvideo") method to segment the foreground from the
background in the video frame. When the [segmentforVideo](https://developers.google.com/mediapipe/api/solutions/js/tasks-vision.imagesegmenter#imagesegmentersegmentforvideo "https://developers.google.com/mediapipe/api/solutions/js/tasks-vision.imagesegmenter#imagesegmentersegmentforvideo") method returns, it invokes our custom callback
function, `replaceBackground`, for doing the background
replacement.

```
const renderVideoToCanvas = async () => {
  if (video.currentTime === lastWebcamTime) {
    window.requestAnimationFrame(renderVideoToCanvas);
    return;
  }
  lastWebcamTime = video.currentTime;
  canvasCtx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

  if (imageSegmenter === undefined) {
    return;
  }

  let startTimeMs = performance.now();

  imageSegmenter.segmentForVideo(video, startTimeMs, replaceBackground);
};
```

### Create Background Replacement Logic

Create the `replaceBackground` function, which merges the custom
background image with the foreground from the camera feed to replace the
background. The function first retrieves the underlying pixel data of the custom
background image and the video feed from the two canvas elements created
earlier. It then iterates through the mask provided by
`ImageSegmenter`, which indicates which pixels are in the
foreground. As it iterates through the mask, it selectively copies pixels that
contain the user’s camera feed to the corresponding background pixel data. Once
that is done, it converts the final pixel data with the foreground copied on to
the background and draws it to a Canvas.

```
function replaceBackground(result) {
  let imageData = canvasCtx.getImageData(0, 0, video.videoWidth, video.videoHeight).data;
  let backgroundData = backgroundCtx.getImageData(0, 0, video.videoWidth, video.videoHeight).data;
  const mask = result.categoryMask.getAsFloat32Array();
  let j = 0;

  for (let i = 0; i < mask.length; ++i) {
    const maskVal = Math.round(mask[i] * 255.0);

    j += 4;
  // Only copy pixels on to the background image if the mask indicates they are in the foreground
    if (maskVal < 255) {
      backgroundData[j] = imageData[j];
      backgroundData[j + 1] = imageData[j + 1];
      backgroundData[j + 2] = imageData[j + 2];
      backgroundData[j + 3] = imageData[j + 3];
    }
  }

 // Convert the pixel data to a format suitable to be drawn to a canvas
  const uint8Array = new Uint8ClampedArray(backgroundData.buffer);
  const dataNew = new ImageData(uint8Array, video.videoWidth, video.videoHeight);
  canvasCtx.putImageData(dataNew, 0, 0);
  window.requestAnimationFrame(renderVideoToCanvas);
}
```

For reference, here is the complete `app.js` file containing all
the logic above:

```
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: Apache-2.0 */

// All helpers are expose on 'media-devices.js' and 'dom.js'
const { setupParticipant } = window;

const { Stage, LocalStageStream, SubscribeType, StageEvents, ConnectionState, StreamType } = IVSBroadcastClient;
const canvasElement = document.getElementById("canvas");
const background = document.getElementById("background");
const canvasCtx = canvasElement.getContext("2d");
const backgroundCtx = background.getContext("2d");
const video = document.getElementById("webcam");

import { ImageSegmenter, FilesetResolver } from "@mediapipe/tasks-vision";

let cameraButton = document.getElementById("camera-control");
let micButton = document.getElementById("mic-control");
let joinButton = document.getElementById("join-button");
let leaveButton = document.getElementById("leave-button");

let controls = document.getElementById("local-controls");
let audioDevicesList = document.getElementById("audio-devices");
let videoDevicesList = document.getElementById("video-devices");

// Stage management
let stage;
let joining = false;
let connected = false;
let localCamera;
let localMic;
let cameraStageStream;
let micStageStream;
let imageSegmenter;
let lastWebcamTime = -1;

const init = async () => {
  await initializeDeviceSelect();

  cameraButton.addEventListener("click", () => {
    const isMuted = !cameraStageStream.isMuted;
    cameraStageStream.setMuted(isMuted);
    cameraButton.innerText = isMuted ? "Show Camera" : "Hide Camera";
  });

  micButton.addEventListener("click", () => {
    const isMuted = !micStageStream.isMuted;
    micStageStream.setMuted(isMuted);
    micButton.innerText = isMuted ? "Unmute Mic" : "Mute Mic";
  });

  localCamera = await getCamera(videoDevicesList.value);
  const segmentationStream = canvasElement.captureStream();

  joinButton.addEventListener("click", () => {
    joinStage(segmentationStream);
  });

  leaveButton.addEventListener("click", () => {
    leaveStage();
  });

  initBackgroundCanvas();

  video.srcObject = localCamera;
  video.addEventListener("loadeddata", renderVideoToCanvas);
};

const joinStage = async (segmentationStream) => {
  if (connected || joining) {
    return;
  }
  joining = true;

  const token = document.getElementById("token").value;

  if (!token) {
    window.alert("Please enter a participant token");
    joining = false;
    return;
  }

  // Retrieve the User Media currently set on the page
  localMic = await getMic(audioDevicesList.value);

  cameraStageStream = new LocalStageStream(segmentationStream.getVideoTracks()[0]);
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
      controls.classList.remove("hidden");
    } else {
      controls.classList.add("hidden");
    }
  });

  stage.on(StageEvents.STAGE_PARTICIPANT_JOINED, (participant) => {
    console.log("Participant Joined:", participant);
  });

  stage.on(StageEvents.STAGE_PARTICIPANT_STREAMS_ADDED, (participant, streams) => {
    console.log("Participant Media Added: ", participant, streams);

    let streamsToDisplay = streams;

    if (participant.isLocal) {
      // Ensure to exclude local audio streams, otherwise echo will occur
      streamsToDisplay = streams.filter((stream) => stream.streamType === StreamType.VIDEO);
    }

    const videoEl = setupParticipant(participant);
    streamsToDisplay.forEach((stream) => videoEl.srcObject.addTrack(stream.mediaStreamTrack));
  });

  stage.on(StageEvents.STAGE_PARTICIPANT_LEFT, (participant) => {
    console.log("Participant Left: ", participant);
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

  cameraButton.innerText = "Hide Camera";
  micButton.innerText = "Mute Mic";
  controls.classList.add("hidden");
};

function replaceBackground(result) {
  let imageData = canvasCtx.getImageData(0, 0, video.videoWidth, video.videoHeight).data;
  let backgroundData = backgroundCtx.getImageData(0, 0, video.videoWidth, video.videoHeight).data;
  const mask = result.categoryMask.getAsFloat32Array();
  let j = 0;

  for (let i = 0; i < mask.length; ++i) {
    const maskVal = Math.round(mask[i] * 255.0);

    j += 4;
    if (maskVal < 255) {
      backgroundData[j] = imageData[j];
      backgroundData[j + 1] = imageData[j + 1];
      backgroundData[j + 2] = imageData[j + 2];
      backgroundData[j + 3] = imageData[j + 3];
    }
  }
  const uint8Array = new Uint8ClampedArray(backgroundData.buffer);
  const dataNew = new ImageData(uint8Array, video.videoWidth, video.videoHeight);
  canvasCtx.putImageData(dataNew, 0, 0);
  window.requestAnimationFrame(renderVideoToCanvas);
}

const createImageSegmenter = async () => {
  const audio = await FilesetResolver.forVisionTasks("https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.2/wasm");

  imageSegmenter = await ImageSegmenter.createFromOptions(audio, {
    baseOptions: {
      modelAssetPath: "https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/latest/selfie_segmenter.tflite",
      delegate: "GPU",
    },
    runningMode: "VIDEO",
    outputCategoryMask: true,
  });
};

const renderVideoToCanvas = async () => {
  if (video.currentTime === lastWebcamTime) {
    window.requestAnimationFrame(renderVideoToCanvas);
    return;
  }
  lastWebcamTime = video.currentTime;
  canvasCtx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

  if (imageSegmenter === undefined) {
    return;
  }

  let startTimeMs = performance.now();

  imageSegmenter.segmentForVideo(video, startTimeMs, replaceBackground);
};

const initBackgroundCanvas = () => {
  let img = new Image();
  img.src = "beach.jpg";

  img.onload = () => {
    backgroundCtx.clearRect(0, 0, canvas.width, canvas.height);
    backgroundCtx.drawImage(img, 0, 0);
  };
};

createImageSegmenter();
init();
```

### Create a Webpack Config File

Add this configuration to your Webpack config file to bundle
`app.js`, so the import calls will work:

```
const path = require("path");
module.exports = {
  entry: ["./app.js"],
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
};
```

### Bundle Your JavaScript files

```
npm run build
```

Start a simple HTTP server from the directory containing
`index.html` and open `localhost:8000` to see the
result:

```
python3 -m http.server -d ./
```

## Android

To replace the background in your live stream, you can use the selfie
segmentation API of [Google
ML Kit](https://developers.google.com/ml-kit/vision/selfie-segmentation "https://developers.google.com/ml-kit/vision/selfie-segmentation"). The selfie segmentation API accepts a camera image as input
and returns a mask that provides a confidence score for each pixel of the image,
indicating whether it was in the foreground or the background. Based on the
confidence score, you can then retrieve the corresponding pixel color from
either the background image or the foreground image. This process continues
until all confidence scores in the mask have been examined. The result is a new
array of pixel colors containing foreground pixels combined with pixels from the
background image.

To integrate background replacement with the IVS real-time streaming Android
broadcast SDK, you need to:

1. Install CameraX libraries and the Google ML kit.
2. Initialize boilerplate variables.
3. Create a custom image source.
4. Manage camera frames.
5. Pass camera frames to Google ML Kit.
6. Overlay camera frame foreground onto your custom background.
7. Feed the new image to a custom image source.

### Install CameraX Libraries and Google ML Kit

To extract images from the live camera feed, use Android’s CameraX library. To
install the CameraX library and Google ML Kit, add the following to your
module’s `build.gradle` file. Replace `${camerax_version}`
and `${google_ml_kit_version}` with the latest version of the [CameraX](https://developer.android.com/jetpack/androidx/releases/camera "https://developer.android.com/jetpack/androidx/releases/camera") and [Google ML Kit](https://developers.google.com/ml-kit/vision/selfie-segmentation/android "https://developers.google.com/ml-kit/vision/selfie-segmentation/android") libraries, respectively.

```
implementation "com.google.mlkit:segmentation-selfie:${google_ml_kit_version}"
implementation "androidx.camera:camera-core:${camerax_version}"
implementation "androidx.camera:camera-lifecycle:${camerax_version}"
```

Import the following libraries:

```
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.ImageProxy
import androidx.camera.lifecycle.ProcessCameraProvider
import com.google.mlkit.vision.segmentation.selfie.SelfieSegmenterOptions
```

### Initialize Boilerplate Variables

Initialize an instance of `ImageAnalysis` and an instance of an
`ExecutorService`:

```
private lateinit var binding: ActivityMainBinding
private lateinit var cameraExecutor: ExecutorService
private var analysisUseCase: ImageAnalysis? = null
```

Initialize a
Segmenter instance in [STREAM_MODE](https://developers.google.com/ml-kit/vision/selfie-segmentation/android#detector_mode "https://developers.google.com/ml-kit/vision/selfie-segmentation/android#detector_mode"):

```
private val options =
        SelfieSegmenterOptions.Builder()
            .setDetectorMode(SelfieSegmenterOptions.STREAM_MODE)
            .build()

private val segmenter = Segmentation.getClient(options)
```

### Create a Custom Image Source

In the `onCreate` method of your activity, create an instance of a
`DeviceDiscovery` object and create a custom image source. The
`Surface` provided by the Custom Image Source will receive the
final image, with the foreground overlaid on a custom background image. You will
then create an instance of a `ImageLocalStageStream` using the Custom
Image Source. The instance of a `ImageLocalStageStream` (named
`filterStream` in this example) can then be published to a stage.
See the [IVS Android Broadcast SDK Guide](broadcast-android.md "broadcast-android.md")
for instructions on setting up a stage. Finally, also create a thread that will
be used to manage the camera.

```
var deviceDiscovery = DeviceDiscovery(applicationContext)
var customSource = deviceDiscovery.createImageInputSource( BroadcastConfiguration.Vec2(
720F, 1280F
))
var surface: Surface = customSource.inputSurface
var filterStream = ImageLocalStageStream(customSource)

cameraExecutor = Executors.newSingleThreadExecutor()
```

### Manage Camera Frames

Next, create a function to initialize the camera. This function uses the
CameraX library to extract images from the live camera feed. First, you create
an instance of a `ProcessCameraProvider` called
`cameraProviderFuture`. This object represents a future result of
obtaining a camera provider. Then you load an image from your project as a
bitmap. This example uses an image of a beach as a background, but it can be any
image you want.

You then add a listener to `cameraProviderFuture`. This listener is
notified when the camera becomes available or if an error occurs during the
process of obtaining a camera provider.

```
private fun startCamera(surface: Surface) {
        val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
        val imageResource = R.drawable.beach
        val bgBitmap: Bitmap = BitmapFactory.decodeResource(resources, imageResource)
        var resultBitmap: Bitmap;


        cameraProviderFuture.addListener({
            val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()


                if (mediaImage != null) {
                    val inputImage =
                        InputImage.fromMediaImage(mediaImage, imageProxy.imageInfo.rotationDegrees)

                            resultBitmap = overlayForeground(mask, maskWidth, maskHeight, inputBitmap, backgroundPixels)
                            canvas = surface.lockCanvas(null);
                            canvas.drawBitmap(resultBitmap, 0f, 0f, null)

                            surface.unlockCanvasAndPost(canvas);

                        }
                        .addOnFailureListener { exception ->
                            Log.d("App", exception.message!!)
                        }
                        .addOnCompleteListener {
                            imageProxy.close()
                        }

                }
            };

            val cameraSelector = CameraSelector.DEFAULT_FRONT_CAMERA

            try {
                // Unbind use cases before rebinding
                cameraProvider.unbindAll()

                // Bind use cases to camera
                cameraProvider.bindToLifecycle(this, cameraSelector, analysisUseCase)

            } catch(exc: Exception) {
                Log.e(TAG, "Use case binding failed", exc)
            }

        }, ContextCompat.getMainExecutor(this))
    }
```

Within the listener, create `ImageAnalysis.Builder` to access each
individual frame from the live camera feed. Set the back-pressure strategy to
`STRATEGY_KEEP_ONLY_LATEST`. This guarantees that only one camera
frame at a time is delivered for processing. Convert each individual camera
frame to a bitmap, so you can extract its pixels to later combine it with the
custom background image.

```
val imageAnalyzer = ImageAnalysis.Builder()
analysisUseCase = imageAnalyzer
    .setTargetResolution(Size(360, 640))
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .build()

analysisUseCase?.setAnalyzer(cameraExecutor) { imageProxy: ImageProxy ->
    val mediaImage = imageProxy.image
    val tempBitmap = imageProxy.toBitmap();
    val inputBitmap = tempBitmap.rotate(imageProxy.imageInfo.rotationDegrees.toFloat())
```

### Pass Camera Frames to Google ML Kit

Next, create an `InputImage` and pass it to the instance of
Segmenter for processing. An `InputImage` can be created from an
`ImageProxy` provided by the instance of
`ImageAnalysis`. Once an `InputImage` is provided to
Segmenter, it returns a mask with confidence scores indicating the likelihood of
a pixel being in the foreground or background. This mask also provides width and
height properties, which you will use to create a new array containing the
background pixels from the custom background image loaded earlier.

```
if (mediaImage != null) {
        val inputImage =
            InputImage.fromMediaImag


segmenter.process(inputImage)
    .addOnSuccessListener { segmentationMask ->
        val mask = segmentationMask.buffer
        val maskWidth = segmentationMask.width
        val maskHeight = segmentationMask.height
        val backgroundPixels = IntArray(maskWidth * maskHeight)
        bgBitmap.getPixels(backgroundPixels, 0, maskWidth, 0, 0, maskWidth, maskHeight)
```

### Overlay the Camera Frame Foreground onto Your Custom

Background

With the mask containing the confidence scores, the camera frame as a bitmap,
and the color pixels from the custom background image, you have everything you
need to overlay the foreground onto your custom background. The
`overlayForeground` function is then called with the following
parameters:

```
resultBitmap = overlayForeground(mask, maskWidth, maskHeight, inputBitmap, backgroundPixels)
```

This function iterates through the mask and checks the confidence values to
determine whether to get the corresponding pixel color from the background image
or the camera frame. If the confidence value indicates that a pixel in the mask
is most likely in the background, it will get the corresponding pixel color from
the background image; otherwise, it will get the corresponding pixel color from
the camera frame to build the foreground. Once the function finishes iterating
through the mask, a new bitmap is created using the new array of color pixels
and returned. This new bitmap contains the foreground overlaid on the custom
background.

```
private fun overlayForeground(
        byteBuffer: ByteBuffer,
        maskWidth: Int,
        maskHeight: Int,
        cameraBitmap: Bitmap,
        backgroundPixels: IntArray
    ): Bitmap {
        @ColorInt val colors = IntArray(maskWidth * maskHeight)
        val cameraPixels = IntArray(maskWidth * maskHeight)

        cameraBitmap.getPixels(cameraPixels, 0, maskWidth, 0, 0, maskWidth, maskHeight)

        for (i in 0 until maskWidth * maskHeight) {
            val backgroundLikelihood: Float = 1 - byteBuffer.getFloat()

            // Apply the virtual background to the color if it's not part of the foreground
            if (backgroundLikelihood > 0.9) {
                // Get the corresponding pixel color from the background image
                // Set the color in the mask based on the background image pixel color
                colors[i] = backgroundPixels.get(i)
            } else {
                // Get the corresponding pixel color from the camera frame
                // Set the color in the mask based on the camera image pixel color
                colors[i] = cameraPixels.get(i)
            }
        }

        return Bitmap.createBitmap(
            colors, maskWidth, maskHeight, Bitmap.Config.ARGB_8888
        )
    }
```

### Feed the New Image to a Custom Image Source

You can then write the new bitmap to the `Surface` provided by a
custom image source. This will broadcast it to your stage.

```
resultBitmap = overlayForeground(mask, inputBitmap, mutableBitmap, bgBitmap)
canvas = surface.lockCanvas(null);
canvas.drawBitmap(resultBitmap, 0f, 0f, null)
```

Here is the complete function for getting the camera frames, passing it to
Segmenter, and overlaying it on the background:

```
@androidx.annotation.OptIn(androidx.camera.core.ExperimentalGetImage::class)
    private fun startCamera(surface: Surface) {
        val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
        val imageResource = R.drawable.clouds
        val bgBitmap: Bitmap = BitmapFactory.decodeResource(resources, imageResource)
        var resultBitmap: Bitmap;

        cameraProviderFuture.addListener({
            // Used to bind the lifecycle of cameras to the lifecycle owner
            val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()

            val imageAnalyzer = ImageAnalysis.Builder()
            analysisUseCase = imageAnalyzer
                .setTargetResolution(Size(720, 1280))
                .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
                .build()

            analysisUseCase!!.setAnalyzer(cameraExecutor) { imageProxy: ImageProxy ->
                val mediaImage = imageProxy.image
                val tempBitmap = imageProxy.toBitmap();
                val inputBitmap = tempBitmap.rotate(imageProxy.imageInfo.rotationDegrees.toFloat())

                if (mediaImage != null) {
                    val inputImage =
                        InputImage.fromMediaImage(mediaImage, imageProxy.imageInfo.rotationDegrees)

                    segmenter.process(inputImage)
                        .addOnSuccessListener { segmentationMask ->
                            val mask = segmentationMask.buffer
                            val maskWidth = segmentationMask.width
                            val maskHeight = segmentationMask.height
                            val backgroundPixels = IntArray(maskWidth * maskHeight)
                            bgBitmap.getPixels(backgroundPixels, 0, maskWidth, 0, 0, maskWidth, maskHeight)

                            resultBitmap = overlayForeground(mask, maskWidth, maskHeight, inputBitmap, backgroundPixels)
                            canvas = surface.lockCanvas(null);
                            canvas.drawBitmap(resultBitmap, 0f, 0f, null)

                            surface.unlockCanvasAndPost(canvas);

                        }
                        .addOnFailureListener { exception ->
                            Log.d("App", exception.message!!)
                        }
                        .addOnCompleteListener {
                            imageProxy.close()
                        }

                }
            };

            val cameraSelector = CameraSelector.DEFAULT_FRONT_CAMERA

            try {
                // Unbind use cases before rebinding
                cameraProvider.unbindAll()

                // Bind use cases to camera
                cameraProvider.bindToLifecycle(this, cameraSelector, analysisUseCase)

            } catch(exc: Exception) {
                Log.e(TAG, "Use case binding failed", exc)
            }

        }, ContextCompat.getMainExecutor(this))
    }
```
