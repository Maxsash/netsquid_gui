import os

def newNetwork(name):
    new_dir = './networks'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    f = open(os.path.join(new_dir, name) + ".py", "w+")
    
    #imports
    f.write("from netsquid.nodes import Network\nfrom netsquid.components import QuantumProcessor, QuantumChannel, Channel\n")

    #function to create new network
    f.write("\ndef new_network():\n\tnetwork = Network(" + name + ")\n")

    #return the final network
    f.write("\n\treturn network\n")
    f.close()
