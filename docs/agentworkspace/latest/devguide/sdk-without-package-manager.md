# Using the Amazon Connect SDK without a package

manager

This guide is intended for developers building Amazon Connect integrations who do not
use npm, webpack, or other JavaScript package managers and bundlers in their web
applications. This includes developers building custom StreamsJS-based contact center
interfaces or third-party applications that run within the Amazon Connect Agent
Workspace.

Amazon Connect recommends using a package manager such as npm and a bundler such as
webpack or Vite for SDK integration. These tools provide dependency management,
automatic updates, tree-shaking, and a streamlined development workflow. If you choose
not to use these tools, this guide describes an alternative approach.

The Amazon Connect SDK is distributed as npm packages. These packages use Node.js-style
module resolution and cannot be loaded directly in a browser using a `<script>`
tag. If your development environment does not include a package manager or bundler, you must
create a prebuilt script file that bundles the SDK packages into a browser-compatible
format.

## Your responsibility

When working without a package manager, it becomes your responsibility to:

1. Set up a one-time build environment to create the bundle
2. Select the specific SDK packages your application requires
3. Build and maintain the bundled script file
4. Update the bundle when SDK versions change

## Why a bundle is required

SDK packages use ES module imports like `import { ContactClient } from
 "@amazon-connect/contact"`. Browsers cannot resolve these package specifiers
directly. A bundler resolves these imports, combines the code, and produces a single
file the browser can execute.

## Exposing the SDK as a global

When using `<script>` tags, there is no module system to share code
between files. The bundle must attach the SDK to a global variable (such as `window.AmazonConnectSDK`) so your application scripts can access it. This is
different from npm-based projects where you import directly from packages.

## Available packages

The SDK consists of multiple packages. Select only the packages your application
needs. Examples include:

| Package                       | Purpose                                                                     |
| ----------------------------- | --------------------------------------------------------------------------- |
| `@amazon-connect/core`        | Core SDK functionality and provider types                                   |
| `@amazon-connect/contact`     | ContactClient for contact operations                                        |
| `@amazon-connect/email`       | EmailClient for email channel operations                                    |
| `@amazon-connect/app`         | App initialization for third-party applications                             |
| `@amazon-connect/app-manager` | Plugin for hosting Connect first-party apps (Cases,<br>Step-by-Step Guides) |
| `@amazon-connect/voice`       | VoiceClient for voice channel operations                                    |

See the [Amazon
Connect SDK repository](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") for the complete list of available packages.
