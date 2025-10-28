# View your experiments

You can view the progress of a running experiment, and you can view experiments
that have completed, stopped, or failed.

Stopped, completed, and failed experiments are automatically removed from your
account after 120 days.

###### To view experiments using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiments**.
3. Choose the **Experiment ID** of the experiment to open
   its details page.
4. Do one or more of the following:
   - Check **Details**, **State** for
     the [state of the
     experiment](#experiment-states "#experiment-states").
   - Choose the **Actions** tab for information about the
     experiment actions.
   - Choose the **Targets** tab for information about the
     experiment targets.
   - Choose the **Timeline** tab for a visual representation
     of the actions based on their start and end times.

###### To view experiments using the CLI

Use the [list-experiments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-experiments.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-experiments.html") command to get a list of experiments, and use the
[get-experiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment.html")
command to get information about a specific experiment.

## Experiment states

An experiment can be in one of the following states:

- **pending** – The experiment is pending.
- **initiating** – The experiment is preparing to start.
- **running** – The experiment is running.
- **completed** – All actions in the experiment completed successfully.
- **stopping** – The stop condition was triggered or the experiment
  was stopped manually.
- **stopped** – All running or pending actions in the experiment are
  stopped.
- **failed** – The experiment failed due to an error, such as
  insufficient permissions or incorrect syntax.
- **cancelled** – The experimented was stopped or prevented from starting due to an engaged safety lever.

## Action states

An action can be in one of the following states:

- **pending** – The action is pending, either because the experiment
  hasn't started or the action is to start later in the experiment.
- **initiating** – The action is preparing to start.
- **running** – The action is running.
- **completed** – The action completed successfully.
- **cancelled** – The experiment stopped before the action started.
- **skipped** – The action has been skipped.
- **stopping** – The action is stopping.
- **stopped** – All running or pending actions in the experiment are
  stopped.
- **failed** – The action failed due to a client error, such as
  insufficient permissions or incorrect syntax.
