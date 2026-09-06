

# Set the language of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-setlanguage"></a>

Sets the language preference for the user that's currently logged in to the Connect Customer agent workspace. The promise resolves once the language change has been persisted, with the resulting language echoed back in the result.

 **Signature** 

```
setLanguage(language: Locale): Promise<SetLanguageResult>
```

 **Usage** 

```
const result: SetLanguageResult = await settingsClient.setLanguage("en_US");
```

 **Input** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| language Required | Locale | The locale to set for the current user. One of en\_US, de\_DE, es\_ES, fr\_FR, ja\_JP, it\_IT, ko\_KR, pt\_BR, zh\_CN, or zh\_TW. | 

 **Output - SetLanguageResult** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| language | Locale (optional) | The locale that was set, echoed from the request. | 

 **Permissions required:** 

```
*
```