import pysimplesoap.client

"Contributed modules"
import pysimplesoap.client
import pysimplesoap.server
import pysimplesoap.simplexml
import pysimplesoap.client
import pysimplesoap.transport

# create a simple consumer
client = pysimplesoap.client.SoapClient(
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="http://example.com/sample.wsdl",
    soap_ns='soap',
    # trace=True,
    ns=False)

while True:
    print('1. Create new info')
    print('2. Read  info by id')
    print('3. Update node by name')
    print('4. Delete')
    print('5. Read all items')
    print('6. break ')
    option = raw_input()

    if option == '1':
        name = raw_input("Enter name: ")
        surname = raw_input("Enter surname: ")
        response = client.Create(name=name, surname=surname)
        result = response.Node
        print(result)

    if option == '2':
        id = raw_input("Enter id name: ")
        response = client.Read(st_id=int(id))
        result = response.Node
        print(result)

    if option == '3':
        id = raw_input("Enter id name: ")
        name = raw_input("New name: ")
        surname = raw_input("New surname: ")
        response = client.Update(st_id=int(id), name=name, surname=surname)
        result = response.Node
        print(result)

    if option == '4':
        id = raw_input("Enter id name: ")
        response = client.Delete(st_id=int(id))
        result = response.Node

    if option == '5':
        response = client.Read_all()
        result = response.Node
        for rs in result:
            print(rs)

    if option == '6':
        break