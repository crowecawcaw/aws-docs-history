

# Viewing the projects list in AWS Device Farm
<a name="how-to-view-projects-list"></a>

You can use the AWS Device Farm console, AWS CLI, or AWS Device Farm API to view the list of projects.

**Topics**
+ [Prerequisites](#how-to-view-projects-list-prerequisites)
+ [View the projects list (console)](#how-to-view-projects-list-console)
+ [View the projects list (AWS CLI)](#how-to-view-projects-list-cli)
+ [View the projects list (API)](#how-to-view-projects-list-api)

## Prerequisites
<a name="how-to-view-projects-list-prerequisites"></a>
+ Create at least one project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md), and then return to this page.

## View the projects list (console)
<a name="how-to-view-projects-list-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. To find the list of available projects, do the following:
   + For mobile device testing projects, on the Device Farm navigation menu, choose **Mobile Device Testing**, then choose **Projects**.
   + For desktop browser testing projects, on the Device Farm navigation menu, choose **Desktop Browser Testing**, then choose **Projects**.

## View the projects list (AWS CLI)
<a name="how-to-view-projects-list-cli"></a>
+ To view the projects list, run the [**list-projects**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-projects.html) command.

  To view information about a single project, run the [**get-project**](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-project.html) command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](cli-ref.md).

## View the projects list (API)
<a name="how-to-view-projects-list-api"></a>
+ To view the projects list, call the [`ListProjects`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListProjects.html) API.

  To view information about a single project, call the [`GetProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetProject.html) API.

For information about the AWS Device Farm API, see [Automating Device Farm](api-ref.md).