<?php
include_once 'dbconnection.php';

// sql to create table
$sql = "CREATE TABLE csv_import (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
initials VARCHAR(50),
age VARCHAR(50),
dateofbirth VARCHAR(50), 
)";

if ($conn->query($sql) === TRUE) {
  echo "Table csv_import created successfully";
} else {
  echo "Error creating table!: " . $conn->error;
}

$conn->close();
?>