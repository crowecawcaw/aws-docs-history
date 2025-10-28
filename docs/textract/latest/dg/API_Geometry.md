# Geometry

Information about where the following items are located on a document page: detected
page, text, key-value pairs, tables, table cells, and selection elements.

## Contents

**BoundingBox**

An axis-aligned coarse representation of the location of the recognized item on the
document page.

Type: [BoundingBox](API_BoundingBox.md "API_BoundingBox.md") object

Required: No

**Polygon**

Within the bounding box, a fine-grained polygon around the recognized item.

Type: Array of [Point](API_Point.md "API_Point.md") objects

Required: No

**RotationAngle**

Provides a numerical value corresponding to the rotation of the WORD block.
Possible values are 0, 90, 180, and 270.

Type: Float

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/Geometry.md "../../../goto/SdkForCpp/textract-2018-06-27/Geometry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/Geometry.md "../../../goto/SdkForJavaV2/textract-2018-06-27/Geometry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/Geometry.md "../../../goto/SdkForRubyV3/textract-2018-06-27/Geometry.md")
