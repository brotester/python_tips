workers = [
    ('April Cisneros', 'heather05', 'hreed@yahoo.com', '1929-08-17'),
    ('Amber Jefferson', 'gloria67', 'harrisrichard@gmail.com', '1918-09-18'),
    ('Denise Ingram', 'walkerlori', 'jeremy88@yahoo.com', '2019-09-04'),
    ('Tyler Spears', 'john72', 'sanchezsarah@gmail.com', '1963-05-31'),
    ('Kayla Mack', 'alexis27', 'sandersvalerie@hotmail.com', '2014-03-08'),
    ('James Stevens', 'quinnkelly', 'vazquezrebecca@hotmail.com', '1984-01-10'),
    ('Timothy Moyer', 'ariassteven', 'laura91@yahoo.com', '1905-08-08'),
    ('Douglas Walters', 'mpotter', 'hbutler@yahoo.com', '1904-11-17'),
    ('Annette Griffin', 'josephwaller', 'tnguyen@gmail.com', '1976-06-08'),
    ('Valerie Butler', 'hendersonrobin', 'michaellowery@hotmail.com', '1913-07-18'),
]


if __name__ == '__main__':
    print('{:15} | {:15} | {:30} | {:5}'.format('Name', 'Nick', 'Mail', 'Birthdate'))
    fmt = '{:15} | {:15} | {:30} | {:5}'
    for name, nick, mail, birthdate in workers:
        print(fmt.format(name, nick, mail, birthdate))
