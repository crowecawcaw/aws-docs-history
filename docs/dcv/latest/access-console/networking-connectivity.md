# Networking and

connectivity

The Amazon DCV Access Console components can all be installed on a single host or on
different hosts.

## Single host setup

In a single host setup, the Authentication Server, the Handler component and the
Web Client are all installed on a single host. An NGINX server can be used to proxy
requests from the web browser to the appropriate component. The web browser should
be able to initiate secure, persistent, bi-directional HTTPS connections with NGNIX.
All the components need bi-directional HTTP connection between each other on the
configured port (see table below). In addition, the Handler component needs to be
able to initiate secure, persistent, bi-directional HTTPS connections with the
Broker and the persistence store (DynamoDB or MariabDB/MySQL).

| Component             | Default Port |
| --------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication Server | 3000         |
| Handler               | 8080         |
| Web Client            | 9000         | ## Multiple host setup In multiple host setup, the Authentication Server, the Handler component and the Web Client can be all installed on different servers. An NGNIX server can be used to proxy requests from the web browser to the Web Client and establish a HTTPS between them. The Authentication Server and the Handler can be configured to accept HTTPS connections. All the components need bi-directional HTTPs connection between them on port 443. In addition, the Handler component needs to be able to initiate secure, persistent, bi-directional HTTPs connections with the Broker and the persistence store (DynamoDB or MariabDB/MySQL). |
