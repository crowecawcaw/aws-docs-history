# Connecting to endpoints

When you have your endpoint, either cluster or instance, you can connect to it using the `mongo` shell or a connection string.

## Connecting using the mongo shell

Use the following structure to construct the string that you need to connect to your cluster or instance using the `mongo`
shell:

```
mongo \
    --ssl \
    --host `Endpoint`:`Port` \
    --sslCAFile global-bundle.pem \
    --username `UserName` \
    --password `Password`
```

###### `mongo` shell examples

Connect to a cluster:

```
mongo \
    --ssl \
    --host `sample-cluster.corcjozrlsfc.us-east-1.docdb.amazonaws.com`:`27017` \
    --sslCAFile global-bundle.pem \
    --username `UserName` \
    --password `Password`
```

Connect to an instance:

```
mongo \
    --ssl \
    --host `sample-cluster-instance.corcjozrlsfc.us-east-1.docdb.amazonaws.com`:`27017` \
    --sslCAFile global-bundle.pem \
    --username `UserName` \
    --password `Password`
```

## Connecting using a connection string

Use the following structure to construct the connection string that you need to connect to your cluster or instance.

```
mongodb://`UserName`:`Password`@`endpoint`:`port`?replicaSet=rs0&ssl_ca_certs=global-bundle.pem
```

###### Connection string examples

Connect to a cluster:

```
mongodb://`UserName`:`Password`@`sample-cluster.cluster-corlsfccjozr.us-east-1`.docdb.amazonaws.com:`27017`?replicaSet=rs0&ssl_ca_certs=global-bundle.pem
```

Connect to an instance:

```
mongodb://`UserName`:`Password`@`sample-cluster-instance.cluster-corlsfccjozr.us-east-1`.docdb.amazonaws.com:`27017`?replicaSet=rs0&ssl_ca_certs=global-bundle.pem
```
