- Entrega & apresentação: 23/05 - Em PDF ou colab e apresentão oral - 20 minutos

# - Definir um conjunto de métricas (seu critério) para avaliar a "saúde" de um repositório.

- O foco pode ser análise do "envelhecimento" (aumento do número de commits, ou concentração de mudanças em poucos arquivos) ou  
da importância (diminuição no número de commits, números de contribuidores, etc.). 

# - Essas métricas devem ser aplicadas em 3 repositórios para comparar os três. 
#    . Os repositórios não precisam ser concorrentes. 

-  Relatório deve ter no mínimo 4 páginas e ser composto de gráficos diversos. Foco gerencial. 

- No final mostre um gráfico comparativo da "saúde" dos três repositórios em ao menos dois aspectos.

##################################################################################################################################

Quais repositórios serão analizdos:
    1 - Django
    2 - Flask
    3 - FastAPI

                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    V

Quais métricas escolhidas para avaliar a saúde de um repositório
    - Variação do número de commits ao logo do tempo
    - desigualdade no número de commits entre os contribuintes
    
    Talvez
        - localidade dos contribuintes, visando acompanhar o alcance do projeto (focar nos 20 contribuintes mais relevantes. Vou fazer manualmente)
    
@@ para testes baixe os repositórios dos projetos no github e crie um ambiente virtual do python para instalar as bibliotecas