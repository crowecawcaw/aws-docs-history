# Configuring public key authentication

To enable SSH public key authentication, you must first generate an SSH key and
associate it with an administrator account by using the `security login publickey
 create` command. This allows the account to access the SVM. The `security
 login publickey create` command accepts the following parameters.

| Parameter             | Description                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-vserver` (Optional) | The name of the SVM that the account accesses. If you are configuring SSH public key authentication<br>for file system users, don't include `-versver`.                                                                          |
| `-username`           | The username of the account. The default value,<br>`admin`, is the default name of the cluster<br>administrator.                                                                                                                 |
| `-index`              | The index number of the public key. The default value is 0 if the<br>key is the first key that's created for the account. Otherwise, the<br>default value is one more than the highest existing index number for<br>the account. |
| `-publickey`          | The OpenSSH public key. Enclose the key in double quotation<br>marks.                                                                                                                                                            |
| `-role`               | The access control role that's assigned to the account.                                                                                                                                                                          |
| `-comment` (Optional) | Descriptive text for the public key. Enclose the text in double<br>quotation marks.                                                                                                                                              |

The following example associates a public key with the SVM administrator account
`svmadmin` for the SVM `svm01`. The public key is assigned
index number `5`.

```
`Fsx0123456::>` `security login publickey create -vserver `svm01` -username `svmadmin` -index `5` -publickey `"ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAspH64CYbUsDQCdW22JnK6J/vU9upnKzd2zAk9C1f7YaWRUAFNs2Qe5lUmQ3ldi8AD0Vfbr5T6HZPCixNAIzaFciDy7hgnmdj9eNGedGr/JNrftQbLD1hZybX+72DpQB0tYWBhe6eDJ1oPLobZBGfMlPXh8VjeU44i7W4+s0hG0E=tsmith@publickey.example.com"``
```

###### Important

You must be an SVM or file system administrator to perform this task.
