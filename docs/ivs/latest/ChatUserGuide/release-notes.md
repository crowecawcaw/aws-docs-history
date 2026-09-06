

# IVS Chat Release Notes
<a name="release-notes"></a>

This document contains all Amazon IVS Chat release notes, latest first, organized by date of release. 

## August 8, 2025
<a name="aug08-25"></a>

### Amazon IVS Chat Client Messaging SDK: iOS 1.0.1
<a name="aug08-25-chat-101-sdk-ios"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [iOS Chat Client Messaging SDK 1.0.1](chat-sdk-ios.md) | **Reference documentation: **[https://aws.github.io/amazon-ivs-chat-messaging-sdk-ios/1.0.1/](https://aws.github.io/amazon-ivs-chat-messaging-sdk-ios/1.0.1/)+  We removed the embedded Bitcode from the SDK.  | 

#### Chat Client Messaging SDK Size: iOS
<a name="chat-101-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| ios-arm64\_x86\_64-simulator | 256 KB | 807 KB | 
| ios-arm64 | 124 KB | 397 KB | 

## December 28, 2023
<a name="dec28-23"></a>

### Amazon IVS Chat User Guide
<a name="sep28-23-chat-ug"></a>

Amazon Interactive Video Service (IVS) Chat is a managed, live-chat feature to go alongside live video streams. In this release, we moved chat information from the IVS Low-Latency Streaming User Guide to a new IVS Chat User Guide. Documentation is accessible from the [Amazon IVS documentation landing page](https://docs.aws.amazon.com/ivs/).

## January 31, 2023
<a name="jan31-23"></a>

### Amazon IVS Chat Client Messaging SDK: Android 1.1.0
<a name="jan31-23-chat-110-sdk-android-ios"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Chat Client Messaging SDK 1.1.0](chat-sdk-android.md) | **Reference documentation: **[https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.1.0/](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.1.0/)+  To support Kotlin Coroutines, we added new IVS Chat Messaging APIs in the com.amazonaws.ivs.chat.messaging.coroutines package. Also see the new Kotlin Coroutines tutorial; part 1 (of 2) is [Chat Rooms](chat-sdk-kotlin-tutorial-chat-rooms.md).  | 

#### Chat Client Messaging SDK Size: Android
<a name="chat-110-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| All architectures (bytecode) | 89 KB | 92 KB | 

## November 9, 2022
<a name="nov09-22"></a>

### Amazon IVS Chat Client Messaging SDK: JavaScript 1.0.2
<a name="nov09-22-chat-102-js"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
|  [JavaScript Chat Client Messaging SDK 1.0.2](chat-sdk-js.md)  | **Reference documentation:** [https://aws.github.io/amazon-ivs-chat-messaging-sdk-js/1.0.2/](https://aws.github.io/amazon-ivs-chat-messaging-sdk-js/1.0.2/)+  Fixed an issue that affected Firefox: clients erroneously received a socket error when they were disconnected from a chat room using the DisconnectUser endpoint.  | 

## September 8, 2022
<a name="sep08-22"></a>

### Amazon IVS Chat Client Messaging SDK: Android 1.0.0 and iOS 1.0.0
<a name="sep08-22-chat-100-sdk-android-ios"></a>


| Platform | Downloads and Changes | 
| --- | --- | 
| [Android Chat Client Messaging SDK 1.0.0](chat-sdk-android.md) | **Reference documentation: **[https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/) | 
| [iOS Chat Client Messaging SDK 1.0.0](chat-sdk-ios.md) | **Reference documentation: **[https://aws.github.io/amazon-ivs-chat-messaging-sdk-ios/1.0.0/](https://aws.github.io/amazon-ivs-chat-messaging-sdk-ios/1.0.0/) | 

#### Chat Client Messaging SDK Size: Android
<a name="chat-100-sdk-size-android"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| All architectures (bytecode) | 53 KB | 58 KB | 

#### Chat Client Messaging SDK Size: iOS
<a name="chat-100-sdk-size-ios"></a>


| Architecture | Compressed Size | Uncompressed Size | 
| --- | --- | --- | 
| ios-arm64\_x86\_64-simulator (bitcode) | 484 KB | 2.4 MB | 
| ios-arm64\_x86\_64-simulator | 484 KB | 2.4 MB | 
| ios-arm64 (bitcode) | 1.1 MB | 3.1 MB | 
|  ios-arm64  | 233 KB | 1.2 MB | 