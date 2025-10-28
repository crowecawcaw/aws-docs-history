# Event

Detailed information about an event.

## Contents

###### Note

In the following list, the required parameters are described first.

**Date**

Specifies the date and time of the event.

Type: Timestamp

Required: No

**EventCategories.EventCategory.N**

Specifies the category for the event.

Type: Array of strings

Required: No

**Message**

Provides the text of this event.

Type: String

Required: No

**SourceArn**

The Amazon Resource Name (ARN) for the event.

Type: String

Required: No

**SourceIdentifier**

Provides the identifier for the source of the event.

Type: String

Required: No

**SourceType**

Specifies the source type for this event.

Type: String

Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/Event.md "../../../goto/SdkForCpp/docdb-2014-10-31/Event.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/Event.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/Event.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/Event.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/Event.md")
