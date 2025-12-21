# Oracle Application Express (APEX)

Amazon RDS supports Oracle Application Express (APEX) through the use of the `APEX`
and `APEX-DEV` options. You can deploy Oracle APEX as a runtime environment or as
a full development environment for web-based applications. Using Oracle APEX, you can build
applications entirely within the web browser. For more information, see [Oracle application Express](https://apex.oracle.com/ "https://apex.oracle.com/") in the Oracle
documentation.

###### Topics

- [Oracle APEX components](#Appendix.Oracle.Options.APEX.components "#Appendix.Oracle.Options.APEX.components")
- [Requirements and
  limitations](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md")
- [Setting up Oracle APEX and
  Oracle Rest Data Services (ORDS)](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md")
- [Configuring Oracle Rest Data Services (ORDS)](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md")
- [Upgrading and removing
  Oracle APEX](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md")

## Oracle APEX components

Oracle APEX consists of the following main components:

- A _repository_ that stores the metadata for Oracle APEX
  applications and components. The repository consists of tables, indexes, and
  other objects that are installed in your Amazon RDS DB instance.
- A _listener_ that manages HTTP communications with Oracle
  APEX clients. The listener resides on a separate host such as an Amazon EC2 instance,
  an on-premises server at your company, or your desktop computer. The listener
  accepts incoming connections from web browsers, forwards them to the Amazon RDS DB instance
  for processing, and then sends results from the repository back to the browsers.

RDS for Oracle supports the following types of listeners:

    + For Oracle APEX version 5.0 and later, use Oracle REST Data Services
     (ORDS) version 19.1 and higher. We recommend that you use the latest
     supported version of Oracle APEX and ORDS. This documentation describes
     older versions for backwards compatibility only.
    + For Oracle APEX version 4.1.1, you can use Oracle APEX Listener
     version 1.1.4.
    + You can use Oracle HTTP Server and `mod_plsql` listeners.


    ###### Note

    Amazon RDS doesn't support the Oracle XML DB HTTP server with the
     embedded PL/SQL gateway as a listener for Oracle APEX. In general,
     Oracle recommends against using the embedded PL/SQL gateway for
     applications that run on the internet.

For more information about these listener types, see [About
choosing a web listener](https://docs.oracle.com/database/apex-5.1/HTMIG/choosing-web-listener.htm#HTMIG29321 "https://docs.oracle.com/database/apex-5.1/HTMIG/choosing-web-listener.htm#HTMIG29321") in the Oracle documentation.

When you add the `APEX` and `APEX-DEV` options to your RDS for Oracle
DB instance, Amazon RDS installs the Oracle APEX repository only. Install your listener on a
separate host.
