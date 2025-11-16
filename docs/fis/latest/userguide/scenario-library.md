# Working with the AWS FIS scenario library

Scenarios define events or conditions that customers can apply to test the resiliency of
their applications, such as the interruption of compute resources on which the application
is running. Scenarios are created and owned by AWS, and minimize undifferentiated heavy
lifting by providing you with a group of pre-defined targets and fault actions (e.g.,
stopping 30% of instances in an autoscaling group) for common application impairments.

Scenarios are provided through a console-only scenario library and run using an AWS FIS
experiment template. In order to run an experiment using a scenario, you will select the
scenario from the library, specify parameters matching your workload details, and save it as an
experiment template in your account.

###### Topics

- [Viewing a scenario](#viewing-a-scenario "#viewing-a-scenario")
- [Using a scenario](#using-a-scenario "#using-a-scenario")
- [Exporting a scenario](#exporting-a-scenario "#exporting-a-scenario")
- [Scenarios reference](scenario-library-scenarios.md "scenario-library-scenarios.md")

## Viewing a scenario

To view a scenario using the console:

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Scenario library**.
3. To view information about a specific scenario, select the scenario card to
   bring up a split panel.
   - In the **Description** tab in the split panel at
     the bottom of the page, you can view a short description of the scenario. You
     can also find a short summary of pre-requisites containing a summary of the
     target resources required and any actions you need to take to prepare the
     resources for use with the scenario. Finally you can also see additional
     information about the targets and actions in the scenario as well as the
     anticipated duration when the experiment runs successfully with default
     settings.
   - In the **Content** tab in the split panel at the
     bottom of the page, you can preview a partially populated version of the
     experiment template that will be created from the scenario.
   - In the **Details** tab in the split panel at the
     bottom of the page, you can find a detailed explanation how the scenario is
     implemented. This may contain detailed information about how individual aspects
     of the scenario are approximated. Where applicable you can also read about what
     metrics to use as stop conditions and to provide observability to learn from the
     experiment. Finally you will find recommendations how to expand the resulting
     experiment template.

## Using a scenario

To use a scenario using the console:

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Scenario library**.
3. To view information about a specific scenario, select the scenario card to
   bring up a split panel
4. To use the scenario, select the scenario card and choose **Create
   template with scenario**.
5. In the **Create experiment template** view fill in any
   missing items.
   1. Some scenarios allow you to edit parameters that are shared
      across multiple actions or targets. This functionality will be disabled
      once you make any changes to the scenario, including changes by the shared
      parameter editing. To use this feature select the **Edit shared parameters**
      button. Edit parameters in the modal and select the **Save** button.
   2. Some experiment templates may have missing action or target
      parameters, highlighted on each action and target card. Select the **Edit** button for each card, add the missing information,
      and select the **Save** button on the card.
   3. All templates require a **Service access**
      execution role. You can choose an existing role or create a new role
      for this experiment template.
   4. We recommend defining one or more optional **Stop
      conditions** by selecting an existing AWS CloudWatch alarm.
      Learn more about [Stop conditions for AWS FIS](stop-conditions.md "stop-conditions.md"). If
      you don't have an alarm configured yet, you can follow the
      instructions at [Using
      Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") and update the experiment template
      later.
   5. We recommend enabling optional experiment **Logs**
      to Amazon CloudWatch logs or to an Amazon S3 bucket. Learn more
      about [Experiment logging for AWS FIS](monitoring-logging.md "monitoring-logging.md").
      If you don't have appropriate resources configured yet, you can
      update the experiment template later.

6. In the **Create experiment template** select **Create
   experiment template**.
7. From the **Experiment templates** view of the AWS FIS console
   select **Start experiment**. Learn more about [Managing AWS FIS experiment templates](experiments.md "experiments.md").

## Exporting a scenario

Scenarios are a console-only experience. While similar to experiment templates,
scenarios are not complete experiment templates and can not be directly imported into
AWS FIS. If you wish to use scenarios as part of your own automation, you can use one of two
paths:

1. Follow the steps in [Using a scenario](#using-a-scenario "#using-a-scenario") to create a
   valid AWS FIS experiment template and export that template.
2. Follow the steps in [Viewing a scenario](#viewing-a-scenario "#viewing-a-scenario") and in
   step 3, from the **Content** tab, copy and save the scenario
   content, then add missing parameters manually to create a valid experiment
   template.
