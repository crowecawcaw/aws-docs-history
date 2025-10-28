# Setting up your Node.js development environment for Elastic Beanstalk

This topic provides instructions to set up a Node.js development environment to test your application locally prior to deploying it to
AWS Elastic Beanstalk. It also references websites that provide installation instructions for useful tools.

###### Topics

- [Install Node.js](#nodejs-devenv-nodejs "#nodejs-devenv-nodejs")
- [Confirm npm installation](#nodejs-devenv-npm "#nodejs-devenv-npm")
- [Install the AWS SDK for Node.js](#nodejs-devenv-awssdk "#nodejs-devenv-awssdk")
- [Install the Express generator](#nodejs-devenv-express "#nodejs-devenv-express")
- [Set up an Express framework and server](#nodejs-devenv-express-framework "#nodejs-devenv-express-framework")

## Install Node.js

Install Node.js to run Node.js applications locally. If you don't have a preference, get the latest version supported by Elastic Beanstalk. See [Node.js](../platforms/platforms-supported.md#platforms-supported.nodejs "../platforms/platforms-supported.md#platforms-supported.nodejs") in the _AWS Elastic Beanstalk Platforms_ document
for a list of supported versions.

Download Node.js at [nodejs.org](https://nodejs.org/en/ "https://nodejs.org/en/").

## Confirm npm installation

Node.js uses the npm package manager to help you install tools and frameworks for use in your application. Since npm is distributed with Node.js, you
will automatically install it when you download and install Node.js. To confirm you have npm installed you can run the following command:

```
$ `npm -v`
```

For more information on npm, visit the [npmjs](https://www.npmjs.com/get-npm "https://www.npmjs.com/get-npm") website.

## Install the AWS SDK for Node.js

If you need to manage AWS resources from within your application, install the AWS SDK for JavaScript in Node.js. Install the SDK with npm:

```
$ `npm install aws-sdk`
```

Visit the [AWS SDK for JavaScript in Node.js](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/") homepage for more information.

## Install the Express generator

Express is a web application framework that runs on Node.js. To use it, first install the Express generator command line application. Once the Express
generator is installed, you can run the **express** command to generate a base project structure for your web application. Once the base
project, files, and dependencies are installed you can start up a local Express server on your development machine.

###### Note

- These steps walk you through installing the Express generator on a Linux operating system.
- For Linux, depending on your permission level to system directories, you might need to prefix some of these commands with
  `sudo`.

###### To install the Express generator on your development environment

1. Create a working directory for your Express framework and server.

```
~$ `mkdir node-express`
~$ `cd node-express`
```

2. Install Express globally so that you have access to the `express` command.

```
~/node-express$ `npm install -g express-generator`
```

3. Depending on your operating system, you may need to set your path to run the `express` command. The output from the previous step
   provides information if you need to set your path variable. The following is an example for Linux.

```
~/node-express$ `export PATH=$PATH:/usr/local/share/npm/bin/express`
```

When you follow the tutorials in this chapter, you'll need to run the **express** command from different directories.
Each tutorial sets up a base Express project structure in it's own directory.

You have now installed the Express command line generator. You can use it to create a framework directory for your web application, set up
dependencies, and start up the web app server. Next, we'll go through the steps to accomplish this in the `node-express` directory that
we created.

## Set up an Express framework and server

Follow these steps to create the base Express framework directories and contents. The tutorials in this chapter also include these steps to set up the
base Express framework in each of the tutorial's application directories.

###### To set up an Express framework and server

1. Run the `express` command. This generates `package.json`, `app.js`, and a few directories.

```
~/node-express$ `express`
```

When prompted, type `y` if you want to continue. 2. Set up local dependencies.

```
~/node-express$ `npm install`
```

3. Verify the web app server starts up.

```
~/node-express$ `npm start`
```

You should see output similar to the following:

```
> nodejs@0.0.0 start /home/local/user/node-express
> node ./bin/www
```

The server runs on port 3000 by default. To test it, run `curl http://localhost:3000` in another terminal, or open a browser on the
local computer and enter URL address `http://localhost:3000`.

Press **Ctrl+C** to stop the server.
