# Implicit profile object types in

Amazon Connect Customer Profiles

You can use any object type that matches the name of a template ID (as returned by
the [ListProfileObjectTypeTemplates](../../../customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.md") API) without explicitly defining it. The
object type will exactly match the definition of the template definition of this
object type. If an explicit object type is defined, it replaces the implicit one.

Implicit object types are included in the [ListProfileObjectTypes](../../../customerprofiles/latest/APIReference/API_ListProfileObjectTypes.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjectTypes.md") API or returned by [GetProfileObjectType](../../../customerprofiles/latest/APIReference/API_GetProfileObjectType.md "../../../customerprofiles/latest/APIReference/API_GetProfileObjectType.md") operations, but they can still be deleted if you
want to remove all data ingested from that object type.
