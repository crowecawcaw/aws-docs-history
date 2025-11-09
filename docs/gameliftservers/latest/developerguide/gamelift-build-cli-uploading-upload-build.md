# Create a build from a

file directory

To create a game build stored in any location, including a local directory, use
the [`upload-build`](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md") AWS CLI command. This command creates a new
build record in Amazon GameLift Servers and uploads files from a location that you specify.

**Send an upload request.** In a command line window,
enter the following **upload-build** command and parameters.

```
aws gamelift upload-build \
    --name `user-defined name of build` \
    --operating-system `supported OS` \
    --server-sdk-version `server SDK for Amazon GameLift Servers version` \
    --build-root `build path` \
    --build-version `user-defined build number` \
    --region `region name`
```

- **operating-system** – The game server build's
  runtime environment. You must specify an OS value. You can't update this later.
- **server-sdk-version** – The version of the Amazon GameLift Servers
  server SDK that your game server is integrated with. If you don't provide a
  value, Amazon GameLift Servers uses the default value `4.0.2`. If you specify an
  incorrect server SDK version, the game server build might fail when calling
  `InitSdk` to establish a connection to the Amazon GameLift Servers
  service.
- **build-root** – The directory path of your
  build files.
- **name** – A descriptive name for the new
  build.
- **build-version** – The version details for the
  build files.
- **region** – The AWS Region where you want to
  create your build. Create the build in the Region where you plan to
  deploy fleets. If you're deploying your game in multiple Regions, create
  a build in each Region.

###### Note

View your current default Region using the [**aws
configure get region**](../../../cli/latest/reference/configure/get.md "../../../cli/latest/reference/configure/get.md"). To change your
default Region, use the [**aws
configure set region `region
 name`**](../../../cli/latest/reference/configure/set.md "../../../cli/latest/reference/configure/set.md") command.
_Examples_

```
aws gamelift upload-build \
 --operating-system AMAZON\_LINUX\_2023 \
 --server-sdk-version "5.0.0" \
    --build-root "~/mygame" \
    --name "My Game Nightly Build" \
    --build-version "build 255" \
    --region us-west-2
```

```
aws gamelift upload-build \
 --operating-system WINDOWS\_2022 \
 --server-sdk-version "5.0.0" \
    --build-root "C:\mygame" \
    --name "My Game Nightly Build" \
    --build-version "build 255" \
    --region us-west-2
```

In response to your upload request, Amazon GameLift Servers provides upload progress. On a
successful upload, Amazon GameLift Servers returns the new build record ID. Upload time depends on
the size of your game files and the connection speed.
