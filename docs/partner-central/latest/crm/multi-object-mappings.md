# Multi-object mapping

Multi-object mapping allows partners to map AWS fields to a primary source object, such as
an opportunity or lead, and to the Salesforce objects related to the primary source.

###### Note

Remember the following when using multi-object mapping:

- When using the Salesforce `Account` object for multi-object-mapping
  with an opportunity object, you must configure the `Default Account` in the
  [ACE custom settings](guided-setup-apis.md#api-sys-config-settings "guided-setup-apis.md#api-sys-config-settings") to receive
  opportunities.
- When receiving an opportunity, if you map to an object other than the chosen
  `Opportunity` object, you must ensure that you link the related object to
  your opportunity record.

For example, when receiving an AWS referral for the first time, the inserted
opportunity has no mapped objects' related IDs _unless_ you
configure the `Default Account` in the ACE custom settings. If you
configure the default account, the referral has the IDs of the chosen opportunity or
account objects. Otherwise, the mapped field value won't be inserted. In that case,
you must modify the opportunity to add the related object ID, and choose
**Sync with AWS**. When AWS pushes the opportunity back to
Salesforce, the mapped object’s field updates because it has a reference to the
object's related ID.

- Select the **Clone Default Account** option in custom settings.
  This allows AWS to clone the default account when necessary, particularly if you map
  account fields to your primary object.

###### To map related objects

1. In Salesforce, navigate to the **ACE Mappings** tab and choose an
   opportunity or lead.
2. From the **Object** selector, choose your source object.

The **Salesforce Fields** column appears and displays the
**>** symbol at the end of any fields that contain related
objects. 3. Select an **>** symbol to expand the list of related objects for
that field. 4. Choose the field that you want to map to the AWS field. 5. Choose **Save**.
