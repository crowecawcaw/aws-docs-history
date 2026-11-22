

# IVS Broadcast SDK: Linux Guide \| Real-Time Streaming

Use the Amazon IVS real-time streaming Linux broadcast SDK to join a stage as a participant and exchange audio with other participants. It runs headless: there is no camera, microphone, or UI.

The SDK is one shared library, `libaws-ivs-realtime.so`, with a C API declared in `aws_ivs_realtime.h` and `aws_ivs_realtime_errors.h`. The Go package `realtime` wraps the C API. This guide shows code samples in C and in Go. The SDK supports the following operations:
+ Join a stage
+ Subscribe to audio from other participants in the stage, mixed or for each participant
+ Publish audio to other participants in the stage

**Latest version of Linux broadcast SDK:** 1.49.0 ([Release Notes](release-notes.md))

**Reference documentation:** For information on the methods available in the IVS Linux Broadcast SDK, see the reference documentation for [C](https://aws.github.io/amazon-ivs-broadcast-docs/latest/linux/c/index.html) and [Go](https://pkg.go.dev/github.com/aws/amazon-ivs-client-go/realtime).

**Platform requirements:** Linux on x86\_64 (amd64) or arm64. For more information about platform requirements, see [Runtime Requirements](broadcast-linux-getting-started.md#broadcast-linux-runtime-requirements).