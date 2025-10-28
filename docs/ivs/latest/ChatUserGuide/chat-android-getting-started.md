# Getting Started with the IVS Chat Client Messaging Android SDK

Before starting, you should be familiar with [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").

## Add the Package

Add `com.amazonaws:ivs-chat-messaging` to your
`build.gradle` dependencies:

```
dependencies {
   implementation 'com.amazonaws:ivs-chat-messaging'
}
```

## Add Proguard Rules

Add the following entries to your R8/Proguard rules file
(`proguard-rules.pro`):

```
-keep public class com.amazonaws.ivs.chat.messaging.** { *; }
-keep public interface com.amazonaws.ivs.chat.messaging.** { *; }
```

## Set Up Your Backend

This integration requires endpoints on your server that talk to the [Amazon IVS
API](../LowLatencyAPIReference/Welcome.md "../LowLatencyAPIReference/Welcome.md"). Use the [official AWS
libraries](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") for access to the Amazon IVS API from your server. These are
accessible within several languages from the public packages; e.g., node.js and
Java.

Next, create a server endpoint that talks to the [Amazon IVS Chat API](../ChatAPIReference/Welcome.md "../ChatAPIReference/Welcome.md") and
creates a token.

## Set Up a Server Connection

Create a method that takes `ChatTokenCallback` as a param and fetches a
chat token from your backend. Pass that token to the `onSuccess` method
of the callback. In case of error, pass the exception to the `onError`
method of the callback. This is needed to instantiate the main `ChatRoom`
entity in the next step.

Below you can find sample code that implements the above using a
`Retrofit` call.

```
// ...

private fun fetchChatToken(callback: ChatTokenCallback) {
    apiService.createChatToken(userId, roomId).enqueue(object : Callback<ChatToken> {
        override fun onResponse(call: Call<ExampleResponse>, response: Response<ExampleResponse>) {
            val body = response.body()
            val token = ChatToken(
                body.token,
                body.sessionExpirationTime,
                body.tokenExpirationTime
            )
            callback.onSuccess(token)
        }

        override fun onFailure(call: Call<ChatToken>, throwable: Throwable) {
            callback.onError(throwable)
        }
    })
}
// ...
```
