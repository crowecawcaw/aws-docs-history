# Amazon EMR 7.10.0 -

Oozie release notes

**Oozie known issues:**

- Version Conflict in Oozie Sharelib:
  - Oozie sharelib contains multiple versions of commons-cli (versions 1.2 and 1.5).
  - If you encounter compatibility issues, consider either:
    - Removing commons-cli-1.2 JAR files.
    - Replacing commons-cli-1.2 with commons-cli-1.5.

- Pig JAR Compatibility:
  - The Pig jar included by default in Oozie sharelib is the open-source jar. This differs from the Pig jar available elsewhere in the EMR cluster,
    on installing the Pig application, which includes additional EMR-specific enhancements and optimizations. Users should be aware of this difference when
    developing Pig workflows.

- The config, `oozie.base.url`, is primarily used for referencing Oozie callback URLs, and by default, they are over HTTP, even with In-Transit Encryption enabled. This is
  expected because as per the [Oozie set-up documentation](https://oozie.apache.org/docs/5.2.1/AG_Install.html#Setting_Up_Oozie_with_HTTPS_SSL "https://oozie.apache.org/docs/5.2.1/AG_Install.html#Setting_Up_Oozie_with_HTTPS_SSL"), _The default HTTPS configuration
  will cause all Oozie URLs to use HTTPS except for the JobTracker callback URLs. This is to simplify configuration (no changes needed outside of Oozie), but this
  is okay because Oozie doesn’t inherently trust the callbacks anyway; they are used as hints._ However, if the config `oozie.base.url` is explicitly set to point
  to HTTPS for Oozie callbacks, it will error out because by default, the certificates required are not added directly in the default Java truststore.
