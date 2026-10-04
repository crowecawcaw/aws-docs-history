

# Share the session working directory
<a name="containers-share-session-directory"></a>

Deadline Cloud writes embedded files and prepares job attachment paths under `Session.WorkingDirectory`. OpenJD values such as `Task.File.Run` contain absolute paths in that directory. A container can't access those paths unless its filesystem includes the session directory.

The default Docker queue environment bind-mounts the directory at the same path and sets it as the container working directory. The same-path mapping lets a portable action use OpenJD paths without translating them for Docker.

When you create a custom wrapping environment, include both options in the container start command:

```
--mount {{ repr_sh("type=bind,src=" + Session.WorkingDirectory + ",dst=" + Session.WorkingDirectory) }} \
--workdir {{ repr_sh(Session.WorkingDirectory) }}
```

Keep the mount read-write when tasks create output or temporary files. Use a separate read-only mount for additional input data that no container action needs to change.

The default wrap script runs container actions as the unprivileged `job-user` identity on the worker. Files created in the mounted directory remain accessible to later session actions.

To verify the mount, submit a task that reads an embedded file, creates a file under `Session.WorkingDirectory`, and then reads that file in a later step.