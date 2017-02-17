SELECT email, firstname
FROM persons LEFT JOIN roles ON persons.id = roles.pid
WHERE email IN('pickles.to@gmail.com','andrew@cela.ca')
