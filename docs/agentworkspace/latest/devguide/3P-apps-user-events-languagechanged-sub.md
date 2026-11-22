

# Subscribe a callback function when an Connect Customer agent workspace user changes languages

Subscribes a callback function to-be-invoked whenever a user LanguageChanged event occurs in the Connect Customer agent workspace.

 **Signature** 

```typescript
onLanguageChanged(handler: UserLanguageChangedHandler)
```

 **Usage** 

```typescript
const handler: UserLanguageChangedHandler = async (data: UserLanguageChanged) => {
    console.log("User LanguageChange occurred! " + data);
};

settingsClient.onLanguageChanged(handler);

// UserLanguageChanged Structure
{
  language: Locale;
  previous: {
    language: Locale | null;
  };
}
```

 **Permissions required:** 

```typescript
User.Configuration.View             
```