# Creating and managing Functions

This page walks you through creating, attaching, updating, and deleting Functions
using the MediaTailor console. Functions let you customize session behavior and ad requests by
running logic at key points during playback.

## Setting up a function

### Creating a function using the console

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Functions**.
3. Choose **Create function**.
4. For **Function ID**, enter a unique name for
   the function (for example, `fetchIdentity`).
5. For **Function type**, choose
   `CUSTOM_OUTPUT`, `HTTP_REQUEST`, or
   `SEQUENTIAL_EXECUTOR`. The console displays the configuration
   fields for the selected type.
6. Fill in the type-specific configuration fields. For a description of each
   function type and its fields, see [Function types and
   composition](monetization-functions-types.md "monetization-functions-types.md").
7. Choose **Create function**.

### Attaching a function to a playback configuration

A function does not run until you attach it to a playback configuration through a
function mapping (a link between a lifecycle hook and a function). The function mapping specifies which lifecycle hook triggers the
function.

1. Open the MediaTailor console.
2. In the navigation pane, choose **Configurations**.
3. Choose the playback configuration you want to update.
4. In the **Function mapping** section, choose
   **Edit**.
5. For each lifecycle hook, select the function to attach:
   - **Session initialization hook**
     — Choose a function to run once at session start.
   - **Ad request hook** — Choose a
     function to run before each ADS request.

6. Choose **Save**.

## Managing functions

### Viewing functions

Navigate to **Functions** to see all functions in
your account. Choose a function name to view its configuration.

### Updating an existing function

To update a function, navigate to **Functions**,
choose the function, and modify the configuration. The update replaces the entire
function definition.

###### Tip

Save a copy of your function configuration before making changes. There is
no built-in versioning or rollback for functions.

## Removing a function

### Detaching a function from a playback configuration

Before you delete a function, remove it from all playback configurations that
reference it.

1. Open the MediaTailor console.
2. In the navigation pane, choose **Configurations**.
3. Choose the playback configuration.
4. In the **Function mapping** section, choose
   **Edit**.
5. Remove the function from the lifecycle hook.
6. Choose **Save**.

### Deleting a function

Navigate to **Functions**, select the function, and
choose **Delete**.

### Deletion blocking rules

MediaTailor prevents you from deleting a function that is still in use.

| Condition                                                                | Result                                                                     |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Function is attached to a playback configuration via function<br>mapping | Delete is blocked. Detach the function first.                              |
| Function is referenced in a<br>`SEQUENTIAL_EXECUTOR`                     | Delete is blocked. Remove the reference from the parent function<br>first. |
| Function is not referenced anywhere                                      | Delete succeeds.                                                           |

## Validation rules

MediaTailor validates your function when you create or update it. The following checks are
performed:

- **Expression syntax** — All expressions
  must be valid JSONata.
- **Restricted functions** — Expressions
  cannot call restricted JSONata functions. See [JSONata expression
  reference](monetization-functions-jsonata.md "monetization-functions-jsonata.md") for the full
  list.
- **Output key prefixes** — All output keys
  must start with a recognized namespace prefix. For the list of accepted
  prefixes, see [Lifecycle hooks](monetization-functions-hooks.md "monetization-functions-hooks.md").
- **Function references** — All function IDs
  in a `FunctionList` must reference existing functions.
- **Circular references** — A function
  cannot reference itself, directly or indirectly.
- **Nesting depth** — A
  `SEQUENTIAL_EXECUTOR` can call other functions, but those
  functions cannot themselves be `SEQUENTIAL_EXECUTOR`s.

For specific values and size limits, see [Limits](monetization-functions-limits.md "monetization-functions-limits.md").

## API reference

To manage functions programmatically, see the [AWS Elemental MediaTailor API Reference](../apireference.md "../apireference.md").
