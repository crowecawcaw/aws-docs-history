# IVS Chat Client Messaging SDK:

Kotlin Coroutines Tutorial Part 1: Chat Rooms

This is the first of a two-part tutorial. You will learn the essentials of
working with the Amazon IVS Chat Messaging SDK by building a fully functional Android app
using the [Kotlin](https://kotlinlang.org/ "https://kotlinlang.org/") programming language and [coroutines](https://kotlinlang.org/docs/coroutines-overview.html "https://kotlinlang.org/docs/coroutines-overview.html"). We call the app _Chatterbox_.

Before you start the module, take a few minutes to familiarize yourself with the
prerequisites, key concepts behind chat tokens, and the backend server necessary for
creating chat rooms.

These tutorials are created for experienced Android developers who are new to
the IVS Chat Messaging SDK. You will need to be comfortable with the Kotlin programming
language and creating UIs on the Android platform.

This first part of the tutorial is broken up into several sections:

1. [Set Up a Local
   Authentication/Authorization Server](#chat-kotlin-rooms-auth-server "#chat-kotlin-rooms-auth-server")
2. [Create a Chatterbox Project](#chat-kotlin-rooms-chatterbox "#chat-kotlin-rooms-chatterbox")
3. [Connect to a Chat Room and Observe
   Connection Updates](#chat-kotlin-rooms-connect "#chat-kotlin-rooms-connect")
4. [Build a Token Provider](#chat-kotlin-rooms-token-provider "#chat-kotlin-rooms-token-provider")
5. [Next Steps](#chat-kotlin-rooms-next-steps "#chat-kotlin-rooms-next-steps")
   For full SDK documentation, start with
   [Amazon IVS Chat Client Messaging SDK](chat-sdk.md "chat-sdk.md") (here in
   the _Amazon IVS Chat User Guide_) and the [Chat Client Messaging: SDK for Android Reference](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/latest/ "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/latest/")
   (on GitHub).

## Prerequisites

- Be familiar with Kotlin and creating applications on the Android platform. If
  you are unfamiliar with creating applications for Android, learn the basics in
  the [Build
  your first app](https://developer.android.com/codelabs/basic-android-kotlin-compose-first-app#0 "https://developer.android.com/codelabs/basic-android-kotlin-compose-first-app#0") guide for Android developers.
- Read and understand [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").
- Create an AWS IAM user with the `CreateChatToken` and
  `CreateRoom` capabilities defined in an existing IAM policy. (See
  [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").)
- Ensure that the secret/access keys for this user are stored in an AWS
  credentials file. For instructions, see the [AWS CLI User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") (especially [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")).
- Create a chat room and save its ARN. See [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md"). (If you don’t save the ARN, you can look it up later with the console or
  Chat API.)

## Set Up a Local

Authentication/Authorization Server

Your backend server will be responsible for both creating chat rooms and
generating the chat tokens needed for the IVS Chat Android SDK to authenticate and
authorize your clients for your chat rooms.

See [Create a Chat Token](getting-started-chat-auth.md "getting-started-chat-auth.md") in _Getting Started with Amazon IVS Chat_. As shown in the
flowchart there, your server-side code is responsible for creating a chat token. This
means your app must provide its own means of generating a chat token by requesting one
from your server-side application.

We use the [Ktor](https://ktor.io/ "https://ktor.io/") framework to create a live local server that manages
the creation of chat tokens using your local AWS environment.

At this point, we expect you have your AWS credentials set up correctly. For
step-by-step instructions, see [Set up AWS temporary credentials and AWS Region for development](../../../sdk-for-java/v1/developer-guide/setup-credentials.md "../../../sdk-for-java/v1/developer-guide/setup-credentials.md").

Create a new directory and call it `chatterbox` and inside it,
another one, called `auth-server`_._

Our server folder will have the following structure:

```
- auth-server
  - src
    - main
      - kotlin
        - com
          - chatterbox
            - authserver
              - Application.kt
       - resources
         - application.conf
         - logback.xml
   - build.gradle.kts
```

_Note: you can directly copy/paste the code here into
the referenced files._

Next, we add all the necessary dependencies and plugins for our auth server
to work:

**Kotlin Script:**

```
// ./auth-server/build.gradle.kts

plugins {
   application
   kotlin("jvm")
   kotlin("plugin.serialization").version("1.7.10")
}

application {
   mainClass.set("io.ktor.server.netty.EngineMain")
}

dependencies {
   implementation("software.amazon.awssdk:ivschat:2.18.1")
   implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.7.20")

   implementation("io.ktor:ktor-server-core:2.1.3")
   implementation("io.ktor:ktor-server-netty:2.1.3")
   implementation("io.ktor:ktor-server-content-negotiation:2.1.3")
   implementation("io.ktor:ktor-serialization-kotlinx-json:2.1.3")

   implementation("ch.qos.logback:logback-classic:1.4.4")
}
```

Now we need to set up logging functionality for the auth server. (For more
information, see [Configure logger](https://ktor.io/docs/logging.html#configure-logger "https://ktor.io/docs/logging.html#configure-logger").)

**XML:**

```
// ./auth-server/src/main/resources/logback.xml

<configuration>
   <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
      <encoder>
         <pattern>%d{YYYY-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
      </encoder>
   </appender>
   <root level="trace">
      <appender-ref ref="STDOUT"/>
   </root>
   <logger name="org.eclipse.jetty" level="INFO"/>
   <logger name="io.netty" level="INFO"/>
</configuration>
```

The [Ktor](https://ktor.io/docs/welcome.html "https://ktor.io/docs/welcome.html") server requires configuration settings, which it
automatically loads from the `application.*` file in the
`resources` directory, so we add that as well. (For more information, see
[Configuration in a file](https://ktor.io/docs/configurations.html#configuration-file "https://ktor.io/docs/configurations.html#configuration-file").)

**HOCON:**

```
// ./auth-server/src/main/resources/application.conf

ktor {
   deployment {
      port = 3000
   }
   application {
      modules = [ com.chatterbox.authserver.ApplicationKt.main ]
   }
}
```

Finally, let's implement our server:

**Kotlin:**

```
// ./auth-server/src/main/kotlin/com/chatterbox/authserver/Application.kt

package com.chatterbox.authserver

import io.ktor.http.*
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.application.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import software.amazon.awssdk.services.ivschat.IvschatClient
import software.amazon.awssdk.services.ivschat.model.CreateChatTokenRequest

@Serializable
data class ChatTokenParams(var userId: String, var roomIdentifier: String)

@Serializable
data class ChatToken(
   val token: String,
   val sessionExpirationTime: String,
   val tokenExpirationTime: String,
)

fun Application.main() {
   install(ContentNegotiation) {
      json(Json)
   }

   routing {
      post("/create_chat_token") {
         val callParameters = call.receive<ChatTokenParams>()
         val request = CreateChatTokenRequest.builder().roomIdentifier(callParameters.roomIdentifier)
            .userId(callParameters.userId).build()
         val token = IvschatClient.create()
            .createChatToken(request)

         call.respond(
            ChatToken(
                token.token(),
                token.sessionExpirationTime().toString(),
                token.tokenExpirationTime().toString()
            )
         )
      }
   }
}
```

## Create a Chatterbox Project

To create an Android project, install and open [Android Studio](https://developer.android.com/studio "https://developer.android.com/studio").

Follow the steps listed in the official Android [Create a Project
guide](https://developer.android.com/studio/projects/create-project "https://developer.android.com/studio/projects/create-project").

- In [Choose your project](https://developer.android.com/studio/projects/create-project "https://developer.android.com/studio/projects/create-project"), choose the
  **Empty Activity** project template for our
  Chatterbox app.

- In [Configure your project](https://developer.android.com/studio/projects/create-project#configure "https://developer.android.com/studio/projects/create-project#configure"),
  choose the following values for configuration fields:
  - **Name**: My App

  - **Package name**:
    com.chatterbox.myapp
  - **Save location**: point at the
    created `chatterbox` directory created in the previous
    step
  - **Language**: Kotlin
  - **Minimum API level**: API 21:
    Android 5.0 (Lollipop)

After specifying all the configuration parameters correctly, our file structure inside
the `chatterbox` folder should look like the following:

```
- app
  - build.gradle
  ...
- gradle
- .gitignore
- build.gradle
- gradle.properties
- gradlew
- gradlew.bat
- local.properties
- settings.gradle
- auth-server
  - src
    - main
      - kotlin
        - com
          - chatterbox
            - authserver
              - Application.kt
       - resources
         - application.conf
         - logback.xml
   - build.gradle.kts
```

Now that we have a working Android project, we can add [com.amazonaws:ivs-chat-messaging](https://mvnrepository.com/artifact/com.amazonaws/ivs-chat-messaging "https://mvnrepository.com/artifact/com.amazonaws/ivs-chat-messaging") and [org.jetbrains.kotlinx:kotlinx-coroutines-core](https://github.com/Kotlin/kotlinx.coroutines "https://github.com/Kotlin/kotlinx.coroutines") to our
`build.gradle` dependencies. (For more information on the [Gradle](https://gradle.org/ "https://gradle.org/") build
toolkit, see [Configure your build](https://developer.android.com/build "https://developer.android.com/build").)

**Note:** At the top of every code snippet,
there is a path to the file where you should be making changes in your project. The path
is relative to the project’s root.

**Kotlin:**

```
// ./app/build.gradle

plugins {
// ...
}

android {
// ...
}

dependencies {
    implementation 'com.amazonaws:ivs-chat-messaging:1.1.0'
    implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.6.4'

// ...
}
```

After the new dependency is added, run **Sync Project
with Gradle Files** in Android Studio to synchronize the project with the
new dependency. (For more information, see [Add build dependencies](https://developer.android.com/build/dependencies "https://developer.android.com/build/dependencies").)

To conveniently run our auth server (created in the previous section) from
the project root, we include it as a new module in `settings.gradle`. (For
more information, see [Structuring and Building a Software Component with
Gradle](https://docs.gradle.org/current/userguide/multi_project_builds.html "https://docs.gradle.org/current/userguide/multi_project_builds.html").)

**Kotlin Script:**

```
// ./settings.gradle

// ...

rootProject.name = "My App"
include ':app'
include ':auth-server'
```

From now on, as `auth-server` is included in the Android project,
you can run the auth server with the following command from the project's root:

**Shell:**

```
./gradlew :auth-server:run
```

## Connect to a Chat Room and Observe

Connection Updates

To open a chat-room connection, we use the [onCreate() activity lifecycle
callback](https://developer.android.com/guide/components/activities/activity-lifecycle "https://developer.android.com/guide/components/activities/activity-lifecycle"), which fires when the activity is first created. The
[ChatRoom constructor](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html") requires us
to provide `region` and `tokenProvider` to instantiate a room
connection.

**Note:** The `fetchChatToken`
function in the snippet below will be implemented in [the next section](#chat-kotlin-rooms-token-provider "#chat-kotlin-rooms-token-provider").

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp
// ...

// AWS region of the room that was created in Getting Started with Amazon IVS Chat
const val REGION = "us-west-2"

class MainActivity : AppCompatActivity() {
    private var room: ChatRoom? = null
    // ...

   override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContentView(R.layout.activity_main)

      // Create room instance
      room = ChatRoom(REGION, ::fetchChatToken)
   }

// ...
}
```

Displaying and reacting to changes in a chat room's connection are essential
parts of making a chat app like `chatterbox`. Before we can start interacting
with the room, we must subscribe to chat-room connection-state events, to get
updates.

In the Chat SDK for coroutine, [`ChatRoom`](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html") expects
us to handle room lifecycle events in [Flow](https://kotlinlang.org/docs/flow.html "https://kotlinlang.org/docs/flow.html"). For now, the functions will
log only confirmation messages, when invoked:

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp
// ...

const val TAG = "Chatterbox-MyApp"

class MainActivity : AppCompatActivity() {
// ...

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...

        // Create room instance
        room = ChatRoom(REGION, ::fetchChatToken).apply {
            lifecycleScope.launch {
                stateChanges().collect { state ->
                    Log.d(TAG, "state change to $state")
                }
            }

            lifecycleScope.launch {
                receivedMessages().collect { message ->
                    Log.d(TAG, "messageReceived $message")
                }
            }

            lifecycleScope.launch {
                receivedEvents().collect { event ->
                    Log.d(TAG, "eventReceived $event")
                }
            }

            lifecycleScope.launch {
                deletedMessages().collect { event ->
                    Log.d(TAG, "messageDeleted $event")
                }
            }

            lifecycleScope.launch {
                disconnectedUsers().collect { event ->
                    Log.d(TAG, "userDisconnected $event")
                }
            }
        }
    }
}
```

After this, we need to provide the ability to read the room-connection
state. We will keep it in the `MainActivity.kt`
[property](https://kotlinlang.org/docs/properties.html "https://kotlinlang.org/docs/properties.html") and initialize it to the default DISCONNECTED state
for rooms (see `ChatRoom`
`state` in the [IVS Chat Android SDK Reference](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/latest/ "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/latest/")). To be able
to keep local state up to date, we need to implement a state-updater function; let’s
call it `updateConnectionState`:

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp
// ...

class MainActivity : AppCompatActivity() {
   private var connectionState = ChatRoom.State.DISCONNECTED

// ...

   private fun updateConnectionState(state: ChatRoom.State) {
      connectionState = state

     when (state) {
          ChatRoom.State.CONNECTED -> {
              Log.d(TAG, "room connected")
          }
          ChatRoom.State.DISCONNECTED -> {
              Log.d(TAG, "room disconnected")
          }
          ChatRoom.State.CONNECTING -> {
              Log.d(TAG, "room connecting")
          }
      }
}
```

Next, we integrate our state-updater function with the [ChatRoom.listener](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/listener.html "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/listener.html")
property:

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp
// ...

class MainActivity : AppCompatActivity() {
// ...

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...

        // Create room instance
        room = ChatRoom(REGION, ::fetchChatToken).apply {
            lifecycleScope.launch {
                stateChanges().collect { state ->
                    Log.d(TAG, "state change to $state")
                    updateConnectionState(state)

                }
            }

      // ...

      }
   }
}
```

Now that we have the ability to save, listen, and react to [ChatRoom](https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html "https://aws.github.io/amazon-ivs-chat-messaging-sdk-android/1.0.0/-amazon%20-i-v-s%20-chat%20-messaging%20-s-d-k%20for%20-android/com.amazonaws.ivs.chat.messaging/-chat-room/index.html") state updates, it's time
to initialize a connection:

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp
// ...

class MainActivity : AppCompatActivity() {
// ...

   private fun connect() {
      try {
         room?.connect()
      } catch (ex: Exception) {
         Log.e(TAG, "Error while calling connect()", ex)
      }
   }

   // ...
}
```

## Build a Token Provider

It's time to create a function responsible for creating and managing chat
tokens in our application. In this example we use the [Retrofit HTTP
client for Android](https://square.github.io/retrofit/ "https://square.github.io/retrofit/").

Before we can send any network traffic, we must set up a network-security
configuration for Android. (For more information, see [Network security configuration](https://developer.android.com/privacy-and-security/security-config "https://developer.android.com/privacy-and-security/security-config").) We begin
with adding network permissions to the [App Manifest](https://developer.android.com/guide/topics/manifest/manifest-intro "https://developer.android.com/guide/topics/manifest/manifest-intro") file. Note the added
`user-permission` tag and `networkSecurityConfig` attribute,
which will point to our new network-security configuration. _In
the code below, replace_ `*<version>*` _with the current version
number of the Chat Android SDK (e.g., 1.1.0)._

**XML:**

```
// ./app/src/main/AndroidManifest.xml

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.chatterbox.myapp">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:allowBackup="true"
        android:fullBackupContent="@xml/backup_rules"
        android:label="@string/app_name"
        android:networkSecurityConfig="@xml/network_security_config"
// ...

// ./app/build.gradle


dependencies {
   implementation("com.amazonaws:ivs-chat-messaging:<version>")
// ...

   implementation("com.squareup.retrofit2:retrofit:2.9.0")
   implementation("com.squareup.retrofit2:converter-gson:2.9.0")
}
```

Declare your local IP address, e.g. `10.0.2.2` and
`localhost` domains as trusted, to start exchanging messages with our
backend:

**XML:**

```
// ./app/src/main/res/xml/network_security_config.xml

<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.2.2</domain>
        <domain includeSubdomains="true">localhost</domain>
    </domain-config>
</network-security-config>
```

Next, we need to add a new dependency, along with [Gson converter addition](https://github.com/square/retrofit/tree/trunk/retrofit-converters/gson "https://github.com/square/retrofit/tree/trunk/retrofit-converters/gson") for
parsing HTTP responses. _In the code below, replace_ `*<version>*` _with the current version number of the Chat Android SDK (e.g.,
1.1.0)._

**Kotlin Script:**

```
// ./app/build.gradle

dependencies {
   implementation("com.amazonaws:ivs-chat-messaging:<version>")
// ...

   implementation("com.squareup.retrofit2:retrofit:2.9.0")
   implementation("com.squareup.retrofit2:converter-gson:2.9.0")
}
```

To retrieve a chat token, we need to make a POST HTTP request from our
`chatterbox` app. We define the request in an interface for Retrofit to
implement. (See [Retrofit documentation](https://square.github.io/retrofit/ "https://square.github.io/retrofit/"). Also familiarize
yourself with the [CreateChatToken](../ChatAPIReference/API_CreateChatToken.md#API_CreateChatToken_RequestBody "../ChatAPIReference/API_CreateChatToken.md#API_CreateChatToken_RequestBody") operation
specification.)

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/network/ApiService.kt

package com.chatterbox.myapp.network

import com.amazonaws.ivs.chat.messaging.ChatToken
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

data class CreateTokenParams(var userId: String, var roomIdentifier: String)

interface ApiService {
   @POST("create_chat_token")
   fun createChatToken(@Body params: CreateTokenParams): Call<ChatToken>
}


// ./app/src/main/java/com/chatterbox/myapp/network/RetrofitFactory.kt

package com.chatterbox.myapp.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitFactory {
   private const val BASE_URL = "http://10.0.2.2:3000"

   fun makeRetrofitService(): ApiService {
       return Retrofit.Builder()
           .baseUrl(BASE_URL)
           .addConverterFactory(GsonConverterFactory.create())
           .build().create(ApiService::class.java)
   }
}
```

Now, with networking set up, it's time to add a function responsible for
creating and managing our chat token. We add it to `MainActivity.kt`, which
was automatically created when the project was [generated](#chat-kotlin-rooms-chatterbox "#chat-kotlin-rooms-chatterbox"):

**Kotlin:**

```
// ./app/src/main/java/com/chatterbox/myapp/MainActivity.kt

package com.chatterbox.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import com.amazonaws.ivs.chat.messaging.*
import com.amazonaws.ivs.chat.messaging.coroutines.*
import com.chatterbox.myapp.network.CreateTokenParams
import com.chatterbox.myapp.network.RetrofitFactory
import retrofit2.Call
import java.io.IOException
import retrofit2.Callback
import retrofit2.Response

// custom tag for logging purposes
const val TAG = "Chatterbox-MyApp"

// any ID to be associated with auth token
const val USER_ID = "test user id"
// ID of the room the app wants to access. Must be an ARN. See Amazon Resource Names(ARNs)
const val ROOM_ID = "arn:aws:..."
// AWS region of the room that was created in Getting Started with Amazon IVS Chat
const val REGION = "us-west-2"

class MainActivity : AppCompatActivity() {

   private val service = RetrofitFactory.makeRetrofitService()
   private var userId: String = USER_ID

// ...

   private fun fetchChatToken(callback: ChatTokenCallback) {
      val params = CreateTokenParams(userId, ROOM_ID)
      service.createChatToken(params).enqueue(object : Callback<ChatToken> {
         override fun onResponse(call: Call<ChatToken>, response: Response<ChatToken>) {
            val token = response.body()
            if (token == null) {
               Log.e(TAG, "Received empty token response")
               callback.onFailure(IOException("Empty token response"))
               return
            }

            Log.d(TAG, "Received token response $token")
            callback.onSuccess(token)
         }

         override fun onFailure(call: Call<ChatToken>, throwable: Throwable) {
            Log.e(TAG, "Failed to fetch token", throwable)
            callback.onFailure(throwable)
         }
      })
   }
}
```

## Next Steps

Now that you’ve established a chat-room connection, proceed to Part 2 of this Kotlin
Coroutines tutorial, [Messages
and Events](chat-sdk-kotlin-tutorial-messages-events.md "chat-sdk-kotlin-tutorial-messages-events.md").
