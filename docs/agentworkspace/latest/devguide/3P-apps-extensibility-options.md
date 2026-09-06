

# RegisterInterceptorOptions in Connect Customer agent workspace
<a name="3P-apps-extensibility-options"></a>

Contains the configuration options for interceptor registration, including timeout and consecutive-block behavior.

 **Signature** 

```
interface RegisterInterceptorOptions {
  timeout?: number;
  maxConsecutiveBlocks?: number;
}
```

 **Properties** 

The following table describes the properties.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| timeout Optional | number | The maximum time in milliseconds to wait for the interceptor to resolve. Default: 5000 (5 seconds). Valid range: 1–10000 milliseconds (hard ceiling: 10 seconds). The service clamps values outside this range to the default. If the interceptor exceeds the timeout, the default action proceeds as if the interceptor returned { continue: true }. | 
| maxConsecutiveBlocks Optional | number | The maximum number of consecutive times the interceptor can block the action before the system overrides and allows the action. Default: 5. Valid range: 0–100. The service clamps values outside this range to the default. The counter resets when the interceptor allows an action. Set to 0 to disable the consecutive block limit. | 