# Docusign Monitor limitations

The following are limitations or notes for Docusign Monitor:

- When a filter is applied using the `cursor` field, the API retrieves records for the next seven days starting from the specified date.
- If no filter is provided, the API retrieves records for the previous seven days from the current date of the API request.
- Docusign Monitor does not support either field-based or record-based partitioning.
- Docusign Monitor does not support the Order By feature.
