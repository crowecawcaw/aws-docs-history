

# Sensitive data detection and redaction in Amazon Bedrock Data Automation
<a name="bda-sensitive-data"></a>

With Amazon Bedrock Data Automation (BDA), you can detect and redact personally identifiable information (PII) in standard and custom outputs. PII detection uses Sensitive Information Filters in Amazon Bedrock Guardrails. BDA disables this feature by default. To enable it, pass modality-specific overrides in `overrideConfiguration` for each modality you want to process.

**Note**  
The sensitive data detection and redaction feature only applies to the JSON results that BDA provides to you. It does not modify your input assets or blueprints.