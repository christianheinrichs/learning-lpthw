According to the official [Python documentation](https://docs.python.org/2/library/stdtypes.html#string-formatting-operations),
the Python format characters are:

<table>
    <tr>
        <td>
            'd'
        </td>
        <td>
            Signed integer decimal.
        </td>
    </tr>
    <tr>
        <td>
            'i'
        </td>
        <td>
            Signed integer decimal.
        </td>
    </tr>
    <tr>
        <td>
            'o'
        </td>
        <td>
            Signed octal value.
        </td>
    </tr>
    <tr>
        <td>
            'u'
        </td>
        <td>
            Obsolete type - it is identical to 'd'.
        </td>
    </tr>
    <tr>
        <td>
            'x'
        </td>
        <td>
            Signed hexadecimal (lowercase).
        </td>
    </tr>
    <tr>
        <td>
            'X'
        </td>
        <td>
            Signed hexadecimal (uppercase).
        </td>
    </tr>
    <tr>
        <td>
            'e'
        </td>
        <td>
            Floating point exponential format (lowercase).
        </td>
    </tr>
    <tr>
        <td>
            'E'
        </td>
        <td>
            Floating point exponential format (uppercase).
        </td>
    </tr>
    <tr>
        <td>
            'f'
        </td>
        <td>
            Floating point decimal format.
        </td>
    </tr>
    <tr>
        <td>
            'F'
        </td>
        <td>
            Floating point decimal format.
        </td>
    </tr>
    <tr>
        <td>
            'g'
        </td>
        <td>
            Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
        </td>
    </tr>
    <tr>
        <td>
            'G'
        </td>
        <td>
            Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
        </td>
    </tr>
    <tr>
        <td>
            'c'
        </td>
        <td>
            Single character (accepts integer or single character string).
        </td>
    </tr>
    <tr>
        <td>
            'r'
        </td>
        <td>
            String (converts any Python object using [repr()](https://docs.python.org/2/library/functions.html#func-repr)).
        </td>
    </tr>
    <tr>
        <td>
            's'
        </td>
        <td>
            String (converts any Python object using [str()](https://docs.python.org/2/library/functions.html#str)).
        </td>
    </tr>
    <tr>
        <td>
            '%'
        </td>
        <td>
            No argument is converted, results in a '%' character in the result.
        </td>
    </tr>
</table>

Source: https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
