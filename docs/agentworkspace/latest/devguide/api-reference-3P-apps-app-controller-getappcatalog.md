

# Get the application catalog in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-getappcatalog"></a>

Returns all the applications that are available in the Connect Customer agent workspace for the current logged-in user.

 **Signature** 

```
getAppCatalog(): Promise<AppConfig[]>
```

 **Usage** 

```
const applications: AppConfig[] = await appControllerClient.getAppCatalog();
```

 **Output - AppConfig** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| arn | string | The AmazonResourceName(ARN) of the application | 
| namespace | string | The immutable application namespace used at the time of registration | 
| id | string | The unique identifier of the application | 
| name | string | Name of the application | 
| description | string | Description of the application | 
| accessUrl | string | URL to access the application | 
| initializationTimeout | number | The maximum time allowed in milliseconds to establish a connection with the workspace | 
| contactHandling.scope | PER\_CONTACT \| CROSS\_CONTACTS | The contact scope that the publisher selected when the application was registered. PER\_CONTACT indicates that AppManager creates a separate instance for each contact, binds each instance to one contact, and destroys it when that contact ends. CROSS\_CONTACTS indicates that AppManager maintains a single instance across contacts for the page session. For more information, see [Application scoping for Connect Customer applications](getting-started-application-contact-scope.md). | 

 **Permissions required:** 

```
*
```