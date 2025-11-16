# Understanding Amazon DCV sessions

Amazon DCV offers two types of sessions—console sessions and virtual sessions. The following table summarizes the differences betweeen
the two types of sessions.

| Session type | Support                                      | Multiple sessions                                             | Required permissions                             | Direct screen capture                                                                                     | GPU-accelerated OpenGL support       |
| ------------ | -------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Console      | Linux, macOS, and Windows Amazon DCV servers | No, only one console session allowed on each server           | Only the admin user can start and close sessions | Yes                                                                                                       | Yes, without additional software     |
| Virtual      | Linux Amazon DCV servers only                | Yes, multiple virtual sessions are allowed on a single server | Any user can start and close sessions            | No, a dedicated X server (Xdcv), runs for each virtual session. The screen is captured from the X server. | Yes, but requires the DCV-GL package |

###### Note

You can't run console and virtual sessions on the same Amazon DCV server at the same time.

## Console sessions

Console sessions are supported on Windows, Linux, and macOS Amazon DCV servers. If you're using a Windows or macOS Amazon DCV server, you can only use console
sessions.

Only one console session can be hosted on the Amazon DCV server at a time. Console sessions are created and managed by the Administrator on
Windows Amazon DCV servers and the root user on Linux and macOS Amazon DCV servers.

With console sessions, Amazon DCV directly captures the content of the desktop screen. If the server is configured with a GPU, Amazon DCV
console sessions have direct access to the GPU.

## Virtual Sessions

Virtual sessions are supported on Linux Amazon DCV servers only.

You can host multiple virtual sessions on the same Amazon DCV server at the same time. Virtual sessions are created and managed by Amazon DCV
users. Amazon DCV users can only manage sessions that they have created. The root user can manage all virtual sessions that are currently
running on the Amazon DCV server.

With virtual sessions, Amazon DCV starts an X server instance, `Xdcv`, and runs a desktop environment inside the X server.
Amazon DCV starts a new dedicated X server instance for each virtual session. Each virtual session uses the display provided by its X
server instance.

###### Note

While Amazon DCV ensures that each virtual session has an independent `Xdcv` display, many other system resources,
including files in the user's home folder, D-Bus services, and devices, are per-user and thus will be shared and accessible
across multiple virtual sessions for the same user.

You should not run multiple virtual sessions on the same Amazon DCV server for the same user at the same time, unless you have set up
your Operating System to mitigate possible concerns about the shared resources.

If the `dcv-gl` package is installed and licensed, Amazon DCV virtual sessions share access to the server's GPUs. To share
hardware-based OpenGL across multiple virtual sessions, you must connect the virtual X server instance to the GPU by configuring the
`dcv-gl.conf` file.
