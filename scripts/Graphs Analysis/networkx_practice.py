import networkx as nx
import matplotlib.pyplot as plt

fh=open("../outputs/csv/bases_edges_april_early.csv", 'r')
fh.readline()
cdrs_net=nx.read_weighted_edgelist(fh, delimiter = ',', create_using=nx.DiGraph())
fh.close()
#N, K = nx.number_of_nodes(cdrs_net), nx.number_of_edges(cdrs_net)
#print N
#print K
#cdrs_net = nx.read_edgelist(fh, create_using=nx.DiGraph(), delimiter=",", edgetype='weight')
#N, K = nx.number_of_nodes(cdrs_net), nx.number_of_edges(cdrs_net)
# print N
# print K
# avg_deg = K/float(N)
# print 'El average degree es: ' + str(avg_deg)

#cdrs_components = list(nx.connected_component_subgraphs(cdrs_net))
#giant_cdrs = cdrs_components[0]
# n, k = nx.number_of_nodes(giant_cdrs), nx.number_of_edges(giant_cdrs)
# print 'Numero de nodos: ' + str(n)
# print 'Numero de arcos: ' + str(k)

# print ''
# print 'IN DEGREE'
# d = {}
# degree_cent = nx.in_degree_centrality(cdrs_net)
# #degree_cent
# claves = list(degree_cent.keys())
# valores = list(degree_cent.values())
# #print claves

# mayores = {}

# for i in range(7):
#     maximo = max(valores)
#     indice = valores.index(maximo)
#     clave = claves[indice]
#     valores.remove(maximo)
#     claves.remove(clave)
#     mayores[clave] = maximo

# for k,v in mayores.items():
#     print k, v



# print ''
# print 'OUT DEGREE'

# degree_cent = nx.out_degree_centrality(cdrs_net)
# #print degree_cent
# claves = list(degree_cent.keys())
# valores = list(degree_cent.values())
# #print claves



# mayores = {}

# for i in range(7):
#     maximo = max(valores)
#     indice = valores.index(maximo)
#     clave = claves[indice]
#     valores.remove(maximo)
#     claves.remove(clave)
#     mayores[clave] = maximo

# for k,v in mayores.items():
#     print k, v

# fh.close()
# '''



# nyc_net = nx.read_edgelist('nyc_edges.csv', create_using=nx.DiGraph(), delimiter=",")
# N, K = nx.number_of_nodes(nyc_net), nx.number_of_edges(nyc_net)
# avg_deg = K/float(N)

# print "Network with 4SQ Venues."
# print "Nodes ", N
# print "Edges", K
# print "Average Degree: ", avg_deg

# d = {}
# f = open("nyc_nodes.csv", "r")
# for line in f:
#     line = line.strip()
#     L = line.split(",")
#     d[L[0]] = L[1]
# f.close()

# #Lo convertimos a NO DIRIGIDO porque el algoritmo para hallar componentes no esta implementado en grafos dirigidos
# nyc_net_ud = nyc_net.to_undirected()
# nyc_net_components = list(nx.connected_component_subgraphs(nyc_net_ud))
# #La primera posicion de esta lista es el GIANT
# nyc_net_mc = nyc_net_components[0]
# print nyc_net_components

# #Encontrar numero de nodos y aristas del GIANT
# N_mc, K_mc = nx.number_of_nodes(nyc_net_mc), nx.number_of_edges(nyc_net_mc)

# #Encontrar el coeficiente de clustering del grafo
# avg_clust = nx.average_clustering(nyc_net_mc)
# print avg_clust

# #Encontrar metricas de centralidad y hallar el TOP 7 de lugares centrales con cada una de estas metricas.

# #Degree Centrality
# degree_cent = nx.degree_centrality(nyc_net_mc)
# print degree_cent
# claves = list(degree_cent.keys())
# valores = list(degree_cent.values())

# mayores = {}

# for i in range(7):
#     maximo = max(valores)
#     indice = valores.index(maximo)
#     clave = claves[indice]
#     valores.remove(maximo)
#     mayores[d[clave]] = maximo
# print mayores
# for k,v in mayores.items():
#     print k, v

# #Betweeness Centrality
# mayores2 = {}
# betweeness_cent = nx.betweenness_centrality(nyc_net_mc)
# claves = list(betweeness_cent.keys())
# valores = list(betweeness_cent.values())
# for i in range(7):
#     maximo = max(valores)
#     indice = valores.index(maximo)
#     clave = claves[indice]
#     valores.remove(maximo)
#     mayores2[d[clave]] = maximo
# print mayores2

#EijenVector Centrality
mayores3 = {}
eigenvector_cent = nx.eigenvector_centrality(cdrs_net)
claves = list(eigenvector_cent.keys())
valores = list(eigenvector_cent.values())
#frecuencias = {}
#for valor in valores:
#	if valor not in frecuencias:
#		frecuencias[valor] = 1
#	else:
#		frecuencias[valor] += 1
#centralities = list(frecuencias.keys())
#cantidades = list(frecuencias.values())
# cantidadesNorm = []
# maximo = max(cantidades)
# for cantidad in cantidades:
# 	cantidadesNorm.append(cantidad/maximo)



"""
plt.plot(centralities, cantidades, 'ro')
plt.title('Log-Log Degree Distribution for July')
plt.xlabel('Degree')
plt.ylabel('Amount of nodes')
plt.yscale('log')
#plt.xscale('log')
plt.show()
"""



f = open("../outputs/csv/topEigenVector_april_early.csv", 'w')
f.write('radiobaseID,eijenvector_value,\n')
for i in range(10):
    maximo = max(valores)
    indice = valores.index(maximo)
    clave = claves[indice]
    valores.remove(maximo)
    claves.remove(clave)
    mayores3[clave] = maximo
    f.write(str(clave) + ',' + str(maximo) + '\n')
print mayores3
f.close()