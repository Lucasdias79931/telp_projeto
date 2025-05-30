input_path = 'about_django/django_resumo.csv'
output_path = 'about_django/django_resumo_corrigido.csv'

with open(input_path, 'r') as f:
    linhas = f.readlines()

with open(output_path, 'w') as f:
    for linha in linhas:
        partes = linha.strip().split(',')
        if len(partes) == 2:  # faltando localidade
            linha = linha.strip() + ',' + '\n'  # adiciona vírgula no final
        f.write(linha)
