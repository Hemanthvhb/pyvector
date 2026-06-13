from kdtree import build, search, insert

def builder():
    data = [
            ([1, 2], "cat"),
            ([3, 4], "dog"),
            ([5, 1], "bird"),
        ]
    return build(data)

def test_search():
    root=builder()
    result=search(root,[1,1])
    assert result[1] == "cat"

def test_insert():
    root=builder()
    root=insert(root,[9,9],"tiger")
    result=search(root,[9,8])
    assert result[1]=="tiger"

def test_mt_search():
    result=search(None,[1,2])
    assert result is None