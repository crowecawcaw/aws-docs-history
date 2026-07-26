# RegisterInterceptorOptions in Connect Customer agent workspace

Contains the configuration options for interceptor registration, including timeout
and consecutive-block behavior.

**Signature**

```

interface RegisterInterceptorOptions {
  timeout?: number;
  maxConsecutiveBlocks?: number;
}
```

**Properties**

The following table describes the properties.

| **Parameter**                   | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timeout _Optional_              | number   | The maximum time in milliseconds to wait for the interceptor to<br>resolve. Default: 5000 (5 seconds). Valid range: 1–10000<br>milliseconds (hard ceiling: 10 seconds). The service clamps values<br>outside this range to the default. If the interceptor exceeds the<br>timeout, the default action proceeds as if the interceptor returned<br>`{ continue: true }`. |
| maxConsecutiveBlocks _Optional_ | number   | The maximum number of consecutive times the interceptor can block<br>the action before the system overrides and allows the action. Default:<br>5. Valid range: 0–100. The service clamps values outside this<br>range to the default. The counter resets when the interceptor allows<br>an action. Set to `0` to disable the consecutive block<br>limit.               |
