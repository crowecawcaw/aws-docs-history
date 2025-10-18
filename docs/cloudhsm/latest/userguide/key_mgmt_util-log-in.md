# Log in to the HSMs in an AWS CloudHSM cluster using KMU

Use the **loginHSM** command in key\_mgmt\_util (KMU) to log in to the
 hardware security modules (HSM) in an AWS CloudHSM cluster. The following command logs in as a [crypto user (CU)](understanding-users-cmu.md "understanding-users-cmu.md") named
 `example_user`. The output indicates a successful login for all
 three HSMs in the cluster. 


```
`Command:` `loginHSM -u CU -s example_user -p `<PASSWORD>```Cfm3LoginHSM returned: 0x00 : HSM Return: SUCCESS

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS`

```
The following shows the syntax for the **loginHSM** command.


```
`Command:` `loginHSM -u `<USER TYPE>` -s `<USERNAME>` -p `<PASSWORD>``
```
