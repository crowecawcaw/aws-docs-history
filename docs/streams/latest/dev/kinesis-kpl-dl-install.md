# Install the KPL

Amazon provides pre-built binaries of the C++ Amazon Kinesis Producer Library (KPL) for
macOS, Windows, and recent Linux distributions (for supported platform details, see the next
section). These binaries are packaged as part of Java .jar files and are automatically invoked
and used if you are using Maven to install the package. To locate the latest versions of the
KPL and KCL, use the following Maven search links:

- [KPL](https://search.maven.org/#search|ga|1|amazon-kinesis-producer "https://search.maven.org/#search|ga|1|amazon-kinesis-producer")
- [KCL](https://search.maven.org/#search|ga|1|amazon-kinesis-client "https://search.maven.org/#search|ga|1|amazon-kinesis-client")
  The Linux binaries have been compiled with the GNU Compiler Collection (GCC) and
  statically linked against libstdc++ on Linux. They are expected to work on any 64-bit Linux
  distribution that includes a glibc version 2.5 or higher.

Users of earlier Linux distributions can build the KPL using the build instructions
provided along with the source on GitHub. To download the KPL from GitHub, see
[Amazon Kinesis Producer Library](https://github.com/awslabs/amazon-kinesis-producer "https://github.com/awslabs/amazon-kinesis-producer").

###### Important

Amazon Kinesis Producer Library (KPL) 0.x will reach end-of-support on January 30, 2026. We **strongly recommend** that you migrate your KPL applications using version 0.x to the latest KPL version before January 30, 2026. To find the latest KPL version, see the [KPL page on Github](https://github.com/awslabs/amazon-kinesis-producer "https://github.com/awslabs/amazon-kinesis-producer"). For information about migrating from KPL 0.x to KPL 1.x, see [Migrate from KPL 0.x to
KPL 1.x](kpl-migration-1x.md "kpl-migration-1x.md").
