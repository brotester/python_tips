from faker import Faker

fake = Faker()
for i in range(10):
    profile = fake.simple_profile()
    print("{}, {}, {}, {}".format(profile['name'], profile['username'], profile['mail'], profile['birthdate']))
