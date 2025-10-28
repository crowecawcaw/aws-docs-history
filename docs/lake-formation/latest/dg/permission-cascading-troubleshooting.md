# Troubleshooting

Common Error: AccessDeniedException

**Cause:** Neither cascading rule is satisfied

**Solution:**

- For identical policies: Grant with `PermissionsWithGrantOption`
- For different policies: Ensure DESCRIBE permissions on all tag-value pairs
