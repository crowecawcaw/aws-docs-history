# Inter-worker encryption

With Amazon EMR versions 6.15.0 and higher, enable mutual-TLS encrypted communication
between workers in your Spark job runs. When enabled, EMR Serverless automatically generates and
distributes a unique certificate for each worker provisioned under your job runs. When these workers communicate
to exchange control messages or transfer shuffle data,
they establish a mutual TLS connection and use the configured certificates to verify the
identity of each other. If a worker is unable to verify another certificate, the
TLS handshake fails, and EMR Serverless aborts the connection between them.

If you're using Lake Formation with EMR Serverless, mutual-TLS encryption is enabled by default.

## Enabling mutual-TLS encryption on EMR Serverless

To enable mutual TLS encryption on your spark application, set
`spark.ssl.internode.enabled` to true when [creating
EMR Serverless application](getting-started.md#gs-cli "getting-started.md#gs-cli"). If you're using the AWS console to create an EMR Serverless application,
choose **Use custom settings**, then expand **Application configuration**, and enter your `runtimeConfiguration`.

```
aws emr-serverless create-application \
--release-label emr-6.15.0 \
--runtime-configuration '{
  "classification": "spark-defaults",
  "properties": {"spark.ssl.internode.enabled": "true"}
}' \
--type "SPARK"
```

If you want to enable mutual TLS encryption for individual spark job runs, set `spark.ssl.internode.enabled`
to true when using `spark-submit`.

```
--conf spark.ssl.internode.enabled=true
```
