# Viewing an Elastic Beanstalk environment's event stream

This topic explains how to access events and notifications associated with your application.

## Viewing events with the Elastic Beanstalk console

###### To view events with the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Events**.

The Events page shows a list of all events that have been recorded for the environment. You can page through the list choosing
**<** (previous), **>** (next), or page numbers. You can filter the type of events shown by using the
**Severity** drop-down
list.

## Viewing events with command line tools

The [EB CLI](eb-cli3.md "eb-cli3.md") and [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") both provide commands for retrieving events. If you are
managing your environment using the EB CLI, use [eb events](eb3-events.md "eb3-events.md") to print a list of events. This command also
has a `--follow` option that continues to show new events until you press **Ctrl+C** to stop output.

To pull events using the AWS CLI, use the `describe-events` command and specify the environment by name or ID:

```
$ `aws elasticbeanstalk describe-events --environment-id e-gbjzqccra3`
{
    "Events": [
        {
            "ApplicationName": "elastic-beanstalk-example",
            "EnvironmentName": "elasticBeanstalkExa-env",
            "Severity": "INFO",
            "RequestId": "a4c7bfd6-2043-11e5-91e2-9114455c358a",
            "Message": "Environment update completed successfully.",
            "EventDate": "2015-07-01T22:52:12.639Z"
        },
...
```

For more information about the command line tools, see [Setting up the EB command line interface (EB CLI) to manage Elastic Beanstalk](eb-cli3.md "eb-cli3.md").
