Roteiro Turístico de Maricá

Este projeto em Python permite ao usuário selecionar um bairro de origem e um ponto turístico de destino em Maricá (RJ) e visualizar a rota mais curta a pé entre eles em um mapa interativo.

🧭 Funcionalidades
✅ Lista completa de bairros e pontos turísticos de Maricá.

✅ Cálculo da rota mais curta utilizando o algoritmo de Dijkstra.

✅ Geração de mapa interativo com a biblioteca Folium.

✅ Salvamento automático do mapa em arquivo .html.

✅ Preparado para futuras funcionalidades com scikit-learn.

🛠️ Requisitos

Instale os pacotes necessários com:

pip install osmnx networkx folium scikit-learn

Nota: O osmnx requer o geopandas, que pode necessitar de bibliotecas de sistema (ex: gdal, fiona). No Linux, instale com:

sudo apt install gdal-bin libgdal-dev

Nota: O OSMnx requer o pacote geopandas, que pode precisar de dependências de sistema (como gdal no Linux).

▶️ Como usar

1.	Clone ou baixe este repositório.
2.	Execute o script Python:

python rota.py

3.	Escolha seu bairro de origem e o ponto turístico desejado.
4.	O mapa gerado será salvo como rota_turistica.html.

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

Mapa salvo como 'rota_turistica.html'

📁 Estrutura do Projeto

📦 roteiro-marica/
├── rota.py                 # Script principal do projeto
├── README.md               # Documentação do projeto
└── rota_turistica.html   # Mapa gerado (após execução)

📌 Observações
•	O mapa utiliza dados do OpenStreetMap.
•	A rede viária usada é do tipo walk (caminhada).

🧑‍💻 Autores
Desenvolvido por Amanda Nick, Bruno Barral, Luana Zenha e Renan Monteiro.
