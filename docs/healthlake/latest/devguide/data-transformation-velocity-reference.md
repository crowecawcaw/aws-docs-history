

# Understanding C-CDA profiles

Complete reference for all Velocity helper functions in HealthLake Data Transformation Agent. All helpers are automatically registered in the Velocity context.

## Helper Categories
<a name="velocity-helper-categories"></a>
+ [Array Helpers](#velocity-array-helpers)
+ [String Helpers](#velocity-string-helpers)
+ [Conditional Helpers](#velocity-conditional-helpers)
+ [Date/Time Helpers](#velocity-datetime-helpers)
+ [Math Helpers](#velocity-math-helpers)
+ [Encoding Helpers](#velocity-encoding-helpers)
+ [JSON Helpers](#velocity-json-helpers)
+ [CDA Specific Helpers](#velocity-cda-helpers)
+ [Care Plan Helpers](#velocity-careplan-helpers)
+ [Specialized Helpers](#velocity-specialized-helpers)

## Array Helpers
<a name="velocity-array-helpers"></a>

Access via: `$arrayHelper`

elementAt(list, index)  
Returns element at specified index.  

```velocity
$arrayHelper.elementAt($myList, 0)
```

charAt(obj, index)  
Returns character at specified index in string.  

```velocity
$arrayHelper.charAt("Hello", 1) ## Returns "e"
```

length(obj)  
Returns length of collection or array.  

```velocity
$arrayHelper.length($myList)
```

strLength(obj)  
Returns string length.  

```velocity
$arrayHelper.strLength("Hello") ## Returns 5
```

slice(list, start, end)  
Returns sublist from start to end index.  

```velocity
$arrayHelper.slice($myList, 1, 3)
```

strSlice(obj, start, end)  
Returns substring from start to end index.  

```velocity
$arrayHelper.strSlice("Hello World", 0, 5) ## Returns "Hello"
```

toArray(obj)  
Converts object to array/list.  

```velocity
$arrayHelper.toArray($singleValue)
```

multipleToArray(values...)  
Combines multiple values into unique array.  

```velocity
$arrayHelper.multipleToArray($list1, $list2, $value)
```

concat(values...)  
Concatenates arrays or strings.  

```velocity
$arrayHelper.concat($array1, $array2)
```

## String Helpers
<a name="velocity-string-helpers"></a>

Access via: `$stringHelper`

toLower(obj)  
Converts to lowercase.  

```velocity
$stringHelper.toLower("HELLO") ## Returns "hello"
```

toUpper(obj)  
Converts to uppercase.  

```velocity
$stringHelper.toUpper("hello") ## Returns "HELLO"
```

trim(obj)  
Removes leading/trailing whitespace.  

```velocity
$stringHelper.trim(" hello ")
```

trimAndLower(obj)  
Trims and converts to lowercase.  

```velocity
$stringHelper.trimAndLower(" HELLO ")
```

trimAndUpper(obj)  
Trims and converts to uppercase.  

```velocity
$stringHelper.trimAndUpper(" hello ")
```

replace(obj, searchRegex, replaceStr)  
Replaces text using regex.  

```velocity
$stringHelper.replace("Hello World", "World", "Universe")
```

match(obj, regex)  
Returns list of regex matches.  

```velocity
$stringHelper.match("abc123def456", "\\d+") ## Returns ["123", "456"]
```

contains(obj, substrings...)  
Checks if string contains any substring.  

```velocity
$stringHelper.contains("Hello World", "World") ## Returns true
```

split(obj, regex)  
Splits string by regex pattern.  

```velocity
$stringHelper.split("a,b,c", ",") ## Returns ["a", "b", "c"]
```

startsWith(obj, prefix)  
Checks if string starts with prefix.  

```velocity
$stringHelper.startsWith("Hello", "He") ## Returns true
```

coalesce(values...)  
Returns first non-null, non-empty value.  

```velocity
$stringHelper.coalesce($null, "", "default") ## Returns "default"
```

concat(values...)  
Concatenates values into string.  

```velocity
$stringHelper.concat("Hello", " ", "World")
```

concatDefined(values...)  
Concatenates only non-null values.  

```velocity
$stringHelper.concatDefined("Hello", $null, "World") ## Returns "HelloWorld"
```

parseReferenceData(obj)  
Extracts text from complex objects (checks \_, displayName, text, value fields).  

```velocity
$stringHelper.parseReferenceData($complexObject)
```

decodeHtmlEntities(obj)  
Decodes HTML entities.  

```velocity
$stringHelper.decodeHtmlEntities("&lt;tag&gt;") ## Returns "<tag>"
```

escapeJsonString(str)  
Escapes special characters for JSON string values. Escapes: \\\\ \\" \\b \\f \\n \\r \\t. Use Case: Escaping user-provided strings that may contain special characters (addresses, names, descriptions).  

```velocity
$stringHelper.escapeJsonString($address)
```

## Conditional Helpers
<a name="velocity-conditional-helpers"></a>

Access via: `$conditionalHelper`

eq(context, params...)  
Checks if context equals any parameter.  

```velocity
$conditionalHelper.eq($status, "active", "completed")
```

ne(context, params...)  
Checks if context does not equal any parameter.  

```velocity
$conditionalHelper.ne($status, "inactive")
```

lt(context, other)  
Less than comparison.  

```velocity
$conditionalHelper.lt($value, 100)
```

gt(context, other)  
Greater than comparison.  

```velocity
$conditionalHelper.gt($value, 0)
```

lte(context, other)  
Less than or equal comparison.  

```velocity
$conditionalHelper.lte($value, 100)
```

gte(context, other)  
Greater than or equal comparison.  

```velocity
$conditionalHelper.gte($value, 0)
```

not(context)  
Logical NOT operation.  

```velocity
$conditionalHelper.not($isEmpty)
```

and(params...)  
Logical AND on all parameters.  

```velocity
$conditionalHelper.and($cond1, $cond2, $cond3)
```

or(params...)  
Logical OR on all parameters.  

```velocity
$conditionalHelper.or($cond1, $cond2, $cond3)
```

## Date/Time Helpers
<a name="velocity-datetime-helpers"></a>

Access via: `$dateHelper`

addHyphensDate(dateString)  
Formats date with hyphens (YYYY-MM-DD).  

```velocity
$dateHelper.addHyphensDate("20231225") ## Returns "2023-12-25"
```

formatAsDateTime(dateTimeString)  
Formats datetime to ISO format.  

```velocity
$dateHelper.formatAsDateTime("20231225120000") ## Returns "2023-12-25T12:00:00.000Z"
```

getDateTime(dateTimeString)  
Converts various datetime formats to ISO.  

```velocity
$dateHelper.getDateTime("2023-12-25 12:00:00")
```

startDateLteEndDate(startDate, endDate)  
Checks if start date ≤ end date.  

```velocity
$dateHelper.startDateLteEndDate("2023-01-01", "2023-12-31") ## Returns true
```

now()  
Returns current timestamp.  

```velocity
$dateHelper.now()
```

## Math Helpers
<a name="velocity-math-helpers"></a>

Access via: `$mathHelper`

isNaN(context)  
Checks if value is not a number.  

```velocity
$mathHelper.isNaN("abc") ## Returns true
```

abs(context)  
Returns absolute value.  

```velocity
$mathHelper.abs(-5) ## Returns 5.0
```

ceil(context)  
Rounds up to nearest integer.  

```velocity
$mathHelper.ceil(4.2) ## Returns 5.0
```

floor(context)  
Rounds down to nearest integer.  

```velocity
$mathHelper.floor(4.8) ## Returns 4.0
```

max(context, params...)  
Returns maximum value.  

```velocity
$mathHelper.max(1, 5, 3, 9, 2) ## Returns 9.0
```

min(context, params...)  
Returns minimum value.  

```velocity
$mathHelper.min(1, 5, 3, 9, 2) ## Returns 1.0
```

pow(context, exponent)  
Returns context raised to exponent power.  

```velocity
$mathHelper.pow(2, 3) ## Returns 8.0
```

random()  
Returns random double between 0.0 and 1.0.  

```velocity
$mathHelper.random()
```

round(context)  
Rounds to nearest integer.  

```velocity
$mathHelper.round(4.6) ## Returns 5
```

sign(context)  
Returns sign of number (-1, 0, or 1).  

```velocity
$mathHelper.sign(-5) ## Returns -1.0
```

trunc(context)  
Truncates decimal part.  

```velocity
$mathHelper.trunc(4.8) ## Returns 4
```

add(context, other)  
Addition operation.  

```velocity
$mathHelper.add(5, 3) ## Returns 8.0
```

subtract(context, other)  
Subtraction operation.  

```velocity
$mathHelper.subtract(5, 3) ## Returns 2.0
```

multiply(context, other)  
Multiplication operation.  

```velocity
$mathHelper.multiply(5, 3) ## Returns 15.0
```

divide(context, other)  
Division operation (returns context if divisor is 0).  

```velocity
$mathHelper.divide(10, 2) ## Returns 5.0
```

## Encoding Helpers
<a name="velocity-encoding-helpers"></a>

Access via: `$encodingHelper`

base64Encode(context)  
Base64 encodes input.  

```velocity
$encodingHelper.base64Encode("Hello World")
```

base64Decode(context)  
Base64 decodes input.  

```velocity
$encodingHelper.base64Decode($encodedData)
```

escapeJson(context)  
Escapes special characters for JSON string values. Escapes: \\\\ \\" \\n \\r \\t. Use Case: Escaping HTML/XML content for embedding in JSON strings (e.g., FHIR narrative div).  

```velocity
$encodingHelper.escapeJson($narrativeHtml)
```

## JSON Helpers
<a name="velocity-json-helpers"></a>

Access via: `$jsonHelper`

toString(context)  
Converts object to string.  

```velocity
$jsonHelper.toString($object)
```

toJsonString(context)  
Serializes object to JSON string.  

```velocity
$jsonHelper.toJsonString($object)
```

toJsonStringPrettier(context)  
Serializes object to pretty-printed JSON.  

```velocity
$jsonHelper.toJsonStringPrettier($object)
```

escapeSpecialChars(context)  
Escapes special JSON characters.  

```velocity
$jsonHelper.escapeSpecialChars($text)
```

unescapeSpecialChars(context)  
Unescapes special JSON characters.  

```velocity
$jsonHelper.unescapeSpecialChars($text)
```

## CDA Specific Helpers
<a name="velocity-cda-helpers"></a>

Access via: `$cdaHelper`

getFirstCdaSectionsByTemplateId(context, templateIds...)  
Returns first matching CDA section for each template ID as a map.  

```velocity
$cdaHelper.getFirstCdaSectionsByTemplateId($msg, "2.16.840.1.113883.10.20.22.2.6.1")
```

getAllCdaSectionsByTemplateId(context, templateIds...)  
Returns all matching CDA sections for template IDs as a list of maps.  

```velocity
$cdaHelper.getAllCdaSectionsByTemplateId($msg, "2.16.840.1.113883.10.20.22.2.1.1")
```

getAllCdaSectionsWithoutTemplateId(context, templateIds...)  
Returns all matching CDA sections without wrapping in normalized name.  

```velocity
$cdaHelper.getAllCdaSectionsWithoutTemplateId($msg, "2.16.840.1.113883.10.20.22.2.1.1")
```

generatePractitionerId(practitioner)  
Generates deterministic UUID for practitioner based on name, address, telecom.  

```velocity
$cdaHelper.generatePractitionerId($assignedEntity)
```

generateOrganizationId(organization)  
Generates deterministic UUID for organization based on name, address, telecom.  

```velocity
$cdaHelper.generateOrganizationId($representedOrganization)
```

getSpecifiedEntryRelationship(entryRelationshipContainer, targetTypeCode)  
Returns first entry relationship matching the target type code.  

```velocity
$cdaHelper.getSpecifiedEntryRelationship($entryRelationship, "SUBJ")
```

getSystemUrl(codeSystem, canBeUnknown)  
Maps OID code system to FHIR system URL.  

```velocity
$cdaHelper.getSystemUrl("2.16.840.1.113883.6.1", false) ## Returns "http://loinc.org"
```

extractRangeFromQuantity(context)  
Extracts range from quantity value (e.g., "10-20").  

```velocity
#set($result = $cdaHelper.extractRangeFromQuantity($quantity))#if($result.isValid) $result.range.low.value - $result.range.high.value#end
```

extractReferenceRange(range)  
Parses lab result reference range from CDA structure.  

```velocity
#set($refRange = $cdaHelper.extractReferenceRange($referenceRange))#if($refRange) Low: $refRange.low.value, High: $refRange.high.value#end
```

personalRelationshipRoleTypeCodeSystem()  
Returns the OID for personal relationship role type code system.  

```velocity
$cdaHelper.personalRelationshipRoleTypeCodeSystem() ## Returns "2.16.840.1.113883.1.11.19563"
```

xmlToString(xmlBlock)  
Converts parsed XML Map structure back to XML string with XHTML-compliant lowercase attributes. Use Case: Converting CDA narrative text sections to FHIR narrative div content. Features: Reconstructs XML elements with proper tags, Converts attribute names to lowercase for XHTML compliance (ID → id), Handles nested elements and lists, Preserves text content from \_ key.  

```velocity
#set($xmlString = $cdaHelper.xmlToString($section.text))
```

## Care Plan Helpers
<a name="velocity-careplan-helpers"></a>

Access via: `$carePlanHelper`

getActivityFromTreatmentPlanEncounter(context)  
Extracts FHIR CarePlan activity from CDA treatment plan encounter. Returns activity with: status, performer, location, scheduledPeriod, code, description.  

```velocity
$carePlanHelper.getActivityFromTreatmentPlanEncounter($encounter)
```

getFirstEffectiveTimeFromObservationComponent(context)  
Returns first effective time value from observation components.  

```velocity
$carePlanHelper.getFirstEffectiveTimeFromObservationComponent($components)
```

## Specialized Helpers
<a name="velocity-specialized-helpers"></a>

Access via: `$specializedHelper`

generateUUID(context)  
Generates deterministic UUID from context using name-based UUID (v5).  

```velocity
$specializedHelper.generateUUID("unique-identifier")
```

generateUUIDV2(context)  
Generates UUID after removing line breaks from context.  

```velocity
$specializedHelper.generateUUIDV2($textWithLineBreaks)
```

ensureUUID(context)  
Checks if input is already a UUID format; returns as-is if UUID, generates deterministic UUID if not. Use Case: Ensuring consistent UUID format for IDs that may already be UUIDs or need conversion.  

```velocity
$specializedHelper.ensureUUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890") ## Returns same UUID
$specializedHelper.ensureUUID("patient-123") ## Generates UUID from input
```

addHyphensSSN(context)  
Formats 9-digit SSN with hyphens (XXX-XX-XXXX).  

```velocity
$specializedHelper.addHyphensSSN("123456789") ## Returns "123-45-6789"
```

nullFlavorAwareOr(values...)  
Returns true if any value is non-null and not a nullFlavor object.  

```velocity
$specializedHelper.nullFlavorAwareOr($value1, $value2, $value3)
```

buildPresentedForm(b64String, component)  
Builds FHIR presentedForm array from base64 strings and observation components.  

```velocity
$specializedHelper.buildPresentedForm($base64Data, $components)
```

extractTextFromNestedProperties(obj)  
Recursively extracts all \_ property values from nested objects.  

```velocity
$specializedHelper.extractTextFromNestedProperties($nestedObject)
```

buildDefaultDiagReportDetails(context)  
Builds default diagnostic report details with standard LOINC code.  

```velocity
$specializedHelper.buildDefaultDiagReportDetails($section)
```

convertFeetAndInchesToCm(context)  
Converts "X ft Y in" format to centimeters.  

```velocity
#set($result = $specializedHelper.convertFeetAndInchesToCm("5 ft 10 in"))#if($result.isValid) $result.value $result.unit ## Returns "177.8 cm"#end
```

extractNumberAndUnit(context)  
Extracts number and unit from string (e.g., "10mg").  

```velocity
#set($result = $specializedHelper.extractNumberAndUnit("10mg"))#if($result.isValid) Value: $result.value, Unit: $result.unit#end
```

extractComparator(context)  
Extracts comparator and number from string (e.g., ">10", "<=5").  

```velocity
#set($result = $specializedHelper.extractComparator(">10"))#if($result.isValid) Comparator: $result.comparator, Number: $result.number#end
```

extractDecimal(context)  
Extracts first decimal number from string.  

```velocity
$specializedHelper.extractDecimal("Value is 123.45") ## Returns 123.45
```

personalRelationshipRoleTypeCodeSystem()  
Returns OID for personal relationship role type code system.  

```velocity
$specializedHelper.personalRelationshipRoleTypeCodeSystem()
```

convertMappedDataToPlainText(context)  
Converts list of key-value maps to plain text format.  

```velocity
$specializedHelper.convertMappedDataToPlainText($mappedData)
```

extractAndMapTableData(context)  
Extracts and maps HTML table data to list of key-value maps. Returns list of maps where keys are column headers and values are cell contents.  

```velocity
$specializedHelper.extractAndMapTableData($tableObject)
```

getObservationCategoryDisplayFromCode(code)  
Returns display name for observation category code. Supported codes: vital-signs, laboratory, imaging, procedure, survey, exam, therapy, activity.  

```velocity
$specializedHelper.getObservationCategoryDisplayFromCode("vital-signs") ## Returns "Vital Signs"
```

## Usage Examples
<a name="velocity-usage-examples"></a>

### Basic Template
<a name="velocity-usage-basic-template"></a>

```velocity
## Access helpers
#set($patientId = $specializedHelper.generateUUID($msg.ClinicalDocument.recordTarget.patientRole.id))
#set($sections = $cdaHelper.getFirstCdaSectionsByTemplateId($msg, "2.16.840.1.113883.10.20.22.2.6.1"))

## String manipulation
#set($name = $stringHelper.trim($msg.ClinicalDocument.recordTarget.patientRole.patient.name.given))
#set($upperName = $stringHelper.toUpper($name))

## Date formatting
#set($date = $dateHelper.addHyphensDate($msg.ClinicalDocument.effectiveTime.value))

## Conditional logic
#if($conditionalHelper.eq($status, "active", "completed"))
  ## Process active/completed status
#end
```

### CDA Section Processing
<a name="velocity-usage-cda-section-processing"></a>

```velocity
## Get all medication sections
#set($medSections = $cdaHelper.getAllCdaSectionsByTemplateId($msg, "2.16.840.1.113883.10.20.22.2.1.1"))

#foreach($section in $medSections)
  ## Process each medication section
  #set($entries = $section.get("_2_16_840_1_113883_10_20_22_2_1_1").entry)
  #foreach($entry in $arrayHelper.toArray($entries))
    ## Process medication entry
  #end
#end
```

### ID Generation
<a name="velocity-usage-id-generation"></a>

```velocity
## Generate practitioner ID
#set($practitionerId = $cdaHelper.generatePractitionerId($assignedEntity))

## Generate location ID
#set($locationId = $cdaHelper.generateLocationId($participantRole))

## Generate organization ID
#set($orgId = $cdaHelper.generateOrganizationId($representedOrganization))
```