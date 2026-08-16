# Runtime versions using Node.js

The following section contains information about the CloudWatch Synthetics runtime versions
for Node.js. This runtime does not have any browser or framework included.

The naming convention for these runtime versions is `syn-`language`
 -`majorversion`.`minorversion``.

## syn-nodejs-5.2

###### Important

Starting Synthetics `syn-nodejs-3.1` and later, Synthetics runtime uses
the new namespace. Please migrate the canary script to use the new namespace. Legacy
namespace will be deprecated in a future release.

- @amzn/synthetics-core → @aws/synthetics-core

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-5.2**

- Multi checks blueprint bug fix – The runtime now correctly resolves
  `${AWS_SECRET:...}` references in global variables and SigV4
  authentication configuration to their stored secret values.
- Upgrade `protobufjs` to 7.5.6 to address the following CVEs:

  - CVE-2026-41242

- Upgrade `jsonpath` to 1.3.0 to address the following CVEs:

  - CVE-2026-1615

- Upgrade `fast-xml-parser` to 5.9.3 to address the following CVEs:

  - CVE-2026-25896

The following earlier runtime versions for Node.js are still supported.

### syn-nodejs-5.1

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-5.1**

- Fix bug where HTTP headers with array values were not being captured properly.
- Upgrade `ws` to 8.20.1 to address the following CVEs:

  - CVE-2026-45736

### syn-nodejs-5.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-5.0**

- Upgrade `brace-expansion` to 5.0.6 to address the following CVE:

  - GHSA-jxxr-4gwj-5jf2

### syn-nodejs-4.2

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-4.2**

- Upgrade `axios` to 1.15.2 to address the following CVEs:

  - CVE-2025-62718
  - CVE-2026-42033
  - CVE-2026-42035
  - CVE-2026-42038
  - CVE-2026-42039
  - CVE-2026-42043
  - CVE-2026-42044
  - CVE-2026-42264

- Upgrade `brace-expansion` to 5.0.5 to address the following CVE:

  - CVE-2026-33750

- Upgrade `fast-xml-builder` to 1.1.7 to address the following CVE:

  - GHSA-5wm8-gmm8-39j9

### syn-nodejs-4.1

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-4.1**

- Upgrade `fast-xml-parser` to 5.5.7 to address the following CVEs:

  - CVE-2026-25128
  - CVE-2026-25896
  - CVE-2026-26278
  - CVE-2026-27942
  - CVE-2026-33036

### syn-nodejs-4.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x

**Changes in syn-nodejs-4.0**

- Applied security patches.

### syn-nodejs-3.1

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x

**Changes in syn-nodejs-3.1**

- Synthetics runtime namespace migration.
- Type definition is available in [npm Registry](https://www.npmjs.com/package/@aws/synthetics-core "https://www.npmjs.com/package/@aws/synthetics-core").
  Please make sure the type definition package version matches your canary's runtime
  version.

### syn-nodejs-3.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x

**Changes in syn-nodejs-3.0**

- Support for multi checks blueprint.
