<?php
	$host = "localhost";      
	$user = "root";         
	$passwd = "1234";   
    $database = "";
    $port = "3307";
	$connect = mysqli_connect($host, $user, $passwd, $database, $port) or die("mysql서버 접속 에러");
	$db = mysqli_select_db($connect, 'movie_db');  //moviedb 연결
	mysqli_select_db($connect, 'movie_db') or die("DB 접속 에러");      //my_db 선택
?>