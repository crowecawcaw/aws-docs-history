# Connect and interact with AWS Cloud.

In this section, you use the MQTT client in the AWS IoT console to monitor the communication
between your evaluation kit and the AWS Cloud.

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. In the navigation pane, choose **Test** and then
   **MQTT Test Client**.
3. In **Subscribe to a topic**, enter `#`, and
   then choose **Subscribe**.

## Connect

n this section, you learn how to connect to AWS Cloud. This is a two step process.

###### To establish a secure connection

1. Open the terminal application on your host machine and enter the command:

```
AT+CONNECT
```

2. After a short time, you will receive the message:

```
OK 1 CONNECTED
```

Congratulations! You are now successfully connected to your AWS Cloud account.

## Send data to AWS Cloud

In this section, you learn how to send a message to AWS Cloud. This is a three step process.

###### To send a "Hello World!" message

1. Open the terminal application on your host machine and enter the command:

```
AT+CONF Topic1=data
```

You should receive the response from the module:

```
OK
```

2. In the terminal application, enter the command:

```
AT+SEND1 Hello World!
```

After a short time, you should receive the message `OK`. 3. In the AWS IoT console MQTT test client you will see
`Hello World!` message with the topic `data`.

## Receive data and commands from AWS Cloud

In this section, you learn how to receive data and commands from AWS Cloud. This is a four step process.

###### To receive messages and data

1. Open the terminal application on your host machine and enter the command:

```
AT+CONF Topic1=MyTopic
```

You should receive the response from the module:

```
OK
```

2. In the terminal, enter the command:

```
AT+SUBSCRIBE1
```

3. In the AWS IoT console MQTT Test Client, choose **Publish to a topic**,
   and enter `MyTopic` in the topic name field. Keep the default
   message ("Hello from AWS IoT console") in the message field, then choose
   **Publish**.
4. In the terminal application, enter the command:

```
AT+GET1
```

You should receive the message:

```
OK Hello from AWS IoT console
```
