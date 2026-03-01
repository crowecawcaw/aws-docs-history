# Subscribe a callback function when an Amazon Connect Agent Workspace user changes languages

Subscribes a callback function to-be-invoked whenever a user LanguageChanged event
occurs in the Amazon Connect Agent Workspace.

**Signature**

```

onLanguageChanged(handler: UserLanguageChangedHandler)

```

**Usage**

```

const handler: UserLanguageChangedHandler = async (data: UserLanguageChanged) => {
    console.log("User LanguageChange occurred! " + data);
};

settingsClient.onLanguageChanged(handler);

// UserLanguageChanged Structure
{
  language: string;
  previous: {
    language: string;
  };
}

```

**Permissions required:**

```

User.Configuration.View

```
