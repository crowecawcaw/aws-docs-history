# Modifying NATIVE_NETWORK_ENCRYPTION

option settings

After you enable the `NATIVE_NETWORK_ENCRYPTION` option, you can modify its
settings. Currently, you can modify `NATIVE_NETWORK_ENCRYPTION` option
settings only with the AWS CLI or RDS API. You can't use the console. The following
example modifies two settings in the option.

```
aws rds add-option-to-option-group \
    --option-group-name my-option-group \
    --options "OptionName=NATIVE_NETWORK_ENCRYPTION,OptionSettings=[{Name=SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER,Value=SHA256},{Name=SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER,Value=SHA256}]" \
    --apply-immediately
```

To learn how to modify option settings using the CLI, see [AWS CLI](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption.CLI "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption.CLI"). For more
information about each setting, see [NATIVE_NETWORK_ENCRYPTION option
settings](Oracle.Options.NNE.md "Oracle.Options.NNE.md").

###### Topics

- [Modifying CRYPTO_CHECKSUM\_\* values](#Oracle.Options.NNE.ModifySettings.checksum "#Oracle.Options.NNE.ModifySettings.checksum")
- [Modifying ALLOW_WEAK_CRYPTO\* settings](#Oracle.Options.NNE.ModifySettings.encryption "#Oracle.Options.NNE.ModifySettings.encryption")

## Modifying CRYPTO_CHECKSUM\_\* values

If you modify **NATIVE_NETWORK_ENCRYPTION** option settings, make
sure that the following option settings have at least one common cipher:

- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`

The following example shows a scenario in which you modify
`SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER`. The configuration is valid because the
`CRYPTO_CHECKSUM_TYPES_CLIENT` and `CRYPTO_CHECKSUM_TYPES_SERVER` both use
`SHA256`.

| Option setting                        | Values before modification                         | Values after modification |
| ------------------------------------- | -------------------------------------------------- | ------------------------- |
| `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` | `**SHA256**`, `SHA384`,<br>`SHA512`                | No change                 |
| `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` | `**SHA256**`, `SHA384`,<br>`SHA512`, `SHA1`, `MD5` | `SHA1,MD5,**SHA256**`     |

For another example, assume that you want to modify `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` from
its default setting to `SHA1,MD5`. In this case, make sure you set
`SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` to `SHA1` or `MD5`. These
algorithms aren't included in the default values for `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`.

## Modifying ALLOW_WEAK_CRYPTO\* settings

To set the `SQLNET.ALLOW_WEAK_CRYPTO*` options from the default value to `FALSE`,
make sure that the following conditions are met:

- `SQLNET.ENCRYPTION_TYPES_SERVER` and `SQLNET.ENCRYPTION_TYPES_CLIENT` have
  one matching secure encryption method. A method is considered secure if it's not `DES`,
  `3DES`, or `RC4` (all key lengths).
- `SQLNET.CHECKSUM_TYPES_SERVER` and `SQLNET.CHECKSUM_TYPES_CLIENT` have one
  matching secure checksumming method. A method is considered secure if it's not
  `MD5`.
- The client is patched with the July 2021 PSU. If the client isn't patched, the client loses the
  connection and receives the `ORA-12269` error.

The following example shows sample NNE settings. Assume that you want to set
`SQLNET.ENCRYPTION_TYPES_SERVER` and `SQLNET.ENCRYPTION_TYPES_CLIENT` to FALSE,
thereby blocking non-secure connections. The checksum option settings meet the prerequisites because they
both have `SHA256`. However, `SQLNET.ENCRYPTION_TYPES_CLIENT` and
`SQLNET.ENCRYPTION_TYPES_SERVER` use the `DES`, `3DES`, and
`RC4` encryption methods, which are non-secure. Therefore, to set the
`SQLNET.ALLOW_WEAK_CRYPTO*` options to `FALSE`, first set
`SQLNET.ENCRYPTION_TYPES_SERVER` and `SQLNET.ENCRYPTION_TYPES_CLIENT` to a secure
encryption method such as `AES256`.

| Option setting                        | Values                        |
| ------------------------------------- | ----------------------------- |
| `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` | `SHA256`, `SHA384`, `SHA512`  |
| `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` | `SHA1,MD5,SHA256`             |
| `SQLNET.ENCRYPTION_TYPES_CLIENT`      | `RC4_256`, `3DES168`, `DES40` |
| `SQLNET.ENCRYPTION_TYPES_SERVER`      | `RC4_256`, `3DES168`, `DES40` |
