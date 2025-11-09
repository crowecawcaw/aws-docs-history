Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Issues concepts

Creating an issue is a quick and efficient way to track work being done within a project.
You can use issues to help you discuss work in daily sync-up meetings, prioritize work, and
more.

This page includes a list of concepts that will help you effectively use issues in CodeCatalyst.

## Active issues

_Active issues_ are issues that are any issues that are not in a
**Draft** status or archived. In other words,
active issues are issues with a status in any of the following status categories:
**Not started**, **Started**, and **Completed**. For
more information about statuses and status categories, see
[Status and status categories](#issues-concepts-status-definition "#issues-concepts-status-definition").

You can view
all of the active issues in your project from the default **Active issues** view.

## Archived issues

An _archived issue_ is an issue that is no longer relevant to your project.
For example, you can [archive an issue](issues-archive-issues.md "issues-archive-issues.md") if it is completed and you no
longer need to see it in the **Done** column, or if it was created in error. Archived issues
can be unarchived if needed.

## Assignee

The _assignee_ is the person the issue is assigned to. If the
person doesn't appear in the list when you search for them, they have not been added to
your project. To add them, see [Inviting
a user to a project](projects-members.md#projects-members-add "projects-members.md#projects-members-add"). To enable multiple assignees to an issue,
see [Enabling or disabling multiple assignees](issues-settings-multiple-assignees.md "issues-settings-multiple-assignees.md"). Issues with
multiple assignees will appear on your board with different colored avatars, each
representing one of the assignees.

## Custom fields

_Custom fields_ allow you to customize different attributes of an
issue according to your needs for tracking and maintaining issues within a project. For
example, you can add a field for roadmapping, a specific due date, or a requester field.

## Estimate

In agile development, the _estimate_ is known as story points. You can use
the estimate for an issue to represent the amount of work required, in addition to the ambiguity and
complexity of the issue. Consider using higher estimates for issues with greater risk, difficulty,
and unknowns.

For more information about estimation types and how to configure them, see [Configuring issue effort estimation](issues-settings-estimation.md "issues-settings-estimation.md").

## Issue

An _issue_ is a record that tracks the work related to your project. You
can create an issue for a feature, a task, a bug, or any other body of work related to your
project. If you're using agile development, an issue can also describe an epic or user story.

## Label

The _label_ is used to group, sort and filter issues. You can enter
a new label name or choose one of the labels from the populated list. This list consists
of recently used labels in the project. An issue can have multiple labels, and a label
can be removed from an issue. To customize labels, see [Categorizing work with labels](issues-labels.md "issues-labels.md").

## Priority

_Priority_ refers to the level of importance of the issue. There
are four options: **Low**, **Medium**,
**High**, and **No priority**.

## Status and status categories

The _status_ is the current state of the issue and is used to quickly check the progress
of an issue through its lifecycle, from inception to completion. All issues must have a status, and
each status belongs to a _status category_. Status categories are used to help organize your
statuses and populate the default issue views.

There are five default statuses and four status categories in CodeCatalyst. You can create other statuses, but you cannot create
other status categories. The following list contains the default statuses and their status categories in parenthesis:
**Backlog (Draft)**, **To do (Not started)**,
**In progress (Started)**, **In review (Started)**, and
**Done (Completed)**.

For more information on working with statuses, see [Tracking work with custom statuses](issues-customize-statuses.md "issues-customize-statuses.md").

## Tasks

_Tasks_ can be added to issues to further break down and organize the work of that issue. You can
add tasks to an issue on creation, or add tasks to an existing issue. When viewing an issue, you can reorder, remove, or mark its tasks as completed.

## Views

Issues in your CodeCatalyst project are displayed in _views_.
Views can either be grid views that show issues in list format or
board views that show issues as tiles in columns organized by issue status.
There are four default views, and you
can [create your own views with custom grouping, filtering, and sorting](issues-creating-view.md "issues-creating-view.md").
The following list contains details about the four default views.

- The **Drafts** view is a grid view that shows issues not currently being worked on.
  Any issue created with a status in the **Draft** status category shows up in this view.
  This view can be used by teams to see which issues are still being defined or are waiting to be assigned and worked on.
- The **Active issues** view is a board view of all issues that are currently being worked on. Any issue
  with a status in the **Not started**, **Started**, or **Completed**
  status categories will show up in this view.
- The **All issues** view is a grid view that shows all the issues in the project,
  both _drafts_ and _active issues_.
- The **Archived** view shows all archived issues.
