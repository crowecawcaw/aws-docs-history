# Integrate application with Amazon Connect

Agent Workspace user data

To integrate your application with agent data from Amazon Connect Agent Workspace, instantiate
the user client as follows:

```

import { SettingsClient } from "@amazon-connect/user";
const settingsClient = new SettingsClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must
first instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md")
which will set up the default AmazonConnectProvider. This is the recommended
option.

Alternatively, see the [API reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md") to customize your client’s configuration. Once the user
client is instantiated, you can use it to make requests.

## Example user

request

The following user event and request are non-exhaustive. For a full list of
available voice events and requests, see the [API
reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md").

```

import { SettingsClient } from "@amazon-connect/user";

const settingsClient = new SettingsClient();
const language = await settingsClient.getLanguage();

console.log(`Got the language: ${language}`);

```
