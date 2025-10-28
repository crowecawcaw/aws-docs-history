# AWS Resilience Hub – Resilience testing

AWS Resilience Hub supports an enhanced integration with the AWS FIS. This integration allows AWS Resilience Hub
to offer tailored recommendations using AWS FIS actions and scenarios based on the specific context
of the application being assessed. Running the recommended experiments or conducting your own
tests using the AWS FIS service will directly contribute to improving your application's resilience
score.

These AWS FIS actions and scenarios test an application's resiliency posture by creating
disruptive events so that you can observe how your application responds. AWS FIS provides multiple
pre-built scenarios and large selection of actions that generate disruptions. In addition, it
also includes controls and guardrails that you need to run the experiments in production. The
controls and guardrails include options to perform automatic roll back or stop the experiment if
specific conditions are met. To get started using the AWS FIS to run experiments from [AWS Resilience Hub console](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/"), complete the
prerequisites that are defined in [Prerequisites](prerequisites.md "prerequisites.md") section.

The following table lists all the available AWS FIS options from the navigation pane and the
links to the associated AWS FIS documentation that contains the procedures to start using AWS FIS
tests from AWS Resilience Hub console.

| AWS FIS navigation menu options and references | AWS FIS navigation menu option                                                                                                                                | AWS FIS documentation                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | --------------------- |
| **Resilience testing**                         | [Create an experiment template](../../../fis/latest/userguide/create-template.md "../../../fis/latest/userguide/create-template.md")                          |
| **Scenario library**                           | [AWS FIS library](../../../fis/latest/userguide/scenario-library.md "../../../fis/latest/userguide/scenario-library.md")                                      |
| **Experiment templates**                       | [Experiment templates for AWS FIS](../../../fis/latest/userguide/manage-experiment-template.md "../../../fis/latest/userguide/manage-experiment-template.md") | The following table lists all the available AWS FIS options from the dropdown menu in **Resilience testing** section and the links to the associated AWS FIS documentation that contains the procedures to start using AWS FIS tests from AWS Resilience Hub console. AWS FIS dropdown menu options and references | AWS FIS dropdown menu option | AWS FIS documentation |
| ---                                            | ---                                                                                                                                                           |
| **Create experiment template**                 | [Create an experiment template](../../../fis/latest/userguide/create-template.md "../../../fis/latest/userguide/create-template.md")                          |
| **Create an experiment from scenario**         | [Using a scenario](../../../fis/latest/userguide/scenario-library.md#using-a-scenario "../../../fis/latest/userguide/scenario-library.md#using-a-scenario")   |
