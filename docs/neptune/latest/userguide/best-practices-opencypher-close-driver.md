# Close driver objects when you're done

Be sure to close the client when you are finished with it, so that the Bolt connections
are closed by the server and all resources associated with the connections are released.
This happens automatically if you close the driver using `driver.close()`.

If the driver is not closed properly, Neptune terminates all idle Bolt connections
after 20 minutes, or after 10 days if you are using IAM authentication.

Neptune supports no more than 1000 concurrent Bolt connections. If you don't
explicitly close connections when you're done with them, and the number of live
connections reaches that limit of 1000, any new connection attempts fail.
