drop table if exists users;
create table users(
	id integer primary key increment,
	name text not null,
	filePath text not null,
) ;

