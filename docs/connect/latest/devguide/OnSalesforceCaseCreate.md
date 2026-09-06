

# OnSalesforceCaseCreate
<a name="OnSalesforceCaseCreate"></a>

## AccountId condition
<a name="AccountId-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an account Id string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.AccountId"
+ Negate - true or false. If set to true, it means *If account id does not equal to the account id specified in the Operands*.

## Name condition
<a name="name-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is an account Id string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Name"
+ Negate - true or false. If set to true, it means *If name does not equal to or does not contain the priority specified in the Operands*.

## Email condition
<a name="email-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is an email string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Email"
+ Negate - true or false. If set to true, it means *If email does not equal to or does not contain the email specified in the Operands*.

## Phone condition
<a name="phone-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a phone string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Phone"
+ Negate - true or false. If set to true, it means *If phone does not equal to or does not contain the phone specified in the Operands*.

## Company condition
<a name="company-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a company string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Company"
+ Negate - true or false. If set to true, it means *If company does not equal to or does not contain the company specified in the Operands*.

## Type condition
<a name="stype-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a type string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Type"
+ Negate - true or false. If set to true, it means *If type does not equal to the type specified in the Operands*.

## Reason condition
<a name="reason-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a reason string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Reason"
+ Negate - true or false. If set to true, it means *If reason does not equal to the reason specified in the Operands*.

## Origin condition
<a name="origin-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an origin string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Origin"
+ Negate - true or false. If set to true, it means *If origin does not equal to the origin specified in the Operands*.

## Subject condition
<a name="subject-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a subject string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Subject"
+ Negate - true or false. If set to true, it means *If subject does not equal to or does not contain the subject specified in the Operands*.

## Priority condition
<a name="spriority-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a priority string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Priority"
+ Negate - true or false. If set to true, it means *If priority does not equal to the priority specified in the Operands*.

## Description condition
<a name="description-condition"></a>

**Parameters**
+ Operator - "EQUALS" or "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a description string. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.Description"
+ Negate - true or false. If set to true, it means *If description does not equal to or does not contain the description specified in the Operands*.

## CustomAttribute condition
<a name="customattribute-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the custom attribute value. 
+ ComparisonValue – "$.ThirdParty.Salesforce.CaseCreate.CustomAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true or false. If set to true, it means *If custom attribute does not equal to the custom attribute specified in the Operands*.