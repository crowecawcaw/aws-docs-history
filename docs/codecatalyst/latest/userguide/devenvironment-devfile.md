Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring a devfile for a Dev Environment

A _devfile_ is an open standard that helps you to
customize your development Dev Environments across your team. A devfile is a YAML file that
codifies your required development tools. By configuring a devfile, you can pre-determine the
project tools and application libraries you need and Amazon CodeCatalyst installs them to your
Dev Environment for you. The devfile is specific to the repository for which it was created, and
you can create a separate devfile for each repository. Your Dev Environment supports commands and
events, and provides a default universal devfile image.

If you create a project using the empty blueprint, you can create a devfile manually. If
you create a project using a different blueprint, CodeCatalyst creates a devfile automatically.
The `/projects` directory of a Dev Environment stores the files that are pulled from
the source repository and the devfile. The `/home` directory, which is empty when
you first create a Dev Environment, stores the files you create while using your Dev Environment.
Everything in the `/projects` and `/home` directories of a Dev Environment
is stored persistently.

###### Note

The `/home` folder only changes if you change the name of the devfile or
devfile component name. If you change the devfile or devfile component name, the contents of
the `/home` directory are replaced and your previous `/home` directory
data cannot be recovered.

If you create a Dev Environment with a source repository that does not contain a devfile in
its root, or if you create a Dev Environment without a source repository, a default universal
devfile is applied to the source repository automatically. The same default universal devfile
image is used for all IDEs. CodeCatalyst currently supports devfile version 2.0.0. For more information about the devfile, see [Devfile schema - Version 2.0.0](https://devfile.io/docs/2.0.0/devfile-schema "https://devfile.io/docs/2.0.0/devfile-schema").

###### Note

You can only include public container images in your devfile.

Note that VPC-connected Dev Environments only support the following devfile images:

- Universal image
- Private Amazon ECR images, if the repository is in the same region as the VPC

###### Topics

- [Editing a repository devfile for a
  Dev Environment](devenvironment-devfile-moving.md "devenvironment-devfile-moving.md")
- [Devfile features supported by CodeCatalyst](#devenvironment-devfile-support "#devenvironment-devfile-support")
- [Example of a devfile for a Dev Environment](#devenvironment-devfile-example "#devenvironment-devfile-example")
- [Troubleshooting a repository devfile using recovery mode](#devenvironment-devfile-recovery "#devenvironment-devfile-recovery")
- [Specifying universal devfile images for a Dev Environment](devenvironment-universal-image.md "devenvironment-universal-image.md")
- [Devfile commands](devenvironment-devfile-commands.md "devenvironment-devfile-commands.md")
- [Devfile events](devenvironment-devfile-events.md "devenvironment-devfile-events.md")
- [Devfile components](devenvironment-devfile-components.md "devenvironment-devfile-components.md")

## Devfile features supported by CodeCatalyst

CodeCatalyst supports the following devfile features on version 2.0.0. For more information about the devfile, see [Devfile schema - Version 2.0.0](https://devfile.io/docs/2.0.0/devfile-schema "https://devfile.io/docs/2.0.0/devfile-schema").

| Feature        | Type                 |
| -------------- | -------------------- |
| `exec`         | Command              |
| `postStart`    | Event                |
| `container`    | Component            |
| `args`         | Component Properties |
| `env`          | Component Properties |
| `mountSources` | Component Properties |
| `volumeMounts` | Component Properties |

## Example of a devfile for a Dev Environment

The following is an example of a simple devfile.

```
schemaVersion: 2.0.0
metadata:
  name: al2
components:
  - name: test
    container:
      image: public.ecr.aws/amazonlinux/amazonlinux:2
      mountSources: true
      command: ['sleep', 'infinity']
  - name: dockerstore
commands:
  - id: setupscript
    exec:
      component: test
      commandLine: "chmod +x script.sh"
      workingDir: /projects/devfiles
  - id: executescript
    exec:
      component: test
      commandLine: "/projects/devfiles/script.sh"
  - id: yumupdate
    exec:
      component: test
      commandLine: "yum -y update --security"
events:
  postStart:
    - setupscript
    - executescript
    - yumupdate

```

Devfile startup, command, and event logs are captured and stored in
`/aws/mde/logs`. To debug devfile behaviour, start up your Dev Environment using a
working devfile and access the logs.

## Troubleshooting a repository devfile using recovery mode

If there's a problem starting your devfile, it will enter recovery mode so that you can still connect to your environment and fix your
devfile. While in recovery mode, running `/aws/mde/mde status` won’t contain the location of your devfile.

```
{
            "status": "STABLE"
        }
```

You can check the error in the logs under `/aws/mde/logs`, fix the devfile, and try running `/aws/mde/mde start` again.
