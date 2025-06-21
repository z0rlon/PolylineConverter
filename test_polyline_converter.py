import polyline_converter as pc


def test_convert_vectors_basic():
    vectors = [(1,1,1),(1,5,1),(5,5,5)]
    params = (10,10,10)
    thresholds = (5,5,2)
    names = ("Param1","Param2","Param3")
    result = pc.convert_vectors(vectors, params, thresholds, names)
    assert result == "(1,1,1),(1,Param2 - 5,1),(Param1 - 5,Param2 - 5,Param3 - 5)"
