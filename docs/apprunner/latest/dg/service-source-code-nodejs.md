# Using the Node.js platform

###### Important

App Runner will end the support for **Node.js 12**, **Node.js 14**, **Node.js 16** and **Node.js 18** on December 1, 2025. For recommendations and more
information, see [End of support for managed runtime
versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

The AWS App Runner Node.js platform provides managed runtimes. Each runtime makes it easy to build
and run containers with web applications based on a Node.js version. When you use a Node.js
runtime, App Runner starts with a managed Node.js runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains the runtime
package for a version of Node.js and some tools. App Runner uses this managed runtime image as a base
image, and adds your application code to build a Docker image. It then deploys this image to run
your web service in a container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

For valid Node.js runtime names and versions, see [Node.js runtime release
information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md").

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

Version syntax for Node.js runtimes:
``major`[.`minor`[.`patch`]]`

For example: `22.14.0`

The following examples demonstrate version locking:

- `22.14` – Lock the major and minor versions. App Runner updates only patch
  versions.
- `22.14.0` – Lock to a specific patch version. App Runner doesn't update your
  runtime version.

###### Topics

- [Node.js runtime configuration](#service-source-code-nodejs.config "#service-source-code-nodejs.config")
- [Callouts for specific runtime
  versions](#service-source-code-nodejs.callouts "#service-source-code-nodejs.callouts")
- [Node.js runtime examples](#service-source-code-nodejs.examples "#service-source-code-nodejs.examples")
- [Node.js runtime release
  information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md")

## Node.js runtime configuration

When you choose a managed runtime, you must also configure, as a minimum, build and run commands. You configure them while [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") your App Runner service. You can do this using one of the following methods:

- Using the App Runner console – Specify the commands in the **Configure build** section of the
  creation process or configuration tab.
- Using the App Runner API – Call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operation. Specify the commands using the `BuildCommand` and
  `StartCommand` members of the [CodeConfigurationValues](../api/API_CodeConfigurationValues.md "../api/API_CodeConfigurationValues.md") data type.
- Using a [configuration file](config-file.md "config-file.md") – Specify one or more build commands in up to
  three build phases, and a single run command that serves to start your application. There are additional optional configuration settings.

Providing a configuration file is optional. When you create an App Runner service using the console or the API, you specify if App Runner gets your configuration
settings directly when it's created or from a configuration file.

With Node.js runtimes specifically, you can also configure the build and runtime using a
JSON file named `package.json` in the root of your source repository. Using
this file, you can configure the Node.js engine version, dependency packages, and various
commands (command line applications). Package managers such as npm or yarn interpret this file
as input for their commands.

For example:

- **npm install** installs packages defined by the
  `dependencies` and `devDependencies` node in
  `package.json`.
- **npm start** or **npm run start** runs the command
  defined by the `scripts/start` node in
  `package.json`.

The following is an example `package.json` file.

```
{
  "name": "node-js-getting-started",
  "version": "0.3.0",
  "description": "A sample Node.js app using Express 4",
  "engines": {
    "node": "22.14.0"
  },
  "scripts": {
    "start": "node index.js",
    "test": "node test.js"
  },
  "dependencies": {
    "cool-ascii-faces": "^1.3.4",
    "ejs": "^2.5.6",
    "express": "^4.15.2"
  },
  "devDependencies": {
    "got": "^11.3.0",
    "tape": "^4.7.0"
  }
}
```

For more information about `package.json`, see

[Creating a package.json
file](https://docs.npmjs.com/creating-a-package-json-file "https://docs.npmjs.com/creating-a-package-json-file") on the _npm Docs_ website.

###### Tips

- If your `package.json` file defines a **start**
  command, you can use it as a **run** command in your App Runner configuration
  file, as the following example shows.

package.json

```
{
  "scripts": {
    "start": "node index.js"
  }
}
```

apprunner.yaml

```
run:
  command: npm start
```

- When you run **npm install** in your development environment, npm
  creates the file `package-lock.json`. This file contains a snapshot
  of the package versions npm just installed. Thereafter, when npm installs dependencies,
  it uses these exact versions. If you install yarn it creates a
  `yarn.lock` file. Commit these files to your source code repository
  to ensure that your application is installed with the versions of dependencies that you
  developed and tested it with.
- You can also use an App Runner configuration file to configure the Node.js version and
  start command. When you do this, these definitions override the ones in
  `package.json`. A conflict between the `node` version in
  `package.json` and the `runtime-version` value in the
  App Runner configuration file causes the App Runner build phase to fail.

## Callouts for specific runtime

versions

### Node.js 22 and Node.js 18

(revised App Runner build)

App Runner now runs an updated build process for applications based on the following runtime versions: Python 3.11, Node.js 22, and Node.js 18. If your application
runs on either one of these runtime versions, see [Managed runtime versions and the App Runner
build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail") for more
information about the revised build process. Applications that use all other runtime versions are not affected, and they continue to use the original build
process.

## Node.js runtime examples

The following examples show App Runner configuration files for building and running a Node.js
service.

###### Note

The runtime version that's used in these examples is `22.14.0`.
You can replace it with a version you want to use. For latest supported Node.js runtime
version, see [Node.js runtime release
information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md").

This example shows a minimal configuration file that you can use with a Node.js
managed runtime. For the assumptions that App Runner makes with a minimal configuration file,
see [Configuration file
examples](config-file-examples.md#config-file-examples.managed "config-file-examples.md#config-file-examples.managed").

###### Example apprunner.yaml

```
version: 1.0
runtime: nodejs22
build:
  commands:
    build:
      - npm install --production
run:
  command: node app.js
```

This example shows the use of all the configuration keys with a Node.js managed
runtime.

###### Note

The runtime version that's used in these examples is
`22.14.0`. You can replace it with a version you want to use.
For latest supported Node.js runtime version, see [Node.js runtime release
information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: nodejs22
build:
  commands:
    pre-build:
      - npm install --only=dev
      - node test.js
    build:
      - npm install --production
    post-build:
      - node node_modules/ejs/postinstall.js
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `22.14.0`
  command: node app.js
  network:
    port: 8000
    env: APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
```

This example shows the use of all the configuration keys with a Node.js managed
runtime in the `apprunner.yaml`. This example include a
`pre-run` section, since this version of Node.js uses the
revised App Runner build.

The `pre-run` parameter is only supported by the revised App Runner build.
Do not insert this parameter in your configuration file if your application uses runtime versions that are supported by the
original App Runner build. For more information, see [Managed runtime versions and the App Runner
build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

###### Note

The runtime version that's used in these examples is
`22.14.0`. You can replace it with a version you want to use.
For latest supported Node.js runtime version, see [Node.js runtime release
information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: nodejs22
build:
  commands:
    pre-build:
      - npm install --only=dev
      - node test.js
    build:
      - npm install --production
    post-build:
      - node node_modules/ejs/postinstall.js
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `22.14.0`
  pre-run:
    - node copy-global-files.js
  command: node app.js
  network:
    port: 8000
    env: APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
```

This example shows how to configure a Node.js application that's developed with Grunt.
[Grunt](https://gruntjs.com/ "https://gruntjs.com/") is a command line JavaScript task
runner. It runs repetitive tasks and manages process automation to reduce human error.
Grunt and Grunt plugins are installed and managed using npm. You configure Grunt by
including the `Gruntfile.js` file in the root of your source
repository.

###### Example package.json

```
{
  "scripts": {
    "build": "grunt uglify",
    "start": "node app.js"
  },
  "devDependencies": {
    "grunt": "~0.4.5",
    "grunt-contrib-jshint": "~0.10.0",
    "grunt-contrib-nodeunit": "~0.4.1",
    "grunt-contrib-uglify": "~0.5.0"
  },
  "dependencies": {
    "express": "^4.15.2"
  },
}
```

###### Example Gruntfile.js

```
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: 'build/<%= pkg.name %>.min.js'
      }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);

};
```

###### Example apprunner.yaml

###### Note

The runtime version that's used in these examples is
`22.14.0`. You can replace it with a version you want to
use. For latest supported Node.js runtime version, see [Node.js runtime release
information](service-source-code-nodejs-releases.md "service-source-code-nodejs-releases.md").

```
version: 1.0
runtime: nodejs22
build:
  commands:
    pre-build:
      - npm install grunt grunt-cli
      - npm install --only=dev
      - npm run build
    build:
      - npm install --production
run:
  runtime-version: `22.14.0`
  command: node app.js
  network:
    port: 8000
    env: APP_PORT
```
