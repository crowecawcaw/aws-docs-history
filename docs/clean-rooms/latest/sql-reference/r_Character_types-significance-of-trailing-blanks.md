# Significance of

trailing blanks

Both CHAR and VARCHAR data types store strings up to _n_ bytes in
length. An attempt to store a longer string into a column of these types results in an
error. However, if the extra characters are all spaces (blanks), the string is truncated
to the maximum length. If the string is shorter than the maximum length, CHAR values are
padded with blanks, but VARCHAR values store the string without blanks.

Trailing blanks in CHAR values are always semantically insignificant. They are
disregarded when you compare two CHAR values, not included in LENGTH calculations, and
removed when you convert a CHAR value to another string type.

Trailing spaces in VARCHAR and CHAR values are treated as semantically insignificant
when values are compared.

Length calculations return the length of VARCHAR character strings with trailing
spaces included in the length. Trailing blanks are not counted in the length for
fixed-length character strings.
