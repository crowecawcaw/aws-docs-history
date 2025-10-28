# Amazon Connect Agent Workspace User API

The SDK provides an `SettingsClient` which serves as an interface that your
app in Amazon Connect Agent Workspace can use to make data requests on user settings.

The `SettingsClient` accepts an optional constructor argument,
`ConnectClientConfig` which itself is defined as:

```

            export type ConnectClientConfig = {
                context?: ModuleContext;
                provider?: AmazonConnectProvider;
             };

```

If you do not provide a value for this config, then the client will default to using
the **AmazonConnectProvider** set in the global provider scope. You can
also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

            import { SettingsClient } from "@amazon-connect/user";
            const settingsClient = new SettingsClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

            import { SettingsClient } from "@amazon-connect/user";

            const settingsClient = new SettingsClient({
                context: sampleContext,
                provider: sampleProvider
        });

```

The following sections describe API calls for working with the User API.

###### Contents

- [LanguageChanged (Subscribing)](3p-apps-user-events-languagechanged-sub.md "3p-apps-user-events-languagechanged-sub.md")
- [LanguageChanged (Unsubscribing)](3p-apps-user-events-languagechanged-unsub.md "3p-apps-user-events-languagechanged-unsub.md")
- [getLanguage()](3p-apps-user-requests-getlanguage.md "3p-apps-user-requests-getlanguage.md")
