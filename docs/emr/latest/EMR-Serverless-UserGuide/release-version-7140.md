

# EMR Serverless 7.14.0
<a name="release-version-7140"></a>

The following table lists the application versions available with EMR Serverless 7.14.0.


| Application | Version | 
| --- | --- | 
| Apache Spark | 3.5.8 | 
| Apache Hive | 3.1.3 | 
| Apache Tez | 0.10.2 | 

**EMR Serverless 7.14.0 release notes**
+ **Changes and enhancements**
  + **Custom image release version validation** — When you use a custom image, EMR Serverless verifies that its base image uses the same Amazon EMR release. If the image's release version doesn't match the application's release version, or the image has no release version, the request is rejected. A message identifies the base image version to use. Rebuild your custom image from the matching EMR Serverless base image.
  + **Increased Serverless storage data limit for Spark jobs** — This release raises the Serverless storage data limit for Spark jobs from 200 GiB to 1 TiB.
  + **Improved fine-grained access control** — This release improves data filters, time travel queries, and Delta Lake table operations on access-controlled tables. It also supports the `VACUUM` operation on Delta Lake tables that use fine-grained access control.