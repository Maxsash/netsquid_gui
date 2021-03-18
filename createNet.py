def newNetwork(name):
    f = open(name + ".py", "w+")
    
    #imports
    f.write("from netsquid.nodes import Network\nfrom netsquid.components import QuantumProcessor, QuantumChannel, Channel\n")

    #function to create new network
    f.write("\ndef new_network():\n\tnetwork = Network(" + name + ")\n")

    #return the final network
    f.write("\n\treturn network\n")
    f.close()
