# Run a package manager and other tools in a

proxy server

Use the following procedures to run a package manager and other tools in a proxy server.

###### To run a tool, such as a package manager, in a proxy server

1. Add the tool to the allow list in your proxy server by adding statements to
   your `squid.conf` file.
2. Add a line to your buildspec file that points to the private endpoint of your
   proxy server.
   The following examples demonstrate how to do this for `apt-get`,
   `curl`, and `maven`. If you use a different tool, the same
   principles apply. Add it to an allow list in the `squid.conf` file
   and add a command to your buildspec file to make CodeBuild aware of your proxy server's
   endpoint.

###### To run `apt-get` in a proxy server

1. Add the following statements to your `squid.conf` file to
   add `apt-get` to an allow list in your proxy server. The first three
   lines allow `apt-get` to run in the build environment.

```
acl allowed_sites dstdomain ppa.launchpad.net # Required for apt-get to run in the build environment
acl apt_get dstdom_regex .*\.launchpad.net # Required for CodeBuild to run apt-get in the build environment
acl apt_get dstdom_regex .*\.ubuntu.com    # Required for CodeBuild to run apt-get in the build environment
http_access allow localnet allowed_sites
http_access allow localnet apt_get
```

2. Add the following statement in your buildspec file so that
   `apt-get` commands look for the proxy configuration in
   `/etc/apt/apt.conf.d/00proxy`.

```
echo 'Acquire::http::Proxy "http://`<private-ip-of-proxy-server>`:3128"; Acquire::https::Proxy "http://`<private-ip-of-proxy-server>`:3128"; Acquire::ftp::Proxy "http://`<private-ip-of-proxy-server>`:3128";' > /etc/apt/apt.conf.d/00proxy
```

###### To run `curl` in a proxy server

1. Add the following to your `squid.conf` file to add
   `curl` to an allow list in your build environment.

```
acl allowed_sites dstdomain ppa.launchpad.net # Required to run apt-get in the build environment
acl allowed_sites dstdomain google.com # Required for access to a webiste. This example uses www.google.com.
http_access allow localnet allowed_sites
http_access allow localnet apt_get

```

2. Add the following statement in your buildspec file so `curl` uses
   the private proxy server to access the website you added to the
   `squid.conf`. In this example, the website is
   `google.com`.

```
curl -x `<private-ip-of-proxy-server>`:3128 https://www.google.com
```

###### To run `maven` in a proxy server

1. Add the following to your `squid.conf` file to add
   `maven` to an allow list in your build environment.

```
acl allowed_sites dstdomain ppa.launchpad.net # Required to run apt-get in the build environment
acl maven dstdom_regex .*\.maven.org # Allows access to the maven repository in the build environment
http_access allow localnet allowed_sites
http_access allow localnet maven
```

2. Add the following statement to your buildspec file.

```
maven clean install -DproxySet=true -DproxyHost=`<private-ip-of-proxy-server>` -DproxyPort=3128
```
