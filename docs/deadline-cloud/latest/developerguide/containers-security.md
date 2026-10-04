

# Security and best practices for container jobs
<a name="containers-security"></a>

## Rootless runtime
<a name="containers-security-rootless"></a>

Deadline Cloud runs Docker in rootless mode. Container actions run as the unprivileged `job-user` identity and don't grant root access to the worker. The managed Docker configuration also enables the `no-new-privileges` setting and uses CDI for GPU access.

Don't add privileged container options, passwordless `sudo`, or access to a root-owned Docker socket. Don't mount the Docker socket inside the workload container.

## Command construction and escaping
<a name="containers-security-command-construction"></a>

Prefer argument-vector forwarding. The default wrap environment passes `WrappedAction.Command` and each value in `WrappedAction.Args` as separate arguments to `docker container exec`. No shell parses those values a second time.

Don't interpolate raw wrapped values into a command such as `bash -c "{{WrappedAction.Command}} {{WrappedAction.Args}}"`. Shell metacharacters in a command or argument can change how the shell parses that command.

When you must embed a value in text that another language parses, use the representation function for that language:


| Parser | Function | Use | 
| --- | --- | --- | 
| POSIX shell | repr\_sh | Shell arguments and paths. | 
| Python | repr\_py | Python literals embedded in Python source. | 
| JSON | repr\_json | Values embedded in a JSON document. | 
| PowerShell | repr\_pwsh | PowerShell literals. | 
| Windows command scripts | repr\_cmd | Values parsed by cmd.exe. | 

A representation function protects only the language that it targets. For example, `repr_py` produces a Python literal, not a shell argument. Pass job parameters as action arguments when the application already accepts an argument vector.

Reference `WrappedAction.*` only in a wrap hook's `command` or `args`. Embedded files are shared by all actions in the environment, including `onEnter` and `onExit`, where wrapped-action values aren't in scope. Keep the embedded wrap script static and pass the wrapped action to it as arguments.

## Images, permissions, and data
<a name="containers-security-images"></a>
+ Use a fixed image version or digest so every session receives the intended image contents.
+ Give build identities permission to push images. Give queue and fleet roles read-only Amazon ECR access.
+ Don't store AWS credentials, license secrets, or private keys in an image.
+ Forward only the environment variables required by the workload. The default queue environment forwards an allowlist of usage-based license variables and doesn't forward the host's AWS credentials.
+ Mount only the directories that the workload requires. Use read-only mounts for input data when no action needs to modify it.
+ Stop only the container created for the current session. Don't prune or stop unrelated containers on the worker.