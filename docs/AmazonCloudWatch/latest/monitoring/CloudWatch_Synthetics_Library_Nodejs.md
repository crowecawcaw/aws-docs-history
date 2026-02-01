# Runtime versions using Node.js

The following section contains information about the CloudWatch Synthetics runtime versions for Node.js. This runtime does not have any browser or framework included.

The naming convention for these runtime versions is
`syn-`language`-`majorversion`.`minorversion``.

##

syn-nodejs-3.1

###### Important

Starting Synthetics `syn-nodejs-3.1` and later, Synthetics runtime uses the new namespace.
Please migrate the canary script to use the new namespace. Legacy namespace will be deprecated in a future release.

- @amzn/synthetics-core → @aws/synthetics-core

**Major dependencies** – AWS Lambda runtime Node.js 20.x

**Changes in syn-nodejs-3.1**

- Synthetics runtime namespace migration.
- Type definition is available in [npm Registry](https://www.npmjs.com/package/@aws/synthetics-core "https://www.npmjs.com/package/@aws/synthetics-core"). Please ensure the type definition package version matches your canary's runtime version.

The following earlier runtime versions for Node.js are still supported.

###

syn-nodejs-3.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x

**Changes in syn-nodejs-3.0**

- Support for multi checks blueprint.
