# Functions quick start guide

This guide walks you through creating your first function, attaching it to a playback
configuration, and verifying that it ran. By the end, you will have a working function that
classifies each viewer's device type (`ctv`, `mobile`, or
`desktop`) and stores it as a player parameter available in every ADS
request.

## Prerequisites

Before you begin, make sure you have an existing MediaTailor playback configuration. If you
don't have one, see [Getting started with MediaTailor](getting-started.md "getting-started.md").

## Step 1: Create a function

In this step, you create a function that classifies the viewer's device type based on
the user agent string and stores the result in player parameters. The function uses a
Custom output type (no external API calls) with a [JSONata expression
reference](monetization-functions-jsonata.md "monetization-functions-jsonata.md") expression to evaluate the
user agent.

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Functions**.
3. Choose **Create function**.
4. In the create wizard modal, select **Create from
   scratch**, then choose **Continue**.
5. Under **Function type**, select the **Custom output** tile.
6. Under **Function details**, enter the
   following:

   - **Function ID**:
     `myFirstFunction`
   - **Description**: `Classify device
  type from user agent`

7. Under **Custom output configuration**, in the
   **Output** section, add one row:

   - **Key**:
     `player_params.deviceType`
   - **Value**: `{%
  $contains(session.user_agent, 'CTV') ? 'ctv' :
  $contains(session.user_agent, 'Mobile') ? 'mobile' : 'desktop'
  %}`

8. Choose **Create function**.

A success notification confirms the function was created, and you are redirected to
the function details page.

The resulting function configuration is:

```
{
    "FunctionId": "myFirstFunction",
    "FunctionType": "CUSTOM_OUTPUT",
    "Description": "Classify device type from user agent",
    "CustomOutputConfiguration": {
        "Runtime": "JSONATA",
        "Output": {
            "player_params.deviceType": "{% $contains(session.user_agent, 'CTV') ? 'ctv' : $contains(session.user_agent, 'Mobile') ? 'mobile' : 'desktop' %}"
        }
    }
}
```

## Step 2: Attach the function to a playback configuration

Map the function to a lifecycle hook on your playback configuration. The mapping tells
MediaTailor when to run the function.

1. In the navigation pane, choose **Configurations**.
2. Choose the playback configuration you want to update.
3. Choose **Edit**.
4. Expand the **Functions configuration**
   section.
5. For **Session initialization hook**, select
   `myFirstFunction` from the dropdown.
6. Choose **Save**.

This attaches `myFirstFunction` to the [Pre-session initialization](monetization-functions-hooks-pre-session.md "monetization-functions-hooks-pre-session.md")
lifecycle hook. The resulting function mapping is:

```
{
    "FunctionMapping": {
        "PRE_SESSION_INITIALIZATION": "myFirstFunction"
    }
}
```

MediaTailor runs the function once at the start of every new session on this playback
configuration.

## Step 3: Start a session and verify the function ran

Start a new playback session to trigger the function. Use a session initialization
request to your playback configuration's session initialization endpoint.

MediaTailor automatically publishes CloudWatch metrics for every function execution — no
opt-in required. After starting a session, check the following metrics in the
`AWS/MediaTailor` namespace to confirm your function ran:

- `PreSessionInitHook.Invocations` — Confirms the hook
  fired.
- `PreSessionInitHook.Errors` — Should be 0 if the function
  succeeded.
- `Function.Invocations` — Confirms the individual function
  executed. This metric includes `FunctionId`,
  `FunctionType`, and `HookType` dimensions so you can
  filter to `myFirstFunction` specifically.

If the function fails, MediaTailor emits error log events to Manifest Logs by default (no
configuration needed):

- `PRE_SESSION_INIT_HOOK_ERROR` — Hook-level failure with
  `errorType` and `cause`.
- `PRE_SESSION_INIT_FUNCTION_ERROR` — Function-level failure
  with the specific `functionId` and error details.

The following example shows a `PRE_SESSION_INIT_FUNCTION_ERROR` event for
a syntax error in the function expression:

```
{
    "eventTimestamp": "2024-01-01T12:00:00.076000000Z",
    "eventType": "PRE_SESSION_INIT_FUNCTION_ERROR",
    "eventDescription": "Function execution failed",
    "awsAccountId": "123456789012",
    "originId": "my-config",
    "sessionId": "session-123",
    "requestId": "req-abc",
    "eventId": "5dc6f040-0f72-4e8c-a64e-25eeef62708c",
    "functionId": "myFirstFunction",
    "functionType": "CUSTOM_OUTPUT",
    "executionTimeMs": 2,
    "errorType": "SYNTAX_ERROR",
    "cause": "Expected \")\" before end of expression",
    "input": {}
}
```

Use the `eventId` field to correlate hook and function error events for
the same execution. The `errorType` field tells you the class of failure
— see [Troubleshooting and
monitoring](monetization-functions-troubleshooting.md "monetization-functions-troubleshooting.md") for a full list of
error types and fixes.

###### Note

For detailed success logging, opt in to
`PRE_SESSION_INIT_HOOK_SUMMARY` and
`PRE_SESSION_INIT_FUNCTION_COMPLETED` events in your Manifest Log
configuration. Summary events show the hook outcome for every execution. Completed
events show each function's input, output, and HTTP request/response details. These
are disabled by default to minimize log costs. For more information, see [Troubleshooting and
monitoring](monetization-functions-troubleshooting.md "monetization-functions-troubleshooting.md").

## What happens behind the scenes

Here is the complete request flow for the function you just created:

1. The player initiates a session with MediaTailor.
2. MediaTailor fires the `PRE_SESSION_INITIALIZATION` lifecycle hook and
   runs `myFirstFunction`.
3. The function evaluates the `session.user_agent` field and writes
   `ctv`, `mobile`, or `desktop` to
   `player_params.deviceType`.
4. MediaTailor creates the session and returns the manifest to the player.
5. The player encounters an ad break during playback.
6. MediaTailor fires the `PRE_ADS_REQUEST` lifecycle hook, then constructs
   the ADS request. Because `deviceType` is stored in player parameters,
   it is available for inclusion in the ADS request URL through dynamic variable
   substitution.
7. The ADS uses the device type to return targeted ad creatives.
8. MediaTailor stitches the ads into the manifest and returns it to the player.

If the function fails for any reason, MediaTailor discards the output and proceeds as if no function were
attached. The viewer still sees ads — just without the device type
targeting.

## Suggested topics

You now have a working function attached to a playback configuration. From
here:

- To learn what input fields and output namespaces are available at each
  lifecycle hook, see [Lifecycle hooks](monetization-functions-hooks.md "monetization-functions-hooks.md").
- To learn about the different function types and how to chain them together,
  see [Function types and
  composition](monetization-functions-types.md "monetization-functions-types.md").
- To see complete working examples, see [Function examples](monetization-functions-examples.md "monetization-functions-examples.md").
