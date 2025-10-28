# Outgoing webhook action using ADK

The outgoing webhook action can initiate an outgoing webhook (OW) and make a POST
request to a provided URL. With the action, you can
bridge
Amazon CodeCatalyst workflows with predefined web services like
status
reporting and sharing artifacts.

###### Topics

- [Prerequisites](#prerequisites-outgoing-webhook "#prerequisites-outgoing-webhook")
- [Update the action definition](#update-action-definition-outgoing-webhook "#update-action-definition-outgoing-webhook")
- [Update the action code](#update-action-code-outgoing-webhook "#update-action-code-outgoing-webhook")
- [Validate the action within the CodeCatalyst workflow](#validate-action-outgoing-webhook "#validate-action-outgoing-webhook")

## Prerequisites

Complete all of the steps in [Getting started with the Action Development Kit](getting-started.md "getting-started.md") before
moving on with developing the action.

### Languages and toolchains

In this example, we'll develop an action using npm and TypeScript.

## Update the action definition

Update the action definition (`action.yml`) that was generated
in [Step 3: Initialize your action project](getting-started.md#initialize-action-workspace "getting-started.md#initialize-action-workspace") with the following
`WebhookRequestURL` and `WebhookRequestHeaders` input
parameters, in addition to `WebhookRequestBody` (optional):

```
SchemaVersion: '1.0'
    Name: 'OutgoingWebhookAction'
    Version: '0.1.0'
    Description: 'Outgoing Webhook Action allows user to send messages within workflow to an arbitrary web server using HTTP request'
    Configuration:
      WebhookRequestURL:
        Description: 'Outgoing webhook URL from an arbitrary web server'
        Required: true
        DisplayName: 'Request URL'
        Type: string
      WebhookRequestHeaders:
        Description: 'The JSON that you want to provide to add HTTP request headers. '
        Required: false
        DisplayName: 'Request Headers'
        Type: string
        Default: false
      WebhookRequestBody:
        Description: 'The JSON that you want to provide to add HTTP request body. '
        Required: false
        DisplayName: 'Request Body'
        Type: string
        Default: false
    Environment:
      Required: false
    Runs:
      Using: 'node16'
      Main: 'dist/index.js'
```

This action invokes the AWS Command Line Interface (AWS CLI), which is preinstalled on the action's runtime environment image within CodeCatalyst.
The output of the CLI command is streamed to the console using stdout.

## Update the action code

The outgoing webhook action contains several source files under the
`lib/` folder. This example code provides configuration of
the entry point and the action itself. Update the
entry
point code in the `lib/index.ts` file that was
generated in [Step 4: Bootstrap the action code](getting-started.md#bootstrap-action-code "getting-started.md#bootstrap-action-code").

While building your action, you can also catch errors by setting summary run messages. For more information, see
[Handling errors](troubleshooting.md#handling-errors "troubleshooting.md#handling-errors").

```
// @ts-ignore
    import * as core from '@aws/codecatalyst-adk-core';
    // @ts-ignore
    import { RunSummaryLevel, RunSummaries } from '@aws/codecatalyst-run-summaries';
    import { runOutgoingWebhookAction } from './action';
    import { OutgoingWebhookInput } from './constants/types';
    import { getBodyInput, getHeadersInput } from './utils/input-util';

    export function main(): void {
        try {
            // Get inputs from the action
            const webhookUrl: string = core.getInput('WebhookRequestURL'); // Outgoing webhook URL from an arbitrary web server
            const headers: Map<string, string> | undefined = getHeadersInput(); // The JSON that you want to provide to add HTTP request headers.
            const body: string | undefined = getBodyInput(); // The JSON that you want to provide to add HTTP request body.

            const actionInput: OutgoingWebhookInput = {
                webhookUrl,
                headers,
                body
            };

            // Run the webhook action
            runOutgoingWebhookAction(actionInput);
        } catch (error) {
            console.log(`Action Failed, reason: ${error}`);
            RunSummaries.addRunSummary(`${error}`, RunSummaryLevel.ERROR);
            core.setFailed(`Action Failed, reason: ${error}`);
        }
    }

    if (require.main === module) {
        main();
    }
```

The action first gets the inputs using the `core.getInput()` ADK API to
initialize required and optional variables. The action then calls the
`runOutgoingWebhookAction()` function to send the HTTP POST request
with the earlier provided input. The source code of the
`runOutgoingWebhookAction()` function is implemented in the
`action.ts` source file. The following code example validates user
input, constructs an executable shell command using `code.command()`, and
logs the result:

```
// @ts-ignore
    import * as core from '@aws/codecatalyst-adk-core';
    import { OUTGOING_WEBHOOK_ERROR } from './constants';
    import { OutgoingWebhookInput } from './constants/types';
    import { validateActionInputs } from './validation/validation';

    export function runOutgoingWebhookAction(input: OutgoingWebhookInput): void {
        validateActionInputs(input);
        const shell_command = webhookRequestCommand(input);
        const { code, stderr } = core.command(shell_command);
        console.log(`shell command: ${shell_command}`);
        if (code !== 0) {
            console.log(stderr);
            throw new Error(OUTGOING_WEBHOOK_ERROR);
        }

        console.log('Outgoing Webhook command was successful');
    }

    export function webhookRequestCommand(input: OutgoingWebhookInput): string {
        const headersCommand = constructHeadersCommand(input.headers);
        const bodyCommand = input.body === undefined ? undefined : `-d '${input.body}' `;
        return constructRequestCommand(input.webhookUrl, headersCommand, bodyCommand);
    }

    export function constructRequestCommand(url: string, headerCommand: string | undefined, bodyCommand: string | undefined): string {
        let command = 'curl -X POST ';
        if (headerCommand) {
            command += headerCommand;
        }
        if (bodyCommand) {
            command += bodyCommand;
        }
        command += url;
        return command;
    }

    export function constructHeadersCommand(headers: Map<string, string> | undefined | string): string | undefined {
        let headerCommand = '';
        if (headers == undefined) return undefined;
        for (const [key, value] of headers) {
            headerCommand += `-H "${key}: ${value}" `;
        }
        return headerCommand;
    }
```

This action invokes the AWS Command Line Interface (AWS CLI), which is preinstalled on the action's runtime environment image within CodeCatalyst.
The output of the CLI command is streamed to the console using stdout.

After bootstrapping and updating the action code, continue with [Step 4: Bootstrap the action code](getting-started.md#bootstrap-action-code "getting-started.md#bootstrap-action-code")
to complete the local build.

## Validate the action within the CodeCatalyst workflow

After
[Testing an action](testing-action.md "testing-action.md"),
validate
the action.

**To validate the action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the workflow with the action that you want to validate, then view
   **Logs** to confirm a successful run.
