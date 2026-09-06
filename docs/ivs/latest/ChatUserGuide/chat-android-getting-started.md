

# Getting Started with the IVS Chat Client Messaging Android SDK
<a name="chat-android-getting-started"></a>

Before starting, you should be familiar with [Getting Started with Amazon IVS Chat](getting-started-chat.md).

## Add the Package
<a name="chat-android-add-package"></a>

Add `com.amazonaws:ivs-chat-messaging` to your `build.gradle` dependencies:

```
dependencies {
   implementation 'com.amazonaws:ivs-chat-messaging'
}
```

## Add Proguard Rules
<a name="chat-android-proguard-rules"></a>

Add the following entries to your R8/Proguard rules file (`proguard-rules.pro`):

```
-keep public class com.amazonaws.ivs.chat.messaging.** { *; }
-keep public interface com.amazonaws.ivs.chat.messaging.** { *; }
```

## Set Up Your Backend
<a name="chat-android-setup-backend"></a>

This integration requires endpoints on your server that talk to the [Amazon IVS API](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html). Use the [official AWS libraries](https://aws.amazon.com/developer/tools/) for access to the Amazon IVS API from your server. These are accessible within several languages from the public packages; e.g., node.js and Java.

Next, create a server endpoint that talks to the [Amazon IVS Chat API](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html) and creates a token.

## Set Up a Server Connection
<a name="chat-android-setup-server"></a>

Create a method that takes `ChatTokenCallback` as a param and fetches a chat token from your backend. Pass that token to the `onSuccess` method of the callback. In case of error, pass the exception to the `onError` method of the callback. This is needed to instantiate the main `ChatRoom` entity in the next step.

Below you can find sample code that implements the above using a `Retrofit` call.

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