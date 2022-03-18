from package import models, config

if config.staging:

    persons = []

    for person in config.fake_db:
        persons.append(
            models.Person(person.username, person.salary)
        )
        print(persons)
else:

    while True:
        username = input('Username: ')
        salary = int(input('Salary: '))

        db.append(models.Person(username, salary))
        print(db)