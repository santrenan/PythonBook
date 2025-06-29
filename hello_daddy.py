users = ['john', 'marie', 'julie', 'daddy', 'marcos']
# users = []

if len(users) == 0:
    print('Precisamos encontrar alguns usuarios.')
else:
    for user in users:
        if user == 'daddy':
            print('Hi daddy!!!')
        else:
            print(f'Olá {user}, como vai?')