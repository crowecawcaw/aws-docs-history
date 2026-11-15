

# Getting started with Docker
<a name="getting-started-docker"></a>

On any system that runs Docker, including Windows and macOS, you can run the emulator in a Docker container. We don’t publish a prebuilt image. You build one from a short Dockerfile that installs the Linux package.

First, install Docker. For the other prerequisites, see [Setting up AWS Emulator](setting-up.md).

## To build the AWS Emulator image
<a name="getting-started-docker-build"></a>

1. In an empty directory, create a file named `Dockerfile` with the following content.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
   ADD https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest/aws-emulator-x86_64.rpm /tmp/aws-emulator.rpm
   RUN rpm -i /tmp/aws-emulator.rpm && rm /tmp/aws-emulator.rpm \
       && mkdir -p /home/emulator && chown 1000 /home/emulator
   USER 1000
   ENV HOME=/home/emulator
   EXPOSE 9297
   ENTRYPOINT ["aws-emulator", "-b", "0.0.0.0"]
   ```

   On computers with Apple silicon or other Arm processors, use the Arm package instead. In the `ADD` line, replace `aws-emulator-x86_64.rpm` with `aws-emulator-aarch64.rpm`.

   The `-b 0.0.0.0` option makes the emulator listen on all addresses inside the container, so Docker can forward its port. The `docker run` command in the next procedure opens the port only to your own machine.

1. Build the image.

   ```
   docker build -t aws-emulator .
   ```

## To run AWS Emulator in a container
<a name="getting-started-docker-run"></a>

1. Create the directory that the container shares with your machine. On Linux, if you skip this step, Docker makes the directory owned by root, and your SDK can’t read it.

    **macOS and Linux** 

   ```
   mkdir -p ~/.aws/emulator
   ```

    **Windows PowerShell** 

   ```
   New-Item -ItemType Directory -Force "$env:USERPROFILE\.aws\emulator"
   ```

1. Start the container.

    **macOS and Linux** 

   ```
   PORT=9297
   docker run --rm --memory=2g --memory-swap=2g -p 127.0.0.1:$PORT:$PORT \
     -e HOME="$HOME" -v "$HOME/.aws/emulator:$HOME/.aws/emulator" \
     aws-emulator -p $PORT
   ```

    **Windows PowerShell** 

   ```
   $port = 9297
   docker run --rm --memory=2g --memory-swap=2g -p "127.0.0.1:${port}:${port}" `
     -v "$env:USERPROFILE\.aws\emulator:/home/emulator/.aws/emulator" `
     aws-emulator -p $port
   ```

   The `-v` option lets your SDK read the credentials and certificate that the emulator creates. It also keeps the telemetry ID between runs, so each run isn’t counted as a new install. On Linux, also add `--user "$(id -u):$(id -g)"` after `docker run` so the files belong to you. To turn off telemetry in the container, see [Turning telemetry off](telemetry.md#telemetry-opt-out).

   On macOS and Linux, `-e HOME` makes the emulator use the same paths in the container as on your computer. So the paths in its `config` file and startup line are correct on your computer. On Windows, they’re paths in the container.

   The `--memory` and `--memory-swap` options limit the emulator to 2 gibibytes (GiB) of memory, with no swap. If the container goes over the limit, it stops with exit code 137, and you lose the emulated resources.

   The startup message shows paths inside the container, such as `/home/emulator/.aws/emulator/config.toml`. Because of the `-v` option, that file is `config.toml` in the `.aws/emulator` folder that you mounted. Edit it there, if needed.

   Use `-p 127.0.0.1:9297:9297`, not `-p 9297:9297`. The short form opens the emulator to your whole network. Other computers could then reach it.

   To pass other emulator options, add them at the end of the command. For all options, see [AWS Emulator command reference](cli-reference.md).

1. In another terminal, set the environment variables for your SDK, as shown in [To point your SDK at a local emulator](point-sdk-to-emulator.md#point-sdk-env).

1. Run your code.

1. To stop the emulator, press **Ctrl\+C** in its terminal. The emulator deletes its files in `~/.aws/emulator/<port>/`, and Docker removes the container. You lose the emulated resources, because the emulator keeps them in memory.

To use another port, change `PORT` (`$port` in PowerShell). The command uses the port on both sides of Docker’s `-p` option and in the emulator’s `-p` option. They must match, because the emulator writes its port into the files that it creates.

To run several emulators at the same time, run the command in a separate terminal for each one, with a different port. Then use that emulator’s port in the environment variables for your SDK.

To keep each emulator’s credentials and certificate, change the port in all three places. If you change only the port on your computer, as in `-p 127.0.0.1:9300:9297`, the containers write to the same subdirectory of `~/.aws/emulator`. They then replace and delete each other’s files.

Don’t use the emulator’s `-p 0` option in a container. Docker can’t forward a port that the emulator picks when it starts.

## To remove the AWS Emulator image
<a name="getting-started-docker-remove"></a>

1. Stop each emulator that’s running. Press **Ctrl\+C** in its terminal.

1. Remove the image.

   ```
   docker image rm aws-emulator
   ```

1. (Optional) Delete the shared directory.
**Important**  
This step deletes all the files that the emulator keeps in your home directory. Do this only when you’re done with the emulator.

    **macOS and Linux** 

   ```
   rm -rf ~/.aws/emulator
   ```

    **Windows PowerShell** 

   ```
   Remove-Item -Recurse -Force "$env:USERPROFILE\.aws\emulator"
   ```