

# Disabling transitive matching
<a name="disable-transitive-matching"></a>

The `enableTransitiveMatching` setting is immutable. You cannot change this setting after you create a workflow.

To disable transitive matching, you must create a new matching workflow without the `enableTransitiveMatching` parameter, or set it to `false` in the `CreateMatchingWorkflow` API request. There is no AWS Entity Resolution console option to disable transitive matching.

To replace a transitive matching workflow with a non-transitive workflow, complete the following steps:

1. Create a new matching workflow using the `CreateMatchingWorkflow` API without the `matchingConfig` parameter, or with `enableTransitiveMatching` set to `false`.

1. Run the new workflow to verify that it produces the expected results.

1. Delete the old transitive matching workflow if it is no longer needed. For more information, see [Deleting a matching workflow](delete-matching-workflow.md).