

# Subscribe a callback function when an Connect Customer agent workspace user changes languages
<a name="3P-apps-user-events-languagechanged-sub"></a>

Subscribes a callback function to-be-invoked whenever a user LanguageChanged event occurs in the Connect Customer agent workspace.

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