

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
  + **Fine-grained access control for Spark Connect sessions** — AWS Lake Formation fine-grained access control is now supported for interactive PySpark sessions that you run through Apache Spark Connect. The table, row, column, and cell-level permissions that you define in Lake Formation are enforced on your session queries. For more information, see [Fine-grained access control with AWS Lake Formation for Spark Connect sessions](spark-connect.md#spark-connect-fgac).
  + **Improved fine-grained access control** — This release improves data filters, time travel queries, and Delta Lake table operations on access-controlled tables. It also supports the `VACUUM` operation on Delta Lake tables that use fine-grained access control.
  + **Merged Spark configuration** — Starting with `emr-7.14.0`, EMR Serverless merges Spark configuration instead of replacing it. It combines the configuration set at the application level with the configuration set for an individual job or session. When the same configuration is set at both levels, the job or session value takes precedence. In earlier releases, the job or session configuration replaces the application-level configuration entirely.