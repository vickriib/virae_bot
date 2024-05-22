def search_groups(query):
    # Implementar lógica para pesquisar grupos baseados na query
    # Retornar uma lista de grupos fictícios como exemplo
    sample_groups = [
        {'id': 1, 'name': 'Grupo de TV'},
        {'id': 2, 'name': 'Grupo de Animangás'},
        {'id': 3, 'name': 'Grupo de Jogos'}
    ]
    return [group for group in sample_groups if query.lower() in group['name'].lower()]
