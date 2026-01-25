AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Other / Miscellaneous Utilities

This section covers various utilities programs, with miscellaneous purposes, that could not be attached to existing categories

In the following paragraphs, `PICTURE` is to be understood as the COBOL `PICTURE` keyword, used to describe fields data type and formats.

## CBL_AND/CBL_OR/CBL_XOR/CBL_EQ/CBL_IMP/CBL_NOT

### Purpose

This relates to the support of bitwise logical operations on data items, found in some COBOL dialects (Micro Focus). Please note that automatic refactor with AWS Transform handles the transformation of bitwise operators usages from Cobol MF dialect to java (see sample usages below). For the modernized code to run properly, the utility application will have to be deployed alongside.

Supported operators:

- Unary Operator:

| Unary Operator | details                      |
| -------------- | ---------------------------- |
| `CBL_NOT`      | Bitwise complement (~target) |

- Binary Operators:

| Binary Operators | details                                  |
| ---------------- | ---------------------------------------- | ------- |
| `CBL_AND`        | Bitwise AND (source & target)            |
| `CBL_OR`         | Bitwise OR (source                       | target) |
| `CBL_XOR`        | Bitwise exclusive OR (source ^ target)   |
| `CBL_EQ`         | Bitwise equivalence (~(source ^ target)) |
| `CBL_IMP`        | Bitwise implication (~source             | target) |

### Signature

Apart from CBL_NOT which has only one operand (target), all other operations have at least two operands, which are data items. The first operand is the source, the second operand is the target. An additional optional argument (length) gives the number of bytes to process (from left to right). If the length is omitted, it defaults to the minimum of source and target sizes (in bytes). The result of the operation is stored in the target. The return code of the program is 0 (unless an exception occurs).

### Checks / Errors Handling

- For each available operator, the number of required arguments is checked. If the minimal number of required argument is not met, an `IllegalArgumentException` will be thrown.
- The optional length integer argument is checked for positivity. If the provided length is negative, a message will be displayed in the logs and the operator won't be applied.

### Sample Usage

- Unary operator sample:

Here is a cobol usage of CBL_NOT:

```
   * TARGET:       00000101
   * OPERATION:     NOT
   * EXPECTED:     11111010 = 64000 dec (2nd byte unchanged - all 0)
        MOVE X'0500' to TARGET
        CALL "CBL_NOT" USING TARGET BY VALUE 1.
```

and the corresponding java modernization:

```
    /*
    TARGET:       00000101
    OPERATION:     NOT
    EXPECTED:     11111010 = 64000 dec (2nd byte unchanged - all 0) */
    ctx.getTarget().getTargetReference().setBytes(new byte[]{ 5, 0 });
    ctrl.callSubProgram("CBL_NOT", CallBuilder.newInstance()
        .byReference(ctx.getTarget().getTargetReference())
        .byValue(1)
        .getArguments(), ctx);
```

- Binary operator sample:

See for instance the following COBOL code using CBL_AND:

```
   * SOURCE:       00000011
   * OPERATION:     AND
   * TARGET:       00000101
   * EXPECTED:     00000001 = 256 dec (2nd byte unchanged - all 0)
        MOVE X'0300' to SRC
        MOVE X'0500' to TARGET
        CALL "CBL_AND" USING SRC TARGET BY VALUE 1.
```

and its java modernization:

```
    /*
    SOURCE:       00000011
    OPERATION:     AND
    TARGET:       00000101
    EXPECTED:     00000001 = 256 dec (2nd byte unchanged - all 0) */
    ctx.getSrc().getSrcReference().setBytes(new byte[]{ 3, 0 });
    ctx.getTarget().getTargetReference().setBytes(new byte[]{ 5, 0 });
    ctrl.callSubProgram("CBL_AND", CallBuilder.newInstance()
        .byReference(ctx.getSrc().getSrcReference())
        .byReference(ctx.getTarget().getTargetReference())
        .byValue(1)
        .getArguments(), ctx);
```

## CEE3ABD

### Purpose

This utility program mimics the behavior of the legacy program with the same name, whose role is to terminate a program with an Abend (abnormal end) code and an optional cleanup timing. The AWS transform engine handles the automatic modernization of calls to CEE3ABD. For the modernized code to run properly, the utility application will have to be deployed alongside.

The program stops the current run unit, using the provided abend code. An information message is printed to the logs, specifying that an user exit has been called with the given code. For now, the timing parameter is NOT taken into account, but is present as an argument for modernization compatibility reasons.

### Signature

The program accepts either 0 or 2 arguments. The two arguments are:

- The Abend code (a data item that must be interpretable as a positive integer value)
- The cleanup timing (a data item that must be interpretable as a positive integer value) -- ignored

When no arguments are provided, the following default values are being used:

- Abend code: 0
- Cleanup Timing: 0

### Checks / Errors Handling

- Checks that either 0 or 2 arguments are being provided, otherwise an `IllegalArgumentException` will be thrown.
- If two arguments are provided, check that: abend code is between 0 and 4095 (both included); timing is between 0 and 5 (both included)

Any failure to these tests will trigger an `IllegalArgumentException`.

### Sample Usage

Here is a sample usage in a COBOL program, from the Carddemo application:

```
   9999-ABEND-PROGRAM.
       DISPLAY 'ABENDING PROGRAM'
       MOVE 0 TO TIMING
       MOVE 999 TO ABCODE
       CALL 'CEE3ABD'.
```

and the corresponding modernized java code:

```
public void _9999AbendProgram(final Cbtrn03cContext ctx, final ExecutionController ctrl) {
    DisplayUtils.display(ctx, ctrl, LOGGER, "ABENDING PROGRAM");
    ctx.getTiming().setTiming(0);
    ctx.getAbcode().setAbcode(999);
    ctrl.callSubProgram("CEE3ABD", CallBuilder.newInstance()
        .getArguments(), ctx);
}
```

## CEEDATE

### Purpose

The CEEDATE utility converts a number that represents a Lilian date (days since October 15, 1582) to a character-base date representation, using a provided format.

It mimics the behaviour of the legacy system utility with the same name.

### Signature

Given its nature, the CEEDATE utility is rather intended to be called from programs.

It takes three or four arguments (last argument is optional):

- The mandatory first argument is a numeric data item whose value will be intepreted as a Lilian date
- The mandatory second argument is an alphanumeric data-item holding the `PICTURE` string used for the date to characters conversion
- The mandatory third argument is the target alphanumeric data item, holding the result of the conversion of first argument using second argument as `PICTURE`
- The fourth optional argument is a data item used to store the feedback code from the utility

### Checks / Errors Handling

- If the number of arguments passed to the utility is not three or four, a `BluageWrapperException` will be thrown
- If the provided first number argument cannot be properly evaluated as a Lilian date (out of bounds), an error message will be logged. Optional feedback code holder, if present, will be fed with a feedback code of severity 3 and message number 2512
- If an exception occurs during date conversion due to an invalid provided `PICTURE`, an error message will be logged. Optional feedback code holder, if present, will be fed with a feedback code of severity 3 and message number 2518
- If, for any reason, the conversion cannot happen properly, the output data item will be filled with blanks
- If the conversion was successfull, the optional feedback code holder will be fed with a feedback code of severity 0 (and no message)

### Sample Usage

Here is a sample call from a COBOL program (the structure for the feedback code holder FC contains ellipsis, as is contains hundreds of conditions (level 88) entries not shown here):

```
   WORKING-STORAGE SECTION.
   01  LILIANS              PIC S9(9) BINARY.
   01  TIMESTAMP-OUT               PIC X(80).
   01  MASK.
       05  MASK-LEN         PIC S9(4) BINARY.
       05  MASK-STR.
           10  MASK-CHR     PIC X OCCURS 0 TO 256
                               DEPENDING ON MASK-LEN.
   01  ROUTINE-NAMES.
       05 CEESECS-ROUTINE    PIC X(08) VALUE 'CEESECS '.
       05 CEELOCT-ROUTINE    PIC X(08) VALUE 'CEELOCT '.
       05 CEEDATE-ROUTINE    PIC X(08) VALUE 'CEEDATE '.
   01  FC.
   ...
   * lilian date for 4 June 1990
       MOVE SPACES TO MASK-STR
       MOVE 148887 TO LILIANS.
       MOVE 23                  TO MASK-LEN
       MOVE 'YYYY-MM-DD-HH:MI:SS.999' TO MASK-STR
       CALL CEEDATE-ROUTINE USING LILIANS
                                  MASK
                                  TIMESTAMP-OUT
                                  FC.
```

## CEELOCT

### Purpose

The CEELOCT utility is used to return the local date/time in three formats:

- Lilian date (the number of days since 14 October 1582)
- Lilian seconds (the number of seconds since 00:00:00 14 October 1582)
- Gregorian character string (in the form `YYYYMMDDHHMISS999`)

It mimics the behaviour of the legacy system utility with the same name.

### Signature

Given its nature, the CEELOCT utility is rather intended to be called from programs.

It takes three or four arguments (last argument is optional):

- The mandatory first argument is a data item, used to store the Lilian date
- The mandatory second argument is a data item, used to store the Lilian seconds
- The mandatory third argument is a data item, used to store the Gregorian date using the form given above
- The optional fourth argument is a data item used to store the feedback code from the utility

### Checks / Errors Handling

- If the number of arguments passed to the utility is not three or four, a `BluageWrapperException` will be thrown
- If any exception occurs during the handling of the conversion from local date/time to any of the output formats: The first and second arguments will be set to 0 and the third argument will be left unchanged; An error message will be logged; Optionally, the feedback code holder will be fed with a feedback code of severity 3 and message number 2531
- On success, all three arguments will be populated with the proper content and the optional feedback code will be fed with a code of severity 0

### Sample Usage

Here is a sample COBOL snippet showing the usage of the CEELOCT utility. The feedback code holder structure FC is not given in full as it contains hundreds of conditions (level 88) entries.

```
   WORKING-STORAGE SECTION.
   01  LILIANS              PIC S9(9) BINARY.
   01  GREGORN              PIC X(80).
   01  SECONDS              COMP-2.
   01  FC.
   ...
   01  ROUTINE-NAMES.
       05 CEESECS-ROUTINE    PIC X(08) VALUE 'CEESECS '.
       05 CEELOCT-ROUTINE    PIC X(08) VALUE 'CEELOCT '.
       05 CEEDATE-ROUTINE    PIC X(08) VALUE 'CEEDATE '.
   ...

       CALL CEELOCT-ROUTINE USING LILIANS
                                  SECONDS
                                  GREGORN
                                  FC.
```

## CEERAN0

### Purpose

The CEERAN0 program is called to generate pseudo-random numbers, between 0.0 and 1.0, using a specified seed. It is based on the multiplicative congruential method algorithm, which requires an user-specified seed. Using 0 as seed is triggering a specific mode where the seed is actually computed from the Greenwich mean time instead (at the time the program is being run). Otherwise, the seed is used as-is. The pseudo-random sequence is predictable.

### Signature

The CEERAN0 program takes three parameters:

- the seed (input parameter), a data item that can be interpreted as positive integer (0 included)
- the random number (output parameter), a data item that can be interpreted as a double precision floating number (whose value will be between 0.0 and 1.0, exclusive); it's the result of the program
- the optional feedback code (output parameter), a data item of 12 bytes, used to store the feedback from the program about the random number computation

### Checks / Errors Handling

- If the number of arguments is not 2 or 3, an `IllegalArgumentException` will be thrown
- The seed value must be between 0 and 2147483646, inclusive. If the seed value is outside of these bounds, an error message will be logged and the feedback code will be set to severity 3 and mesage number to 2524. The resulting random number will be set to -1.0 (analog to legacy behaviour)
- If the seed value is set to 0, but the system was unable to retrieve Greewich mean time (for any reason), the computation will be made using the value 1 as fallback and the feedback code will be set to severity 1 and message number to 2523. The random numbere computation will continue with the fallback seed value (analog to legacy behaviour)

### Sample Usage

This a java sample demonstrating how to use the CEERAN0 program, using all parameters including the feedback code, with bits from several layers (entity, service):

```
//Entity layer
public class Randomin extends RecordEntity {
    private final Group root = new Group(getData()).named("RANDOMIN");
    private final Elementary randomin = new Elementary(root,new BinaryIntegerType(4, true),new BigDecimal("0")).named("RANDOMIN");
    ...

public class Randomout extends RecordEntity {
    private final Group root = new Group(getData()).named("RANDOMOUT");
    private final Elementary randomout = new Elementary(root,new DoubleFloatingPointType(),new BigDecimal("0")).named("RANDOMOUT");
    ...
public class Returncode1 extends RecordEntity {
    private final Group root = new Group(getData()).named("RETURNCODE");
    private final Elementary returncode1 = new Elementary(root,new AlphanumericType(12)," ").named("RETURNCODE");
    ...

// Service layer
    CallHandler.newInstance(ctrl, ctx, ctx.getErrorContext())
        .byReference(ctx.getRandomin().getRandominReference(),
        ctx.getRandomout().getRandomoutReference(),
        ctx.getReturncode1().getReturncode1Reference())
        .call("CEERAN0");
```

## CEESECS

### Purpose

The CEESECS utility converts a timestamp string representation into Lilian seconds (the number of seconds since 00:00:00 14 October 1582).

### Signature

Given its nature, the CEESECS utility is rather intended to be called from programs.

It takes three or four arguments (last argument is optional):

- The mandatory first argument is a data item whose value will be intepreted as a timestamp
- The mandatory second argument is an alphanumeric data-item holding the `PICTURE` string used to specify how to interpret the first argument
- The mandatory third argument is the data item, holding the result of the conversion of first argument using second argument as `PICTURE`
- The fourth optional argument is a data item used to store the feedback code from the utility

### Checks / Errors Handling

- If the number of arguments passed to the utility is not three or four, a `BluageWrapperException` will be thrown
- If the timestamp passed to the utility as argument is invalid, an error message will be logged and optionally, the feedback code holder will be fed with a feedback code of severity 3 and message number 2513
- If the picture passed to the utility as argument is invalid, an error message will be logged and optionally, the feedback code holder will be fed with a feedback code of severity 3 and message number 2518
- If, for any reason, the lilian seconds output cannot be computed, the third argument (output) will be set to 0

### Sample Usage

Here is a sample call to CEESECS utility in a COBOL program:

```
   WORKING-STORAGE SECTION.
   01  SECONDS              COMP-2.
   01  TIMESTAMP-IN.
       05  TIMESTAMP-IN-LEN        PIC S9(4) BINARY.
       05  TIMESTAMP-IN-STR.
           10  TIMESTAMP-IN-CHAR   PIC X OCCURS 0 TO 256
                               DEPENDING ON TIMESTAMP-IN-LEN.
   01  MASK.
       05  MASK-LEN         PIC S9(4) BINARY.
       05  MASK-STR.
           10  MASK-CHR     PIC X OCCURS 0 TO 256
                               DEPENDING ON MASK-LEN.
   01  FC.
   ...
   01  ROUTINE-NAMES.
       05 CEESECS-ROUTINE    PIC X(08) VALUE 'CEESECS '.
       05 CEELOCT-ROUTINE    PIC X(08) VALUE 'CEELOCT '.
       05 CEEDATE-ROUTINE    PIC X(08) VALUE 'CEEDATE '.
   ...
   ...
   * date for lilian second 12,799,191,601.123
       MOVE '1988-5-16-19:00:01.123' TO TIMESTAMP-IN-STR
       MOVE 23                  TO MASK-LEN
       MOVE 'YYYY-MM-DD-HH:MI:SS.999' TO MASK-STR
       CALL CEESECS-ROUTINE USING TIMESTAMP-IN
                                  MASK
                                  SECONDS
                                  FC.
```

## ILBOABN0

### Purpose

The purpose of the ILBOABN0 program is to interrupt the current run unit in a controlled way, using an user-provided abend (abnormal end) code. Often used in error handling dedicated programs.

The interruption of the current run unit occurs by throwing a `StopRunUnitException`.

### Signature

The ILBOABN0 program takes a single mandatory argument which is a data item containing the abend code (that has to be interpretable as an integer).

### Checks / Errors Handling

While throwing the `StopRunUnitException` to interrupt the current run unit run, the program will set the return code to the value provided as first argument. In addition, an information message will be logged.

### Sample Usage

Here is a java sample usage of the ILBOABN0 program, resulting from a COBOL modernization through AWS transform:

```
   77  WS-ABND-CODE          COMP   PIC S9(4)      VALUE +1234.
...
...

   1970-ABNDIT.
       CALL 'ILBOABN0' USING WS-ABND-CODE.
```

and the matching java modernization:

```
//Entity layer
private final Group root = new Group(getData());
private final Elementary wsAbndCode = new Elementary(root,new BinaryType(4, 0, "STD", false, false, true),Short.valueOf("1234"));
...

//Service layer
@Override
public void _1970Abndit(final MyPgmContext ctx, final ExecutionController ctrl) {
   ctrl.callSubProgram("ILBOABN0", CallBuilder.newInstance()
       .byReference(ctx.getWsAbndCode().getWsAbndCodeReference())
       .getArguments(), ctx);
```
