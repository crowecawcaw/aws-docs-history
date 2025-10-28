# Viewing a list of runs in AWS Device Farm

You can use the Device Farm console, AWS CLI, or API to view a list of runs for a project.

###### Topics

- [View a list of runs (console)](#how-to-view-runs-list-console "#how-to-view-runs-list-console")
- [View a list of runs (AWS CLI)](#how-to-view-runs-list-cli "#how-to-view-runs-list-cli")
- [View a list of runs (API)](#how-to-view-runs-list-api "#how-to-view-runs-list-api")

## View a list of runs (console)

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. In the list of projects, choose the project that corresponds to the list you want to view.

###### Tip

You can use the search bar to filter the project list by name.

## View a list of runs (AWS CLI)

- Run the [**list-runs**](../../../cli/latest/reference/devicefarm/list-runs.md "../../../cli/latest/reference/devicefarm/list-runs.md") command.

To view information about a single run, run the [**get-run**](../../../cli/latest/reference/devicefarm/get-run.md "../../../cli/latest/reference/devicefarm/get-run.md")
command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](cli-ref.md "cli-ref.md").

## View a list of runs (API)

- Call the [`ListRuns`](../APIReference/API_ListRuns.md "../APIReference/API_ListRuns.md") API.

To view information about a single run, call the
[`GetRun`](../APIReference/API_GetRun.md "../APIReference/API_GetRun.md") API.

For information about the Device Farm API, see [Automating Device Farm](api-ref.md "api-ref.md").
