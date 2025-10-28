# Known Issues & Workarounds in the IVS

iOS Broadcast SDK | Real-Time Streaming ​

This document lists known issues that you might encounter when using the Amazon IVS
real-time streaming iOS broadcast SDK and suggests potential workarounds.

- Changing Bluetooth audio routes can be unpredictable. If you connect a new
  device mid-session, iOS may or may not automatically change the input route.
  Also, it is not possible to choose between multiple Bluetooth headsets that are
  connected at the same time. This happens in both regular broadcast and stage
  sessions.

**Workaround:** If you plan to use a Bluetooth
headset, connect it before starting the broadcast or stage and leave it
connected throughout the session.

- Participants using an iPhone 14, iPhone 14 Plus, iPhone 14 Pro, or iPhone 14
  Pro Max may cause an audio echo issue for other participants.

**Workaround:** Participants using the affected
devices can use headphones to prevent the echo issue for other
participants.

- When a participant joins with a token that is being used by another
  participant, the first connection is disconnected without a specific
  error.

**Workaround:** None.

- There is a rare issue where the publisher is publishing but the publish state
  that subscribers receive is `inactive`.

**Workaround:** Try leaving and then joining the
session. If the issue remains, create a new token for the publisher.

- When a participant is publishing or subscribing, it is possible to receive an
  error with code 1400 that indicates disconnection due to a network issue, even
  when the network is stable.

**Workaround:** Try republishing /
resubscribing.

- A rare audio-distortion issue may occur intermittently during a stage session,
  typically on calls of longer durations.

**Workaround:** The participant with distorted
audio can either leave and rejoin the session, or unpublish and republish their
audio to fix the issue.
