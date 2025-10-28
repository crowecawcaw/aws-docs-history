**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How AWS Shield detects events

AWS operates service-level detection systems for the AWS network and individual AWS
services, to ensure that they remain available during a DDoS attack. Additionally,
resource-level detection systems monitor each individual AWS resource to ensure that
traffic toward the resource remains within expected parameters. This combination protects
both the targeted AWS resource and AWS services, by applying mitigations that drop known
bad packets, highlight potentially malicious traffic, and prioritize traffic from end
users.

Detected events appear in your Shield Advanced event summaries, attack details, and Amazon CloudWatch
metrics as either the name of the DDoS attack vector or as `Volumetric` if the
evaluation was based on traffic volume instead of signature. For more information on the
attack vector dimensions that are available within the `DDoSDetected` CloudWatch
metric, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md").

###### Topics

- [AWS Shield detection logic for infrastructure layer
  threats (layer 3 and layer 4)](ddos-event-detection-infrastructure.md "ddos-event-detection-infrastructure.md")
- [Shield Advanced detection logic for application layer threats (layer 7)](ddos-event-detection-application.md "ddos-event-detection-application.md")
- [Shield Advanced detection logic for multiple resources in an application](ddos-event-detection-multiple-resources.md "ddos-event-detection-multiple-resources.md")
