

# Viewing a list of runs in AWS Device Farm
<a name="how-to-view-runs-list"></a>

You can use the Device Farm console, AWS CLI, or API to view a list of runs for a project.

**Topics**
+ [View a list of runs (console)](#how-to-view-runs-list-console)
+ [View a list of runs (AWS CLI)](#how-to-view-runs-list-cli)
+ [View a list of runs (API)](#how-to-view-runs-list-api)

## View a list of runs (console)
<a name="how-to-view-runs-list-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. In the list of projects, choose the project that corresponds to the list you want to view.
**Tip**  
You can use the search bar to filter the project list by name.

## View a list of runs (AWS CLI)
<a name="how-to-view-runs-list-cli"></a>
+ Run the [**list-runs**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-runs.html) command.

  To view information about a single run, run the [**get-run**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-run.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](cli-ref.md).

## View a list of runs (API)
<a name="how-to-view-runs-list-api"></a>
+ Call the [`ListRuns`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListRuns.html) API.

  To view information about a single run, call the [`GetRun`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRun.html) API.

For information about the Device Farm API, see [Automating Device Farm](api-ref.md).