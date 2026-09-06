

# Auth APIs
<a name="auth-apis"></a>

The following APIs enable you to manage API keys for Amazon Location Service. Use these operations to create keys, configure restrictions, rotate keys, and monitor your key inventory.
+ **CreateKey**: Creates a new API key with specified restrictions and optional expiration. Returns the key value used to authenticate subsequent API requests. For more information, see [CreateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_CreateKey.html) in the *Amazon Location Service API Reference*.
+ **DescribeKey**: Retrieves the details of an existing API key, including its restrictions, expiration, and key value. For more information, see [DescribeKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_DescribeKey.html) in the *Amazon Location Service API Reference*.
+ **UpdateKey**: Modifies an existing API key's restrictions, expiration, or description. Use this operation to tighten permissions, extend or set expiration, or deactivate a key. For more information, see [UpdateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_UpdateKey.html) in the *Amazon Location Service API Reference*.
+ **DeleteKey**: Permanently deletes an API key. You can only delete keys that have been inactive for at least 90 days. For more information, see [DeleteKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_DeleteKey.html) in the *Amazon Location Service API Reference*.
+ **ListKeys**: Returns a list of API keys in your account and Region, including metadata such as key name, status, and expiration. For more information, see [ListKeys](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_ListKeys.html) in the *Amazon Location Service API Reference*.

## Common use cases
<a name="auth-apis-common-use-cases"></a>

The following are common use cases for API key management operations.
+ **Create a key for a map application**: Create a key restricted to `geo-maps:*` actions on the default maps provider resource, suitable for a web page that only renders maps.
+ **Create a key for maps and places**: Create a key that allows both map rendering and geocoding by specifying multiple allowed actions and resources in a single key.
+ **Rotate an API key**: Create a new key, update your application to use it, then deactivate the old key by setting its expiration to a past date using `UpdateKey`.
+ **Add domain restrictions**: Update an existing key to restrict usage to specific web domains using referrer-based client restrictions.
+ **Audit key inventory**: List all keys in the account using `ListKeys` to identify unused or expiring keys for cleanup.
+ **Revoke a compromised key**: Deactivate a key immediately by updating its status with `UpdateKey`, then delete it after 90 days using `DeleteKey`.