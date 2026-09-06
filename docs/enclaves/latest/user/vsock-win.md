

# Working with the vsock socket in Windows
<a name="vsock-win"></a>

This topic provides information that is specific to working with the vsock socket on Windows instances.

**Topics**
+ [Terminology](#terminology)
+ [AWS vsock socket implementation](#implementation)
+ [Using the Winsock2 functions with vsock sockets](#apis)
+ [Unsupported Winsock2 functions](#unsupported-apis)
+ [Known issues](#known-issues)

## Terminology
<a name="terminology"></a>

**Service Provider Interface**  
The Service Provider Interface (SPI) is a library registered with the Windows Sockets 2 (Winsock2) API to support a new address family for the vsock socket. The vsock SPI is available in a 64-bit version only. Only 64-bit applications can use vsock sockets.

**Port**  
The port component of an address. This is a 32-bit unsigned value.

**Local address**  
The address of a vsock socket on the host on which the application is running. The address includes a context identifier (CID) and a port. The CID and port value pairs are concatenated with a '`.`' when written as a string. For example, a host with CID of `3` that listens on port `1234` has a listening address of `3.1234`.

**Peer**  
A host that this host is communicating with over the vsock socket.

**Remote address**  
The address of the vsock socket of the peer. The address includes a context identifier (CID) and a port. The CID and port value pairs are concatenated with a '`.`' when written as a string. For example, a host with CID of `3` that listens on port `1234` has a listening address of `3.1234`.

## AWS vsock socket implementation
<a name="implementation"></a>

The following are considerations for vsock socket implementation using Winsock2.

**Topics**
+ [Build-time dependencies](#build-time)
+ [Runtime](#run-time)
+ [Loopback support](#loopback)

### Build-time dependencies
<a name="build-time"></a>

Some value definitions are required to create and interact with vsock sockets. These include the definitions of `AF_VSOCK`, `sockaddr_vm`, and some reserved values for CIDs and ports. It is recommended that you include these definitions by including the `VirtioVsock.h` header in your code. For more information, about the header, see the [ Nitro Enclaves SDK Github repository](https://github.com/aws/aws-nitro-enclaves-sdk-c/tree/main/include/aws/vsock/VirtioVsock.h).

### Runtime
<a name="run-time"></a>

To create a Winsock2 socket with the `AF_VSOCK` address family, the vsock SPI must be registered with Winsock2. The vsock SPI is registered during the AWS Nitro Enclaves installation. Currently, the vsock SPI is available in a 64-bit version and supports only 64-bit applications. For more information about installing AWS Nitro Enclaves on a Windows instance, see [Install Nitro CLI](nitro-enclave-cli-install-win.md#install-cli-win).

### Loopback support
<a name="loopback"></a>

Loopback is not supported with vsock sockets. Attempts to `connect()` to a CID that belongs to the same host could result in an error.

## Using the Winsock2 functions with vsock sockets
<a name="apis"></a>

This section highlights differences between the Winsock2 functions and the AWS implementation for the vsock SPI.

**Note**  
Functions not listed below follow the Winsock2 implementation and behave as described in the [Winsock2 API documentation](https://docs.microsoft.com/en-us/windows/win32/api/Winsock2/) without any AWS specific nuances. For a list of the unsupported Winsock2 functions, see [Unsupported Winsock2 functions](#unsupported-apis).

**Topics**
+ [`WSAAccept()/accept()`](#WSAAccept)
+ [WSAAddressToString()](#WSAAddressToString)
+ [WSABind()/bind()](#WSABind)
+ [WSAConnect()/connect()](#WSAConnect)
+ [WSAEventSelect()](#WSAEventSelect)
+ [WSAGetPeerName()](#WSAGetPeerName)
+ [WSAGetSockName()](#WSAGetSockName)
+ [WSAGetSockOpt()/getsockopt()](#WSAGetSockOpt)
+ [WSAIoctl()/ioctlsocket()](#WSAIoctl)
+ [WSAListen()/listen()](#WSAListen)
+ [WSASend()/send()](#WSASend)
+ [WSASetSockOpt()/setsockopt()](#WSASetSockOpt)
+ [WSASocket()/socket()](#WSASocket)
+ [WSAStringToAddress()](#WSAStringToAddress)
+ [WSARecv()/recv()](#WSARecv)

### `WSAAccept()/accept()`
<a name="WSAAccept"></a>

If a vsock transport reset or device disable event occurs after receiving a connection request, but before `accept()` is called, `accept()` returns an invalid socket and `WSAGetLastError()` returns the value `WSAECONNRESET`.

### WSAAddressToString()
<a name="WSAAddressToString"></a>

Converts `sockaddr_vm` to a string in the `CID.Port` format.

### WSABind()/bind()
<a name="WSABind"></a>

To create a connection using a specific local port, you must call `bind()` with a valid local CID and the desired local port before calling `connect()`. An enclave-enabled Amazon EC2 instance is always assigned local CID of `3`. A socket bound to `SOCKADDR_VM_CID_ANY` can only be used for listening and cannot be used with `connect()`. `SO_REUSEADDR` and `SO_EXCLUSIVEADDRUSE` are not configurable. AWS vsock sockets behave as if `SO_EXCLUSIVEADDRUSE` is enabled for all sockets. That is, if any socket is bound to a local `CID.port` pair, no other socket can bind to that same local `CID.port` except as an `accept()` from a listening socket that is bound to `SOCKADDR_VM_CID_ANY.port` or `CID.port`. Additionally, sockets cannot be bound to `SOCKADDR_VM_CID_ANY.port` when any other socket on the host is bound to an address with the same local port value and any CID.

### WSAConnect()/connect()
<a name="WSAConnect"></a>

Outgoing connection requests have a non-configurable `1` second timeout before the peer responds with a connection acceptance packet. When using `WSAConnect()`, caller data and callee data are not supported. Specifying caller data results in an error and specifying callee data returns a length of `0`. QOS options are also not supported and return an error if specified.

### WSAEventSelect()
<a name="WSAEventSelect"></a>

`FD_OOB`, `FD_QOS`, `FD_GROUP_QOS`, `FD_ROUTING_INTERFACE_CHANGE`, and `FD_ADDRESS_LIST_CHANGE` will never be signaled in the current implementation. However, they do not return an error if specified.

### WSAGetPeerName()
<a name="WSAGetPeerName"></a>

Gets the peer’s socket address as a `sockaddr_vm`.

### WSAGetSockName()
<a name="WSAGetSockName"></a>

Gets the local socket address as a `sockaddr_vm`.

### WSAGetSockOpt()/getsockopt()
<a name="WSAGetSockOpt"></a>

Only the following `optname` parameters are supported:
+ `SO_LINGER`
+ `SO_DONTLINGER`
+ `SO_RCVBUF`
+ `SO_ACCEPTCONN`
+ `SO_PROTOCOL_INFOW`
+ `SO_TYPE`

For more information, see [ getsockopt function](https://docs.microsoft.com/en-us/windows/win32/api/Winsock2/nf-Winsock2-getsockopt) on the Windows app developer documentation website.

### WSAIoctl()/ioctlsocket()
<a name="WSAIoctl"></a>

Only the following `ioctls` are supported:
+ `FIONBIO`
+ `FIONREAD`

For more information, see [ ioctlsocket function](https://docs.microsoft.com/en-us/windows/win32/api/Winsock2/nf-Winsock2-ioctlsocket) on the Windows app developer documentation website.

### WSAListen()/listen()
<a name="WSAListen"></a>

Setting a backlog size of `0` or less sets the backlog size to `0`. Setting the backlog size to a value greater than the implementation-specific maximum backlog size, which is currently `2048`, sets the backlog size to the implementation-specific maximum backlog size. Reducing the backlog size while connection requests exist on a listening socket rejects some of the connection requests until the number of connections is equal to, or less than, the new backlog size.

### WSASend()/send()
<a name="WSASend"></a>

No flags are supported for these functions. The flag values must be set to `0`. If you specify a different value, an error is returned.

### WSASetSockOpt()/setsockopt()
<a name="WSASetSockOpt"></a>

This function follows the Winsock2 implementation. However, only the following options are supported:
+ `SO_LINGER`
+ `SO_DONTLINGER`
+ `SO_RCVBUF`

`SO_RCVBUF` has a minimum value of `4096` bytes and a maximum value of `2` MB. Requested buffer sizes are rounded down to a power of `2`, or to `2` MB if the value is greater than `2` MB. Received buffer size defaults to `256` KB.

For more information, see [ ioctlsocket function](https://docs.microsoft.com/en-us/windows/win32/api/Winsock2/nf-Winsock2-ioctlsocket) on the Windows app developer documentation website.

### WSASocket()/socket()
<a name="WSASocket"></a>

This function returns a new `SOCKET`. With the AWS vsock SPI, this `SOCKET` is also a `HANDLE` that allows you to call functions, such as `ReadFile` and `WriteFile` directly on the `SOCKET`. 

This function must be called with `af = AF_VSOCK` and `type = SOCK_STREAM`. Only the `WSA_FLAG_OVERLAPPED` flag is supported when calling `WSASocket()`, which allows overlapped IO on the `SOCKET` that is returned. If `socket()` is called, the `WSA_FLAG_OVERLAPPED` flag is set. For more information about overlapped creation of sockets, see [ socket function](https://docs.microsoft.com/en-us/windows/win32/api/Winsock2/nf-Winsock2-socket) on the Windows app developer documentation website.

### WSAStringToAddress()
<a name="WSAStringToAddress"></a>

Converts a string in the format of `CID.Port` to a `sockaddr_vm`.

### WSARecv()/recv()
<a name="WSARecv"></a>

Only the `MSG_PEEK` flag is supported for this function.

## Unsupported Winsock2 functions
<a name="unsupported-apis"></a>

The following Winsock2 functions are not supported with AWS vsock sockets.
+ `WSACancelBlockingCall()`
+ `WSAAsyncSelect()`
+ `WSAGetQosByName()`
+ `WSAJoinLeaf()`
+ `WSARecvDisconnect()`
+ `WSASendDisconnect()`
+ `WSARecvFrom()`
+ `WSASendTo()`

## Known issues
<a name="known-issues"></a>

### Some IOs cannot be canceled
<a name="cancel"></a>

When calling `WSASend()`, `WSARecv()`, or `WSAIoctl()` on an overlapped socket, either with `lpOverlapped` omitted or with `lpCompletionRoutine` specified, the IO cannot be canceled by the user using `CancelIo` or `CancelIoEx`. `CancelIoEx` returns an error with `GetLastError()` returning `ERROR_NOT_FOUND`. All IOs can be canceled by calling `closesocket()`.