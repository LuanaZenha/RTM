Roteiro Turístico de Maricá

Este projeto em Python permite ao usuário selecionar um bairro de origem e um ponto turístico de destino em Maricá (RJ) e visualizar a rota mais curta a pé entre eles em um mapa interativo.

🧭 Funcionalidades
•	Lista de bairros e pontos turísticos da cidade.
•	Cálculo automático da rota mais curta usando algoritmo de Dijkstra.
•	Geração de mapa interativo com Folium.
•	Salva o resultado como um arquivo HTML visualizável em qualquer navegador.

🛠️ Requisitos

Instale os pacotes necessários com:

pip install osmnx networkx folium

Nota: O OSMnx requer o pacote geopandas, que pode precisar de dependências de sistema (como gdal no Linux).

▶️ Como usar

1.	Clone ou baixe este repositório.
2.	Execute o script Python:

python rota.py

3.	Escolha seu bairro de origem e o ponto turístico desejado.
4.	O mapa gerado será salvo como rota_real_marica.html.

🗺️ Exemplo de uso

Escolha seu bairro de origem:
1: Centro de Maricá
2: Flamengo
...

Digite o número do bairro: 1

Escolha o ponto turístico de destino:
1: Praia de Itaipuaçu
2: Praia de Guaratiba
...

Digite o número do ponto turístico: 7

Calculando rota, aguarde...

Mapa salvo como 'rota_real_marica.html'

📁 Estrutura

rota.py
README.md

rota_real_marica.html (gerado após execução)

📌 Observações
•	O mapa utiliza dados do OpenStreetMap.
•	A rede viária usada é do tipo walk (caminhada).

🧑‍💻 Autores
Desenvolvido por Amanda Nick, Bruno Barral, Luana Zenha e Renan Monteiro.
