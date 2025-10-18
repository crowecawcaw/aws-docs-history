# DeleteIndexField

## Description


Removes an `IndexField`  from the search domain. For more information, see [Configuring Index Fields](configuring-index-fields.md "configuring-index-fields.md") in the *Amazon CloudSearch Developer Guide*.


## Request Parameters


 For information about the common parameters that all actions use, see [Common Parameters](CommonParameters.md "CommonParameters.md"). 





**DomainName**


A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).


Type: 
 String



 Length constraints:
 
 Minimum length of
 3.
 
 Maximum length of
 28.
 



 Required: Yes
 




**IndexFieldName**


The name of the index field your want to remove from the domain's indexing options.


Type: 
 String



 Length constraints:
 
 Minimum length of
 1.
 
 Maximum length of
 64.
 



 Required: Yes
 




## Response Elements


 The following 
 element is 
 returned in a structure named `DeleteIndexFieldResult`. 





**IndexField**


The status of the index field being deleted.


Type: 
 [IndexFieldStatus](API_IndexFieldStatus.md "API_IndexFieldStatus.md")





## Errors


 For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md"). 





**Base**


An error occurred while processing the request.


 HTTP Status Code: 400




**Internal**


An internal error occurred while processing the request. If this problem persists,
 report an issue from the [Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/").


 HTTP Status Code: 500




**InvalidType**


The request was rejected because it specified an invalid type definition.


 HTTP Status Code: 409




**ResourceNotFound**


The request was rejected because it attempted to reference a resource that does not exist.


 HTTP Status Code: 409
