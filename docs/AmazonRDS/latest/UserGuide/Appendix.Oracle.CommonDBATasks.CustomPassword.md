

# Creating custom functions to verify passwords
<a name="Appendix.Oracle.CommonDBATasks.CustomPassword"></a>

You can create a custom password verification function in the following ways:
+ To use standard verification logic, and to store your function in the `SYS` schema, use the `create_verify_function` procedure. 
+ To use custom verification logic, or to avoid storing your function in the `SYS` schema, use the `create_passthrough_verify_fcn` procedure. 