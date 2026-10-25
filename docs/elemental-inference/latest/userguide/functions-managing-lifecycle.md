

# Function status
<a name="functions-managing-lifecycle"></a>

A function's status controls what you can change about it.


| Status | Meaning | 
| --- | --- | 
| AVAILABLE | The function exists and no feed uses it. Everything about it can be changed, and it can be deleted. | 
| REFERENCED | At least one feed has a function output, enabled or disabled, that points at it. You can change the expressions and the description, as long as the request expression keeps reading the same media context. You can't change the name or the target, and you can't delete the function. | 
| CREATING, DELETING, DELETED | Transitional and terminal states. A create response always reports CREATING, and a delete response reports DELETING. | 

The `references` field of the function lists the IDs of the feeds that use it, which is how you find what is holding a function you want to delete. In the console, the same information is on the function's **Feed references** tab.