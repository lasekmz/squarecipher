import pytest

from squarecipher import normalize, row_length, divide_rows

def test_can_normalize_some_text():
	assert normalize("A sentence without spaces.") == normalize("asentencewithoutspaces")
	assert normalize("Egad! Watson, t'is this; no punctuation?...") == normalize("egadwatsontisthisnopunctuation")

def test_to_determine_how_many_characters_are_in_a_row():
	assert row_length("isaperfectsquare") == 4
	assert row_length("asentencewithoutspaces") == 5

def test_to_divide_string_into_rows():
	assert divide_rows("asentencewithoutspaces") == ["asent","encew","ithou","tspac","es"]
	assert divide_rows("egadwatsontisthisnopunctuation") == ["egadwa","tsonti","sthisn","opunct","uation"]

