def create_actor(**kwargs):
    data = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }

    if len(kwargs) > 0:
        data.update(kwargs)

    return data


print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
