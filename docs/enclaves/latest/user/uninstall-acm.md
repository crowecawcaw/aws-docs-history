# Uninstall ACM for Nitro Enclaves

If you no longer want to use [AWS Certificate Manager for Nitro Enclaves](nitro-enclave-refapp.md "nitro-enclave-refapp.md"), use the following
procedure to uninstall it.

###### To uninstall ACM for Nitro Enclaves

1. Stop the web server.
   - **NGINX**

   ```
   `$` sudo systemctl stop nginx
   ```

   - **Apache**

   ```
   `$` sudo systemctl stop httpd
   ```

2. Stop the ACM for Nitro Enclaves service.

```
`$` sudo systemctl stop nitro-enclaves-acm.service
```

3. Uninstall ACM for Nitro Enclaves.

```
`$` sudo yum remove aws-nitro-enclaves-acm
```
