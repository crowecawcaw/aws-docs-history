# Set the language of a user in Connect Customer agent workspace

Sets the language preference for the user that's currently logged in to the
Connect Customer agent workspace. The promise resolves once the language change
has been persisted, with the resulting language echoed back in the result.

**Signature**

```

setLanguage(language: Locale): Promise<SetLanguageResult>

```

**Usage**

```

const result: SetLanguageResult = await settingsClient.setLanguage("en_US");

```

**Input**

| **Parameter**       | **Type** | **Description**                                                                                                                                         |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| language _Required_ | Locale   | The locale to set for the current user. One of<br>`en_US`, `de_DE`, `es_ES`,<br>`fr_FR`, `ja_JP`, `it_IT`,<br>`ko_KR`, `pt_BR`, `zh_CN`, or<br>`zh_TW`. |

**Output - SetLanguageResult**

| **Parameter** | **Type**          | **Description**                                   |
| ------------- | ----------------- | ------------------------------------------------- |
| language      | Locale (optional) | The locale that was set, echoed from the request. |

**Permissions required:**

```

*

```
