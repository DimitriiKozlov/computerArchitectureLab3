from mock import patch
import unittest
from pysimplesoap.client import SoapClient



class TestLab3(unittest.TestCase):

    def test_client(self):
        global client
        client = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/', # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=True,
            ns=False)


    @patch("operations.create")
    def test_create(self, mock_create):
        mock_create.return_value = '<Node>New doc created</Node>'
        #print mock_create.return_value
        resp = client.Create(name="123m1", surname="123n2")
        print resp.Node
        mock_create.return_value = resp.Node


    @patch("operations.read")
    def test_create(self, mock_read):
        #print mock_create.return_value
        resp = client.Read()
        print resp.Node
        mock_read.return_value = resp.Node




    @patch("operations.update")
    def test_update(self, mock_update):
        #print mock_create.return_value
        resp = client.Create(name="123m1", surname="123n2")
        print resp.Node
        mock_update.return_value = resp.Node



    @patch("operations.delete")
    def test_create(self, mock_delete):
        mock_delete.return_value = '<Node>doc deleted</Node>'
        #print mock_create.return_value
        resp = client.Create(name="123m1", surname="123n2")
        print resp.Node
        mock_delete.return_value = resp.Node
