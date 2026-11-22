

# Starting extenddb-dev

Running `extenddb-dev` requires Docker, or another container runtime that can run images from Docker Hub.

Run the following command to start `extenddb-dev` with a file-backed database. Data persists across container restarts.

```
docker run -d -p 127.0.0.1:18080:18080 -v extenddb:/var/lib/extenddb extenddb/extenddb-dev
```

In the preceding command:

`-p 127.0.0.1:18080:18080`  
Publishes container port 18080 on the host loopback address.

`-v extenddb:/var/lib/extenddb`  
Uses `extenddb`, the named Docker volume that holds the database.

`extenddb/extenddb-dev`  
The image that the container runs.

With `extenddb-dev`, you connect over plain HTTP on port 18080. Publish the port on the loopback address, as shown in the preceding command.

**Important**  
If you publish the port with a bare `-p 18080:18080`, you publish it on every network interface of the host. Then anyone who can reach the host can read, change, and delete every table, because `extenddb-dev` enforces no access control.

For a database that disappears when the container stops, use the in-memory mode. This option suits test suites that need a clean database on each run.

```
docker run -d -p 127.0.0.1:18080:18080 -e EXTENDDB__STORAGE__SQLITE__PATH=:memory: extenddb/extenddb-dev
```

The `extenddb-dev` image includes a Docker health check. In Docker Compose, a test service can wait for it with `depends_on` and `condition: service_healthy`.