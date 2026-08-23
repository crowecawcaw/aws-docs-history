# Function types and composition

AWS Elemental MediaTailor provides four function types, each designed for a different category of work.
You choose a type when you create a function, and the type determines what the function can
do at runtime. This page explains how each type executes, when to use it, and how to compose
functions into multi-step pipelines.

## Function type overview

| Type                  | Category             | Purpose                                                                                                        |
| --------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `CUSTOM_OUTPUT`       | Data transformation  | Evaluate expressions against the current session state and produce<br>outputs. No external calls.              |
| `HTTP_REQUEST`        | External integration | Make an HTTP call to an external service, then evaluate output<br>expressions that can reference the response. |
| `SEQUENTIAL_EXECUTOR` | Orchestration        | Run a sequence of functions in order, passing data between steps<br>through temporary data.                    |
| `CONCURRENT_EXECUTOR` | Orchestration        | Run a set of functions in parallel up to a maximum concurrency,<br>then combine their outputs.                 |

Each type serves a distinct role. Choose a type when you create a function — the
type determines what the function can do at runtime.

## Composition rules

MediaTailor enforces the following limits on function composition:

| Rule                                         | Limit                                                                                                       |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Maximum nesting depth                        | 2 (an executor can contain functions, but those children cannot be<br>executors themselves)                 |
| Steps per sequence                           | 1 to 10                                                                                                     |
| Children per concurrent executor             | 1 to 10                                                                                                     |
| Maximum concurrency (concurrent executor)    | 1 to 2                                                                                                      |
| Total function executions per lifecycle hook | 20                                                                                                          |
| Circular references                          | Not allowed. A function cannot reference itself, directly or<br>indirectly.                                 |
| Function existence                           | All functions referenced in a `FunctionList` must exist<br>before you create or update the parent executor. |
| Unique namespaces (concurrent executor)      | Each child must have a unique alias or function ID within the<br>executor.                                  |

When you create a function, MediaTailor validates expression syntax, checks for restricted
functions, verifies that all referenced functions exist, and detects circular references.
When you attach a function to a playback configuration, MediaTailor additionally validates
that all output keys across the entire function tree are compatible with the assigned
lifecycle hook.
