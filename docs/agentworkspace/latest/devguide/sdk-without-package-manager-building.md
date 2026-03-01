# Building the script file

This section provides step-by-step instructions for creating a browser-consumable
bundle from the SDK npm packages.

## Prerequisites

The following prerequisites are required:

- Node.js 18 or later installed
- npm (comes with Node.js)
- A text editor

## Step 1: Create the build project directory

Create a new directory to hold your build configuration. This directory will
contain npm tooling but the output bundle will be usable without npm.

```

mkdir connect-sdk-bundle
cd connect-sdk-bundle
```

## Step 2: Initialize the npm project

```

npm init -y
```

## Step 3: Install the SDK packages you need

For an email-based solution using EmailClient and ContactClient:

```

npm install @amazon-connect/core @amazon-connect/contact @amazon-connect/email
```

If you are building a third-party app (not embedded in StreamsJS), also install:

```

npm install @amazon-connect/app
```

If you are integrating with StreamsJS and want to host Connect first-party apps
(such as Cases or Step-by-Step Guides), also install:

```

npm install @amazon-connect/app-manager
```

## Step 4: Install the bundler

Install esbuild, a fast JavaScript bundler:

```

npm install --save-dev esbuild
```

## Step 5: Create the entry file

Create a file that imports the SDK modules you need and exposes them as a global:

```

mkdir src
```

**For StreamsJS integration** (`src/entry-streams.js`):

```

// Entry file for StreamsJS integration
import { ContactClient } from "@amazon-connect/contact";
import { EmailClient } from "@amazon-connect/email";

// Expose the SDK on the window object
window.AmazonConnectSDK = {
  ContactClient,
  EmailClient,
};
```

**For StreamsJS with first-party apps** (`src/entry-streams-with-apps.js`):

If you want to host Connect first-party apps like Cases or Step-by-Step Guides
alongside the CCP, include the app-manager plugin:

```

// Entry file for StreamsJS integration with 1P app support
import { ContactClient } from "@amazon-connect/contact";
import { EmailClient } from "@amazon-connect/email";
import { AppManagerPlugin } from "@amazon-connect/app-manager";

// Expose the SDK on the window object
window.AmazonConnectSDK = {
  AppManagerPlugin,
  ContactClient,
  EmailClient,
};
```

**For third-party app** (`src/entry-app.js`
):

```

// Entry file for third-party app integration
import { AmazonConnectApp } from "@amazon-connect/app";
import { ContactClient } from "@amazon-connect/contact";
import { EmailClient } from "@amazon-connect/email";

// Expose the SDK on the window object
window.AmazonConnectSDK = {
  AmazonConnectApp,
  ContactClient,
  EmailClient,
};
```

## Step 6: Add build scripts to package.json

Edit `package.json` to add build scripts:

```

{
  "name": "connect-sdk-bundle",
  "version": "1.0.0",
  "scripts": {
    "build:streams": "esbuild src/entry-streams.js --bundle --minify --sourcemap --format=iife --target=es2020 --outfile=dist/connect-sdk-streams.bundle.js",
    "build:app": "esbuild src/entry-app.js --bundle --minify --sourcemap --format=iife --target=es2020 --outfile=dist/connect-sdk-app.bundle.js",
    "build": "npm run build:streams && npm run build:app"
  }
}
```

## Step 7: Build the bundle

```

npm run build
```

This creates the following files in the `dist/` directory:

- `connect-sdk-streams.bundle.js` - Bundle for StreamsJS
  integration
- `connect-sdk-streams.bundle.js.map` - Source map for debugging
- `connect-sdk-app.bundle.js` - Bundle for third-party apps
- `connect-sdk-app.bundle.js.map` - Source map for debugging

## Step 8: Copy the bundle to your project

Copy the appropriate `.js` file (and optionally the `.map`
file for debugging) to your static website's assets folder:

```

cp dist/connect-sdk-streams.bundle.js /path/to/your/website/assets/vendor/
# or
cp dist/connect-sdk-app.bundle.js /path/to/your/website/assets/vendor/
```

## Complete build project structure

After completing all steps, your build project should look like this:

```

connect-sdk-bundle/
├── package.json
├── package-lock.json
├── node_modules/
├── src/
│   ├── entry-streams.js
│   └── entry-app.js
└── dist/
    ├── connect-sdk-streams.bundle.js
    ├── connect-sdk-streams.bundle.js.map
    ├── connect-sdk-app.bundle.js
    └── connect-sdk-app.bundle.js.map
```
