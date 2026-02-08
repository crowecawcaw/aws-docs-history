AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime artifacts

AWS Blu Age Runtime artifacts are the components for deploying and running modernized applications. This
document outlines the different types of artifacts available, their storage locations, and
how to access them.

## AWS Blu Age Runtime artifacts

### Artifacts contents

In both Release and Pre-release buckets, you'll find:

**gapwalk-x.y.z.zip**

This archive, where x.y.z represents the version number (see [AWS Blu Age versioning](ba-versioning.md "ba-versioning.md")), contains the core
AWS Blu Age Runtime components essential for executing AWS Blu Age applications, including:

| Artifact                      | Description                                                                       | Type | Distribution Folder |
| ----------------------------- | --------------------------------------------------------------------------------- | ---- | ------------------- |
| gapwalk-application-x.y.z.war | Blu Age main web application **Gapwalk**                                          | War  | webapps             |
| \*.jar                        | Blu Age Runtime Framework \*_Shared Libraries_<br>• (Gapwalk)                     | Jars | shared              |
| gapwalk-\*-x.y.z.war          | Blu Age additional web applications **(utility-pgm, hierarchical support, ... )** | War  | webapps-extra       |
| bac-x.y.z.war / jac-x.y.z.war | Blu Age **Administration Consoles (non-standalone)**                              | War  | webapps-consoles    |

**aws-bluage-webapps-x.y.z.zip**

This archive, where x.y.z follows the same versioning scheme as above, includes Blu Age Administration Consoles (standalone)

- **BAC** (Blusam console) WAR file, which is
  used for monitoring the Blusam database.
- **JAC** (JICS console) WAR file, used for
  monitoring the JICS database.
- Necessary supporting libraries.

### Package Signature Verification

The released zip files are provided as digitally signed ZIP archives to ensure security and authenticity.
Digital signatures help verify that the files you download are genuine, unaltered, and officially released
by our organization. This prevents tampering and protects against malware or compromised files that could
be maliciously distributed.

To verify the signature of the ZIP file before using it, you can use the following command:

`jarsigner -verify -certs -verbose aws-bluage-runtime-x.y.z.zip`

Here the result example for a certified file :

```
...
jar verified.
```

For details on how security vulnerabilities are addressed, see [AWS Mainframe Modernization Refactor with AWS Blu Age release
overview](lifecycle-m2.md#lifecycle-ba-overview "lifecycle-m2.md#lifecycle-ba-overview").

###### Note

While we strive to release our products without CVEs, new CVEs may appear
later on.
