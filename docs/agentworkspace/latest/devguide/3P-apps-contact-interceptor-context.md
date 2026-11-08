

# ContactInterceptorContext in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-context"></a>

Defines the invocation context that the contact interceptor methods receive.

**Signature**

```
type ContactInterceptorContext = {
  contactId?: string;
}
```

**Properties**

The following table describes the properties.


| **Property** | **Type** | **Description** | 
| --- | --- | --- | 
| contactId Optional | string | The identifier of the contact that triggered the action. When no specific contact initiated the action, the value is absent. Although the SDK types this property as an optional string, the agent workspace can also pass null in that case, so treat both null and a missing value as no contact. | 