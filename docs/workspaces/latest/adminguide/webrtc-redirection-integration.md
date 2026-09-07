

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

Add this initialization code to your application. The callback runs when the proxy is ready, or after the timeout if redirection is not available.

```
let proxy = null;

function handleInitCallback(result) {
    if (result.success) {
        // Redirection is available
        proxy = result.proxy;
        console.log('WebRTC redirection enabled, version:', proxy.getVersion());
        console.log('Client info:', proxy.clientInfo);

        // Override WebRTC APIs to use redirection
        proxy.overrideWebRTC();

        // Set up reconnection handling
        setupReconnectionHandling();
    } else {
        // Not in a redirection environment  - use standard WebRTC
        console.log('WebRTC redirection not available:', result.error);
    }
}

// Register the initialization callback
if (globalThis.DCVWebRTCPeerConnectionProxyV2) {
    globalThis.DCVWebRTCPeerConnectionProxyV2.setInitCallback(handleInitCallback, 5000);
}
```

Key points:
+ Check for `globalThis.DCVWebRTCPeerConnectionProxyV2` to detect the extension
+ Call `setInitCallback()` with your handler and a timeout - 5000 ms is recommended
+ The callback receives a result object with a `success` boolean and either `proxy` or `error`
+ Call `proxy.overrideWebRTC()` to redirect standard WebRTC APIs

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

You can customize the heartbeat timing:

```
proxy.resetHeartbeat({
    heartbeatTimeoutMs: 5000,      // Time before marking unavailable
    heartbeatIntervalPeriodMs: 500 // How often to check
});
```

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

Use `proxy.clientInfo` to determine which client platform the user is connecting from:

```
// clientInfo contains:
// - platform: 'web' | 'windows' | 'macOS' | 'linux'
// - version: SDK version string
// - userAgent: browser user agent string
// - browserDetails: { browser: string, version: string }

switch (proxy.clientInfo.platform) {
    case 'web':     console.log('Connecting from web client'); break;
    case 'windows': console.log('Connecting from Windows native client'); break;
    case 'macOS':   console.log('Connecting from macOS native client'); break;
    case 'linux':   console.log('Connecting from Linux native client'); break;
}
```

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
                proxy.resetHeartbeat({ heartbeatTimeoutMs: 5000, heartbeatIntervalPeriodMs: 500 });
                setupDeviceChangeListener();
            } else {
                console.log('Redirection not available:', result.error);
            }
        }, 5000);
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
+ Always check for redirection availability - never assume the proxy exists
+ Call `overrideWebRTC()` early - before creating any WebRTC objects
+ Map audio elements before use - call `mapAudioElement()` before setting `srcObject`
+ Handle reconnection - after reconnection, all proxy objects are invalid; always create new WebRTC objects
+ Test both modes - ensure your app works correctly with and without redirection
+ Use standard WebRTC APIs - the proxy transparently redirects them; no custom APIs are needed for basic use
+ Clean up resources - remove event listeners and close connections when done

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
+ Review heartbeat configuration if unavailability is detected too slowly or too quickly

## API reference
<a name="webrtc-api-reference"></a>

The following summarizes the proxy API:

```
interface DCVWebRTCProxy {
    // Version and client info
    getVersion(): string;
    clientInfo: {
        platform: 'web' | 'windows' | 'macOS' | 'linux';
        version: string;
        userAgent: string;
        browserDetails: { browser: string; version: string; };
    };

    // Core methods
    overrideWebRTC(): void;
    mapAudioElement(element: HTMLAudioElement): void;

    // Device management
    makeMediaDevicesProxy(): MediaDevices;

    // Status monitoring
    addStatusChangeEventListener(callback: (event: StatusChangeEvent) => void): void;
    resetHeartbeat(config: { heartbeatTimeoutMs: number, heartbeatIntervalPeriodMs: number }): void;

    // Access original (non-redirected) browser APIs
    overridenApis: Map<string, Function>;
}

interface StatusChangeEvent {
    status: 'available' | 'unavailable';
    lastHeartbeat?: number;
}
```