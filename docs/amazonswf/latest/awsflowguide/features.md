# Workflow and Activity Type Registration

Amazon SWF requires activity and workflow types to be registered before they can be used. The framework
automatically registers the workflows and activities in the implementations you add to the worker. The framework
looks for types that implement workflows and activities and registers them with Amazon SWF. By default, the framework uses
the interface definitions to infer registration options for workflow and activity types. All workflow interfaces are
required to have either the `@WorkflowRegistrationOptions` annotation or the
`@SkipRegistration` annotation. The workflow worker registers all workflow types it is configured with
that have the `@WorkflowRegistrationOptions` annotation. Similarly, each activity method is required to be
annotated with either the `@ActivityRegistrationOptions` annotation or the `@SkipRegistration`
annotation or one of these annotations must be present on the `@Activities` interface. The activity worker
registers all activity types that it is configured with that an `@ActivityRegistrationOptions` annotation
applies to. The registration is performed automatically when you start one of the workers. Workflow and activity
types that have the `@SkipRegistration` annotation are not registered.
`@ActivityRegistrationOptions`, and `@SkipRegistration` annotations have override semantics and
the most specific one is applied to an activity type.

Note that Amazon SWF doesn't allow you to re-register or modify the type once it has been registered. The framework
will try to register all types, but if the type is already registered it will not be re-registered and no error will
be reported.

If you need to modify registered settings, you must register a new version of the type. You can also override
registered settings when starting a new execution or when calling an activity that uses the generated clients.

The registration requires a type name and some other registration options. The default implementation
determines these as follows:

## Workflow Type Name and Version

The framework determines the name of the workflow type from the workflow interface. The form of the default
workflow type name is {`prefix`}{`name`}. The
{`prefix`} is set to the name of the `@Workflow` interface followed by a '.'
and the {`name`} is set to the name of the `@Execute` method. The default name
of the workflow type in the preceding example is `MyWorkflow.startMyWF`. You can override the default
name using the name parameter of the `@Execute` method. The default name of the workflow type in the
example is `startMyWF`. The name must not be an empty string. Note that when you override the name
using `@Execute`, the framework doesn't automatically prepend a prefix to it. You are free to use
your own naming scheme.

The workflow version is specified using the `version` parameter of the
`@Execute` annotation. There is no default for `version` and it must be
explicitly specified; `version`is a free form string, and you are free to use your own
versioning scheme.

## Signal Name

The name of the signal can be specified using the name parameter of the `@Signal` annotation.
If not specified, it is defaulted to the name of the signal method.

## Activity Type Name and Version

The framework determines the name of the activity type from the activities interface. The form of the
default activity type name is {`prefix`}{`name`}. The
{`prefix`} is set to the name of the `@Activities` interface followed by a '.'
and the {`name`} is set to the method name. The default
{`prefix`} can be overridden in the `@Activities` annotation on the activities
interface. You can also specify the activity type name using the `@Activity` annotation on the activity
method. Note that when you override the name using `@Activity`, the framework will not automatically
prepend a prefix to it. You are free to user your own naming scheme.

The activity version is specified using the version parameter of the `@Activities` annotation.
This version is used as the default for all activities defined in the interface and can be overridden on a
per-activity basis using the `@Activity` annotation.

## Default Task List

The default task list can be configured using the `@WorkflowRegistrationOptions` and
`@ActivityRegistrationOptions` annotations and setting the `defaultTaskList` parameter. By
default, it is set to `USE_WORKER_TASK_LIST`. This is a special value that instructs the
framework to use the task list that is configured on the worker object that is used to register the activity or
workflow type. You can also choose to not register a default task list by setting the default task list to
`NO_DEFAULT_TASK_LIST` using these annotations. This can be used in cases where you want to
require that the task list be specified at run time. If no default task list has been registered, then you must
specify the task list when starting the workflow or calling the activity method using the
`StartWorkflowOptions` and `ActivitySchedulingOptions` parameters on the respective method
overload of the generated client.

## Other Registration Options

All workflow and activity type registration options that are allowed by the Amazon SWF API can be specified
through the framework.

For a complete list of _workflow_ registration options, see the following:

- [@Workflow](annotations.md#annotations-workflow "annotations.md#annotations-workflow")
- [@Execute](annotations.md#annotations-execute "annotations.md#annotations-execute")
- [@WorkflowRegistrationOptions](annotations.md#annotations-workflowregistrationoptions "annotations.md#annotations-workflowregistrationoptions")
- [@Signal](annotations.md#annotations-signal "annotations.md#annotations-signal")

For a complete list of _activity_ registration options, see the following:

- [@Activity](annotations.md#annotations-activity "annotations.md#annotations-activity")
- [@Activities](annotations.md#annotations-activities "annotations.md#annotations-activities")
- [@ActivityRegistrationOptions](annotations.md#annotations-activityregistration "annotations.md#annotations-activityregistration")

If you want to have complete control over type registration, see [Worker Extensibility](running.md#running.workerextend "running.md#running.workerextend").
