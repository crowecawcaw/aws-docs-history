# Managing your AWS FIS experiments

AWS FIS enables you to perform fault injection experiments on your
AWS workloads. To get started, create an [experiment template](experiment-templates.md "experiment-templates.md"). After you create an experiment template, you can
use it to start an experiment.

An experiment is finished when one of the following occurs:

- All [actions](action-sequence.md "action-sequence.md") in the template completed
  successfully.
- A [stop condition](stop-conditions.md "stop-conditions.md") is triggered.
- An action cannot be completed because of an error. For example, if the
  [target](targets.md "targets.md") cannot be found.
- The experiment is [stopped manually](stop-experiment.md "stop-experiment.md").
  You cannot resume a stopped or failed experiment. You also cannot rerun a completed experiment.
  However, you can start a new experiment from the same experiment template. You can optionally
  update the experiment template before you specify it again in a new experiment.

###### Tasks

- [Start an experiment](run-experiment.md "run-experiment.md")
- [View your experiments](view-experiment-progress.md "view-experiment-progress.md")
- [Tag an experiment](tag-experiment.md "tag-experiment.md")
- [Stop an experiment](stop-experiment.md "stop-experiment.md")
- [List resolved targets](list-experiment-resolved-targets.md "list-experiment-resolved-targets.md")
