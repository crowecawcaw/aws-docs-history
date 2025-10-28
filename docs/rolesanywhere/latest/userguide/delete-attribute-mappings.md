# Delete attribute mappings

## Delete attribute mappings (command line interface)

`delete-attribute-mapping` enables you to delete mapping rules from your profile.
When using that profile, the attribute specified by the deleted mapping rule will not be mapped from a certificate.

To delete a mapping rule, using the following command:

```
`$`aws rolesanywhere delete-attribute-mapping \
        --certificate-field `CERTIFICATE_FIELD` \
        --specifiers `SPECIFIERS` \
        --profile-id `PROFILE_ID`
```

The `CERTIFICATE_FIELD` can be in one of `x509Subject`,
`x509Issuer` and `x509SAN`. The `SPECIFIER`
is a string enforced by a standard (for example, OID) that exists in your current mapping rules.

For example, to delete mapping rules for `x509Subject/CN` and `x509Subject/OU`,
use the following command:

```
`$`aws rolesanywhere delete-attribute-mapping \
        --certificate-field x509Subject \
        --specifiers CN OU \
        --profile-id `PROFILE_ID`
```

## Delete attribute mappings (console)

1. Sign in to [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home "https://console.aws.amazon.com/rolesanywhere/home").
2. Scroll to find profile table and **choose the profile** to remove
   certificate attribute mappings.
3. Within profile detail page scroll towards **Certificate attribute mappings**
   section and choose **Manage mappings**.
4. Scroll to find the corresponding attribute mapping row and click on **Remove
   mapping** button associated with it.
5. Select **Save changes** to remove attribute mappings.
