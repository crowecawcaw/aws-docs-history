

# Setting up attribute-level access
<a name="setting-up-attribute-level-access"></a>

 Attribute-Based Access Control (ABAC) adds an additional layer of precision by restricting access based on business context. Using product and site attributes, you can ensure that planners only see details for the specific products and locations they manage, while managers maintain visibility across their teams' areas of responsibility. 

 Any user with the 'Admin' role can configure access by product and sites for other users: 

1. Navigate to the Users page from the left navigation bar.

1. From the list of users in that instance, select the user that needs configuration.

1. By default, in the Data access section, users will have "Grant full access to all products and sites" enabled. When this toggle is on, it provides access to all products and sites (how it worked prior to this launch).

1. Toggle off "Grant full access to all products and sites" and the product and sites configuration section will become visible. No products or sites will be assigned when first accessed.

1. Click the Add/Remove button for either products or sites based on what you need to configure. Use the search to find and select the items needed for that user.

1. Multiple users can have the same product or site assigned to them. A user can have a maximum of 1,000 product-site combinations.

1. Previously configured products or sites can be removed using the same interface.

1. Review and confirm the full list of additions and removals in the final page of the wizard to complete the access configuration.

 Once product and site access has been configured, access for that user will be restricted based on these assignments: 
+ All users can view any exception or recommendation page, regardless of whether it was generated for a product or site included in their access control.
+ To perform mutate actions (such as dismissing an exception or changing status from In Progress to Complete), users must have the appropriate product OR site configured in their access control.
+ Users with configured access control can also use User Assignment and the Access View Toggle.