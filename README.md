## Repositório do Projeto Interdisciplinar para SI II

## OBJETIVO
Desenvolvimento de algoritmos de força bruta e genético para resolver o problema do circuito Flyfood (variante do caixeiro viajante) e realização de estudo comparativo.

## DESCRIÇÃO
Estamos no ano de 2025 e nesse futuro não tão distante o trânsito está caótico. As empresas de delivery já não conseguem fazer entregas em um tempo aceitável e o custo com entregadores está muito alto, pois mão-de-obra humana está cada vez mais valorizada devido à grande oferta de empregos (ok… essa última parte é mais sonho do que realidade, mas vamos considerá-la). Então, um ex-aluno do BSI-UFRPE resolve criar uma empresa chamada FlyFood para fazer entregas utilizando drones.

Essas máquinas voadoras fantásticas podem receber uma rota de entregas e executá-la à risca. Ou seja, elas podem voar desde o local de origem do pedido (por exemplo, restaurante ou lanchonete) com vários pedidos no seu compartimento de carga e entregar em vários endereços espalhados na cidade. Essa capacidade de sair com vários pedidos otimiza bastante o tempo de entrega dos pedidos. No entanto, nem tudo são flores. A capacidade das baterias dos drones continuam sendo um problema. Sendo assim, é preciso otimizar ao máximo o trajeto do drone para conseguir concluir todas as entregas dentro do ciclo da bateria.

Com esse cenário em vista, já nos dias atuais (2022) o empreendedor da FlyFood vai começar a desenvolver um algoritmo de roteamento. Ou seja, um algoritmo que seja capaz de definir o menor trajeto para a realização de todas as entregas do drone.

Para abstrair as questões de encontrar endereços e obter coordenadas GPS, vamos trabalhar com uma matriz que representa os pontos da cidade.

Dada a matriz exemplo: Temos o ponto superior esquerdo é o (0,0) e nessa posição não existe um ponto de entrega. Já no ponto (1,1) existe o ponto de entrega A. Os demais pontos de entrega estão nos pontos B (3,2), C (2,4) e D (0, 4). No exemplo acima, a origem do drone, ou seja onde ele é carregado com os pedidos, é o ponto R (3,0). Por convenção, o ponto R sempre será o ponto de origem e retorno.

Vamos considerar também que o drone não consegue andar na "diagonal". Ou seja, ele só consegue percorrer essa matriz na horizontal ou na vertical. Sendo assim, para ir do ponto A para o ponto B ele precisa percorrer 3 dronômetros (unidade de medida de custo do percurso). Para ir de B para D a distância é de 5 dronômetros.

Seu trabalho será elaborar um algoritmo que vai ler uma matriz, a partir de um arquivo, com o ponto de origem e retorno; e pontos de entrega. Ele deverá retornar a ordem em que o drone deve percorrer os pontos de entrega. Essa ordem deve ser a de menor custo, ou seja, a que o drone vá percorrer a menor distância em dronômetros.

O formato do arquivo de entrada será o seguinte para a matriz de exemplo.

4 5 <br>
0 0 0 0 D <br>
0 A 0 0 0 <br>
0 0 0 0 C <br>
R 0 B 0 0 <br>

Sua resposta deverá ser a sequência de pontos (em forma de string) que produz o menor circuito possível a ser percorrido pelo drone entre os pontos de entrega, partindo e retornando ao ponto R (o ponto R não precisa ser incluído na sequência de resposta). Por exemplo: "A D C B".

Divirta-se!
