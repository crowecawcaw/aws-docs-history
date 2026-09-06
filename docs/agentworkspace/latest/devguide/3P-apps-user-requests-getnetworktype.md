

# Get the network type of the current Connect Customer instance in Connect Customer agent workspace
<a name="3P-apps-user-requests-getnetworktype"></a>

Returns the network type of the Connect Customer instance associated with the user that's currently logged in to the Connect Customer agent workspace. The returned `NetworkType` is either `"DUAL_STACK"` or `"IPV4"`.

```
async getNetworkType(): Promise<NetworkType>
```

 **Permissions required:** 

```
*
```