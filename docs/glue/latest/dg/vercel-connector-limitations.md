

# Limitations and notes for the Vercel connector

The following are limitations and notes for the Vercel connector:
+ Vercel is supported as a source only. Writing to Vercel is not supported.
+ The `projects-env` entity doesn't decrypt environment variables. The `value` column contains the encrypted value for encrypted and sensitive variables, and the stored value for plain variables. To exclude values from your job output, leave `value` out of `SELECTED_FIELDS`.
+ Job bookmarks are not supported.