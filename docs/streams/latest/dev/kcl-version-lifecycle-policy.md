# KCL version lifecycle policy

This topic outlines the version lifecycle policy for Amazon Kinesis Client Library (KCL). AWS regularly provides new releases for KCL versions to support new features and enhancements, bug fixes, security patches, and dependency updates. We recommend that you stay up-to-date with KCL versions to keep up with the latest features, security updates, and underlying dependencies. We **don't** recommend continued use of an unsupported KCL version.

The lifecycle for major KCL versions consists of the following three phases:

- **General availability (GA)** – During this phase, the major version is fully supported. AWS provides regular minor and patch version releases that include support for new features or API updates for Kinesis Data Streams, as well as bug and security fixes.
- **Maintenance mode** – AWS limits patch version releases to address critical bug fixes and security issues only. The major version won't receive updates for new features or APIs of Kinesis Data Streams.
- **End-of-support** – The major version will no longer receive updates or releases. Previously published releases will continue to be available through public package managers and the code will remain on GitHub. Use of a version which has reached end-of-support is done at the user’s discretion. We recommend that you upgrade to the latest major version.

| Major version | Current phase        | Release date | Maintenance mode date | End-of-support date |
| ------------- | -------------------- | ------------ | --------------------- | ------------------- |
| KCL 1.x       | Maintenance mode     | 2013-12-19   | 2025-04-17            | 2026-01-30          |
| KCL 2.x       | General availability | 2018-08-02   | --                    | --                  |
| KCL 3.x       | General availability | 2024-11-06   | --                    | --                  |
