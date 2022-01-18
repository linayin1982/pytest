import smtplib
import pytest
from src.util import algo

content = "content"
smtpserver = "mail.python.org"

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

class Test_Params_Fixture:

    @pytest.fixture(scope="class", params=[0,1])
    def req_param(self, request):
        print(request.param)
        return request.param

    @pytest.fixture(scope="class")
    def my_fixture(self, req_param):
        "Call incident creation api."
        # POST request to API using req_param in request data, get data from API
        my_data = {'abc': 123, 'severity': 0} # this data is from API
        return my_data

    def test_incident_severity(self, my_fixture, req_param):
        assert my_fixture.get('severity', False) == req_param

class TestSMTPConnection:
    def test_showhelo(self,smtp_connection):
        assert 0, smtp_connection.helo()

class TestRequest:
    @pytest.mark.fixt_data(42,'say',name='hello')
    def test_fixt(self,fixt):
        assert fixt == 42

    @pytest.fixture()
    def fixt(self,request):
        marker = request.node.get_closest_marker("fixt_data")
        if marker is None:
            # Handle missing marker in some way...
            data = None
        else:
            data = marker.args[0]
            data1 = marker.args[1]
            print(data1)
            data2 = marker.kwargs
            print(data2)
            print(**[[1,2,3]])
            # Do something with the data
            return data
