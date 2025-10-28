# Permission cascading rules

Lake Formation uses two rules for permission cascading. A principal can cascade permissions if **either** rule is satisfied:

Rule 1: Identical tag policy with grantable permissions

- The LF-Tag policy must be exactly the same as the LF-Tag policy used by the producer account to share resources with the consumer account.
- The consumer account must have grantable permissions (`PermissionsWithGrantOption`) on the tag policy.

Rule 2: DESCRIBE permission on all tag-value pairs

- The consumer account must have `DESCRIBE` permission on all tag-value pairs specified in the
  policy.
- No grantable permissions required.
