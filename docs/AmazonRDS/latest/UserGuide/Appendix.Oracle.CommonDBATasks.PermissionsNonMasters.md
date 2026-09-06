

# Granting privileges to non-master users
<a name="Appendix.Oracle.CommonDBATasks.PermissionsNonMasters"></a>

You can grant select privileges for many objects in the `SYS` schema by using the `SELECT_CATALOG_ROLE` role. The `SELECT_CATALOG_ROLE` role gives users `SELECT` privileges on data dictionary views. The following example grants the role `SELECT_CATALOG_ROLE` to a user named `user1`. 

```
GRANT SELECT_CATALOG_ROLE TO {{user1}};
```

You can grant `EXECUTE` privileges for many objects in the `SYS` schema by using the `EXECUTE_CATALOG_ROLE` role. The `EXECUTE_CATALOG_ROLE` role gives users `EXECUTE` privileges for packages and procedures in the data dictionary. The following example grants the role `EXECUTE_CATALOG_ROLE` to a user named *user1*. 

```
GRANT EXECUTE_CATALOG_ROLE TO {{user1}};
```

The following example gets the permissions that the roles `SELECT_CATALOG_ROLE` and `EXECUTE_CATALOG_ROLE` allow. 

```
  SELECT * 
    FROM ROLE_TAB_PRIVS  
   WHERE ROLE IN ('SELECT_CATALOG_ROLE','EXECUTE_CATALOG_ROLE') 
ORDER BY ROLE, TABLE_NAME ASC;
```

The following example creates a non-master user named `user1`, grants the `CREATE SESSION` privilege, and grants the `SELECT` privilege on a table named *sh.sales*.

```
CREATE USER {{user1}} IDENTIFIED BY PASSWORD;
GRANT CREATE SESSION TO {{user1}};
GRANT SELECT ON {{sh.sales}} TO {{user1}};
```