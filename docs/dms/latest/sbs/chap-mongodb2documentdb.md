# Install and configure MongoDB community edition

Perform these steps on the Amazon EC2 instance that you launched in [Launch an Amazon EC2 instance](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md").

1.  Go to [Install MongoDB community edition on Amazon Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/ "https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/") in the MongoDB documentation and follow the instructions there.
2.  By default, the MongoDB server (`mongod`) only allows loopback connections from IP address 127.0.0.1 (localhost). To allow connections from elsewhere in your Amazon VPC, do the following:
    1. Edit the `/etc/mongod.conf` file and look for the following lines.

    ```
    # network interfaces
    net:
      port: 27017
      bindIp: 127.0.0.1  # Enter 0.0.0.0,:: to bind to all IPv4 and IPv6 addresses or, alternatively, use the net.bindIpAll setting.
    ```

    2. Modify the `bindIp` line so that it looks like the following.

    ```
      bindIp: public-dns-name
    ```

    3. Replace `public-dns-name` with the actual public DNS name for your instance, for example `ec2-11-22-33-44.us-west-2.compute.amazonaws.com`.
    4. Save the `/etc/mongod.conf` file, and then restart `mongod`.

    ```
    sudo service mongod restart
    ```

3.  Populate your MongoDB instance with data by doing the following:
    1. Use the `wget` command to download a JSON file containing sample data.

    ```
    wget http://media.mongodb.org/zips.json
    ```

    2. Use the `mongoimport` command to import the data into a new database (`zips-db`).

    ```
    mongoimport --host public-dns-name:27017 --db zips-db --file zips.json
    ```

    3. After the import completes, use the `mongo` shell to connect to MongoDB and verify that the data was loaded successfully.

    ```
    mongo --host public-dns-name:27017
    ```

    4. Replace `public-dns-name` with the actual public DNS name for your instance.
    5. At the `mongo` shell prompt, enter the following commands.

    ```
    use zips-db

    db.zips.count()

    db.zips.aggregate( [
       { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
       { $group: { _id: "$_id.state", avgCityPop: { $avg: "$pop" } } }
    ] )
    ```

    The output should display the following:

        * The name of the database (`zips-db`)
        * The number of documents in the `zips` collection (29353)
        * The average population for cities in each state

    6. Exit from the `mongo` shell and return to the command prompt by using the following command.

    ```
    exit
    ```
