# Package your game build files

Before uploading your configured game server to Amazon GameLift Servers, package the game build files
into a build directory. This process is a requirement when hosting with an EC2 managed
fleet, and is a best practice when hosting with an Anywhere fleet. The build directory
should include all the components that are required to run your game servers and host
game sessions. This might include the following:

- **Game server binaries** – The binary
  files required to run the game server. A build can include binaries for multiple
  game servers built to run on the same platform. For a list of supported
  platforms, see [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md").
- **Dependencies** – Any dependent files
  that your game server executables require to run. Examples include assets,
  configuration files, and dependent libraries.

###### Note

For game builds created with the server SDK for Amazon GameLift Servers for C++ (including those
created with the Unreal plugin), include the OpenSSL DLL for the same
version of OpenSSL that you built the server SDK with. See the server SDK
README file for more details.

- **Install script** (Optional) – A script
  file to handle tasks that install your game build on Amazon GameLift Servers hosting servers.
  Place this file at the root of the build directory. Amazon GameLift Servers runs the install
  script as part of fleet creation.
  You can set up any application in your build, including your install script, to access
  your resources securely on other AWS services. For information about ways to do this,
  see [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").

After you've packaged your build files, make sure that your game server can run on a
clean installation of your target OS to verify that all required dependencies are
included and that your install script is accurate.
