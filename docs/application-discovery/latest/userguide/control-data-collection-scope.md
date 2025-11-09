AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Controlling the scope of vCenter data

collection

The vCenter user requires read-only permissions on each ESX host or VM to inventory using
Application Discovery Service. Using the permission settings, you can control which hosts and VMs are included in
the data collection. You can either allow all hosts and VMs under the current vCenter to be
inventoried, or grant permissions on a case-by-case basis.

###### Note

As a security best practice, we recommend against granting additional, unneeded
permissions to the vCenter user of the Application Discovery Service.

The following procedures describe configuration scenarios ordered from least granular to
most granular. These procedures are for vSphere Client v6.7.0.2. The procedures for other
versions of the client might be different, depending on which version of the vSphere client
you are using.

###### To discover data about _all_ ESX hosts and VMs under

the current vCenter

1. In your VMware vSphere client, choose **vCenter** and then choose
   either **Hosts and Clusters** or **VMs and
   Templates**.
2. Choose a datacenter resource and then choose
   **Permissions**.
3. Choose the vCenter user and then choose the symbol to add, edit, or remove a user
   role.
4. Choose **Read-only** from the **Role**
   menu.
5. Choose **Propagate to children** and then choose
   **OK**.

###### To discover data about a _specific_ ESX host and

_all_ of its child objects

1. In your VMware vSphere client, choose **vCenter** and then choose
   either **Hosts and Clusters** or **VMs and
   Templates**.
2. Choose **Related Objects**, **Hosts**.
3. Open the context (right-click) menu for the host name and choose **All
   vCenter Actions**, **Add Permission**.
4. Under **Add Permission**, add the vCenter user to the host. For
   **Assigned Role**, choose **Read-only**.
5. Choose **Propagate to children**, **OK**.

###### To discover data about a _specific_ ESX host or

child VM

1. In your VMware vSphere client, choose **vCenter** and then choose
   either **Hosts and Clusters** or **VMs and
   Templates**.
2. Choose **Related Objects**.
3. Choose **Hosts** (showing a list of ESX hosts known to vCenter)
   or **Virtual Machines** (showing a list of VMs across all ESX
   hosts).
4. Open the context (right-click) menu for the host or VM name and choose
   **All vCenter Actions**, **Add
   Permission**.
5. Under **Add Permission**, add the vCenter user to the host or
   VM. For **Assigned Role**, choose **Read-only**, .
6. Choose **OK**.

###### Note

If you chose **Propagate to children**, you can still remove the
read-only permission from ESX hosts and VMs on a case-by-case basis. This option has no
effect on inherited permissions applying to other ESX hosts and VMs.
