

# Connect Customer agent workspace User API
<a name="api-reference-3P-apps-user"></a>

The Amazon Connect SDK provides an `SettingsClient` which serves as an interface that your app in Connect Customer agent workspace can use to make data requests on user settings.

The `SettingsClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
        export type ConnectClientConfig = {  
            context?: ModuleContext;  
            provider?: AmazonConnectProvider;
         };
```

If you do not provide a value for this config, then the client will default to using the ** AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```
        import { SettingsClient } from "@amazon-connect/user";
        const settingsClient = new SettingsClient({ provider });
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. This is the recommended option.

Alternatively, providing a constructor argument:

```
        import { SettingsClient } from "@amazon-connect/user";
        
        const settingsClient = new SettingsClient({
            context: sampleContext,  
            provider: sampleProvider
    });
```

The following sections describe API calls for working with the User API.

**Topics**
+ [getLanguage()](3P-apps-user-requests-getlanguage.md)
+ [onLanguageChanged()](3P-apps-user-events-languagechanged-sub.md)
+ [offLanguageChanged()](3P-apps-user-events-languagechanged-unsub.md)
+ [getUserArn()](3P-apps-user-requests-getuserarn.md)
+ [getInstanceId()](3P-apps-user-requests-getinstanceid.md)
+ [getNetworkType()](3P-apps-user-requests-getnetworktype.md)
+ [setLanguage()](3P-apps-user-requests-setlanguage.md)
+ [setVisualMode()](3P-apps-user-requests-setvisualmode.md)
+ [onVisualModeChange()](3P-apps-user-events-visualmodechange-sub.md)
+ [offVisualModeChange()](3P-apps-user-events-visualmodechange-unsub.md)