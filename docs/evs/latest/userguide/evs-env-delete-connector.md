

# Delete an Amazon EVS environment connector
<a name="evs-env-delete-connector"></a>

You can delete a connector when it is no longer needed.

More info on connectors can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-connector).

**Note**  
The connector must be in an Active, Create Failed, or Update Failed state to be deleted.

**Note**  
All entitlements associated with the connector must be deleted before the connector can be removed.

 **To delete an Amazon EVS environment connector** 

Follow these steps to delete an Amazon EVS connector.

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment containing the connector.

1. Select the **Connectors** tab.

1. Select the connector you want to delete.

1. Choose **Delete Connector**.

1. Confirm the deletion.

1. To verify completion, check that the connector no longer appears in the list.

1. Open a new terminal session.

1. Delete the connector. See example command below for reference.

   ```
   aws evs delete-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi
   ```

1. To verify completion, use the **list-environment-connectors** command and confirm the connector is no longer listed.

   ```
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```