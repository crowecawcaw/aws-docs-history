AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# How to use the network diagram in AWS Migration Hub

This section describes how to use the network diagram in Migration Hub.

###### To use the network diagram

1. In the navigation pane, under **Discover**, choose
   **Servers**.
2. To view details about the server, choose the hostname of the server from the
   **Server info** column. The server's detail page displays information about
   the server, such as hostname, IP address, performance metrics, and so on.
3. Choose **Network**. The icon for the server you choose is centered in the
   network diagram. Connections fan out from the center server to servers that are directly
   connected to the server you choose.
   The network diagram console is divided into three panes: toolbar, diagram, and the server
   detail/selected server list pane.

The following topics describe the network diagram console panes.

###### Topics

- [Toolbar](#network-diagram-toolbar "#network-diagram-toolbar")
- [Diagram](#network-diagram-pane "#network-diagram-pane")
- [Server details and selected server list](#network-diagram-server-details "#network-diagram-server-details")

## Toolbar

Choosing an icon on the toolbar performs an action or opens a pane with more choices. Only
one of these panes can be open at any one time.

The toolbar icons are described in the following table.

| Icon                                                                               | Name             | Description                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gear icon representing settings or configuration options.                          | Settings         | To change your settings, choose<br>Gear icon representing settings or configuration options.<br>.                                                                                                                        |
| Funnel icon representing a filter or narrowing down of information.                | Filters          | To filter server connections, choose<br>Funnel icon representing a filter or narrowing down of information.<br>and then clear the check box next to each port number that you do not<br>want to display connections for. |
| Magnifying glass icon with a plus sign, representing a search or zoom-in function. | Zoom in          | To zoom in on the diagram, choose<br>Magnifying glass icon with a plus sign, representing a search or zoom-in function.<br>.                                                                                             |
| Magnifying glass icon with a plus sign, representing a search or zoom-in function. | Zoom out         | To zoom out, choose<br>Magnifying glass icon with a plus sign, representing a search or zoom-in function.<br>.                                                                                                           |
| Icon representing a full-screen or expand view option.                             | Zoom to fit      | To zoom to fit the entire diagram in the current view, choose<br>Icon representing a full-screen or expand view option.<br>.                                                                                             |
| Icon with four arrows pointing outward from a central point, indicating expansion. | View full screen | To view the diagram full screen, choose<br>Icon with four arrows pointing outward from a central point, indicating expansion.<br>.                                                                                       |

## Diagram

This section describes the icons used in the diagram to show network server nodes and how
to interact with the diagram.

- [Diagram Icons](#network-diagram-icons "#network-diagram-icons")
- [Adding a server to a diagram](#network-diagram-add-server "#network-diagram-add-server")
- [Interacting with the diagram](#network-diagram-controls "#network-diagram-controls")

### Diagram Icons

The icons used in the diagram are shown in the following table.

| Icon                                                                                                                       | Name                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List icon with three horizontal lines representing a menu or navigation button.                                            | Server                                                                                            | Represents a server that is running a discovery agent that is part of your<br>network.<br>To view details about a server, right-click<br>List icon with three horizontal lines representing a menu or navigation button.<br>and then choose **View server details**.<br>To select a server for a group application, right-click<br>List icon with three horizontal lines representing a menu or navigation button.<br>and then choose **Select Server**. |
| Checkmark icon indicating confirmation or completion of a task or selection.                                               | Selected Server                                                                                   | Represents a server that you selected for group application.<br>To deselect a server, choose<br>Checkmark icon indicating confirmation or completion of a task or selection.<br>and then choose **Unselect server\*<br>• in the server<br>details pane.<br>To select a server for a group application, right-click<br>Checkmark icon indicating confirmation or completion of a task or selection.<br>and then choose **Select Server\*\*.               |
| Server icon labeled "Server Hostname Application" representing a cloud service.                                            | Server<br>with application label                                                                  | Represents a server that belongs to a group application. The name of the application<br>is displayed under the server icon. The names of all the applications the server belongs<br>to are displayed.                                                                                                                                                                                                                                                    |
| Circular diagram showing 12 AWS services with icons and names around a central AWS logo.                                   | Server without agent                                                                              | Represents a server in your network that doesn't have Discovery Agent installed.<br>To view details about the server, choose<br>Circular diagram showing 12 AWS services with icons and names around a central AWS logo.<br>.                                                                                                                                                                                                                            |
| Plus sign icon inside a circle, indicating an add or create action.<br>Minus sign icon in a dark blue circular background. | Plus sign on upper right corner of server icon<br>Minus sign on upper right corner of server icon | Represents that the server has servers connected to it that aren't shown in the<br>diagram. To expand the network from the server node, choose<br>Plus sign icon inside a circle, indicating an add or create action.<br>on the server icon.<br>To collapse the network back to the server node, choose<br>Minus sign icon in a dark blue circular background.<br>on the server icon.                                                                    |

### Adding a server to a diagram

You can search for servers to add to the diagram by searching by hostname or by IP
address. You'll get results after adding your search criteria and pressing
**Enter**.

###### To search for servers to add to the network diagram

1. Choose the search icon on the toolbar, and then choose **Hostname** or
   **IP address**.
2. Type the criteria for your search in the search box.

For example, to search for servers that contain **IAM** in their
hostname, enter **IAM**. Or, enter **0.0.0.** to search for
servers that contain **0.0.0.** in their IP address. 3. From the result, select the servers to add to the diagram, and then choose
**+** to add them to the diagram.

### Interacting with the diagram

You can interact with the diagram in the following ways:

- To pan around, choose and drag on empty areas in the diagram.
- To zoom in and out, scroll up and down, respectively.
- To highlight all the connections to and from a server on the diagram, hover over a
  server icon.
- To see a server's details in the server detail pane, choose a server icon.
  - Inbound ports only shows ports that are being opened on the server.
  - Outbound ports aren't displayed.
  - Hovering over a port highlights all the connections that open that port on the
    diagram.

- Hold shift and choose servers to select them for grouping applications or other
  actions.

## Server details and selected server list

Server details and the list of selected servers share the pane right of the diagram. You
can toggle back and forth between the server details view and the selected server list view by
choosing the server icon.

To see details about a server on the diagram, choose the server icon. Details about the
server display in the pane to the right of the diagram.

You can use the following options to select servers from the network diagram:

- On the network diagram, choose a server node icon. Details about the server show in the
  server details pane, where you choose **Select server**.
- On the network diagram, open the context (right-click) menu on the server node icon, and
  then choose **Select server** from the dropdown list.
- Choose **Select all** to select all the servers for grouping that are in
  your diagram. Only the servers with the Discovery Agent running on them are selected.
- Hold **shift** to select multiple servers at the same time.

Selected servers are shown in a list in the same pane as the server details. You can toggle
back and forth between the server details view and the selected server list view by choosing the
server icon.

After you select one or more servers, you can create an application, or add to an existing
one, by choosing **Group as application**. You can add a descriptive tag to the
selected servers by choosing **Add tag** from the **Actions**
menu. Doing so shows a dialog box where you can type a value for **Key**, and
optionally a value for **Value**. For more information, see [Step 3: Group servers as
applications](gs-new-user-discovery.md#gs-discovery-group-as-applications "gs-new-user-discovery.md#gs-discovery-group-as-applications").
