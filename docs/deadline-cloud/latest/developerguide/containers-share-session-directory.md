

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

## Return output files from a container
<a name="containers-session-directory-outputs"></a>

Deadline Cloud uploads output files to job attachments only from the output locations that the job template declares. A job attachments output location is a `PATH` job parameter with a `dataFlow` value of `OUT`. Files in an output location appear in Deadline Cloud monitor and download with `deadline job download-output`. Files that the container writes anywhere else stay on the worker and are deleted with the session. That includes other paths in the session working directory.

When no `SHARED` location in the job's storage profile covers an output location, job attachments maps it to a path in the session working directory.

The session directory is mounted at the same path inside the container, so pass the parameter value to the application as its output directory. The following partial job template declares an output location and passes it to the task command:

```
parameterDefinitions:
- name: OutputDir
  type: PATH
  objectType: DIRECTORY
  dataFlow: OUT
  default: ./output
steps:
- name: Process
  script:
    actions:
      onRun:
        command: my-app
        args: ["--output-dir", "{{Param.OutputDir}}"]
```

If the application writes only to a fixed path inside the image, copy the files into the output location at the end of the task. A symbolic link to a path that exists only inside the container doesn't resolve on the worker host, so the worker skips it.

The worker uploads outputs as the job user. The default wrap script runs container actions as the container's root user, which rootless Docker maps to the job user on the worker host. If your custom environment runs actions as a different user, files that it creates might be unreadable to the job user, and the output upload fails. In that case, change the owner of the output files to the container's root user at the end of the task. For the full upload rules, see [how the worker chooses output files](getting-output-files-from-a-job.md#job-attachments-output-file-rules).