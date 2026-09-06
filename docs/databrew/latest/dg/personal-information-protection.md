

# Identifying and handling personally identifiable information (PII)
<a name="personal-information-protection"></a>

When you build analytic functions or machine learning models, you need safeguards to prevent exposure of personally identifiable information (PII) data. *PII* is personal data that can be used to identify an individual, such as an address, bank account number, or phone number. For example, when data analysts and data scientists use datasets to discover general demographic information, they should not have access to specific individuals' PII. 

DataBrew provides data masking mechanisms to obfuscate PII data during data preparation process. Depending on your organization's needs, there are different PII data redaction mechanisms available. You can obfuscate the PII data so that users can't revert it back, or you can make the obfuscation reversible. 

Identifying and masking PII data in DataBrew involves building a set of transforms that customers can use to redact PII data. Part of this process is providing PII data detection and statistics in the **Data Profile overview** dashboard on the DataBrew console. 

You can use the following data-masking techniques:
+ *Substitution* – Replace PII data with other authentic-looking values.
+ *Shuffling* – Shuffle the value from the same column in different rows. 
+ *Deterministic encryption* – Apply deterministic encryption algorithms to the column values. Deterministic encryption always produces the same ciphertext for a value. 
+ *Probabilistic encryption* – Apply probabilistic encryption algorithms to the column values. Probabilistic encryption produces different ciphertext each time that it's applied. 
+ *Decryption* – Decrypt columns based on encryption keys. 
+ *Nulling out or deletion* – Replace a particular field with a null value or delete the column. 
+ *Masking out* – Use character scrambling or mask certain portions in the columns. 
+ *Hashing* – Apply hash functions to the column values. 

For more information on using transforms, see [Personally identifiable information (PII) recipe steps](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.pii.html). For more information on using profile jobs to detect PII, including a list of the entity types that can be detected, see [EntityDetectorConfiguration section for configuring PII](https://docs.aws.amazon.com/databrew/latest/dg/profile.configuration.html#entity-detector-configuration) in *Building a profile job configuration programmatically*.