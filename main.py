import os
import pandas as pd
from matplotlib import pyplot as plt


def plot_localidade(df, titulo, destine):

    try:
        df = df[df['localidade'].notna()]

        distribuicao = pd.crosstab(index=df['localidade'].str.upper(), columns='frequência')
        distribuicao = distribuicao.sort_values(by='frequência', ascending=False)

        fig, ax = plt.subplots()
        distribuicao.plot(kind='bar', legend=False, ax=ax)

        ax.set_title(f'Distribuição Regional Entre Alguns Colaboradores do {titulo}')
        ax.set_xlabel('Localidade')
        ax.set_ylabel('Frequência')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        #plt.show()

        fig.savefig(destine, dpi=300, bbox_inches='tight')
    except IOError as e:

        print(f'Erro ao tentar verificar distribuição geografica para <{titulo}>')
        print(f" error <{e}>")
        exit(1)
    except Exception as e:
        print(f'Erro ao tentar verificar distribuição geografica para<{titulo}>')

        print('Erro ao tentar medir taxa de crescimento')
        print(f'Error <{e}>')
        exit(1)


def N_commits_por_trimestre(df, titulo, destine):
    try:
        df['date_commit'] = pd.to_datetime(df['date_commit'], dayfirst=True)
        df['trimestre'] = df['date_commit'].dt.to_period('Q')

        commits_por_trimestre = df.groupby('trimestre').size().sort_index()

        fig, ax = plt.subplots()
        commits_por_trimestre.plot(kind='line', marker='o', ax=ax)

        ax.set_title(f'Número de Commits do {titulo} por trimestres')
        ax.set_xlabel("Trimestre")
        ax.set_ylabel('Nº de commit')
        ax.grid(True)

        plt.xticks(rotation=45)
        plt.tight_layout()

        fig.savefig(destine, dpi=300)
    except IOError as e:

        print(f'Erro ao tentar medir taxa de crescimento para <{titulo}>')
        print(f" error <{e}>")
        exit(1)
    except Exception as e:
        print(f'Erro ao tentar medir taxa de crescimento para <{titulo}>')
        print(f'Error <{e}>')
        exit(1)
    
def medir_desigualdade_commits(df, titulo, destine):
    try:
        df_sorted = df.sort_values(by='n_commits', ascending=False).head(30)
        
        fig, ax = plt.subplots(figsize=(10, 8))  
        df_sorted.plot(kind='barh', x='nome', y='n_commits', ax=ax, legend=False, color='skyblue')
        
        ax.set_title(f'Commits por Contribuidor (Top 30) - {titulo.upper()}')
        ax.set_xlabel('Nº de Commits')
        ax.set_ylabel('Contribuidor')
        plt.gca().invert_yaxis()  
        
        plt.tight_layout()
        fig.savefig(destine, dpi=300)
    except IOError as e:
        print(f'Erro ao tentar medir a desigualdade no número de commits para <{titulo}>')
        print(f" error <{e}>")
        exit(1)
    except Exception as e:
        print(f'Erro ao tentar medir a desigualdade no número de commits para <{titulo}>')
        print(f'Error <{e}>')
        exit(1)
def plot_variacao_commits_projetos_ano(dfs_dict, titulo, destine):
    try:
        plt.figure(figsize=(10,6))
        
        for nome_projeto, df in dfs_dict.items():
            df['date_commit'] = pd.to_datetime(df['date_commit'], dayfirst=True)
            df['ano'] = df['date_commit'].dt.year
            
            commits_por_ano = df.groupby('ano').size().sort_index()
            
            plt.plot(commits_por_ano.index.astype(str), commits_por_ano.values, marker='o', label=nome_projeto)
        
        plt.title(f'Variação da Quantidade de Commits por Ano - {titulo}')
        plt.xlabel('Ano')
        plt.ylabel('Número de Commits')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(destine, dpi=300)
        plt.close()
    except IOError as e:
        print(f'Erro ao tentar gerar gráfico de variação para <{titulo}>')
        print(f"error <{e}>")
        exit(1)
    except Exception as e:
        print(f'Erro inesperado ao gerar gráfico de variação para <{titulo}>')
        print(f'Error <{e}>')
        exit(1)

def plot_localidade_comparativa(dfs_dict, titulo, destine):
    try:
        lista_dfs = []

        for nome_projeto, df in dfs_dict.items():
            df = df[df['localidade'].notna()].copy()
            df['localidade'] = df['localidade'].str.upper()
            df['Projeto'] = nome_projeto
            lista_dfs.append(df[['localidade', 'Projeto']])

        combinado = pd.concat(lista_dfs)

        tabela = pd.crosstab(combinado['localidade'], combinado['Projeto'])

        tabela['total'] = tabela.sum(axis=1)
        tabela = tabela.sort_values(by='total', ascending=False).drop(columns='total')

       
        fig, ax = plt.subplots(figsize=(12, 6))
        tabela.plot(kind='bar', ax=ax)

        ax.set_title(f'Distribuição Regional Entre Alguns Colaboradores do {titulo}')
        ax.set_xlabel('Localidade')
        ax.set_ylabel('Frequência')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        fig.savefig(destine, dpi=300, bbox_inches='tight')
       

    except Exception as e:
        print(f'Erro ao gerar gráfico comparativo de localidade: {e}')
        exit(1)



here = os.path.abspath(os.path.dirname(__file__))

#histograma da distribuição da localidade dos contribuintes

django_amb = os.path.join(here,'about_django')
flask_amb = django_amb.replace('django','flask')
fastApi_amb = django_amb.replace('django','fastApi')



django = pd.read_csv(os.path.join(django_amb, 'django_resumo.csv'))

plot_localidade(django, 'Django',os.path.join(django_amb, 'localidade_contribuintes_django.png'))

fastApi = pd.read_csv(os.path.join(fastApi_amb,'fastApi_resumo.csv'))
plot_localidade(fastApi, 'FastApi',os.path.join(fastApi_amb, 'localidade_contribuintes_fastApi.png'))

_flask = pd.read_csv(os.path.join(flask_amb, 'flask_resumo.csv'))
plot_localidade(_flask, 'Flask',os.path.join(flask_amb, 'localidade_contribuintes_flask.png'))



# Visualização trimestral do número de semestre

django_amb = os.path.join(here,'about_django')
flask_amb = django_amb.replace('django','flask')
fastApi_amb = django_amb.replace('django','fastApi')


django = pd.read_csv(os.path.join(django_amb, 'django_commits.csv'))

N_commits_por_trimestre(django, 'Django',os.path.join(django_amb, 'n_commits_por_trimeste_dajngo.png'))


fastApi = pd.read_csv(os.path.join(fastApi_amb, 'fastApi_commits.csv'))

N_commits_por_trimestre(fastApi, 'FastApi',os.path.join(fastApi_amb, 'n_commits_por_trimeste_fastApi.png'))

_flask = pd.read_csv(os.path.join(flask_amb, 'flask_commits.csv'))

N_commits_por_trimestre(_flask, 'Flask',os.path.join(flask_amb, 'n_commits_por_trimeste_flask.png'))
    




django = pd.read_csv(os.path.join(django_amb, 'django_resumo.csv'))

medir_desigualdade_commits(django, 'Django',os.path.join(django_amb, 'desigualdade_commits_dajngo.png'))

fastApi = pd.read_csv(os.path.join(fastApi_amb, 'fastApi_resumo.csv'))

medir_desigualdade_commits(fastApi, 'FastApi',os.path.join(fastApi_amb, 'desigualdade_commits_FastApi.png'))

_flask = pd.read_csv(os.path.join(flask_amb, 'flask_resumo.csv'))

medir_desigualdade_commits(_flask, 'Flask',os.path.join(flask_amb, 'desigualdade_commits_flask.png'))




# Analizar a variação no número de commits entre os três projetos
django = pd.read_csv(os.path.join(django_amb, 'django_commits.csv'))
fastApi = pd.read_csv(os.path.join(fastApi_amb, 'fastApi_commits.csv'))
_flask = pd.read_csv(os.path.join(flask_amb, 'flask_commits.csv'))

dfs = {
    'Django': django,
    'Flask': _flask,
    'FastApi': fastApi
}

plot_variacao_commits_projetos_ano(dfs, 'Projetos Django, Flask e FastApi', os.path.join(here, 'variacao_Ncommitis_flask_django_fastApi.png'))


django = pd.read_csv(os.path.join(django_amb, 'django_resumo.csv'))
fastApi = pd.read_csv(os.path.join(fastApi_amb, 'fastApi_resumo.csv'))
_flask = pd.read_csv(os.path.join(flask_amb, 'flask_resumo.csv'))


dfs = {
    'Django': django,
    'Flask': _flask,
    'FastApi': fastApi
}


plot_localidade_comparativa(dfs,'Django, Flask e Fast',os.path.join(here,'comparativo_regional.png'))

