# Best practices

- **For Identical Policies**: Ensure the principal has grantable permissions (`PermissionsWithGrantOption`)
- **For Different Policies**: Grant DESCRIBE permissions on all required tag-value pairs
- **Security Consideration**: DESCRIBE permissions on tag-value pairs enable cascading for any non-identical policy using those LF-Tags
- **Testing**: Always test permission cascading in a non-production environment first
