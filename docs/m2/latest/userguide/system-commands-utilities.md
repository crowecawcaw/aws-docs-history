AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Commands Utilities

This section is related to utility programs whose role is to handle user commands, provided using control cards.

## IKJEFT1A/IKJEFT1B/KEQEFT01/IKJEFT01/DSNDBTCH

### IKJEFT1A Purpose

IKJEFT1A and its aliases execute TSO (**T**ime **S**haring **O**ption) commands in batch jobs without requiring an interactive TSO session, bridging non-interactive batch and interactive TSO environments.

Mimics legacy IKJEFT1A behavior with environment-specific differences: for instance, DB2 TERM(inate) commands are ignored on modern environments (logged as informational).

###### Note

Command syntax not detailed here - IKJEFT1A uses legacy command datasets unchanged. Please refer to legacy platform documentation for TSO command details.

### IKJEFT1A Signature

Uses `SYSTSIN` dataset for command input (defined via JCL `DD` directive). Modernized version uses the same dataset unchanged. Invoked only in modernized Groovy jobs scripts.

### IKJEFT1A related configuration parameters

The behaviour of the utility is influenced by the following configuration parameter:

- `systin.encoding`

Please see [Available properties for optional web
applications](ba-runtime-key-value.md#ba-runtime-key-value-web "ba-runtime-key-value.md#ba-runtime-key-value-web") for details about configuring this parameter.

### IKJEFT1A Checks/Error handling

When an unsupported command is present in the SYSTSIN dataset then a `RuntimeException` is thrown.

### IKJEFT1A Sample usages

The legacy JCL script (which uses an inlined content of the `SYSTSIN` dataset, using `DD *` directive)

```
//*********************************************************************
//* READ THE TEMPORARY INPUT FILE                                     *
//*********************************************************************
// IF IDCM00032.RC = 1 THEN
//067FILEKEY  EXEC PGM=IKJEFT01,DYNAMNBR=20
//SYSTSIN   DD *
 DSN SYSTEM(DB2P)
 RUN  PROGRAM(067-fileKey) PLAN(FILEKEYPLAN)    PARM('RT')
 END
/*
//TEMPVSAM  DD DSN=IDXVIDEO.TEMPVSAM,DISP=SHR
//FKOUT     DD DSN=output(out067.txt),DISP=(NEW,CATLG)
// ENDIF
//*********************************************************************
```

and the matching modernized script (in groovy) -- the inlined content of `SYSTSIN` dataset is represented by a "stream" --

```
// STEP 067FILEKEY - PGM - IKJEFT01***********************************************
def step067FILEKEY(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("067FILEKEY", "IKJEFT01", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .fileSystem("SYSTSIN")
                        .stream(
""" DSN SYSTEM(DB2P)
 RUN  PROGRAM(067-fileKey) PLAN(FILEKEYPLAN)    PARM('RT')
 END
""", getEncoding())
                        .build()
                        .bluesam("TEMPVSAM")
                        .dataset("IDXVIDEO.TEMPVSAM")
                        .disposition("SHR")
                        .build()
                        .fileSystem("FKOUT")
                        .path("output(out067.txt)")
                        .disposition("NEW")
                        .normalTermination("CATLG")
                        .build()
                        .getFileConfigurations())
                    .withParameters(params)
                    .runProgram("IKJEFT01")
                })
        }
    }
}
```

## QCMDEXC

### QCMDEXC Purpose

This utility program emulates the behaviour of the AS/400 system utility QCMDEXC, used to run system commands in a dynamic way at runtime.

Features:

- Parses and executes commands dynamically.
- Supports named and positional parameter formats.

### QCMDEXC Signature

Accepts 1-2 parameters:

- First: Alphanumeric data containing commands to execute
- Second (optional): length in bytes to read from first parameter (defaults to full length)

### QCMDEXC Checks/Error handling

For the following cases, a `RuntimeException` will be thrown:

- When the number of provided arguments is not one or two;
- If the commands argument is empty or if the command to be run is unrecognized;
- If the command run fails for any reason; in addition, the return code from the program will be set to 1.

### QCMDEXC Sample usages

Here is a sample usage from a legacy COBOL program: the data item `CL-COMMANDX` is fitted with commands before being used as argument for the QCMDEXC program call:

```
       INITIALIZE CL-COMMANDX.

       STRING
           "CPYF FROMFILE(PLAYERS) TOFILE(" DELIMITED BY SIZE,
           "NEWFILE"                      DELIMITED BY SIZE,
           ") MBROPT(*REPLACE) FMTOPT(*NOCHK) CRTFILE(*YES)"
                                          DELIMITED BY SIZE
           INTO CL-COMMANDX
       END-STRING.

       CALL "QCMDEXC"                  USING CL-COMMANDX
                                             CLENGTHX.
```

Once modernized into java code, this becomes:

```
    DataUtils.initialize(ctx.getClCommandx().getClCommandxReference());
    StringConcatenationBuilder.newInstance(ctx.getClCommandx().getClCommandxReference())
        .addDelimitedBySize("CPYF FROMFILE(PLAYERS) TOFILE(")
        .addDelimitedBySize("NEWFILE")
        .addDelimitedBySize(") MBROPT(*REPLACE) FMTOPT(*NOCHK) CRTFILE(*YES)")
        .end();
    ctrl.callSubProgram("QCMDEXC", CallBuilder.newInstance()
        .byReference(ctx.getClCommandx().getClCommandxReference())
        .byReference(ctx.getClengthx().getClengthxReference())
        .getArguments(), ctx);
```

Please note that legacy commands contents are being used "as-is" in the modernized code, without any modification.
