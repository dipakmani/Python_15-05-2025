# Let's create examples of all major data types in Python with outputs

# 1. Numeric types: int, float, complex
numeric_examples = {
    "int": [10, -5, 0, 999, 1234567890, 42, -100, 1, 7, 200],
    "float": [10.5, -3.14, 0.0, 999.99, 1e3, -0.001, 3.14159, 2.0, 100.1, 5.5],
    "complex": [1+2j, -3+4j, 0+0j, 5-2j, 2+0j, -1-1j, 3.14+2.71j, 0+1j, 1j, -1j]
}

# 2. Sequence types: str, list, tuple
sequence_examples = {
    "str": ["Hello", "Python", "", "123", "abc123", " ", "New\nLine", "Tab\tCharacter", "😀", "Hello World!"],
    "list": [[1, 2], [], [1, 2, 3], ["a", "b"], [10], list("abc"), [None], [1.1, 2.2], [True, False], [1, "a", 3.0]],
    "tuple": [(1,), (), (1, 2, 3), ("a",), (1, "b"), tuple("xyz"), (None,), (1.1,), (True, False), (3, "a", 7.8)]
}

# 3. Set types: set, frozenset
set_examples = {
    "set": [{1, 2, 3}, set(), {10}, {"a", "b"}, {1, 1, 2}, set("abc"), {True, False}, {1.1, 2.2}, {None}, {1, "a", 2.5}],
    "frozenset": [frozenset({1, 2}), frozenset(), frozenset({10}), frozenset("abc"), frozenset({None}),
                  frozenset({1.1, 2.2}), frozenset({"a", "b"}), frozenset([1, "a"]), frozenset({True, False}), frozenset("123")]
}

# 4. Mapping type: dict
dict_examples = [
    {"a": 1}, {}, {"x": 10, "y": 20}, {1: "one", 2: "two"}, {"name": "Alice", "age": 25},
    dict(a=1, b=2), {"key": None}, {None: "value"}, {"float": 1.1}, {"mixed": [1, 2, 3]}
]

# 5. Boolean type: bool
bool_examples = [True, False, bool(1), bool(0), bool([]), bool([1]), bool(""), bool("Text"), bool(None), bool(3.14)]

# 6. Binary types: bytes, bytearray, memoryview
binary_examples = {
    "bytes": [b"Hello", bytes(5), b"", bytes([65, 66]), b"123", b"\x00\x01", bytes("abc", "utf-8"), b"A", b"Z", b"\xff"],
    "bytearray": [bytearray(5), bytearray(b"Hello"), bytearray(), bytearray([1, 2]), bytearray(b"123"), 
                  bytearray("abc", "utf-8"), bytearray([0, 255]), bytearray(b"A"), bytearray(b"Z"), bytearray(b"\xff")],
    "memoryview": [memoryview(b"abc"), memoryview(bytes(3)), memoryview(bytearray(b"123")), memoryview(b"XYZ"),
                   memoryview(bytearray(b"test")), memoryview(b"\x00\x01"), memoryview(bytes([65, 66])),
                   memoryview(b"A"), memoryview(b"\xff"), memoryview(b"0")]
}

output = {
    "Numeric": numeric_examples,
    "Sequence": sequence_examples,
    "Set": set_examples,
    "Dict": dict_examples,
    "Boolean": bool_examples,
    "Binary": binary_examples
}

output
