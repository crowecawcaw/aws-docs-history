

# MediaConnect router I/O states
<a name="io-state-changes"></a>

An AWS Elemental MediaConnect router I/O transitions through different states from the moment you create it through to the moment you delete it. These states can be grouped into several categories:
+ Operational transitions: **Starting** and **Stopping** states manage the activation of an I/O
+ Settings updates: The **Updating** state handles modifications to an I/O’s configuration 
+ Maintenance: The **Migrating** state indicates that the I/O is undergoing a maintenance operation

 The following illustration shows the I/O lifecycle and the transitions between I/O states. Note that depending on the type of I/O, it may begin its lifecycle directly in the **Standby** state, bypassing the **Creating** state.

![State diagram showing MediaConnect router I/O lifecycle. Main states are Creating, Standby, and Active, with transition states (Starting/Stopping) between them. The Updating state branches from both Standby and Active, returning to its origin state. The Migrating state branches from Active only, returning to Active after maintenance completes. The lifecycle ends with Deleting state. Black arrows show transitions, blue arrows indicate returns.](http://docs.aws.amazon.com/mediaconnect/latest/ug/images/router-io-state-diagram.png)


## State definitions
<a name="io-state-definitions"></a>

The following definitions describe each state in detail, in the order you might typically encounter them:

**Creating**  
MediaConnect is creating the router I/O and setting up the necessary resources and configurations. During this process, the service prepares the I/O to handle content routing and establishes its initial settings.

**Standby**  
The router I/O is ready for use. This is the default state after you create or stop an I/O. In this state, the I/O is fully configured and idle, but is prepared to start processing content as soon as you activate it.

**Starting**  
This is a transition state where MediaConnect is starting up the router I/O to prepare for content processing. The service activates the necessary components to begin handling media streams according to the I/O's configuration.

**Active**  
The router I/O is actively processing content. For inputs, this means receiving content from the source and making it available for routing. For outputs, this means receiving routed content and sending it to the configured destination. 

**Updating**  
This is a configuration change state where MediaConnect is updating specific settings for the I/O, such as the protocol configuration or maximum bitrate. During this state, the service applies the requested changes while maintaining the I/O's existing connections and routing assignments.

**Migrating**  
MediaConnect is in the process of performing a maintenance operation on the router I/O. This state occurs during scheduled maintenance windows or manual restart operations. The I/O returns to its previous state after the maintenance operation completes.

**Stopping**  
This is a transition state where MediaConnect is stopping the router I/O's operations. The service stops content processing and prepares the I/O to return to the Standby state.

**Deleting**  
MediaConnect is in the process of permanently removing the router I/O. After this state, the router I/O will no longer exist.

In addition, the following states manage error handling:

**Error**  
This is an error handling state where the router I/O has encountered an issue that prevents normal operation. Common issues that can trigger this state include network connectivity problems, resource constraints, or configuration conflicts. The I/O remains in this state until MediaConnect can initiate recovery procedures or until manual intervention resolves the underlying issue.

**Recovering**  
This is an error handling state where MediaConnect is attempting to resolve issues that caused the I/O to enter an error state. During this state, MediaConnect works to restore the I/O's functionality based on its configured settings and routing assignments.