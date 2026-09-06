# View AS2 server details

You can find a list of details and properties for an individual AWS Transfer Family server.
Server properties include protocols, status, and more. For AS2 servers, you can also
view the AS2 asynchronous MDN egress IP addresses.

![The server details console page for an AS2 server showing protocol and identity provider section.](images/as2-server-details-top.png)
![The server details console page for an AS2 server showing the endpoint details section.](images/as2-server-details-endpoints.png)
![The server details console page for an AS2 server showing the users and agreements sections (AS2 servers do not have any listed users).](images/as2-server-details-users-agreements.png)
![The server details console page for an AS2 server showing the server host keys and additional details sections.](images/as2-server-details-keys-additional.png)
Each AS2 server is assigned three static IP addresses. Use these IP addresses for
sending asynchronous MDNs to your trading partners over AS2.

![Panel from an AS2 server details page, showing the list of service-managed static IP addresses.](images/as2-server-details-static-ips.png)
The bottom portion of the AS2 server details page contains details for any attached
workflow and monitoring and tagging information.

![The server details console page for an AS2 server, showing tag details.](images/as2-server-details-workflows-monitoring.png)
![The server details console page for an AS2 server, showing tag details.](images/edit-server-details-tags.png)
