AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Upgrading instructions for AWS Blu Age

This page contains instructions for upgrading the AWS Blu Age version.

## Common upgrades

In most of the cases, when upgrading the AWS Blu Age Runtime (non-managed) version, you should replace the artifacts
(WARs, configuration files, scripts, etc.) of your previous version with the ones provided in the
new one and restart your application. Make sure to perform extensive regression tests of your
modernized applications once you upgrade. You may also contact your AWS Blu Age delivery manager for
specific instructions applicable to your application.

To upgrade the AWS Blu Age Runtime (managed) version, see [Managed runtime environments in AWS Mainframe Modernization](environments-m2.md "environments-m2.md").

Some upgrades may require additional configuration to ensure compatibility. In that case,
follow the instructions for that specific upgrade.

## Migrating from 3.10.0 to 4.0.0

The main change in 4.0.0 is the migration from Spring Boot 2.7 to Spring Boot 3.2 and from
Tomcat 9 to Tomcat 10.

### Code changes

This section lists changes required to make the modernized code compatible with AWS Blu Age Runtime
4.0.0. You can skip this section if you decide to launch a new generation using the 4.0.0
version on Blu Insights (Transformation Center).

**POM changes**

| Group                    | ArtifactId                       | Change                                                                      |
| ------------------------ | -------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| org.slf4j                | slf4j-api                        | Remove (is a transitive dependency)                                         |
| org.yaml                 | snakeyaml                        | Remove (is a transitive dependency)                                         |
| org.springframework.boot | spring-boot-starter-web          | - Upgrade spring.boot.version to 3.2.4 - Remove exclusion of log4j-to-slf4j |
| org.springframework.boot | spring-boot-starter-jta-atomikos | Change to com.atomikos:transactions-spring-boot3-starter:6.0.0              |
| org.apache.commons       | commons-dbcp2                    | Upgrade to 2.10.0                                                           |
| org.postgresql           | postgreql                        | Upgrade to 42.7.2                                                           |
| com.microsoft.sqlserver  | mssql-jdbc                       | Upgrade to 12.4.2.jre11                                                     |
| com.oracle.database.jdbc | ojdbc8                           | Change to ojdbc11 version 23.3.0.23.09                                      | **Migrate from Javax to Jakarta** The tomcat upgrade comes with a migration from the Javax Java package to Jakarta. **Make sure to update your imports accordingly from javax.\* to jakarta.\***. Nearly all the old referenced classes in the Javax package can be found in Jakarta. Known exceptions to this are the `javax.sql` and `javax.xml` packages, which are still unchanged. **Atomikos change** Due to the dependency change referenced above, references to `org.springframework.boot.jta.atomikos.AtomikosDataSourceBean` must be changed to `com.atomikos.spring.AtomikosDataSourceBean`. **PostgreSQL dialect removal** The custom class `PostgreSQLDialect.java` is removed. References to it in the main launcher must be removed too. ### Deployment (AWS Blu Age Runtime (non-managed)) **Tomcat** This version is compatible with Tomcat `10.1.17`. Upgrading the Tomcat server to this version is required to run the Blu Age Runtime `4.0.0`. Make sure to port the old configuration changes (notably the Catalina properties). **Shared dependencies** The runtime shared folder contains the up-to-date dependencies. **Extra dependencies** If you used extra dependencies (not included on the runtime), you might need to update them. The readme file in the extra folder lists the supported versions. |
