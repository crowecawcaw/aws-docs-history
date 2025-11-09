Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with devfiles

Consult the following sections to troubleshoot problems related to devfiles in CodeCatalyst. For more
information on devfiles, see [Configuring a devfile for a Dev Environment](devenvironment-devfile.md "devenvironment-devfile.md").

###### Topics

- [My Dev Environment is using
  the default universal devfile even though I have implemented a custom image in a
  custom devfile](#troubleshooting-devenvironments-custom-image "#troubleshooting-devenvironments-custom-image")
- [My project is not
  building in my Dev Environment with the default universal devfile](#troubleshooting-devenvironments-default-image "#troubleshooting-devenvironments-default-image")
- [I want to move a repository devfile for a
  Dev Environment](#troubleshooting-devenvironments-devfile-moving "#troubleshooting-devenvironments-devfile-moving")
- [I'm having a problem starting my devfile](#troubleshooting-devenvironments-devfile-recovery "#troubleshooting-devenvironments-devfile-recovery")
- [I'm not sure how to check my devfile status](#troubleshooting-devenvironments-devfile-status "#troubleshooting-devenvironments-devfile-status")
- [My devfile is not compatible with the tooling provided in the latest image](#troubleshooting-devenvironments-devfile-version "#troubleshooting-devenvironments-devfile-version")

## My Dev Environment is using

the default universal devfile even though I have implemented a custom image in a
custom devfile

If CodeCatalyst encounter errors while starting a Dev Environment that is using a custom devfile, the Dev Environment defaults to the default universal devfile. To fix the problem,
you can check the exact error in the logs under `/aws/mde/logs/devfile.log`. You can also check if `postStart` execution
was successful in your logs: `/aws/mde/logs/devfileCommand.log`.

## My project is not

building in my Dev Environment with the default universal devfile

To fix the problem check that you are not using a custom devfile. If you are not using a custom devfile, view the `devfile.yaml` file in the source repository of the project to locate and fix any errors.

## I want to move a repository devfile for a

Dev Environment

You can move the default devfile in `/projects/devfile.yaml` to your source code repository. To update the
location of the devfile, use following command:
`/aws/mde/mde start --location `repository-name`/devfile.yaml`.

## I'm having a problem starting my devfile

If there's a problem starting your devfile, it will enter recovery mode so that you can still connect to your environment and fix your
devfile. While in recovery mode, running `/aws/mde/mde status` won’t contain the location of your devfile.

```
{
    "status": "STABLE"
}
```

You can check the error in the logs under `/aws/mde/logs`, fix the devfile, and try running `/aws/mde/mde start` again.

## I'm not sure how to check my devfile status

You can check your devfile status by running `/aws/mde/mde status`. After running this command, you may see one of the following:

- `{"status": "STABLE", "location": "devfile.yaml" }`

This indicates that your devfile is correct.

- `{"status": "STABLE" }`

This indicates that your devfile is could not start and has entered recovery mode.

You can check the exact error in the logs under `/aws/mde/logs/devfile.log`.

You can also check if `postStart` execution
was successful in your logs: `/aws/mde/logs/devfileCommand.log`.

For more information, see [Specifying universal devfile images for a Dev Environment](devenvironment-universal-image.md "devenvironment-universal-image.md").

## My devfile is not compatible with the tooling provided in the latest image

In your Dev Environment, `devfile` or `devfile postStart` may fail if the `latest` tooling does not have the tooling required for a specific project. To fix the problem, do the following:

1. Navigate to your devfile.
2. In your devfile, update to a granular image version instead of `latest`. It may look similar to the following:

```
components:
  - container:
      image: public.ecr.aws/amazonlinux/universal-image:1.0
```

3. Create a new Dev Environment using the updated devfile.
