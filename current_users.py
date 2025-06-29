current_users = ['john', 'marie', 'julie', 'daddy', 'marcos']
new_users = ['julio', 'maria', 'julie', 'daddy', 'nirvana']

item = 0
for user in new_users:
    if user.lower() in current_users[item].lower():
        print(f'{user} já existe em users.')
    else:
        print(f'{user} foi adicionado em users')
        current_users.append(user)

    item += 1

print(current_users)

