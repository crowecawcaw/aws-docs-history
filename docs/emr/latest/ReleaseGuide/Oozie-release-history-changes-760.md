# Amazon EMR 7.6.0 -

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
