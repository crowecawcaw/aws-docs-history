

# Docker queue environment overview
<a name="containers-queue-environment"></a>

The default Docker queue environment declares the `EXPR` and `WRAP_ACTIONS` OpenJD extensions. Its own enter and exit actions manage the rootless Docker daemon and session container on the worker. Three wrap actions replace the actions of inner environments and tasks while the queue environment is active.

The following flow shows how the queue environment wraps a task action:

1. The portable job template provides an `onRun` command and its arguments.

1. The session runtime wraps the original `onRun` action inside `onWrapTaskRun` instead of running the command directly.

1. The hook passes `WrappedAction.Command`, `WrappedAction.Args`, and `WrappedAction.Environment` to a static wrap script as separate arguments.

1. The wrap script uses `docker container exec` to run the original command and arguments inside the rootless session container.

The wrapping environment's `onEnter` action starts the session container, and its `onExit` action stops the container. The container bind-mounts the session directory at the same path. It can also bind-mount persistent storage for reusable caches.

![A portable job template passes its original onRun action into the onWrapTaskRun boundary. The action passes to a static wrap script as WrappedAction values and runs inside a rootless session container. The queue environment starts and stops the container, which mounts the session directory and optional persistent storage.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/wrap-actions-flow.png)



| Queue environment action | Runs in | Purpose | 
| --- | --- | --- | 
| onEnter | Worker | Starts the rootless daemon, authenticates to Amazon ECR, pulls the image, and starts the session container. | 
| onWrapEnvEnter | Container | Runs an inner environment's enter action. | 
| onWrapTaskRun | Container | Runs each task's application command and arguments. | 
| onWrapEnvExit | Container | Runs an inner environment's exit action. | 
| onExit | Worker | Stops the session container, rootless daemon, and user manager. | 

The wrapping environment must define all three wrap actions. Each hook receives the original action through `WrappedAction.Command`, `WrappedAction.Args`, and `WrappedAction.Environment`. The following partial template shows how the default environment forwards those values:

```
specificationVersion: "environment-2023-09"
extensions:
  - WRAP_ACTIONS
  - EXPR
environment:
  name: DockerContainer
  script:
    actions:
      onWrapEnvEnter:
        command: bash
        args:
          - "{{Env.File.Wrap}}"
          - "{{ flatten([['-e', e] for e in WrappedAction.Environment]) }}"
          - "--"
          - "{{WrappedAction.Command}}"
          - "{{WrappedAction.Args}}"
      onWrapTaskRun:
        command: bash
        args:
          - "{{Env.File.Wrap}}"
          - "{{ flatten([['-e', e] for e in WrappedAction.Environment]) }}"
          - "--"
          - "{{WrappedAction.Command}}"
          - "{{WrappedAction.Args}}"
      onWrapEnvExit:
        command: bash
        args:
          - "{{Env.File.Wrap}}"
          - "{{ flatten([['-e', e] for e in WrappedAction.Environment]) }}"
          - "--"
          - "{{WrappedAction.Command}}"
          - "{{WrappedAction.Args}}"
```

The wrap script receives the command as an argument vector and runs the original action inside rootless Docker as the unprivileged `job-user` identity. The script forwards only the known usage-based license variables from the host. It doesn't forward AWS credentials into the container.

The default environment mounts the session working directory at the same path. It selects GPUs through the Container Device Interface (CDI) when available and propagates the wrapped action's exit status. For data-sharing details, see [Share the session working directory](containers-share-session-directory.md).

## Customize a Docker queue environment
<a name="containers-queue-customize"></a>

The console creates a default Docker queue environment. You can use that template as a starting point for application-specific mounts, environment variables, networking, image selection, and runtime options. Preserve the rootless daemon lifecycle, the session-directory mount, and all three wrap hooks when you customize the template.

The `EXPR` extension supports conditional expressions. The following partial enter-script example chooses between two images and adds GPU arguments only when the `UseGpu` parameter is true:

```
IMAGE={{ repr_sh(Param.GpuImage if Param.UseGpu else Param.CpuImage) }}
GPU_ARGS=({{ repr_sh(['--gpus', 'all'] if Param.UseGpu else []) }})

docker container run \
    --rm \
    --detach \
    "${GPU_ARGS[@]}" \
    --mount {{ repr_sh("type=bind,src=" + Session.WorkingDirectory + ",dst=" + Session.WorkingDirectory) }} \
    --workdir {{ repr_sh(Session.WorkingDirectory) }} \
    "$IMAGE"
```

You can also select a wrapper script conditionally in each hook. The following partial action chooses a container wrapper or host wrapper from one queue environment parameter:

```
onWrapTaskRun:
  command: bash
  args:
    - "{{ Env.File.WrapContainer if Param.RunInContainer else Env.File.WrapHost }}"
    - "{{ flatten([['-e', e] for e in WrappedAction.Environment]) }}"
    - "--"
    - "{{WrappedAction.Command}}"
    - "{{WrappedAction.Args}}"
```

Use the same runtime condition for `onWrapEnvEnter`, `onWrapTaskRun`, and `onWrapEnvExit`. Keeping all lifecycle phases in the same runtime prevents an inner environment from entering in one context and exiting in another. The `WRAP_ACTIONS` extension requires all three hooks even when a condition selects the host wrapper.

A host wrapper must apply `WrappedAction.Environment`, preserve the original argument boundaries, and return the wrapped action's exit status. Pass command and argument values as an argument vector. Don't combine raw values into a string for `bash -c`. For quoting rules, see [Command construction and escaping](containers-security.md#containers-security-command-construction).

## OpenJD specifications
<a name="containers-openjd-references"></a>

The [OpenJD expression language proposal](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0005-expression-language.md) on the GitHub website defines expression evaluation, typed paths, and session symbols.

The [OpenJD expression function library proposal](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0006-expression-function-library.md) on the GitHub website defines `flatten` and the `repr_*` functions.

The [OpenJD extended parameter types proposal](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0007-extend-parameter-types.md) on the GitHub website defines list-valued parameters that portable templates can use.

The [OpenJD environment wrap actions proposal](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0008-environment-wrap-actions.md) on the GitHub website defines the three wrap hooks and `WrappedAction.*` values.