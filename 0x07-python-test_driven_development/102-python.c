#include <Python.h>

void print_python_string(PyObject *p)
{
    PyUnicodeObject *string = (PyUnicodeObject *)p;
    Py_ssize_t length;
    Py_UCS4 *value;
    Py_UCS4 max_ucs4 = 0;
    int is_ascii = 1;
    int i;

    if (!PyUnicode_Check(string))
    {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(string);
    value = PyUnicode_AsUCS4Copy(string);
    if (!value)
    {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }

    for (i = 0; i < length; i++)
    {
        if (value[i] >= 128)
        {
            is_ascii = 0;
            break;
        }
        if (value[i] > max_ucs4)
            max_ucs4 = value[i];
    }

    fprintf(stderr, "[.] string object info\n");
    fprintf(stderr, "  type: %s\n", is_ascii ? "compact ascii" : "compact unicode object");
    fprintf(stderr, "  length: %ld\n", length);
    fprintf(stderr, "  value: %ls\n", (wchar_t *)value);

    free(value);
}
