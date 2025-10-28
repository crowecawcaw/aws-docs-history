# AWS Elastic Beanstalk and AWS X-Ray

###### Important

End of support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md") and for information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

AWS Elastic Beanstalk platforms include the X-Ray daemon. You can [run the daemon](xray-daemon-beanstalk.md "xray-daemon-beanstalk.md") by setting an option in the Elastic Beanstalk console or with a configuration
file.

On the Java SE platform, you can use a Buildfile file to build your application with Maven
or Gradle on-instance. The X-Ray SDK for Java and AWS SDK for Java are available from Maven, so you can
deploy only your application code and build on-instance to avoid bundling and uploading all of
your dependencies.

You can use Elastic Beanstalk environment properties to configure the X-Ray SDK. The method that Elastic Beanstalk
uses to pass environment properties to your application varies by platform. Use the X-Ray SDK's
environment variables or system properties depending on your platform.

- **[Node.js platform](../../../elasticbeanstalk/latest/dg/create_deploy_nodejs.md "../../../elasticbeanstalk/latest/dg/create_deploy_nodejs.md")** – Use [environment variables](xray-sdk-nodejs-configuration.md#xray-sdk-nodejs-configuration-envvars "xray-sdk-nodejs-configuration.md#xray-sdk-nodejs-configuration-envvars")
- **[Java SE
  platform](../../../elasticbeanstalk/latest/dg/java-se-platform.md "../../../elasticbeanstalk/latest/dg/java-se-platform.md")** – Use [environment variables](xray-sdk-java-configuration.md#xray-sdk-java-configuration-envvars "xray-sdk-java-configuration.md#xray-sdk-java-configuration-envvars")
- **[Tomcat
  platform](../../../elasticbeanstalk/latest/dg/java-tomcat-platform.md "../../../elasticbeanstalk/latest/dg/java-tomcat-platform.md")** – Use [system properties](xray-sdk-java-configuration.md#xray-sdk-java-configuration-sysprops "xray-sdk-java-configuration.md#xray-sdk-java-configuration-sysprops")
  For more information, see [Configuring AWS X-Ray Debugging](../../../elasticbeanstalk/latest/dg/environment-configuration-debugging.md "../../../elasticbeanstalk/latest/dg/environment-configuration-debugging.md") in the AWS Elastic Beanstalk Developer Guide.
