# Enable CloudWatch Application Signals

Use CloudWatch Application Signals to automatically instrument your applications on AWS so that you
can track application performance against your business objectives. Application Signals
provides you a unified, application-centric view of your Java applications, their
dependencies, and their edges. For more information, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md").

CloudWatch Application Signals leverages the CloudWatch agent to receive metrics and traces from your
auto-instrumented applications, optionally apply rules to reduce high cardinality, and
then publish the processed telemetry to CloudWatch. You can provide custom configuration to the
CloudWatch agent specifically for Application Signals using the agent configuration file. To
start with, the presence of an `application_signals` section under the
`metrics_collected` section within the `logs` section of the agent
configuration file specifies that the CloudWatch agent will receive metrics from your
auto-instrumented applications. Similarly, the presence of an
`application_signals` section under the `traces_collected` section
within the `traces` section of the agent configuration file specifies that the
CloudWatch agent is enabled to receive traces from your auto-instrumented applications. In
addition, you can optionally pass in custom configuration rules to reduce publishing
high-cardinality telemetry as outlined in this section.

- For Amazon EKS clusters, when you install the [Amazon CloudWatch
  Observability](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md") EKS add-on, the CloudWatch agent is by default enabled to receive
  both metrics and traces from your auto-instrumented applications. If you would like to
  optionally pass in custom configuration rules, you can do so by passing in a custom
  agent configuration to the Amazon EKS add-on when you create or update it by using
  additional configuration, as outlined in [(Optional) Additional configuration](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration").
- For RedHat for OpenShift on AWS (ROSA), when you install the CloudWatch agent operator
  using helm charts, the CloudWatch agent is by default enabled to receive both metrics and
  traces from your auto-instrumented applications. If you would like to optionally pass
  in custom configuration rules, you can do so by passing in a custom agent
  configuration by using the Helm chart, as outlined in [(Optional) Additional configuration](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration").
- For other supported platforms including Amazon EC2, you must start the CloudWatch agent with
  an agent configuration that enables Application Signals by specifying the
  `application_signals` sections and optionally any custom configuration
  rules as outlined later in this section.
  The following is an overview of the fields in the CloudWatch agent configuration file that
  are related to CloudWatch Application Signals.

- `logs`
  - `metrics_collected` – This field can contain sections to
    specify that the agent is to collect logs to enable use cases such as CloudWatch
    Application Signals and Container Insights with enhanced observability for
    Amazon EKS.

  ###### Note

  Previously this section was also used to specify that the agent is to
  collect logs that are in embedded metric format. Those settings are no longer
  needed.

      - `application_signals` (Optional) Specifies that you want to
       enable CloudWatch Application Signals to receive metrics from your auto-instrumented
       applications to facilitate CloudWatch Application Signals.




      	* `rules` (Optional) An array of rules to conditionally
      	 select metrics and traces and apply actions to handle high-cardinality
      	 scenarios. Each rule can contain the following fields:




      		+ `rule_name` (Optional) The name of the rule.
      		+ `selectors` (Optional) An array of metrics and traces
      		 dimension matchers. Each selector must provide the following
      		 fields:




      			- `dimension` Required if `selectors` is
      			 not empty. This specifies the dimension of metrics and traces to
      			 use as a filter.
      			- `match` Required if `selectors` is not
      			 empty. A wildcard pattern used for matching values of the
      			 specified dimension.
      		+ `action` (Optional) The action to be applied to metrics
      		 and traces that match the specified selectors. The value of
      		 `action` must be one of the following keywords:




      			- `keep` Specifies to send only the metrics and
      			 traces to CloudWatch if matched by the `selectors`.
      			- `drop` Specifies to drop the metric and traces that
      			 match the `selectors`.
      			- `replace` Specifies to replace the dimensions of
      			 the metrics and traces that match `selectors`. They are
      			 replaced according to the `replacements`
      			 section.
      		+ `replacements` Required if `action` is
      		 `replace`. An array of dimension and value pairs that
      		 will be applied to metrics and traces that match the specified
      		 `selectors` when the `action` is
      		 `replace`. Each replacement must provide the following
      		 fields:




      			- `target_dimension` Required if
      			 `replacements` is not empty. Specifies the dimension
      			 that needs to be replace.
      			- `value` Required if `replacements` is
      			 not empty. The value to replace the original value of
      			 `target_dimension` with.
      	* `limiter` (Optional) Use this section to limit how many
      	 metrics and dimensions Application Signals sends to CloudWatch, to optimize your
      	 costs.




      		+ `disabled` (Optional) If `true`, the metric
      		 limiting feature is disabled. The default is `false`
      		+ `drop_threshold` (Optional) The maximum number of
      		 distinct metrics per service in one rotation interval that can be
      		 exported by one CloudWatch agent. The default is 500.
      		+ `rotation_interval` (Optional) The interval at which
      		 the limiter resets the metric records for distinction counting. This
      		 is expressed as a string with a sequence of numbers and a unit suffix.
      		 Fractions are supported. The supported unit suffixes are
      		 `s`, `m`, `h`, `ms`,
      		 `us`, and `ns`. The default is `1h` for one hour.
      		+ `log_dropped_metrics` (Optional) Specifies whether the
      		 agent should write logs to the CloudWatch agent logs when Application
      		 Signals metrics are dropped. The default is `false`.


      		###### Note

      		To activate this logging, the `debug` parameter in
      		 the `agent` section must also be set to
      		 `true`.

- `traces`
  - `traces_collected`
    - `application_signals` Optional. Specify this to enable the CloudWatch
      agent to receive traces from your auto-instrumented applications for
      facilitating CloudWatch Application Signals.

###### Note

Even though the custom `application_signals` rules are specified under
the `metrics_collected` section that is contained in the `logs`
section, they also implicitly apply to the `traces_collected` section as
well. The same set of rules will apply to both metrics and traces.

When there are multiple rules with different actions, they apply in the following
sequence: `keep`, then `drop`, then `replace`.

The following is an example of a full CloudWatch agent configuration file that applies
custom rules.

```
{
  "logs": {
    "metrics_collected": {
      "application_signals": {
        "rules": [
          {
            "rule_name": "keep01",
            "selectors": [
              {
                "dimension": "Service",
                "match": "pet-clinic-frontend"
              },
              {
                "dimension": "RemoteService",
                "match": "customers-service"
              }
            ],
            "action": "keep"
          },
          {
            "rule_name": "drop01",
            "selectors": [
              {
                "dimension": "Operation",
                "match": "GET /api/customer/owners/*"
              }
            ],
            "action": "drop"
          },
          {
            "rule_name": "replace01",
            "selectors": [
              {
                "dimension": "Operation",
                "match": "PUT /api/customer/owners/*/pets/*"
              },
              {
                "dimension": "RemoteOperation",
                "match": "PUT /owners"
              }
            ],
            "replacements": [
              {
                "target_dimension": "Operation",
                "value": "PUT /api/customer/owners/{ownerId}/pets{petId}"
              }
            ],
            "action": "replace"
          }
        ]
      }
    }
  },
  "traces": {
    "traces_collected": {
      "application_signals": {}
    }
  }
}
```

For the previous example configuration file, the `rules` are processed as
follows:

1. Rule `keep01` ensures that any metrics and traces with the dimension
   `Service` as `pet-clinic-frontend` and the dimension
   `RemoteService` as `customers-service` are kept.
2. For the processed metrics and traces after applying `keep01`, the
   `drop01` rule ensures that metrics and traces with the dimension
   `Operation` as `GET /api/customer/owners/*` are
   dropped.
3. For the processed metrics and traces after applying `drop01`, the
   `replace01` rule updates metrics and traces that have the dimension
   `Operation` as `PUT /api/customer/owners/*/pets/*` and the
   dimension `RemoteOperation` as `PUT /owners` such that their
   `Operation` dimension is now replaced to be `PUT
 /api/customer/owners/{ownerId}/pets{petId}`.
   The following is a complete example of a CloudWatch configuration file that manages
   cardinality in Application Signals by changing the metric limit to 100, enabling the
   logging of dropped metrics, and setting the rotation interval to two hours.

```
{
    "logs": {
        "metrics_collected": {
            "application_signals": {
                "limiter": {
                    "disabled": false,
                    "drop_threshold": 100,
                    "rotation_interval": "2h",
                    "log_dropped_metrics": true
                }
            }
        },
        "traces": {
            "traces_collected": {
                "application_signals": {}
            }
        }
    }
}
```
