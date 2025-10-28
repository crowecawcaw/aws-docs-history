# EntityDetectorConfiguration

Configuration of entity detection for a profile job. When undefined, entity
detection is disabled.

## Contents

###### Note

In the following list, the required parameters are described first.

**EntityTypes**

Entity types to detect. Can be any of the following:

- USA_SSN
- EMAIL
- USA_ITIN
- USA_PASSPORT_NUMBER
- PHONE_NUMBER
- USA_DRIVING_LICENSE
- BANK_ACCOUNT
- CREDIT_CARD
- IP_ADDRESS
- MAC_ADDRESS
- USA_DEA_NUMBER
- USA_HCPCS_CODE
- USA_NATIONAL_PROVIDER_IDENTIFIER
- USA_NATIONAL_DRUG_CODE
- USA_HEALTH_INSURANCE_CLAIM_NUMBER
- USA_MEDICARE_BENEFICIARY_IDENTIFIER
- USA_CPT_CODE
- PERSON_NAME
- DATE

The Entity type group USA_ALL is also supported, and includes all of the
above entity types except PERSON_NAME and DATE.

Type: Array of strings

Array Members: Minimum number of 1 item.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[A-Z_][A-Z\\d_]*$`

Required: Yes

**AllowedStatistics**

Configuration of statistics that are allowed to be run on columns that
contain detected entities. When undefined, no statistics will be computed
on columns that contain detected entities.

Type: Array of [AllowedStatistics](API_AllowedStatistics.md "API_AllowedStatistics.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/EntityDetectorConfiguration.md "../../../goto/SdkForCpp/databrew-2017-07-25/EntityDetectorConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/EntityDetectorConfiguration.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/EntityDetectorConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/EntityDetectorConfiguration.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/EntityDetectorConfiguration.md")
