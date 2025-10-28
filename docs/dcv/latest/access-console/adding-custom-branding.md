# Adding your custom branding

To customize the Amazon DCV Access Console with your organizational branding, you need to update the following with your preferred configurations:

- Authentication Server
- Web Client

## Updating customization on the Authentication Server

1. Connect to the host on which you are running the Authentication Server.
2. Create a backup directory and copy the files that will be changed.

```
`$` mkdir custom_branding_bkp
```

```
`$` sudo cp /opt/aws/dcv-access-console-auth-server/dcv-access-console-auth-server-*.jar custom_branding_bkp/
```

3. Create a working directory.

```
`$` mkdir custom_branding
```

```
`$` cd custom_branding
```

4. Copy the Authentication Server.

```
`$` sudo cp /opt/aws/dcv-access-console-auth-server/dcv-access-console-auth-server-*.jar .
```

5. Unzip the relevant files.

```
`$` unzip dcv-access-console-auth-server-*.jar BOOT-INF/classes/static/_next/static/chunks/app/login/*.js
```

```
`$` unzip dcv-access-console-auth-server-*.jar BOOT-INF/classes/static/service-name.svg
```

```
`$` unzip dcv-access-console-auth-server-*.jar BOOT-INF/classes/static/favicon.ico
```

```
`$` unzip dcv-access-console-auth-server-*.jar BOOT-INF/classes/static/login-background.svg
```

6. Replace the existing images file paths with paths to your new custom **organization logo**
   , **favicon**, and **login background images**.

```
`$` sudo cp `path-to-new-favicon.ico` BOOT-INF/classes/static/favicon.ico
```

```
`$` sudo cp `path-to-new-service-name.svg` BOOT-INF/classes/static/service-name.svg
```

```
`$` sudo cp `path-to-new-login-background.svg` BOOT-INF/classes/static/login-background.svg
```

7. Update the **alternative text** for the organization logo.

```
`$` OLD_ALT="Access Console"
```

```
`$` NEW_ALT="My new logo alt text"
```

```
`$` sudo sed -i "s/alt:\"$OLD_ALT\"/alt:\"$NEW_ALT\"/g" BOOT-INF/classes/static/_next/static/chunks/app/login/page-*.js
```

8. Update the **login message** on the login screen.

```
`$` OLD_TAGLINE="Manage and connect to your Amazon DCV sessions."
```

```
`$` NEW_TAGLINE="My new tag line"
```

```
`$` sudo sed -i "s/tagline:\"$OLD_TAGLINE\"/tagline:\"$NEW_TAGLINE\"/g" BOOT-INF/classes/static/_next/static/chunks/app/login/page-*.js
```

9. Replace the files in the jar.

```
`$` zip -ur dcv-access-console-auth-server-*.jar BOOT-INF/
```

10. Copy the new jar.

```
`$` sudo cp dcv-access-console-auth-server-*.jar /opt/aws/dcv-access-console-auth-server/
```

11. Reload the daemon and restart the authorization server.

```
`$` sudo systemctl daemon-reload  sudo systemctl restart dcv-access-console-auth-server
```

## Updating customization on the Web Client

1. Connect to the host on which you are running the Web Client.
2. Create a backup directory and copy the files that will be changed.

```
`$` mkdir custom_branding_bkp
```

```
`$` sudo cp -r /opt/aws/dcv-access-console-webclient custom_branding_bkp/
```

3. Replace the existing images file paths with paths to your new custom **organization logo**
   , **favicon**, and **login background images** (the login background image is used
   on the Web Client for error messages).

```
`$` sudo cp `path-to-new-service-name.svg` /opt/aws/dcv-access-console-webclient/public/service-name.svg
```

```
`$` sudo cp `path-to-new-favicon.ico.body`/opt/aws/dcv-access-console-webclient/.next/server/app/favicon.ico.body
```

```
`$` sudo cp `path-to-new-login-background.svg`/opt/aws/dcv-access-console-webclient/public/login-background.svg
```

4. Update the **alternative text** for the organization logo.

```
`$` OLD_ALT="Access Console"
```

```
`$` NEW_ALT="My new logo alt text"
```

```
`$` grep -rl "alt:\"$OLD_ALT\"" /opt/aws/dcv-access-console-webclient/.next/ | xargs sed -i "s/alt:\"$OLD_ALT\"/alt:\"$NEW_ALT\"/g"
```

5. Replace the **Documentation** URL.

```
`$` OLD_DOC_LINK="https:\/\/docs.aws.amazon.com\/dcv\/latest\/sm-admin\/what-is-sm.html"
```

```
`$` NEW_DOC_LINK="https:\/\/example.com"
```

```
`$` grep -rl $OLD_DOC_LINK /opt/aws/dcv-access-console-webclient/.next/ | xargs sed -i "s/$OLD_DOC_LINK/$NEW_DOC_LINK/g"
```

6. Replace the **Downloads** URL.

```
`$` OLD_DOWNLOADS_LINK="https:\/\/download.nice-dcv.com\/"
```

```
`$` NEW_DOWNLOADS_LINK="https:\/\/example.com"
```

```
`$` grep -rl $OLD_DOWNLOADS_LINK /opt/aws/dcv-access-console-webclient/.next/ | xargs sed -i "s/$OLD_DOWNLOADS_LINK/$NEW_DOWNLOADS_LINK/g"
```
