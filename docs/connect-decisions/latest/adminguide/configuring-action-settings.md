

# Configuring Action Settings
<a name="configuring-action-settings"></a>

 Amazon Connect Decisions allows you to control for which action types it should offer to perform operations on your behalf in your Enterprise Resource Planning (ERP) system. By default, all action types are disabled, and you must enable this feature for each desired action type. 

**Note**  
 Enabling support for a given action type controls whether the option of Amazon Connect Decisions performing the action on your behalf will be presented throughout the system (e.g.: when reviewing an Insight with a recommendation of the given type). Amazon Connect Decisions will not perform these actions (even when support is enabled) until you accept the specific recommendation. 

**Supported action types:**
+ Create Purchase Order
+ Update Purchase Order
+ Cancel Purchase Order

**Configure actions support for each action type:**

1. In your instance of Amazon Connect Decisions, navigate to the Data Management page

1. Select the `Actions` tab

1. Find the action type you wish to configure in the listing

1. To enable support for the action type:
   + Select one of the connections listed in the dropdown menu for that action type
   + Note: the dropdown will display only the available connections that have been configured of a type supporting the `Actions` capability (e.g.: `SAP S/4HANA`)

1. To disable support for the action type:
   + Select `No connection` in the dropdown menu for that action type

1. Click `Save` to save your changes