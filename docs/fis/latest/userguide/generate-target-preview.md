# Generate a target preview from an experiment template

Before you start an experiment, you can generate a target preview to verify that your experiment template is configured to target the expected resources.
The resources that are targeted when you begin the actual experiment may be different from those in the preview, as resources may be removed, updated, or sampled randomly.
When you generate a target preview, you start an experiment that skips all actions.

###### Note

Generating a target preview does not allow you to verify that you have the necessary permissions to take actions on your resources.

###### To start a target preview using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiment
   templates**.
3. To view the targets for the experiment template, choose **Targets**.
4. To verify your target resources for the experiment template, choose **Generate Preview**. When you run an experiment, this target preview will be
   automatically updated with the targets from the most recent experiment.

###### To start a target preview using the CLI

- Run the following [start-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html") command. Replace the values in italics with your own values.

```
aws fis start-experiment \
    --experiment-options actionsMode=skip-all \
    --experiment-template-id `*EXTxxxxxxxxx*`
```
