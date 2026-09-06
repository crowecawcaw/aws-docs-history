

# Get the language of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-getlanguage"></a>

Returns the language setting for the current user in the Connect Customer agent workspace.

```
async getLanguage(): Promise<Locale | null>        
```

 **Permissions required:** 

```
User.Configuration.View              
```