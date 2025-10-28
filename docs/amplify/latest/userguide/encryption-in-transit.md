# Encryption in transit

Encryption in transit refers to protecting your data from being intercepted while it moves
between communication endpoints. Amplify Hosting provides encryption for data in-transit by
default. All communication between customers and Amplify and between Amplify and its
downstream dependencies is protected using TLS connections that are signed using the Signature
Version 4 signing process. All Amplify Hosting endpoints use SHA-256 certificates that are
managed by AWS Private Certificate Authority. For more information, see [Signature
Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") and [What is AWS Private Certificate Authority](../../../acm-pca/latest/userguide/PcaWelcome.md "../../../acm-pca/latest/userguide/PcaWelcome.md").
