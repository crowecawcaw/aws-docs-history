

# Stopping Amazon DCV sessions
<a name="managing-sessions-lifecycle-stop"></a>

A console session can only be stopped by the administrator on Windows Amazon DCV servers, and the root user on Linux and macOS Amazon DCV servers. A virtual session on a Linux Amazon DCV server can only be stopped by the root user or the Amazon DCV user who created it. 

**Note**  
Stopping a session closes all of the applications that are running in the session.

To stop a console or virtual session on a Windows, Linux, or macOS Amazon DCV server, use the `dcv close-session` command and specify the unique session ID.

**Topics**
+ [Syntax](#managing-sessions-lifecycle-stop-syntax)
+ [Example](#example)

## Syntax
<a name="managing-sessions-lifecycle-stop-syntax"></a>

```
dcv close-session {{session-id}}
```

## Example
<a name="example"></a>

For example, the following command stops a session with the unique ID of `my-session`.

```
dcv close-session {{my-session}}
```