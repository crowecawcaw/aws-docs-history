

# Sensitive data

This section describes how Amazon Textract Insights detects personally identifiable information (PII) in your results. Optionally, it writes a redacted copy so that downstream consumers don't see raw sensitive values.

The topics explain how to configure detection on a project: the detection mode, which results to scan, which entity types to look for, and how masked values appear. They also list the entity types you can request, such as names, addresses, financial identifiers, and country-specific ID numbers. Sensitive data detection can scan both extraction results and custom extraction results.