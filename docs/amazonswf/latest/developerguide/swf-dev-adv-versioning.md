# Versioning

Business needs often require you to have different implementations or variations of the same workflow or
activity running simultaneously. For example, you might want to test a new implementation of a workflow while
another one is in production. You might also want to run two different implementations with two different feature
sets, such as a basic and premium implementation. Versioning enables you to run multiple implementations of
workflows and activities concurrently, for any purpose that meets your requirements.

Workflow and activity types have a version associated with them which is specified at registration time.
Version is a free-form string and you can choose your own versioning scheme. In order to create a new version of a
registered type, you should register it with the same name and a different version. [Task lists in Amazon SWF](swf-dev-task-lists.md "swf-dev-task-lists.md") , described earlier, can further help you to
implement versioning. Consider a situation in which you have long-running workflow executions of a given type
already in progress, and circumstances require that you revise the workflow, such as to add a new feature. You
could implement the new feature by creating new versions of activity types and workers, and a new decider. Then
you could launch executions of the new workflow version using a different set of task lists. This way, you could
have executions of workflows of different versions running simultaneously without affecting each other.
