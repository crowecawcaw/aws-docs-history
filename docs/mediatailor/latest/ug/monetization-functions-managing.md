

# Creating and managing Functions
<a name="monetization-functions-managing"></a>

This page walks you through creating, attaching, updating, and deleting Functions using the MediaTailor console. Functions let you customize session behavior and ad requests by running logic at key points during playback.

## Setting up a function
<a name="monetization-functions-managing-setup"></a>

### Creating a function using the console
<a name="monetization-functions-managing-create-console"></a>

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/).

1. In the navigation pane, choose **Functions**.

1. Choose **Create function**.

1. For **Function ID**, enter a unique name for the function (for example, `fetchIdentity`).

1. For **Function type**, choose `CUSTOM_OUTPUT`, `HTTP_REQUEST`, or `SEQUENTIAL_EXECUTOR`. The console displays the configuration fields for the selected type.

1. Fill in the type-specific configuration fields. For a description of each function type and its fields, see [Function types and composition](monetization-functions-types.md).

1. Choose **Create function**.

### Attaching a function to a playback configuration
<a name="monetization-functions-managing-attach"></a>

A function does not run until you attach it to a playback configuration through a function mapping (a link between a lifecycle hook and a function). The function mapping specifies which lifecycle hook triggers the function.

1. Open the MediaTailor console.

1. In the navigation pane, choose **Configurations**.

1. Choose the playback configuration you want to update.

1. In the **Function mapping** section, choose **Edit**.

1. For each lifecycle hook, select the function to attach:
   + **Session initialization hook** — Choose a function to run once at session start.
   + **Ad request hook** — Choose a function to run before each ADS request.

1. Choose **Save**.

## Managing functions
<a name="monetization-functions-managing-ops"></a>

### Viewing functions
<a name="monetization-functions-managing-view"></a>

Navigate to **Functions** to see all functions in your account. Choose a function name to view its configuration.

### Updating an existing function
<a name="monetization-functions-managing-update"></a>

To update a function, navigate to **Functions**, choose the function, and modify the configuration. The update replaces the entire function definition.

**Tip**  
Save a copy of your function configuration before making changes. There is no built-in versioning or rollback for functions.

## Removing a function
<a name="monetization-functions-managing-remove"></a>

### Detaching a function from a playback configuration
<a name="monetization-functions-managing-detach"></a>

Before you delete a function, remove it from all playback configurations that reference it.

1. Open the MediaTailor console.

1. In the navigation pane, choose **Configurations**.

1. Choose the playback configuration.

1. In the **Function mapping** section, choose **Edit**.

1. Remove the function from the lifecycle hook.

1. Choose **Save**.

### Deleting a function
<a name="monetization-functions-managing-delete"></a>

Navigate to **Functions**, select the function, and choose **Delete**.

### Deletion blocking rules
<a name="monetization-functions-managing-delete-blocking"></a>

MediaTailor prevents you from deleting a function that is still in use.


| Condition | Result | 
| --- | --- | 
| Function is attached to a playback configuration via function mapping | Delete is blocked. Detach the function first. | 
| Function is referenced in a SEQUENTIAL\_EXECUTOR | Delete is blocked. Remove the reference from the parent function first. | 
| Function is not referenced anywhere | Delete succeeds. | 

## Validation rules
<a name="monetization-functions-managing-validation"></a>

MediaTailor validates your function when you create or update it. The following checks are performed:
+ **Expression syntax** — All expressions must be valid JSONata.
+ **Restricted functions** — Expressions cannot call restricted JSONata functions. See [JSONata expression reference](monetization-functions-jsonata.md) for the full list.
+ **Output key prefixes** — All output keys must start with a recognized namespace prefix. For the list of accepted prefixes, see [Lifecycle hooks](monetization-functions-hooks.md).
+ **Function references** — All function IDs in a `FunctionList` must reference existing functions.
+ **Circular references** — A function cannot reference itself, directly or indirectly.
+ **Nesting depth** — A `SEQUENTIAL_EXECUTOR` can call other functions, but those functions cannot themselves be `SEQUENTIAL_EXECUTOR`s.

For specific values and size limits, see [Limits](monetization-functions-limits.md).

## API reference
<a name="monetization-functions-managing-api-ref"></a>

To manage functions programmatically, see the [AWS Elemental MediaTailor API Reference](https://docs.aws.amazon.com/mediatailor/latest/apireference/).