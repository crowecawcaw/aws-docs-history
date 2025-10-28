# Getting Started with Amazon DCV

To use Amazon DCV, install the Amazon DCV server software on a server. The Amazon DCV
server software is used to create a secure [session](../adminguide/managing-sessions.md "../adminguide/managing-sessions.md"). You
install and run your applications on the server. The server uses its hardware to
perform the high-performance processing that the installed applications require.
Your users access the application by remotely connecting to the session using a
Amazon DCV client application. When the connection is established, the Amazon DCV server
software compresses the visual output of the application and streams it back to
the client application in an encrypted pixel stream. The client application receives
the compressed pixel stream, decrypts it, and then outputs it to the local
display.

After you choose a Amazon DCV client and connect to it, you are able to interact with the Amazon DCV session.
For more information about using the Amazon DCV clients to interact with sessions, see [Using Amazon DCV](using.md "using.md").

###### Contents

- [Requirements](requirements.md "requirements.md")
- [Step 1: Get the session information](getting-started-session.md "getting-started-session.md")
- [Step 2: Choose a client](getting-started-choose.md "getting-started-choose.md")
- [Step 3: Connect to a session](using-connecting.md "using-connecting.md")
  - [Connecting using the Windows client](using-connecting-win.md "using-connecting-win.md")
  - [Connecting using the web browser client](using-connecting-browser-connect.md "using-connecting-browser-connect.md")
  - [Connecting using the Linux client](using-connecting-linux.md "using-connecting-linux.md")
  - [Connecting using the macOS client](using-connecting-mac.md "using-connecting-mac.md")
  - [Connecting using URI](using-connecting-uri.md "using-connecting-uri.md")

- [Step 4: Create a connection file (optional)](using-connection-file.md "using-connection-file.md")
  - [Creating the connection file](using-connection-file.md#connection-file-create "using-connection-file.md#connection-file-create")
  - [Supported parameters](using-connection-file.md#connection-file-params "using-connection-file.md#connection-file-params")
    - [[version] parameters](using-connection-file.md#param-version "using-connection-file.md#param-version")
    - [[connect] parameters](using-connection-file.md#param-connect "using-connection-file.md#param-connect")
    - [[options] parameters](using-connection-file.md#param-option "using-connection-file.md#param-option")
    - [[debug] parameters](using-connection-file.md#param-debug "using-connection-file.md#param-debug")

  - [Running the connection file](using-connection-file.md#connection-file-execute "using-connection-file.md#connection-file-execute")
