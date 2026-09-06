

# Interceptor callback type in Connect Customer agent workspace
<a name="3P-apps-extensibility-interceptor-type"></a>

Defines the callback signature and return value for an interceptor. An interceptor receives a context object and returns a result that indicates whether the action proceeds.

 **Signature** 

```
type Interceptor<T> = (context: T) => Promise<InterceptorResult>

type InterceptorResult = boolean | { continue: boolean }
```

 **Context** 

For the currently supported interceptor keys, the context object is:

```
{ contactId?: string }
```

 **Return value** 

The following table describes the return values.


| **Return value** | **Shorthand** | **Effect** | 
| --- | --- | --- | 
| { continue: true } | true | Allow the default action to proceed. | 
| { continue: false } | false | Block the default action. | 