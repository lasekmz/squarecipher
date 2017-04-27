import pytest

from squarecipher import normalize, row_length, divide_rows, maker, join

def test_can_normalize_some_text():
	assert normalize("A sentence without spaces.") == normalize("asentencewithoutspaces")
	assert normalize("Egad! Watson, t'is this; no punctuation?...") == normalize("egadwatsontisthisnopunctuation")

def test_to_determine_how_many_characters_are_in_a_row():
	assert row_length("isaperfectsquare") == 4
	assert row_length("asentencewithoutspaces") == 5

def test_to_divide_string_into_rows():
	assert divide_rows("asentencewithoutspaces") == ["asent","encew","ithou","tspac","es"]
	assert divide_rows("egadwatsontisthisnopunctuation") == ["egadwa","tsonti","sthisn","opunct","uation"]

def test_make_new_words():
	assert maker(["asent","encew","ithou","tspac","es"]) == ["aeite","sntss","echp","neoa","twuc"] 
	assert maker(["egadwa","tsonti","sthisn","opunct","uation"]) == ["etsou","gstpa","aohut","dnini","wtsco","aintn"]

def test_can_join_together_encrpted_words():
	assert join(["aeite","sntss","echp","neoa","twuc"]) == ("aeite sntss echp neoa twuc")
	assert join(["etsou","gstpa","aohut","dnini","wtsco","aintn"]) == ("etsou gstpa aohut dnini wtsco aintn") 
