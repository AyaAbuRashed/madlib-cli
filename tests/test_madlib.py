from madlib_cli.madlib_cli import read_template
from madlib_cli.madlib_cli import read_template2
from madlib_cli.madlib_cli import parse
from madlib_cli.madlib_cli import merge


def test_read_empty():
    actual = read_template2("./files/empty.txt")
    expected = ""
    assert actual == expected

def test_parse_with_placeholders():
    actual1, actual2 = parse("Hello  this is {Name}, I am {Age} years old.")
    expected1, expected2 = "Hello  this is $, I am $ years old.", ["Name", "Age"]
    assert actual1 == expected1 and actual2 == expected2

def test_merge_with_placeholders():
    actual = merge("Hello  this is $, I am $ years old", ["Aya", "22"])
    expected = "Hello  this is Aya, I am 22 years old"
    assert actual == expected 