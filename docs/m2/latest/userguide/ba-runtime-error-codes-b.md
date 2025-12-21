AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error Codes related to Blusam

Blusam error codes, prefixed with `BA-B`.

| Key        | Severity | Text                                                                                                                                                                                                                                                                            | Additional details                                                                                                                  |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `BA-B0001` | Warn     | Invalid value for `bluesam.disabled`. Only `true` is supported to disable Blusam. The default behavior is that Bluesam is enabled. Set `bluesam.disabled: true` in your configuration if you want to disable Bluesam. Remove the property to keep Blusam enabled.               |                                                                                                                                     |
| `BA-B0011` | Warn     | Invalid value for `bluesam.cache`. Only `ehcache` or `redis` are supported cache implementations. Set `bluesam.cache: ehcache` to use EhCache implementation, or `bluesam.cache: redis` to use Redis implementation. Remove the property if you don't want to use Blusam cache. |                                                                                                                                     |
| `BA-B0021` | Fatal    | Blusam is active but blusam datasource is not defined in the configuration. Set `datasource.blusamDs` configuration keys (subkeys url, username, password...) or use an AWS secret.                                                                                             | See [Blusam configuration](ba-shared-blusam.md#ba-shared-blusam-configuration "ba-shared-blusam.md#ba-shared-blusam-configuration") |
