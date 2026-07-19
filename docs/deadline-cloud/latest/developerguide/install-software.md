# Install and configure software required for jobs

After you set up the Deadline Cloud worker agent, you can prepare the worker host with any software
that is required to run jobs.

When you submit a job to a queue with an associated `jobRunAsUser`, the job runs
as that user. When a job is submitted with commands that are not an absolute path, that command
must be found in the `PATH` of that user.

On Linux, you might specify the `PATH` for a user in one of the following:

- their `~/.bashrc` or `~/.bash_profile`
- system configuration files such as `/etc/profile.d/*`
  and `/etc/profile`
- shell startup scripts: `/etc/bashrc`.
  On Windows, you might specify the `PATH` for a user in one of the following:

- their user-specific environment variables
- the system-wide environment variables

## Install digital content creation tool adaptors

Deadline Cloud provides OpenJobDescription adaptors for using popular digital content creation (DCC)
applications. To use these adaptors in a customer-managed fleet, you must install the DCC software
and the application adaptors. Then, ensure the software's executable programs are available on
the system search path (for example, in the `PATH` environment variable).

To install a digital content creation (DCC) adaptor on a customer-managed fleet

1. Open a terminal:

   1. On Linux, open a terminal as the `root` user (or use
      `sudo` or `su`).
   2. On Windows, open an administrator command prompt or PowerShell terminal.

2. Install the adaptor package for your DCC application. The following example installs
   the Maya adaptor:

```
pip install deadline-cloud-for-maya
```

The following table lists the adaptor package name and documentation link for each
supported DCC application:

| DCC application                                                                                  | Adaptor package                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Adobe After Effects](../userguide/adobe-after-effects.md "../userguide/adobe-after-effects.md") | [deadline-cloud-for-after-effects](https://github.com/aws-deadline/deadline-cloud-for-after-effects "https://github.com/aws-deadline/deadline-cloud-for-after-effects") on GitHub |
| [Autodesk 3ds Max](../userguide/autodesk-3ds-max.md "../userguide/autodesk-3ds-max.md")          | [deadline-cloud-for-3ds-max](https://github.com/aws-deadline/deadline-cloud-for-3ds-max "https://github.com/aws-deadline/deadline-cloud-for-3ds-max") on GitHub                   |
| [Autodesk Maya](../userguide/autodesk-maya.md "../userguide/autodesk-maya.md")                   | [deadline-cloud-for-maya](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya") on GitHub                            |
| [Autodesk VRED](../userguide/autodesk-vred.md "../userguide/autodesk-vred.md")                   | [deadline-cloud-for-vred](https://github.com/aws-deadline/deadline-cloud-for-vred "https://github.com/aws-deadline/deadline-cloud-for-vred") on GitHub                            |
| [Blender](../userguide/blender.md "../userguide/blender.md")                                     | [deadline-cloud-for-blender](https://github.com/aws-deadline/deadline-cloud-for-blender "https://github.com/aws-deadline/deadline-cloud-for-blender") on GitHub                   |
| [Chaos V-Ray for Maya](../userguide/autodesk-maya.md "../userguide/autodesk-maya.md")            | [deadline-cloud-for-maya](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya") on GitHub                            |
| [Foundry Nuke](../userguide/foundry-nuke.md "../userguide/foundry-nuke.md")                      | [deadline-cloud-for-nuke](https://github.com/aws-deadline/deadline-cloud-for-nuke "https://github.com/aws-deadline/deadline-cloud-for-nuke") on GitHub                            |
| [KeyShot Studio](../userguide/keyshot.md "../userguide/keyshot.md")                              | [deadline-cloud-for-keyshot](https://github.com/aws-deadline/deadline-cloud-for-keyshot "https://github.com/aws-deadline/deadline-cloud-for-keyshot") on GitHub                   |
| [Maxon Cinema 4D](../userguide/maxon-cinema-4d.md "../userguide/maxon-cinema-4d.md")             | [deadline-cloud-for-cinema-4d](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d") on GitHub             |
| [Maxon Redshift for Maya](../userguide/autodesk-maya.md "../userguide/autodesk-maya.md")         | [deadline-cloud-for-maya](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya") on GitHub                            |
| [SideFX Houdini](../userguide/sidefx-houdini.md "../userguide/sidefx-houdini.md")                | [deadline-cloud-for-houdini](https://github.com/aws-deadline/deadline-cloud-for-houdini "https://github.com/aws-deadline/deadline-cloud-for-houdini") on GitHub                   |
| [Unreal Engine](../userguide/epic-unreal-engine.md "../userguide/epic-unreal-engine.md")         | [deadline-cloud-for-unreal-engine](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine "https://github.com/aws-deadline/deadline-cloud-for-unreal-engine") on GitHub |

###### Installing multiple adaptors on the same worker

If you install more than one DCC adaptor on the same worker, install each adaptor
into its own Python virtual environment. Adaptors can pin different version ranges
for shared Python packages (for example, `deadline` or
`openjd-adaptor-runtime`). An environment with multiple adaptors might fail
with a `ResolutionImpossible` error. It might also silently downgrade a shared
package and break the adaptors that need the newer version.
