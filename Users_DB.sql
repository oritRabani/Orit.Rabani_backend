DROP TABLE Users;
CREATE TABLE Users(
  User_id int auto_increment primary key,
  Name varchar(255),
  Email varchar(255),
  Password varchar(255),
  Phone_number varchar(120),
  Gender varchar(1)
);