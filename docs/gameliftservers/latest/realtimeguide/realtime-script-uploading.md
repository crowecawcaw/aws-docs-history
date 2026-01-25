# Upload a script for Amazon GameLift Servers Realtime servers

When you're ready to deploy Amazon GameLift Servers Realtime for your game, upload completed Realtime server script
files to Amazon GameLift Servers. Do this by creating a Amazon GameLift Servers script resource and specifying the location of
your script files. You can also update server script files that are already deployed by
uploading new files for an existing script resource.

When creating a script, you can choose the Node.js runtime version. Node.js 24.x runs on Amazon Linux 2023,
while Node.js 10.x uses Amazon Linux 2. Amazon GameLift Servers automatically manages Node.js minor and patch version updates for
new fleets. The runtime will remain unchanged for a fleet once it is created. If you would like to pick a
specific minor and patch version of Node.js you can install it using an install script. See
[Add an install script (optional)](#realtime-script-uploading-install-script "#realtime-script-uploading-install-script").

When you create a new script resource, Amazon GameLift Servers assigns it a unique script ID (for example,
`script-1111aaaa-22bb-33cc-44dd-5555eeee66ff`) and uploads a copy of the
script files. Upload time depends on the size of your script files and on your connection
speed.

After you create the script resource, Amazon GameLift Servers deploys the script with a new Amazon GameLift Servers Realtime fleet.
Amazon GameLift Servers installs your server script onto each instance in the fleet, placing the script files
in `/local/game`.

To troubleshoot fleet activation problems related to the server script, see [Debug managed EC2 fleets for Amazon GameLift Servers Realtime](fleets-creating-debug-realtime.md "fleets-creating-debug-realtime.md").

## Package script files

Your server script can include one or more files combined into a single .zip file for
uploading. The .zip file must contain all files that your script needs to run.

You can store your zipped script files in either a local file directory or in an
Amazon Simple Storage Service (Amazon S3) bucket.

### Add an install script (optional)

Similar to [Add a build install script](../developerguide/gamelift-build-cli-uploading-install.md "../developerguide/gamelift-build-cli-uploading-install.md") for an Amazon GameLift Servers build, you can optionally add an install script to
customize the runtime environment for your Realtime script. This feature is only available for
scripts using Node.js version 24.x and later.

To add an install script, include a file named
`install.sh` in the root directory of your script .zip file. Amazon GameLift Servers will automatically
detect and execute this script during fleet deployment.

###### Example Install script example

This example `install.sh` file installs Node.js 24.10.0 to replace the default
Node.js 24.x runtime:

```
#!/bin/bash

# Remove existing Node.js installation
sudo rm -rf /local/NodeJS/*

# Install Node.js v24.10.0
curl -L https://nodejs.org/dist/v24.10.0/node-v24.10.0-linux-x64.tar.xz | sudo tar -xJ -C /local/NodeJS --strip-components=1
```
