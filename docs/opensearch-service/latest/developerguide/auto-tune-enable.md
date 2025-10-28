# Enabling or disabling Auto-Tune

OpenSearch Service enables Auto-Tune by default on new domains. To enable or disable Auto-Tune on
existing domains, we recommend using the console, which simplifies the process. Enabling
Auto-Tune doesn't cause a blue/green deployment.

You currently can't enable or disable Auto-Tune using
AWS CloudFormation.

###### To enable Auto-Tune on an existing domain

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home ").
2. In the navigation pane, under **Domains**, choose the
   domain name to open the cluster configuration.
3. Choose **Turn on** if Auto-Tune isn't already
   enabled.
4. Optionally, select **Off-peak window** to schedule
   optimizations that require a blue/green deployment during the domain's
   configured off-peak window. For more information, see [Scheduling Auto-Tune enhancements](auto-tune-schedule.md "auto-tune-schedule.md").
5. Choose **Save changes**.
   To enable Auto-Tune using the AWS CLI, send an [UpdateDomainConfig](../APIReference/API_UpdateDomainConfig.md "../APIReference/API_UpdateDomainConfig.md") request:

```
aws opensearch update-domain-config \
  --domain-name `my-domain` \
  --auto-tune-options DesiredState=ENABLED
```
