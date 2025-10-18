# Build your own custom OpenTelemetry Collector

You can build your own custom OpenTelemetry Collector to get the best application observability experience in CloudWatch with OpenTelemetry. In this setup, you need to build your own OpenTelemetry Collector with open source CloudWatch components.


## Prerequisite


Make sure *Transaction Search* is enabled in CloudWatch. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md").


## Build your own collector


You can build your own collector with the following configuration to monitor your application in CloudWatch with OpenTelemetry. For more information, see [Building a custom collector](https://opentelemetry.io/docs/collector/custom-collector/ "https://opentelemetry.io/docs/collector/custom-collector/").


The common configuration for CloudWatch.



```

dist:
  name: otelcol-dev
  description: OTel Collector for sending telemetry to CloudWatch.
  output_path: ./otelcol-dev
extensions:
  - gomod: github.com/open-telemetry/opentelemetry-collector-contrib/extension/sigv4authextension v0.111.0
  - gomod: github.com/open-telemetry/opentelemetry-collector-contrib/extension/awsproxy v0.113.0
exporters:
  - gomod: go.opentelemetry.io/collector/exporter/otlpexporter v0.111.0
  - gomod: go.opentelemetry.io/collector/exporter/otlphttpexporter v0.111.0
receivers:
  - gomod: go.opentelemetry.io/collector/receiver/otlpreceiver v0.111.0
            
```

Additional configuration for traces.



```
# Enable Tracing 
dist:
  name: otelcol-dev
  description: OTel Collector for sending telemetry to CloudWatch.
  output_path: ./otelcol-dev
extensions:
    #Include common configurations and your custom extensions

exporters:
    #Include common configurations and your custom extensions
 
receivers:
  - gomod: go.opentelemetry.io/collector/receiver/otlpreceiver v0.111.0
processors:
  - gomod: github.com/amazon-contributing/opentelemetry-collector-contrib/processor/awsapplicationsignalsprocessor v0.113.0
  - gomod: github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor v0.113.0
  - gomod: github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstransformprocessor v0.113.0
replaces:
  - github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/awsutil v0.113.0 => github.com/amazon-contributing/opentelemetry-collector-contrib/internal/aws/awsutil v0.113.0
  - github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/cwlogs v0.113.0 => github.com/amazon-contributing/opentelemetry-collector-contrib/internal/aws/cwlogs v0.113.0
  - github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsemfexporter v0.113.0 => github.com/amazon-contributing/opentelemetry-collector-contrib/exporter/awsemfexporter v0.113.0
  - github.com/openshift/api v3.9.0+incompatible => github.com/openshift/api v0.0.0-20180801171038-322a19404e37
            
```

###### Note

Note the following:
 


* After the collector is built, deploy and configure the custom collector in a host or kubernetes environment by following the procedure under [OpenTelemetry Collector Contrib](CloudWatch-OTLPSimplesetup.md "CloudWatch-OTLPSimplesetup.md").
* For information on setting up custom OpenTelemetry collector with Application Signals Processor, see an [Application Signals custom configuration](https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/appsignals_custom_otel_setup/custom-opentelemetry.yaml "https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/appsignals_custom_otel_setup/custom-opentelemetry.yaml")example.
 Application Signals Processor only supports the latest versions of the OpenTelemetry Collectors for custom builds. For information on the supported versions, see [opentelemetry-collector-contrib repository.](https://github.com/amazon-contributing/opentelemetry-collector-contrib/tags "https://github.com/amazon-contributing/opentelemetry-collector-contrib/tags")
