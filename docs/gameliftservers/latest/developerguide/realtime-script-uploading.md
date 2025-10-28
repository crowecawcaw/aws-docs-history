# Deploy a script for Amazon GameLift Servers Realtime

When you're ready to deploy Amazon GameLift Servers Realtime for your game, upload completed Realtime server script
files to Amazon GameLift Servers. Do this by creating a Amazon GameLift Servers script resource and specifying the location of
your script files. You can also update server script files that are already deployed by
uploading new files for an existing script resource.

When you create a new script resource, Amazon GameLift Servers assigns it a unique script ID (for example,
`script-1111aaaa-22bb-33cc-44dd-5555eeee66ff`) and uploads a copy of the
script files. Upload time depends on the size of your script files and on your connection
speed.

After you create the script resource, Amazon GameLift Servers deploys the script with a new Amazon GameLift Servers Realtime fleet.
Amazon GameLift Servers installs your server script onto each instance in the fleet, placing the script files
in `/local/game`.

To troubleshoot fleet activation problems related to the server script, see [Debug Amazon GameLift Servers fleet issues](fleets-creating-debug.md "fleets-creating-debug.md").

## Package script files

Your server script can include one or more files combined into a single .zip file for
uploading. The .zip file must contain all files that your script needs to run.

You can store your zipped script files in either a local file directory or in an
Amazon Simple Storage Service (Amazon S3) bucket.
