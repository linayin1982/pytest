import pytest
from src.util import algo

content = "content"

@pytest.mark.skip
class TestFixture:
    @pytest.fixture
    def data(self):
        return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]

    def test_sel_sort(self,data):
        sorted_vals = algo.sel_sort(data)
        assert sorted_vals == sorted(data)

    @pytest.mark.parametrize("word,expected", [('kayak', True), ('civic', True), ('forest', False)])
    def test_is_palindrome(self,word, expected):
        assert expected == algo.is_palindrome(word)

@pytest.mark.must
class TestFixtureMust:
    def test_needsfiles(self,tmpdir):
        d = tmpdir/"sub"
        d.mkdir()
        f = d/"hello.txt"
        # f = tmpdir.mkdir("sub".join("hello.txt"))
        f.write_text(content,encoding='utf-8')
        assert f.read_text(encoding='utf-8') == content



