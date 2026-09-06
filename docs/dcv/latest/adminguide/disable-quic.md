

# Disabling the QUIC UDP transport protocol
<a name="disable-quic"></a>

By default, since version 2024.0, Amazon DCV supports both the WebSocket protocol, which is based on TCP, and the QUIC protocol, which is based on UDP for data transport.

The QUIC transport protocol is based on UDP. If your network experiences high latency and packet loss, using QUIC might improve performance. With QUIC, the server continues to use WebSocket for authentication traffic.

**Note**  
You can use QUIC only if UDP traffic is permitted by your network and security configuration.

With QUIC enabled, clients can use the QUIC protocol for transporting data when connecting to a Amazon DCV server session. If clients don't use the QUIC protocol when they connect, they use WebSocket. For more information about the QUIC protocol, see [ Connecting to a Amazon DCV Session](https://docs.aws.amazon.com/dcv/latest/userguide/using-connecting.html) in the *Amazon DCV User Guide*.

------
#### [ Windows Amazon DCV server ]

**To disable the use of QUIC (UDP) for data transport in Amazon DCV**

1. Open the Windows Registry Editor and navigate to the **HKEY\_USERS\\S-1-5-18\\Software\\GSettings\\com\\nicesoftware\\dcv\\connectivity\\** key.

1. Open the **enable-quic-frontend** parameter. For **Value data**, enter `0`.
**Note**  
If you can't find the parameter, create a new DWORD (32-bit) parameter and name it `enable-quic-frontend`.

1. Close the Windows Registry Editor.

1. [Stop](manage-stop.md) and [restart](manage-start.md) the Amazon DCV server.

------
#### [ Linux Amazon DCV server ]

**To disable the use of QUIC (UDP) for data transport in Amazon DCV**

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.

1. In the `[connectivity]` section, do the following:
   + For `enable-quic-frontend`, specify `false`.

   ```
   [connectivity]
   enable-quic-frontend=false
   ```

1. Save and close the file.

1. [Stop](manage-stop.md) and [restart](manage-start.md) the Amazon DCV server.

------
#### [ macOS Amazon DCV server ]

**To disable the use of QUIC (UDP) for data transport in Amazon DCV**

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.

1. In the `[connectivity]` section, do the following:
   + For `enable-quic-frontend`, specify `false`.

   ```
   [connectivity]
   enable-quic-frontend=false
   ```

1. Save and close the file.

1. [Stop](manage-stop.md) and [restart](manage-start.md) the Amazon DCV server.

------