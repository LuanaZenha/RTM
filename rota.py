import osmnx as ox
import networkx as nx
import folium

# Lista de bairros (origens possíveis)
bairros = {
    1: ("Centro de Maricá", (-22.915887241134016, -42.819610837674425)),
    2: ("Flamengo", (-22.916142993479482, -42.8128615255951)),
    3: ("Mumbuca", (-22.911020938237538, -42.8273644305292)),
    4: ("Itapeba", (-22.90701337253586, -42.83140582085482)),
    5: ("Parque Nanci", (-22.92184066427019, -42.84612059468948)),
    6: ("Ponta Grossa", (-22.92046432394212, -42.85489905736248)),
    7: ("São José do Imbassaí", (-22.939356599292424, -42.87651469922347)),
    8: ("Araçatiba", (-22.926553634386003, -42.82705707566545)),
    9: ("Jacaroá", (-22.934965552328965, -42.80624999075233)),
    10: ("Barra de Maricá", (-22.96075413229002, -42.81972141197444)),
    11: ("Zacarias", (-22.95914972670989, -42.83499681625325)),
    12: ("Restinga de Maricá", (-22.95953774538306, -42.84566549440735)),
    13: ("Retiro", (-22.922219933256034, -42.86430270563025)),
    14: ("Camburi", (-22.909443880247235, -42.81723049629146)),
    15: ("Pindobas", (-22.88257867071839, -42.86308663238033)),
    16: ("Caxito", (-22.885204838186414, -42.819153200885)),
    17: ("Ubatiba", (-22.875446987982325, -42.804311478724415)),
    18: ("Pilar", (-22.866623590685514, -42.78070911062736)),
    19: ("Lagarto", (-22.846461264883075, -42.78379623665348)),
    20: ("Silvado", (-22.874491960469108, -42.757130561110905)),
    21: ("Condado de Maricá", (-22.894091183854453, -42.7954272480335)),
    22: ("Marquês de Maricá", (-22.902545389528104, -42.7925791508369)),
    23: ("Jaconé", (-22.913732631738526, -42.635639363365534)),
    24: ("Cordeirinho", (-22.954888731962075, -42.73959892804163)),
    25: ("Guaratiba", (-22.95648153196455, -42.79293807160315)),
    26: ("Jardim Interlagos", (-22.935887268111696, -42.76781681932371)),
    27: ("Balneário Bambuí", (-22.940185574479116, -42.753209548724094)),
    28: ("Pindobal", (-22.91689337040561, -42.74598480039793)),
    29: ("Caju", (-22.932204042201445, -42.808173760368796)),
    30: ("Manoel Ribeiro", (-22.904171765126428, -42.71738678665955)),
    31: ("Espraiado", (-22.888318849904632, -42.70739738506861)),
    32: ("Vale da Figueira", (39.30096287244705, -8.625236130412375)),
    33: ("Bananal", (-22.92106841646982, -42.72253040192725)),
    34: ("Chácaras de Inoã", (-22.935320087166684, -42.95141846873016)),
    35: ("Calaboca", (-22.90550279901531, -42.944203893543886)),
    36: ("SPAR", (-22.896880647179767, -42.933430882884)),
    37: ("Santa Paula", (-22.891430852387668, -42.925839533775324)),
    38: ("Cassorotiba", (-22.881721987763598, -42.89625200269932)),
    39: ("Itaipuaçu", (-22.9612173220956, -42.98986713346667)),
    40: ("Morada das Águias", (-22.95429094458332, -43.00032099236323)),
    41: ("Rincão Mimoso", (-22.946238756301202, -42.978846471417775)),
    42: ("Barroco", (-22.95970155795847, -42.982803151533815)),
    43: ("Jardim Atlântico Oeste", (-22.962588056078094, -42.96552762154443)),
    44: ("Jardim Atlântico Central", (-22.95719720246473, -42.949271565810484)),
    45: ("Jardim Atlântico Leste", (-22.96327623469234, -42.93594284543281)),
    46: ("Cajueiros", (-22.94396843105541, -42.92929176390177)),
    47: ("Itaocaia Valley", (-22.934302086475707, -42.965901636000964)),
}


# Pontos turísticos (destinos possíveis)
pontos_turisticos = {
    1: ("Praia de Itaipuaçu", (-22.966471130555203, -42.99698232362043)),
    2: ("Praia de Guaratiba", (-22.960055701962496, -42.79952206221672)),
    3: ("Praia de Cordeirinho", (-22.957334693248278, -42.746781789203474)),
    4: ("Praia de Ponta Negra", (-22.95581283439762, -42.69843619402791)),
    5: ("Praia de Jaconé", (-22.94508756773028, -42.67996300573703)),
    6: ("Praia da Sacristia", (-22.950020349252714, -42.682663674902784)),
    7: ("Pedra do Elefante", (-22.974438245003434, -43.017235992900524)),
    8: ("Pedra do Macaco", (-22.924354703856995, -42.895871082321555)),
    9: ("Cachoeira do Espraiado", (-22.869636489795514, -42.689961087580315)),
    10: ("Cachoeira do Silvado", (-22.871161243062645, -42.737240073864)),
    11: ("Grutas do Spar", (-22.89075088481428, -42.94693217571235)),
    12: ("Gruta da Sacristia", (-22.951109647599896, -42.68232888120455)),
    13: ("Parque Estadual da Serra da Tiririca", (-22.973149788819484, -43.02769226057085)),
    14: ("Túnel da Antiga Estrada de Ferro de Maricá", (-22.900747965004186, -42.94404260269869)),
    15: ("Igreja Matriz de Nossa Senhora do Amparo", (-22.912912045677917, -42.817103567315826)),
    16: ("Capela de Santo Antônio", (-22.917166522170913, -42.77187174524128)),
    17: ("Capela de São Jorge", (-22.896696342620153, -42.70979929290328)),
    18: ("Capela Nossa Senhora da Saúde", (-22.860509206310464, -42.80750984921519)),
    19: ("Fazenda do Pilar", (-22.852763650766605, -42.78064101726065)),
    20: ("Farol de Ponta Negra", (-22.9603865447931, -42.69282096221675)),
    21: ("Orla da lagoa de Araçatiba", (-22.919468569888565, -42.82723946857988)),
    22: ("Canal de Ponta Negra", (-22.9563807174775, -42.69388700639455)),
    23: ("Lagoa de Jaconé", (-22.929125457195614, -42.63974707075392)),
}


# Exibir e selecionar bairro
print("Escolha seu bairro de origem:")
for k, (nome, _) in bairros.items():
    print(f"{k}: {nome}")
origem_id = int(input("Digite o número do bairro: "))
origem_nome, origem_coord = bairros.get(origem_id)

# Exibir e selecionar ponto turístico
print("\nEscolha o ponto turístico de destino:")
for k, (nome, _) in pontos_turisticos.items():
    print(f"{k}: {nome}")
destino_id = int(input("Digite o número do ponto turístico: "))
destino_nome, destino_coord = pontos_turisticos.get(destino_id)

# Baixar grafo viário
print("\nCalculando rota, aguarde...")
G = ox.graph_from_place("Maricá, Rio de Janeiro, Brazil", network_type="walk")

# Encontrar nós mais próximos
orig_node = ox.distance.nearest_nodes(G, X=origem_coord[1], Y=origem_coord[0])
dest_node = ox.distance.nearest_nodes(G, X=destino_coord[1], Y=destino_coord[0])

# Calcular rota com Dijkstra
rota = nx.dijkstra_path(G, orig_node, dest_node, weight="length")

# Coordenadas da rota
rota_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in rota]

# Criar mapa
mapa = folium.Map(location=origem_coord, zoom_start=13)
folium.Marker(location=origem_coord, popup=f"Origem: {origem_nome}", icon=folium.Icon(color='green')).add_to(mapa)
folium.Marker(location=destino_coord, popup=f"Destino: {destino_nome}", icon=folium.Icon(color='red')).add_to(mapa)
folium.PolyLine(rota_coords, color="blue", weight=4).add_to(mapa)

# Salvar mapa
mapa.save("rota_real_marica.html")
print("\nMapa salvo como 'rota_real_marica.html'")
