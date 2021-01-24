<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <link rel='icon' href='favicon.ico' type='image/x-icon'/ >
    <link href="https://fonts.googleapis.com/css?family=Lora&display=swap" rel="stylesheet">
    <title>Wasserstand - Widacher</title>
    <script data-ad-client="ca-pub-4348814037136269" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

</head>
<h1>Wasserstand - Bach Widacher</h1>
<nav>
  <ul class="navigation">
      <li><a class="active" href="index.php">Home</a></li>
      <li><a href="project.html">Über das Projekt</a></li>
      <li><a href="kontakt.html">Kontakt</a></li>
    </ul>
</nav>
<p class="center"> Die Uhrzeit wird im UTC format angegeben (-2 Stunden). </p>
<?php
$servername = "192.168.111.61";
$username = "root";
$password = "123ict";
$dbname = "bach";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT time, distanz, up FROM wasser ORDER BY time desc LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<h3>Zeitpunkt: "  . $row["time"]. "</h3><br> <h3>Distanz zum Überlauf " . $row["distanz"]. " Zentimeter </h3><br><h3> Wasserstand " . $row["up"]. " Zentimeter </h3><br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>

