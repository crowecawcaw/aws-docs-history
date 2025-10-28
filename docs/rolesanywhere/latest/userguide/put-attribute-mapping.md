# Put attribute mappings

## Put attribute mappings (command line interface)

`put-attribute-mapping` enables you to attach new mapping rules to your profile.
When using that profile, the certificate mapping behavior changes according to your customized rules.

To put a mapping rule, using the following command:

```
`$`aws rolesanywhere put-attribute-mapping \
        --certificate-field `CERTIFICATE_FIELD` \
        --mapping-rules specifier=`SPECIFIER` \
        --profile-id `PROFILE_ID`
```

The `CERTIFICATE_FIELD` can be in one of `x509Subject`,
`x509Issuer` and `x509SAN`. The `SPECIFIER`
is a string enforced by a standard (for example, OID) that can map to a piece of information encoded in the certificate.

For example, to add mapping rules for `x509Subject/CN` and `x509Subject/OU`,
use the following command:

```
`$`aws rolesanywhere put-attribute-mapping \
        --certificate-field x509Subject \
        --mapping-rules specifier=CN specifier=OU \
        --profile-id `PROFILE_ID`
```

## Put attribute mappings (console)

1. Sign in to [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home "https://console.aws.amazon.com/rolesanywhere/home").
2. Scroll to find profile table and **choose the profile** to add
   certificate attribute mappings.
3. Within profile detail page scroll towards **Certificate attribute mappings**
   section and choose **Manage mappings**.
4. Scroll to find the **Add mappings** button and click on it.
5. Choose a certificate field from either `Subject`, `Issuer`, or `Subject
Alternative Name` in the dropdown list, and enter the specifier
6. Select **Save changes** to add attribute mappings.
