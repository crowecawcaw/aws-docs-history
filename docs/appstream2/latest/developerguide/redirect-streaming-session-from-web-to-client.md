# Redirect a Streaming Session from the Web Browser to the WorkSpaces Applications Client

You can configure WorkSpaces Applications to redirect a streaming session from a web browser to the
WorkSpaces Applications client. That way, when your users sign in to WorkSpaces Applications and start a streaming session
in their web browser, their session is redirected to
the WorkSpaces Applications client. To do so, perform these steps.

1. Use the WorkSpaces Applications `CreateStreamingURL` API action to generate a streaming URL.
2. Add the following prefix for the custom WorkSpaces Applications client handler to the streaming URL: `amazonappstream:`

Together, the prefix and streaming URL are formatted as follows:

`amazonappstream:``base64encoded(streamingURL)`

###### Note

When encoding the URL, make sure that the encoding is in UTF-8.

Powershell sample to encode:
`[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("Streaming/IdpURL"))` 3. When users are redirected to the streaming URL, their browser detects that the link
must be opened by the WorkSpaces Applications client. 4. Users are prompted to choose whether they want to
start the streaming session by using the WorkSpaces Applications client. 5. After the prompt, either of the following occurs:

    * If the WorkSpaces Applications client is installed, the user can choose to continue the streaming session by
     using the WorkSpaces Applications client.
    * If the WorkSpaces Applications client is not installed, the browser behavior varies as follows:




    	+ Chrome — No message is displayed.
    	+ Firefox — A message states that the user needs a new app to open Amazon AppStream.
    	+ Microsoft Edge — No message is displayed.
    	+ Internet Explorer — A message notifies the user that the WorkSpaces Applications client is not installed.


    	In this case, users can select the **Download AppStream Client** link to download the client. After they download the client, they can install it, and
    	 refresh their browser to start the streaming session by using the
    	 client.

## Create a Windows desktop shortcut using the default browser

To create a Windows desktop shortcut using the default browser to launch the
client, use the following sample Powershell script.

```

$StringToEncode = '`your URL string`'

$encodedUrl = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($StringToEncode))

$shortcutContent = "
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,0
[InternetShortcut]
IDList=
URL=amazonappstream:$encodedUrl
IconIndex=0
HotKey=0
IconFile=$env:USERPROFILE\AppData\Local\AppStreamClient\appstreamclient.exe
"

Set-Content -Path "$env:USERPROFILE\Desktop\AppStream 2.0 Client Launcher.url" -Value $shortcutContent

```
