# export

The **export** command sets IAM credentials as environment variables. You
must export the following variables, one at a time. Do not include a space before or after the
equal (=) sign.

**Syntax**

```
`Outpost>``export `variable`=`value``
```

**Parameters**

This command takes a variable assignment statement,
`variable`=`value`. For
example:

- AWS_ACCESS_KEY_ID=`access-key-id`
- AWS_SECRET_ACCESS_KEY=`secret-access-key`
- AWS_SESSION_TOKEN=`session-token`
- AWS_DEFAULT_REGION=`server-parent-Region`

###### Example output: Successful credential import

```
`Outpost>`export AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE`

`result: OK
checksum: `checksum``
```

```
`Outpost>`export AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

`result: OK
checksum: `checksum``
```

```
`Outpost>`export AWS_SESSION_TOKEN=`MIICiTCCAfICCQD6m7oRw0uXOjANBgk
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=`

`result: OK
checksum: `checksum``
```

```
`Outpost>`export AWS_DEFAULT_REGION=`us-west-2`

`result: OK
checksum: `checksum``
```
