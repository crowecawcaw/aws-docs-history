# Using Amazon MQ for ActiveMQ

Amazon MQ makes it easy to create a message broker with the computing and storage resources
that fit your needs. You can create, manage, and delete brokers using the AWS Management Console, Amazon MQ
REST API, or the AWS Command Line Interface.

Amazon MQ for ActiveMQ brokers can be deployment as _single-instance
brokers_ or _active/standby brokers_. For both
deployment modes, Amazon MQ provides high durability by storing its data redundantly.

###### Note

Amazon MQ uses [Apache KahaDB](http://activemq.apache.org/kahadb.html "http://activemq.apache.org/kahadb.html") as its data store.
Other data stores, such as JDBC and LevelDB, aren't supported.

You can access your brokers by using [any programming language that ActiveMQ supports](http://activemq.apache.org/cross-language-clients.html "http://activemq.apache.org/cross-language-clients.html") and by enabling TLS explicitly for the following protocols:

- [AMQP](http://activemq.apache.org/amqp.html "http://activemq.apache.org/amqp.html")
- [MQTT](http://activemq.apache.org/mqtt.html "http://activemq.apache.org/mqtt.html")
- MQTT over [WebSocket](http://activemq.apache.org/websockets.html "http://activemq.apache.org/websockets.html")
- [OpenWire](http://activemq.apache.org/openwire.html "http://activemq.apache.org/openwire.html")
- [STOMP](http://activemq.apache.org/stomp.html "http://activemq.apache.org/stomp.html")
- STOMP over WebSocket
  To learn about Amazon MQ REST APIs, see the _[Amazon MQ REST API Reference](../api-reference.md "../api-reference.md")_.
