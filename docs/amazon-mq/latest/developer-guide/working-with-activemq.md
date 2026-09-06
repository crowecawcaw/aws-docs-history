

# Using Amazon MQ for ActiveMQ
<a name="working-with-activemq"></a>

Amazon MQ makes it easy to create a message broker with the computing and storage resources that fit your needs. You can create, manage, and delete brokers using the AWS Management Console, Amazon MQ REST API, or the AWS Command Line Interface.

Amazon MQ for ActiveMQ brokers can be deployment as *single-instance brokers* or *active/standby brokers*. For both deployment modes, Amazon MQ provides high durability by storing its data redundantly.

**Note**  
Amazon MQ uses [Apache KahaDB](https://activemq.apache.org/kahadb.html) as its data store. Other data stores, such as JDBC and LevelDB, aren't supported.

You can access your brokers by using [any programming language that ActiveMQ supports](https://activemq.apache.org/cross-language-clients.html) and by enabling TLS explicitly for the following protocols:
+ [AMQP](https://activemq.apache.org/amqp.html)
+ [MQTT](https://activemq.apache.org/mqtt.html)
+ MQTT over [WebSocket](https://activemq.apache.org/websockets.html)
+ [OpenWire](https://activemq.apache.org/openwire.html)
+ [STOMP](https://activemq.apache.org/stomp.html)
+ STOMP over WebSocket

To learn about Amazon MQ REST APIs, see the *[Amazon MQ REST API Reference](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/)*.