

# Integrate your web application with WebRTC redirection
<a name="webrtc-redirection-integration"></a>

WebRTC redirection enables web applications running inside WorkSpaces sessions to use native client-side audio devices. This topic shows web application developers how to detect the WebRTC redirection environment and integrate with it.

When WebRTC redirection is enabled on a WorkSpace, the Amazon DCV WebRTC Redirection browser extension injects a proxy SDK into the web page. Your application can detect this proxy and use it to redirect standard WebRTC API calls - including getUserMedia and RTCPeerConnection - to the user's local devices rather than the remote WorkSpace's virtual devices. This provides significantly better performance and lower latency compared to streaming media through the DCV display protocol.

Your application must handle both cases: when running inside a WorkSpace with WebRTC redirection enabled, and when running in a standard browser without it. The proxy is optional - if it is not present, your application can fall back to standard WebRTC.

## Prerequisites
<a name="webrtc-prereqs"></a>

### For end users
<a name="webrtc-prereqs-users"></a>

End users need the following:
+ A WorkSpace using DCV protocol. For more information, see [Protocols for WorkSpaces Personal](amazon-workspaces-networking.md#amazon-workspaces-protocols).
**Note**  
WebRTC redirection on the server side is currently supported only on Windows WorkSpaces.
+ A supported WorkSpaces client from [clients.amazonworkspaces.com](https://clients.amazonworkspaces.com). Supported platforms: Windows, macOS, Linux (Ubuntu 22.04 and Ubuntu 24.04, amd64), and Web.
+ WebRTC redirection enabled through Group Policy. When enabled, the policy automatically installs the browser extension on Chrome and Edge through the registry. For more information, see [Manage your Windows WorkSpaces in WorkSpaces Personal](group_policy.md). If needed, users can install the extension manually: [Chrome](https://chromewebstore.google.com/detail/amazon-dcv-webrtc-redirec/diilpfplcnhehakckkpmcmibmhbingnd) and [Edge](https://microsoftedge.microsoft.com/addons/detail/amazon-dcv-webrtc-redirec/kjbbkjjiecchbcdoollhgffghfjnbhef).

### For developers
<a name="webrtc-prereqs-devs"></a>

Your web application must:
+ Use standard WebRTC APIs (such as getUserMedia and RTCPeerConnection)
+ Include detection and initialization code as described in this topic

## How to integrate
<a name="webrtc-how-to-integrate"></a>

Integration involves four steps: detect the redirection environment, override WebRTC APIs, map audio elements, and handle reconnection.

### Step 1: Detect the redirection environment
<a name="webrtc-step1-detect"></a>

The following JavaScript code detects the redirection environment and initializes the proxy. The callback runs when a proxy object becomes available.

```
let proxy = null;

function handleInitCallback(result) {
    if (result.success) {
        // A proxy object exists. It is not necessarily attached yet.
        proxy = result.proxy;
        console.log('WebRTC redirection enabled, host library version:', proxy.getVersion());

        // Override WebRTC APIs to use redirection.
        proxy.overrideWebRTC();

        // Start the heartbeat. Keeps the defaults when called with no arguments.
        proxy.resetHeartbeat();

        setupReconnectionHandling();

        if (proxy.status === 'available') {
            startCall();   // Already attached: no further event is coming.
        }
    } else {
        // Not in a redirection environment — use standard WebRTC.
        console.log('WebRTC redirection not available:', result.error);
    }
}

// Register the initialization callback
if (globalThis.DCVWebRTCPeerConnectionProxyV2) {
    globalThis.DCVWebRTCPeerConnectionProxyV2.setInitCallback(handleInitCallback);
}
```

**Important**  
A `success` result means that a proxy object exists, not that redirection is attached. The callback can run before the proxy completes its first handshake with the client — for example, when your application loads while the session's signaling channel is briefly down. Before that handshake the proxy status is `new` and `proxy.clientInfo` is `null`.  
Check `proxy.status` rather than waiting unconditionally for an event. An `available` event fires only on a transition, and `setInitCallback()` can hand you a proxy that is already attached, in which case no further event arrives. If `proxy.status` is already `available`, proceed immediately; otherwise wait for the first `available` event.  
`unavailable` is reported only by the heartbeat timing out, so it cannot arrive sooner than the 10000 ms timeout. Its `data` is the last known client information, or `null` if the proxy never attached.

Key points:
+ Check for `globalThis.DCVWebRTCPeerConnectionProxyV2` to detect the extension
+ Call `setInitCallback()` with your handler. Your callback runs when redirection initializes; it is not called on a timer if redirection is unavailable, so run your own timer if your application needs a fallback.
+ The callback receives a result object with a `success` boolean and either `proxy` or `error`
+ Call `proxy.overrideWebRTC()` to redirect standard WebRTC APIs. This replaces `navigator.mediaDevices.getUserMedia`, `enumerateDevices`, `addEventListener`, `removeEventListener`, `ondevicechange` and `getDisplayMedia`, along with `window.RTCPeerConnection`, `RTCPeerConnection.generateCertificate` and `window.AudioContext`. The originals stay reachable through `proxy.overridenApis` and `proxy.getOverridenApi(name)`, keyed by names such as `window.AudioContext`.
+ Use `DCVWebRTCPeerConnectionProxyV2` with `setInitCallback()`. Earlier integrations read the `globalThis.DCVWebRTCRedirProxy` instance directly. The redirection client retains that global for backward compatibility. It publishes the global after the first successful handshake and never clears it, so its presence means the proxy attached at least once, not that it is attached now — read `proxy.status` for that. In a new application, call `setInitCallback()` to register your callback, then call `addStatusChangeEventListener()` to track readiness, as described in [Step 4: Handle reconnection](#webrtc-step4-reconnection).

**Important**  
Call `resetHeartbeat()` once after you obtain the proxy, however you obtained it. With no arguments it keeps the default timing.  
The heartbeat is what detects that the client went away. If it is not running, nothing times out, so your application never receives `unavailable` even when the client disconnects. Registering a status listener does not start it.

**Note**  
`overrideWebRTC()` also replaces `window.Worker`. That interception is experimental and does not implement the full `Worker` interface: it returns a plain object carrying `postMessage`, `terminate`, `addEventListener`/`removeEventListener` and write-only `onmessage`, `onerror` and `onmessageerror` setters, so `instanceof Worker` does not hold. It is subject to change; don't depend on it. If your application constructs its own web workers, retrieve the original constructor with `proxy.getOverridenApi('window.Worker')`.

### Step 2: Use standard WebRTC APIs
<a name="webrtc-step2-apis"></a>

After calling `overrideWebRTC()`, use WebRTC APIs normally. The proxy transparently redirects them to the local client.

**Note**  
Video redirection is not currently supported. Set `video: false` in `getUserMedia` requests.

```
// Get user media  - automatically redirected
const stream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: false   // Video redirection not yet supported
});

// Create peer connection  - automatically redirected
const pc = new RTCPeerConnection(configuration);

// Everything else works as standard WebRTC
pc.addTrack(stream.getAudioTracks()[0], stream);
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);
```

If you need to access the original browser APIs (for example, to capture video from the remote browser rather than the local client), they are preserved in `proxy.overridenApis`:

```
// Get the original getUserMedia (runs in remote browser, not redirected)
const originalGetUserMedia = proxy.overridenApis.get('navigator.mediaDevices.getUserMedia');

// Available original APIs:
// 'navigator.mediaDevices.getUserMedia'
// 'navigator.mediaDevices.addEventListener'
// 'navigator.mediaDevices.removeEventListener'
// 'navigator.mediaDevices.enumerateDevices'
// 'navigator.mediaDevices.getDisplayMedia'
// 'window.RTCPeerConnection'
// 'window.RTCPeerConnection.generateCertificate'
// 'window.AudioContext'
// 'window.Worker' (experimental)

const remoteStream = await originalGetUserMedia.call(navigator.mediaDevices, {
    audio: false,
    video: true
});
```

### Step 3: Map audio elements
<a name="webrtc-step3-audio"></a>

For audio playback, call `mapAudioElement()` before setting `srcObject` on any audio element.

```
const audioElement = document.querySelector('audio#remote-audio');

// Map the audio element before setting srcObject
proxy.mapAudioElement(audioElement);

// Now use the audio element normally
audioElement.srcObject = remoteStream;
await audioElement.play();

// Control playback
audioElement.pause();
audioElement.volume = 0.8;
audioElement.muted = false;

// Change output device
await audioElement.setSinkId(deviceId);
```

### Step 4: Handle reconnection
<a name="webrtc-step4-reconnection"></a>

The redirection service can become temporarily unavailable, for example due to network issues or client reconnection.

**Important**  
After reconnection, all previously created proxy objects become invalid because the client browser context is completely reloaded. You must close existing connections and create new WebRTC objects.

```
function setupReconnectionHandling() {
    proxy.addStatusChangeEventListener((event) => {
        switch (event.status) {
            case 'unavailable':
                console.error('Redirection lost');
                handleRedirectionLost();
                break;
            case 'available':
                console.info('Redirection restored');
                handleRedirectionRestored();
                break;
        }
    });
}

function handleRedirectionLost() {
    // Try to close cleanly  - proxies may throw exceptions after reconnection
    try {
        if (peerConnection) { peerConnection.close(); }
    } catch (error) {
        console.warn('Error closing peer connection (proxy may be invalid):', error);
    }
    showReconnectingMessage();
}

function handleRedirectionRestored() {
    // IMPORTANT: All existing proxy objects are invalid after reconnection.
    // Create new RTCPeerConnection, MediaStream, and other WebRTC objects.
    hideReconnectingMessage();
    restartCall(); // Must create fresh WebRTC objects
}
```

The heartbeat is what detects that the client went away: when a heartbeat round-trip exceeds `heartbeatTimeoutMs`, the proxy reports `unavailable`. Call `resetHeartbeat()` once after you obtain the proxy to start it; with no arguments it keeps the default timing. Pass values to change it. For the two timing values, the defaults shown are also the minimums:

```
proxy.resetHeartbeat({
    heartbeatTimeoutMs: 10000,       // Minimum and default. Time before marking unavailable.
    heartbeatIntervalPeriodMs: 1000, // Minimum and default. How often to send a heartbeat.
    heartbeatFailureThreshold: 1     // Optional, default 1. Consecutive misses before marking unavailable.
});
```

**Note**  
The proxy raises a `heartbeatTimeoutMs` below 10000, or a `heartbeatIntervalPeriodMs` below 1000, to the minimum and logs a warning. `unavailable` is reported reliably only at or above these values: a tighter request is raised to the minimum, so it fires later than you asked, and under sustained CPU pressure on the WorkSpace it can be suppressed altogether. On WorkSpaces under sustained CPU pressure, a longer `heartbeatTimeoutMs`, such as 20000, gives the event loop more headroom.

## Enabling the Compute Pressure API
<a name="webrtc-compute-pressure"></a>

Redirection records the CPU pressure of the application frame as diagnostic telemetry, which it includes in the periodic statistics the extension logs. Where the Compute Pressure API (`PressureObserver`) is available to the frame, it records the browser's reported pressure state. Where it is not, it falls back to an estimate derived from how late the frame's own timers run. The frame's `compute-pressure` Permissions-Policy governs that availability, so consider enabling it when you deploy:
+ If your application runs in an iframe inside a host web application, add the `allow` attribute to the iframe and serve the delegating header from the embedding application:

  ```
  <iframe src="https://your-app.example.com/..." allow="compute-pressure"></iframe>
  ```

  ```
  Permissions-Policy: compute-pressure=(self "https://your-app.example.com")
  ```
+ If your application is the top-level page, you don't need to do anything. The browser allows same-origin use by default.

**Note**  
This policy affects diagnostic telemetry only. It does not change how redirection behaves, and no functionality depends on it. The benefit of enabling it is a pressure reading reported by the browser rather than one inferred from timer lateness.  
Neither source is reliable for a frame that is not in the foreground. The Compute Pressure API delivers updates only while the document has focus, and the fallback estimate is withheld for a hidden frame because a throttled background timer would otherwise look like severe pressure. Treat a reading taken while the frame was in the background as last known rather than current.  
This is a web-platform permission on the page, not a browser extension permission, so no extension permission can grant it. Availability can also depend on the browser version.

## Device enumeration
<a name="webrtc-device-enumeration"></a>

Device changes - for example, a user plugging in a headset - are automatically detected. Use `makeMediaDevicesProxy()` to listen for device changes on the local client:

```
const mediaDevices = proxy.makeMediaDevicesProxy();
mediaDevices.ondevicechange = async () => {
    const devices = await navigator.mediaDevices.enumerateDevices();
    updateDeviceList(devices);
};
```

Use `proxy.clientInfo` to determine which client platform the user is connecting from. It is `null` until the proxy completes its first handshake with the client. If `proxy.status` is already `available`, read it directly; otherwise read it in your `available` status handler, which delivers the same object as `event.data`:

```
// clientInfo contains:
// - platform: 'web' | 'windows' | 'macOS' | 'linux'
// - version: version of the redirection library running in the DCV client,
//            as an object { major, minor, patch, buildNumber, gitHash,
//            versionStr }. Compare with proxy.getVersion() for the host side.
// - userAgent: browser user agent string
// - browserDetails: { browser: string, version: string }

function readClientInfo(clientInfo) {
    switch (clientInfo.platform) {
        case 'web':     console.log('Connecting from web client'); break;
        case 'windows': console.log('Connecting from Windows native client'); break;
        case 'macOS':   console.log('Connecting from macOS native client'); break;
        case 'linux':   console.log('Connecting from Linux native client'); break;
    }
}

if (proxy.status === 'available') {
    readClientInfo(proxy.clientInfo);
} else {
    proxy.addStatusChangeEventListener((event) => {
        if (event.status === 'available') {
            readClientInfo(event.data);
        }
    });
}
```

**Note**  
Some redirection behavior requires a minimum version of the redirection library in the client. `navigator.mediaDevices.getDisplayMedia`, for example, is gated on 2.1.4 or later. Check `clientInfo.version` rather than assuming the capability is present. This is the redirection library's version, which is not the Amazon WorkSpaces client version.

## Advanced: Audio processing with Web Audio API
<a name="webrtc-advanced-audio"></a>

You can use the Web Audio API to process audio streams before sending them through a peer connection:

```
const audioContext = new AudioContext();
const source = audioContext.createMediaStreamSource(micStream);
const gainNode = audioContext.createGain();
const destination = audioContext.createMediaStreamDestination();

source.connect(gainNode);
gainNode.connect(destination);

// Control microphone volume
gainNode.gain.value = 0.5; // 50% volume

// Use the processed stream
pc.addTrack(destination.stream.getAudioTracks()[0], destination.stream);
```

## Complete example
<a name="webrtc-complete-example"></a>

The following example demonstrates a complete integration with initialization, reconnection handling, device change detection, and call setup:

```
let proxy = null;
let peerConnection = null;
let localStream = null;

function initializeRedirection() {
    if (globalThis.DCVWebRTCPeerConnectionProxyV2) {
        globalThis.DCVWebRTCPeerConnectionProxyV2.setInitCallback((result) => {
            if (result.success) {
                proxy = result.proxy;
                proxy.overrideWebRTC();
                proxy.addStatusChangeEventListener(handleStatusChange);
                proxy.resetHeartbeat();
                setupDeviceChangeListener();

                // setInitCallback can return an already-attached proxy, in which
                // case no 'available' event follows.
                if (proxy.status === 'available') {
                    startCall();
                }
            } else {
                console.log('Redirection not available:', result.error);
            }
        });
    }
}

function handleStatusChange(event) {
    if (event.status === 'unavailable') {
        try {
            if (peerConnection) { peerConnection.close(); peerConnection = null; }
            if (localStream) { localStream.getTracks().forEach(t => t.stop()); localStream = null; }
        } catch (error) {
            console.warn('Error cleaning up (proxies invalid):', error);
            peerConnection = null;
            localStream = null;
        }
    } else if (event.status === 'available') {
        startCall(); // Create fresh WebRTC objects
    }
}

function setupDeviceChangeListener() {
    const mediaDevices = proxy.makeMediaDevicesProxy();
    mediaDevices.ondevicechange = async () => {
        const devices = await navigator.mediaDevices.enumerateDevices();
        updateDeviceUI(devices);
    };
}

async function startCall() {
    try {
        localStream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
        peerConnection = new RTCPeerConnection({ iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] });
        localStream.getTracks().forEach(track => peerConnection.addTrack(track, localStream));

        peerConnection.ontrack = (event) => {
            const remoteAudio = document.querySelector('audio#remote');
            if (proxy) { proxy.mapAudioElement(remoteAudio); }
            remoteAudio.srcObject = event.streams[0];
            remoteAudio.play();
        };

        peerConnection.onicecandidate = (event) => {
            if (event.candidate) { sendToSignalingServer({ type: 'ice-candidate', candidate: event.candidate }); }
        };

        const offer = await peerConnection.createOffer();
        await peerConnection.setLocalDescription(offer);
        sendToSignalingServer({ type: 'offer', sdp: offer });
    } catch (error) {
        console.error('Failed to start call:', error);
    }
}

initializeRedirection();
```

## Testing your integration
<a name="webrtc-testing"></a>

### Without redirection
<a name="webrtc-testing-without"></a>

Your application works normally when the extension is not installed, when running outside a WorkSpace, or when WebRTC redirection is not enabled through Group Policy. Test by opening your application in a regular browser.

### With redirection
<a name="webrtc-testing-with"></a>

To test with redirection enabled:

1. Create a WorkSpace using DCV protocol and enable the WebRTC redirection Group Policy setting. See [Manage your Windows WorkSpaces in WorkSpaces Personal](group_policy.md).

1. Download and install a WorkSpaces client from [clients.amazonworkspaces.com](https://clients.amazonworkspaces.com) and connect to the WorkSpace. Verify the Chrome or Edge extension is installed (automatic when the GPO is set).

1. Open your web application in the WorkSpace browser. Check the console for the "WebRTC redirection enabled" message. Verify audio functionality with local devices, test device enumeration and switching, and verify reconnection handling.

## Best practices
<a name="webrtc-best-practices"></a>

Follow these recommendations when integrating with WebRTC redirection:
+ Always check for redirection availability — never assume the proxy exists, and don't treat a `success` result as proof that redirection is attached; check `proxy.status`, and wait for the first `available` event only if it is not already `available`
+ Call `overrideWebRTC()` early - before creating any WebRTC objects
+ Map audio elements before use - call `mapAudioElement()` before setting `srcObject`
+ Handle reconnection - after reconnection, all proxy objects are invalid; always create new WebRTC objects
+ Test both modes - ensure your app works correctly with and without redirection
+ Use standard WebRTC APIs - the proxy transparently redirects them; no custom APIs are needed for basic use
+ Clean up resources — call `removeStatusChangeEventListener()` for listeners you registered, and close connections when done

## Troubleshooting
<a name="webrtc-troubleshooting"></a>

### Redirection not detected
<a name="webrtc-troubleshooting-not-detected"></a>
+ Verify the browser extension is installed and enabled (check `chrome://extensions`)
+ Confirm the WebRTC redirection Group Policy is enabled on the WorkSpace
+ Verify you are running inside a WorkSpace using DCV protocol
+ Check the browser console for initialization messages
+ Verify the WorkSpaces client version supports WebRTC redirection (Windows 5.21.0 or later, macOS 5.31.0 or later, Linux 2026.0 or later, or Web client)

### Audio or video not working
<a name="webrtc-troubleshooting-audio-video"></a>
+ Verify `overrideWebRTC()` was called before creating any WebRTC objects
+ Verify audio elements are mapped with `mapAudioElement()` before setting `srcObject`
+ Check the browser console for errors
+ Verify device permissions are granted

### Reconnection issues
<a name="webrtc-troubleshooting-reconnection"></a>
+ Implement `addStatusChangeEventListener()` to detect availability changes
+ After reconnection, always create new RTCPeerConnection and MediaStream objects - old proxies are invalid and will throw
+ If `unavailable` is reported during normal operation, check whether the WorkSpace is under CPU pressure before you change the heartbeat configuration. Because the 10000 ms timeout and 1000 ms interval are minimums, you cannot make detection faster; a longer timeout, such as 20000 ms, makes reporting more tolerant of a starved event loop.
+ If `unavailable` never arrives when the client disconnects, the heartbeat is not running. Call `resetHeartbeat()` once after you obtain the proxy; registering a status listener does not start it. Lowering `heartbeatTimeoutMs` is not the fix, and a value below the minimum is raised to it anyway.

## API reference
<a name="webrtc-api-reference"></a>

The following summarizes the proxy API:

```
interface DCVWebRTCProxy {
    // Version of the redirection library on the remote host.
    getVersion(): LibraryVersion;

    // 'new' before the first handshake, then 'available' / 'unavailable'.
    // Check this instead of waiting unconditionally for an event: an
    // 'available' event fires only on a transition.
    status: 'new' | 'available' | 'unavailable';

    // Connected client info. null until the first successful handshake.
    // Each 'available' event also delivers it as StatusChangeEvent.data.
    clientInfo: ClientInfo | null;

    // Core methods. overrideWebRTC() replaces the six
    // navigator.mediaDevices entries listed in Step 1, plus
    // window.RTCPeerConnection, RTCPeerConnection.generateCertificate and
    // window.AudioContext. It also replaces window.Worker, but that
    // interception is experimental — don't rely on it.
    overrideWebRTC(): void;
    mapAudioElement(element: HTMLAudioElement): void;

    // Device management
    makeMediaDevicesProxy(): MediaDevices;

    // Status monitoring
    addStatusChangeEventListener(callback: (event: StatusChangeEvent) => void): void;
    removeStatusChangeEventListener(callback: (event: StatusChangeEvent) => void): void;
    // Call once after you obtain the proxy to start the heartbeat. With no
    // argument it keeps the defaults. heartbeatTimeoutMs has a minimum and
    // default of 10000; heartbeatIntervalPeriodMs has a minimum and default
    // of 1000; heartbeatFailureThreshold defaults to 1 and has no minimum.
    resetHeartbeat(config?: { heartbeatTimeoutMs?: number, heartbeatIntervalPeriodMs?: number, heartbeatFailureThreshold?: number }): void;

    // Access original (non-redirected) browser APIs
    overridenApis: Map<string, Function>;
    getOverridenApi(name: string): Function | undefined;
}

interface LibraryVersion {
    major: number;
    minor: number;
    patch: number;
    buildNumber: number;
    gitHash: string;
    versionStr: string;
}

interface ClientInfo {
    platform: 'web' | 'windows' | 'macOS' | 'linux';
    // Version of the redirection library in the client, not the Amazon
    // WorkSpaces client version.
    version: LibraryVersion;
    userAgent: string;
    browserDetails: { browser: string; version: string; };
}

interface StatusChangeEvent {
    status: 'available' | 'unavailable';
    data: ClientInfo | null;  // Same object as proxy.clientInfo at the time of the event.
    lastHeartbeat?: number;   // Included on 'unavailable' events.
}
```