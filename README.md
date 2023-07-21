## Hello and thank you for grading this.

### MySQL Setup Steps
```
$ mysql -u root -p
<ENTER MYSQL ROOT PASSWORD>
mysql> drop database littlelemon;
mysql> create user 'lulu'@'localhost';
mysql> create database littlelemon;
mysql> grant all on littlelemon.* to 'lulu'@'localhost';
mysql> flush privileges;
mysql> exit
Bye
```

Thanks to [Dan's Cheat Sheets](https://cheat.readthedocs.io/en/latest/mysql.html#create-a-new-mysql-database)

### API Paths to test
- POST /restaurant/api-token-auth/
- /restaurant/booking/tables/
- /restaurant/menu/
