# Configuring your application's dependencies on Elastic Beanstalk

Your application might have dependencies on some Node.js modules, such as the ones you specify in `require()` statements.
These modules are stored in a `node_modules` directory. When your application runs, Node.js loads the modules from this
directory. For more information, see [Loading from node_modules
folders](https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders "https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders") in the Node.js documentation.

You can specify these module dependencies using a `package.json` file. If Elastic Beanstalk detects this file and a
`node_modules` directory isn't present, Elastic Beanstalk runs `npm install` as the _webapp_ user. The `npm
 install` command installs the dependencies in the `node_modules` directory, which Elastic Beanstalk creates beforehand. The `npm
 install` command accesses the packages listed in the `package.json` file from the public npm registry or other locations. For
more information, see the [npm Docs](https://docs.npmjs.com/about-the-public-npm-registry "https://docs.npmjs.com/about-the-public-npm-registry") website.

If Elastic Beanstalk detects the `node_modules` directory, Elastic Beanstalk doesn't run `npm install`, even if a
`package.json` file exists. Elastic Beanstalk assumes that the dependency packages are available in the `node_modules`
directory for Node.js to access and load.

The following sections provide more information about establishing your Node.js module dependencies for your application.

###### Note

If you experience any deployment issues when Elastic Beanstalk is running `npm install`, consider an alternate approach. Include the
`node_modules` directory with the dependency modules in your application source bundle. Doing so can circumvent issues with
installing dependencies from the public npm registry while you investigate the issue. Because the dependency modules are sourced from a local directory,
dong this might also help reduce deployment time. For more information, see [Including Node.js dependencies in a node_modules directory](#nodejs-platform-nodemodules "#nodejs-platform-nodemodules")

## Specifying Node.js dependencies with a package.json file

Include a `package.json` file in the root of your project source to specify dependency packages and to provide a start command.
When a `package.json` file is present, and a `node_modules` directory isn't present in the root of your project
source, Elastic Beanstalk runs `npm install` as the _webapp_ user to install dependencies from the public npm registry. Elastic Beanstalk also
uses the `start` command to start your application. For more information about the `package.json` file, see [Specifying dependencies in a
`package.json` file](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file "https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file") in the _npm Docs_ website.

Use the `scripts` keyword to provide a start command. Currently, the `scripts` keyword is used instead of the legacy
`NodeCommand` option in the `aws:elasticbeanstalk:container:nodejs` namespace.

###### Example package.json – Express

```
{
    "name": "my-app",
    "version": "0.0.1",
    "private": true,
    "dependencies": {
      "ejs": "latest",
      "aws-sdk": "latest",
      "express": "latest",
      "body-parser": "latest"
    },
    "scripts": {
      "start": "node app.js"
    }
  }
```

###### Production mode and dev dependencies

To specify your dependencies in the `package.json` file use the _dependencies_ and
_devDependencies_ attributes. The _dependencies_ attribute designates packages required by your application in
production. The _devDependencies_ attribute designates packages that are only needed for local development and testing.

If you need to install the _devDependencies_ packages, set the NPM_USE_PRODUCTION environment property to `false`.
With this setting we will not use the above options when running npm install. This will result in the _devDependencies_ packages
being installed.

## Including Node.js dependencies in a node_modules directory

To deploy dependency packages to environment instances together with your application code, include them in a directory that's named
`node_modules` in the root of your project source. For more information, see [Downloading and installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally "https://docs.npmjs.com/downloading-and-installing-packages-locally") in the _npm
Docs_ website.

When you deploy a `node_modules` directory to an AL2023/AL2 Node.js platform version, Elastic Beanstalk assumes that you're
providing your own dependency packages, and avoids installing dependencies that are specified in a [package.json](#nodejs-platform-packagejson "#nodejs-platform-packagejson") file. Node.js looks for dependencies in the `node_modules` directory. For more information, see
[Loading from node_modules Folders](https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders "https://nodejs.org/api/modules.html#modules_loading_from_node_modules_folders") in the
Node.js documentation.

###### Note

If you experience any deployment issues when Elastic Beanstalk is running `npm install`, consider using the approach described in this topic as a
workaround while you investigate the issue.

### Considerations for Node.js on Amazon Linux 2

Read this section if you're using a _Node.js_ platform branch running on _Amazon Linux 2_.

###### Note

The information in this topic applies to Node.js platform branches running on Amazon Linux 2. Content here describes AL2-specific features and behaviors that differ from AL2023.

###### Command variations

The command options vary depending on the npm version included on the Amazon Linux 2 platform branch that your application runs on.

- npm v6 — Elastic Beanstalk installs dependencies in production mode by default. It uses the command `npm install --production`.
- npm v7 or greater — Elastic Beanstalk omits the _devDependencies_. It uses the command `npm install --omit=dev`.
  Both of the commands listed above do not install the packages that are _devDependencies_.

###### SSH and HTTPS protocols for Git dependencies

Starting with the March 7, 2023 Amazon Linux 2 platform release, you can use the SSH and HTTPS protocols to retrieve packages from a Git repository. Platform branch Node.js 16 supports both the SSH and HTTPS protocols. Node.js 14 only supports the HTTPS protocol.

###### Example package.json – Node.js 16 supports both HTTPS and SSH

```
    ...
    "dependencies": {
      "aws-sdk": "https://github.com/aws/aws-sdk-js.git",
      "aws-chime": "git+ssh://git@github.com:aws/amazon-chime-sdk-js.git"
    }
```

###### Versions and version ranges

Use the `engines` keyword in the `package.json` file to specify the Node.js version that you want your application to use. You can also specify a version range using npm notation. For more information about the syntax for version ranges, see [Semantic Versioning using npm](https://nodejs.dev/learn/semantic-versioning-using-npm "https://nodejs.dev/learn/semantic-versioning-using-npm") on the Node.js website. The `engines` keyword in the Node.js
`package.json` file replaces the legacy `NodeVersion` option in the `aws:elasticbeanstalk:container:nodejs` namespace.

###### Important

The feature to specify version ranges is not available for Node.js platform branches running on AL2023. We only support one Node.js version within a specific Node.js branch on AL2023. If your `package.json` file specifies a version range, we'll ignore it and default to the platform branch version of Node.js.

###### Example `package.json` – Single Node.js version

```
{
    ...
    "engines": { "node" : "14.16.0" }
  }
```

###### Example `package.json` – Node.js version range

```
{
    ...
    "engines": { "node" : ">=10 <11" }
  }
```

When a version range is indicated, Elastic Beanstalk installs the latest Node.js version that the platform has available within the range. In this example, the range indicates that the version must be greater than or equal to version 10, but less than version 11. As a result, Elastic Beanstalk installs the latest Node.js version 10.x.y, which is available on the [supported platform](../platforms/platforms-supported.md#platforms-supported.nodejs "../platforms/platforms-supported.md#platforms-supported.nodejs").

Be aware that you can only specify a Node.js version that corresponds with your platform branch. For example, if you're using the Node.js 16 platform branch, you can only specify a 16.x.y
Node.js version. You can use the version range options supported by npm to allow for more flexibility. For valid Node.js versions for each platform branch, see [Node.js](../platforms/platforms-supported.md#platforms-supported.nodejs "../platforms/platforms-supported.md#platforms-supported.nodejs") in the _AWS Elastic Beanstalk Platforms_ guide.

###### Note

When support for the version of Node.js that you are using is removed from the platform, you must change or remove the Node.js version setting prior to doing a [platform update](using-features.platform.md "using-features.platform.md"). This might occur when a security vulnerability is identified for one or more versions of Node.js.

When this happens, attempting to update to a new version of the platform that doesn't support the configured Node.js version fails. To avoid needing to create a new environment, change the Node.js version setting in `package.json` to a Node.js version that is supported by both the old platform version and the new one. You have the option to specify a Node.js version range that includes a supported version, as described earlier in this topic. You also have the option to remove the setting, and then deploy the new source bundle.
