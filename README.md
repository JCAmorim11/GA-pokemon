# GA-pokemon# Computação Evolucionária, a Genética Pokémon
***Este projeto trata-se de um trabalho de conclusão de curso para a FATEC-SP***
*O tema deste trabalho é demonstrar a utilização de algoritmos geneticos com base no jogo eletrônico pokemon, tendo como base as versões [Ruby/Sapphire/Emerald ](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Ruby_and_Sapphire_Versions "Ruby/Sapphire/Emerald ") lançados no periodo de 2002 -- Ruby e Sapphire -- e 2005 -- Emerald -- que são conhecidas na comunidade como a _terceira geração_ da franquia de jogos*



## Desafio Proposto
Usar um algoritmo genético, para selecionar um time de 6 pokémons capaz de passar por oito batalhas do ginasio, e as quatro batalhas contra a elite 4

**(NÍVEL SERÁ IGNORADO, todos estarão no nível 100)**

(**HABILIDADES SERÃO IGNORADAS,** será feito como se ela não existisse pois seu impacto não é tão relevante nas batalhas, ver para mais detalhes: [https://bulbapedia.bulbagarden.net/wiki/Ability](https://bulbapedia.bulbagarden.net/wiki/Ability)**)**

### Regras:
-----

1. O time selecionado pelo algoritmo pode ter de 1 à 6 pokemons
2. O time selecionado pode possuir pokemons repetidos  (sem limitação de repetição)
3. Os moves são selecionados aleatoriamente baseado em todas os moves que o pokemon do time poder ter segundo a lista disponível na API [PokeApi](https://pokeapi.co/)
4. Um pokemon selecionado terá stats e move aleatórios baseados na media geral do pokemon
5. Os pokemons selecionados poderão ter de 1 à 4 moves
6. NENHUM POKEMON pode ter moves repetidos
7. Os pokemons dos times adversários terão moves e  stats idênticos em todas as rodadas possíveis
8.  Os PP (Power point) funcionam normalmente, logo se um pokemon ficar sem pp não poderá mais usar aquele move na batalha.
9. Os PP (Power Points) e HP sempre estarão cheios no inicio de cada batalha
10. Poções não serão utilizadas por nenhum dos lados (*mesmo que in GAME a IA use, não serão utilizados nesse caso*)
11. Berries e outros itens que podem ser utilizados pelos pokemons durante a batalha que se classificam como “*[Held items](https://bulbapedia.bulbagarden.net/wiki/Held_item)*” não serão utilizados..
12. As mecânicas de IVs — [*Individuals Values*](https://bulbapedia.bulbagarden.net/wiki/Individual_values) — e EVs — [](https://bulbapedia.bulbagarden.net/wiki/Individual_values)[*Effort Values*](https://bulbapedia.bulbagarden.net/wiki/Effort_values) — padrões do jogo da terceira geração não serão levadas em conta, os stats dos pokemons serão modificados livremente pelo algoritmo — [*levando em conta sempre o base stats do pokemon*](https://bulbapedia.bulbagarden.net/wiki/Base_stats) — para facilitar a manipulação dos dados pelo programa. (Para entender melhor ver: [https://pokemondb.net/pokebase/137236/what-are-evs-and-ivs-and-how-do-they-work](https://pokemondb.net/pokebase/137236/what-are-evs-and-ivs-and-how-do-they-work))
13. Como não é possível saber com exatidão os stats dos pokemons adversários, será utilizados seus base stats sem modificação. (Para entender melhor ver: [https://bulbapedia.bulbagarden.net/wiki/Base_stats](https://bulbapedia.bulbagarden.net/wiki/Base_stats))
14. A batalha será considerada uma **derrota** caso todo o time tenha HP=0 OU caso nenhum pokemon do time tenha PP > 0 em algum move.
15. Uma batalha será considerado uma **vitória** caso todo o time adversário — expresso na tabela abaixo — tenha  HP=0
16. Caso o time adversário tenha todos os seus pokémon com PP=0 em todos os moves que eles utilizam,  a batalha não será encerrada, apenas será terminada nas condições estabelecidas de **vitória** e **derrota**





























