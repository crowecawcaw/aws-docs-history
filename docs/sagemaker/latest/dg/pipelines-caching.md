# Caching pipeline steps

In Amazon SageMaker Pipelines, you can use step caching to save time and resources when rerunning pipelines.
Step caching reuses the output of a previous successful run of a step (instead of recomputing it) when
the step has the same configuration and inputs. This helps you achieve consistent results across
pipeline reruns with identical parameters. The following topic shows you how to configure and turn
on step caching for your pipelines.

When you use step signature caching, Pipelines tries to find a previous run of your current
pipeline step with the same values for certain attributes. If found, Pipelines propagates the
outputs from the previous run rather than recomputing the step. The attributes checked are
specific to the step type, and are listed in [Default cache key attributes by pipeline step
type](pipelines-default-keys.md "pipelines-default-keys.md").

You must opt in to step caching — it is off by default. When you turn on step caching, you
must also define a timeout. This timeout defines how old a previous run can be to remain a
candidate for reuse.

Step caching only considers successful runs — it never reuses failed runs.
When multiple successful runs exist within the timeout period, Pipelines uses the
result for the most recent successful run. If no successful runs match in the timeout period,
Pipelines reruns the step. If the executor finds a previous run that meets the criteria but is
still in progress, both steps continue running and update the cache if they're
successful.

Step caching is only scoped for individual pipelines, so you can’t reuse a step from another
pipeline even if there is a step signature match.

Step caching is available for the following step types:

- [Processing](build-and-manage-steps-types.md#step-type-processing "build-and-manage-steps-types.md#step-type-processing")
- [Training](build-and-manage-steps-types.md#step-type-training "build-and-manage-steps-types.md#step-type-training")
- [Tuning](build-and-manage-steps-types.md#step-type-tuning "build-and-manage-steps-types.md#step-type-tuning")
- [AutoML](build-and-manage-steps-types.md#step-type-automl "build-and-manage-steps-types.md#step-type-automl")
- [Transform](build-and-manage-steps-types.md#step-type-transform "build-and-manage-steps-types.md#step-type-transform")
- [ClarifyCheck](build-and-manage-steps-types.md#step-type-clarify-check "build-and-manage-steps-types.md#step-type-clarify-check")
- [QualityCheck](build-and-manage-steps-types.md#step-type-quality-check "build-and-manage-steps-types.md#step-type-quality-check")
- [EMR](build-and-manage-steps-types.md#step-type-emr "build-and-manage-steps-types.md#step-type-emr")

###### Topics

- [Turn on step caching](pipelines-caching-enabling.md "pipelines-caching-enabling.md")
- [Turn off step caching](pipelines-caching-disabling.md "pipelines-caching-disabling.md")
- [Default cache key attributes by pipeline step
  type](pipelines-default-keys.md "pipelines-default-keys.md")
- [Cached data access control](pipelines-access-control.md "pipelines-access-control.md")
