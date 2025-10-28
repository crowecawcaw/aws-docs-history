# Troubleshoot common environment-variable format errors

When you input Livy and Spark configurations, there are environment-variable formats that aren't supported and can cause errors. The procedure
takes you through a series of steps to help ensure that you use correct formats.

**Inputting your own Livy and Spark configurations while installing Livy**

You can configure any Apache Livy or Apache Spark environment variable with the `env.*` Helm property. Follow
the steps below to convert the example configuration
`example.config.with-dash.withUppercase` to a supported environment variable format.

1. Replace uppercase letters with a 1 and a lowercase of the letter.
   For example, `example.config.with-dash.withUppercase`
   becomes `example.config.with-dash.with1uppercase`.
2. Replace dashes (-) with 0. For example,
   `example.config.with-dash.with1uppercase` becomes `example.config.with0dash.with1uppercase`
3. Replace dots (.) with underscores (\_). For example,
   `example.config.with0dash.with1uppercase` becomes `example_config_with0dash_with1uppercase`.
4. Replace all lowercase letters with uppercase letters.
5. Add the prefix `LIVY_` to the variable name.
6. Use the variable while installing Livy through the helm chart using the format
   --set env.`YOUR_VARIABLE_NAME`.value=`yourvalue`
   For example, to set the Livy and Spark configurations
   `livy.server.recovery.state-store = filesystem` and
   `spark.kubernetes.executor.podNamePrefix = my-prefix`, use these Helm properties:

```
—set env.LIVY_LIVY_SERVER_RECOVERY_STATE0STORE.value=filesystem
—set env.LIVY_SPARK_KUBERNETES_EXECUTOR_POD0NAME0PREFIX.value=myprefix

```
