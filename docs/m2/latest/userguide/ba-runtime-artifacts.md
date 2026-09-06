

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime artifacts
<a name="ba-runtime-artifacts"></a>

AWS Transform for mainframe Runtime artifacts are the components for deploying and running modernized applications. This document outlines the different types of artifacts available, their storage locations, and how to access them.

## AWS Transform for mainframe Runtime artifacts
<a name="ba-runtime-artifacts-contents"></a>

### Artifacts contents
<a name="ba-runtime-artifacts-artifacts"></a>

The following artifacts are accessible from [AWS Transform for mainframe refactor Toolbox](https://bluinsights.aws/docs/bluage-toolbox-introduction).

**gapwalk-x.y.z.zip**

This archive, where x.y.z represents the version number (see [AWS Transform for mainframe versioning](https://docs.aws.amazon.com/m2/latest/userguide/ba-versioning.html)), contains the core AWS Transform for mainframe Runtime components essential for executing AWS Transform for mainframe applications, including:


| Artifact | Description | Type | Distribution Folder | 
| --- | --- | --- | --- | 
| gapwalk-application-x.y.z.war | AWS Transform for mainframe main web application Gapwalk | War | webapps | 
| \*.jar | AWS Transform for mainframe Runtime Framework Shared Libraries (Gapwalk) | Jars | shared | 
| gapwalk-\*-x.y.z.war | AWS Transform for mainframe additional web applications (utility-pgm, hierarchical support, ... ) | War | webapps-extra | 
| bac-x.y.z.war / jac-x.y.z.war | AWS Transform for mainframe Administration Consoles (non-standalone) | War | webapps-consoles | 
| gapwalk-runtime-x.y.z-javadoc.zip | AWS Transform for mainframe Runtime Framework Javadoc | zip | api-docs | 
| gapwalk-webapps-x.y.z-javadoc.zip | AWS Transform for mainframe Administration Consoles (BAC and JAC) Javadoc | zip | api-docs | 

**aws-bluage-webapps-x.y.z.zip**

This archive, where x.y.z follows the same versioning scheme as above, includes AWS Transform for mainframe Administration Consoles (standalone)
+ **BAC** (Blusam console) WAR file, which is used for monitoring the Blusam database.
+ **JAC** (JICS console) WAR file, used for monitoring the JICS database.
+ Necessary supporting libraries.

### Package Signature Verification
<a name="ba-runtime-signed"></a>

The released zip files are provided as digitally signed ZIP archives to ensure security and authenticity. Digital signatures help verify that the files you download are genuine, unaltered, and officially released by our organization. This prevents tampering and protects against malware or compromised files that could be maliciously distributed.

To verify the signature of the ZIP file before using it, you can use the following command:

`jarsigner -verify -certs -verbose aws-bluage-runtime-x.y.z.zip`

Here the result example for a certified file :

```
...
jar verified.
```

For details on how security vulnerabilities are addressed, see [AWS Mainframe Modernization Refactor with AWS Transform for mainframe release overview](https://docs.aws.amazon.com/m2/latest/userguide/lifecycle-m2.html#lifecycle-ba-overview).

**Note**  
While we strive to release our products without CVEs, new CVEs may appear later on.